"""
Ethical Logging Module for Python Web Applications

This module demonstrates secure logging practices that protect user privacy and sensitive data.
Key principles:
- Never log passwords, API keys, or personal identifiers
- Use structured logging for better analysis and filtering
- Implement log levels and rotation for production use
- Provide clear audit trails without compromising security

ETHICAL LOGGING GUIDELINES:
- Log what happened, not who it happened to (when possible)
- Use hashed identifiers instead of raw user IDs when needed
- Implement data retention policies
- Never log in plain text: passwords, tokens, credit cards, SSNs
- Consider GDPR/privacy implications of all logged data
"""

import json
import logging
import logging.handlers
import re
import hashlib
import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from functools import wraps


# SENSITIVE DATA PATTERNS - Add more as needed
SENSITIVE_PATTERNS = {
    # Authentication & Security
    'password': r'(?i)(password|passwd|pwd|secret|token|key|api_key|auth_token)["\s]*[:=]\s*["\']?[^"\'\s]+["\']?',
    'email': r'(?i)(email|e-mail|mail)["\s]*[:=]\s*["\']?[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}["\']?',
    'phone': r'(?i)(phone|mobile|tel|telephone)["\s]*[:=]\s*["\']?[\d\-\+\(\)\s]+["\']?',
    'ssn': r'(?i)(ssn|social|security)["\s]*[:=]\s*["\']?[\d\-]+["\']?',
    'credit_card': r'(?i)(credit|card|cc|number)["\s]*[:=]\s*["\']?[\d\-\s]+["\']?',
    'ip_address': r'(?i)(ip|address)["\s]*[:=]\s*["\']?[\d\.]+["\']?',
    'user_id': r'(?i)(user_id|userid|uid|id)["\s]*[:=]\s*["\']?[\w\-]+["\']?',
}

# Fields that should never be logged (even if they appear safe)
BLOCKED_FIELDS = {
    'password', 'passwd', 'pwd', 'secret', 'token', 'key', 'api_key',
    'auth_token', 'session_id', 'cookie', 'authorization', 'bearer'
}


class SensitiveDataFilter:
    """Filter to remove or mask sensitive information from log messages."""
    
    def __init__(self, mask_char: str = '*', mask_length: int = 8):
        self.mask_char = mask_char
        self.mask_length = mask_length
        self.compiled_patterns = {k: re.compile(v) for k, v in SENSITIVE_PATTERNS.items()}
    
    def mask_sensitive_data(self, text: str) -> str:
        """Replace sensitive data with masked values."""
        if not isinstance(text, str):
            return text
            
        masked_text = text
        
        # Replace patterns with masks
        for pattern_name, pattern in self.compiled_patterns.items():
            masked_text = pattern.sub(f'[{pattern_name.upper()}_MASKED]', masked_text)
        
        return masked_text
    
    def filter_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively filter sensitive data from dictionaries."""
        if not isinstance(data, dict):
            return data
            
        filtered = {}
        for key, value in data.items():
            # Block completely blocked fields
            if key.lower() in BLOCKED_FIELDS:
                filtered[key] = '[BLOCKED]'
                continue
                
            # Mask sensitive values
            if isinstance(value, str):
                filtered[key] = self.mask_sensitive_data(value)
            elif isinstance(value, dict):
                filtered[key] = self.filter_dict(value)
            elif isinstance(value, list):
                filtered[key] = [self.filter_dict(item) if isinstance(item, dict) 
                               else self.mask_sensitive_data(item) if isinstance(item, str)
                               else item for item in value]
            else:
                filtered[key] = value
                
        return filtered


@dataclass
class LogEntry:
    """Structured log entry with metadata and filtered content."""
    timestamp: str
    level: str
    message: str
    module: str
    function: str
    line_number: int
    user_context: Optional[str] = None  # Hashed user identifier if needed
    request_id: Optional[str] = None
    ip_address: Optional[str] = None  # Masked IP
    additional_data: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


class EthicalLogger:
    """Main logging class that implements ethical logging practices."""
    
    def __init__(self, 
                 name: str = "web_app",
                 log_file: str = "app.log",
                 max_bytes: int = 10 * 1024 * 1024,  # 10MB
                 backup_count: int = 5,
                 log_level: str = "INFO"):
        
        self.name = name
        self.filter = SensitiveDataFilter()
        
        # Configure logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # Prevent duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers(log_file, max_bytes, backup_count)
    
    def _setup_handlers(self, log_file: str, max_bytes: int, backup_count: int):
        """Setup file and console handlers with rotation."""
        
        # File handler with rotation
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def _get_caller_info(self) -> tuple:
        """Get calling function information for context."""
        import inspect
        frame = inspect.currentframe().f_back.f_back
        return (
            frame.f_code.co_name,
            frame.f_globals.get('__name__', 'unknown'),
            frame.f_lineno
        )
    
    def _create_log_entry(self, 
                         level: str, 
                         message: str, 
                         **kwargs) -> LogEntry:
        """Create a structured log entry."""
        function, module, line = self._get_caller_info()
        
        # Filter any additional data
        filtered_data = self.filter.filter_dict(kwargs) if kwargs else None
        
        return LogEntry(
            timestamp=datetime.utcnow().isoformat(),
            level=level,
            message=self.filter.mask_sensitive_data(message),
            module=module,
            function=function,
            line_number=line,
            additional_data=filtered_data,
            **{k: v for k, v in kwargs.items() if k not in ['additional_data']}
        )
    
    def info(self, message: str, **kwargs):
        """Log info message with ethical filtering."""
        entry = self._create_log_entry("INFO", message, **kwargs)
        self.logger.info(json.dumps(entry.to_dict(), default=str))
    
    def warning(self, message: str, **kwargs):
        """Log warning message with ethical filtering."""
        entry = self._create_log_entry("WARNING", message, **kwargs)
        self.logger.warning(json.dumps(entry.to_dict(), default=str))
    
    def error(self, message: str, **kwargs):
        """Log error message with ethical filtering."""
        entry = self._create_log_entry("ERROR", message, **kwargs)
        self.logger.error(json.dumps(entry.to_dict(), default=str))
    
    def debug(self, message: str, **kwargs):
        """Log debug message with ethical filtering."""
        entry = self._create_log_entry("DEBUG", message, **kwargs)
        self.logger.debug(json.dumps(entry.to_dict(), default=str))
    
    def critical(self, message: str, **kwargs):
        """Log critical message with ethical filtering."""
        entry = self._create_log_entry("CRITICAL", message, **kwargs)
        self.logger.critical(json.dumps(entry.to_dict(), default=str))


def hash_user_identifier(identifier: str, salt: str = "web_app_salt") -> str:
    """Create a hash of user identifier for logging purposes.
    
    This allows tracking user actions without exposing actual identifiers.
    Use different salts for different environments.
    """
    return hashlib.sha256(f"{identifier}{salt}".encode()).hexdigest()[:16]


def log_function_call(logger: EthicalLogger, 
                     include_args: bool = True, 
                     include_result: bool = False):
    """Decorator to log function calls with ethical filtering.
    
    Args:
        logger: EthicalLogger instance
        include_args: Whether to log function arguments (filtered)
        include_result: Whether to log function results (filtered)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log function entry
            func_name = func.__name__
            
            # Filter arguments if requested
            log_data = {}
            if include_args:
                # Convert args to kwargs for easier filtering
                arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
                args_dict = dict(zip(arg_names, args))
                args_dict.update(kwargs)
                log_data['arguments'] = args_dict
            
            logger.info(f"Function {func_name} called", **log_data)
            
            try:
                result = func(*args, **kwargs)
                
                # Log result if requested
                if include_result:
                    logger.info(f"Function {func_name} completed successfully", 
                              result=result)
                
                return result
                
            except Exception as e:
                # Log errors with context
                logger.error(f"Function {func_name} failed with error: {str(e)}",
                           error_type=type(e).__name__,
                           error_message=str(e))
                raise
        
        return wrapper
    return decorator


# Example usage and demonstration
def demonstrate_ethical_logging():
    """Demonstrate the ethical logging functionality."""
    
    # Initialize logger
    logger = EthicalLogger("demo_app", "demo.log")
    
    print("=== Ethical Logging Demonstration ===\n")
    
    # Example 1: Basic logging
    logger.info("User login attempt", user_id="user123", ip="192.168.1.100")
    
    # Example 2: Logging with sensitive data (will be filtered)
    logger.warning("Authentication failed", 
                  username="john.doe@example.com",
                  password="secret123",
                  ip="10.0.0.1")
    
    # Example 3: Logging user actions
    logger.info("User profile updated", 
               user_id="user456",
               changes={"email": "new@example.com", "phone": "555-1234"})
    
    # Example 4: Error logging
    try:
        # Simulate an error
        raise ValueError("Invalid input data")
    except Exception as e:
        logger.error("Data validation failed", 
                    input_data={"email": "test@example.com", "ssn": "123-45-6789"},
                    error=str(e))
    
    # Example 5: Using the decorator
    @log_function_call(logger, include_args=True, include_result=True)
    def process_user_data(user_id: str, email: str, password: str):
        """Example function that processes user data."""
        return {"status": "success", "user_id": user_id}
    
    # Call the decorated function
    process_user_data("user789", "user@example.com", "mypassword123")
    
    print("\n=== Log entries created (check demo.log file) ===")
    print("Notice how sensitive data is automatically filtered and masked!")


if __name__ == "__main__":
    demonstrate_ethical_logging()
