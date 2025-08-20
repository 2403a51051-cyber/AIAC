import hashlib
import uuid

# Python script to collect user data and suggestions for data protection/anonymization

# Collect user data
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

# Display collected data (for demonstration purposes)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")

# --- Data Protection and Anonymization Suggestions ---

# 1. Do not store sensitive data (like emails) in plain text.
#    Instead, hash the email before storing it.

def hash_email(email):
  # Hash the email using SHA-256
  return hashlib.sha256(email.encode()).hexdigest()

hashed_email = hash_email(email)
print(f"Hashed Email (for storage): {hashed_email}")

# 2. Avoid storing names if not necessary, or replace with pseudonyms.
#    For example, generate a random user ID instead of using the real name.

user_id = str(uuid.uuid4())
print(f"Generated User ID (instead of name): {user_id}")

# 3. Store age only if required, and consider storing age range instead of exact age.
def get_age_range(age):
  age = int(age)
  if age < 18:
    return "Under 18"
  elif age < 30:
    return "18-29"
  elif age < 50:
    return "30-49"
  else:
    return "50+"

age_range = get_age_range(age)
print(f"Age Range (for anonymization): {age_range}")

# 4. Always use secure storage (e.g., encrypted databases) for any sensitive information.
#    Never log or print sensitive data in production environments.

# 5. If sharing data, remove or mask direct identifiers (name, email) and use anonymized fields.