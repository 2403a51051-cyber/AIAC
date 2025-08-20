"""
Responsible Machine Learning Classification Model

This program demonstrates how to train, evaluate, and deploy a machine learning model
while considering ethical implications, bias detection, and fairness.

RESPONSIBLE AI GUIDELINES:
- Always validate data quality and representativeness
- Test for bias across different demographic groups
- Provide model explanations for transparency
- Monitor model performance continuously
- Document limitations and assumptions
- Consider societal impact of predictions

LIMITATIONS & RISKS:
- This is a simple model for educational purposes
- Real-world applications require more sophisticated approaches
- Accuracy may vary significantly across different populations
- Bias detection is basic and may miss subtle forms of discrimination
- Fairness metrics are simplified and may not capture all concerns

FAIRNESS CONSIDERATIONS:
- Models can perpetuate existing societal biases
- Different groups may experience different error rates
- Historical data may contain discriminatory patterns
- Regular bias audits are essential for production systems
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report, 
                           confusion_matrix, roc_auc_score)
from sklearn.preprocessing import StandardScaler
import shap
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

class ResponsibleMLModel:
    """
    A machine learning model wrapper that includes bias detection,
    fairness metrics, and explainability features.
    
    This class demonstrates responsible AI practices including:
    - Bias detection across different groups
    - Fairness metrics calculation
    - Model explainability using SHAP
    - Performance monitoring
    """
    
    def __init__(self, model=None, sensitive_features=None):
        """
        Initialize the responsible ML model.
        
        Args:
            model: The machine learning model to use
            sensitive_features: List of sensitive attribute names for fairness analysis
        """
        self.model = model or RandomForestClassifier(n_estimators=100, random_state=42)
        self.sensitive_features = sensitive_features or []
        self.scaler = StandardScaler()
        self.feature_names = None
        self.explainer = None
        self.bias_metrics = {}
        
    def prepare_data(self, X, y, test_size=0.2, random_state=42):
        """
        Prepare and split the data for training and testing.
        
        Args:
            X: Feature matrix
            y: Target variable
            test_size: Proportion of data for testing
            random_state: Random seed for reproducibility
        """
        # Store feature names for interpretability
        if hasattr(X, 'columns'):
            self.feature_names = list(X.columns)
        else:
            self.feature_names = [f'feature_{i}' for i in range(X.shape[1])]
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
        
        # Scale features (important for fairness analysis)
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        return X_train_scaled, X_test_scaled, y_train, y_test
    
    def train(self, X_train, y_train):
        """
        Train the model and prepare explainability tools.
        
        Args:
            X_train: Training features
            y_train: Training targets
        """
        print("Training model...")
        self.model.fit(X_train, y_train)
        
        # Prepare SHAP explainer for model interpretability
        print("Preparing explainability tools...")
        self.explainer = shap.TreeExplainer(self.model)
        
        print("Model training completed!")
    
    def evaluate_performance(self, X_test, y_test):
        """
        Evaluate model performance with comprehensive metrics.
        
        Args:
            X_test: Test features
            y_test: Test targets
            
        Returns:
            dict: Performance metrics
        """
        print("\n=== MODEL PERFORMANCE EVALUATION ===")
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_proba)
        
        print(f"Accuracy: {accuracy:.4f}")
        print(f"ROC AUC: {auc:.4f}")
        
        # Detailed classification report
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        print("\nConfusion Matrix:")
        print(cm)
        
        # Cross-validation score for robustness
        cv_scores = cross_val_score(self.model, X_test, y_test, cv=5)
        print(f"\nCross-validation scores: {cv_scores}")
        print(f"CV Mean: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
        
        return {
            'accuracy': accuracy,
            'auc': auc,
            'cv_scores': cv_scores,
            'confusion_matrix': cm
        }
    
    def detect_bias(self, X_test, y_test, sensitive_attr_name, sensitive_attr_values):
        """
        Detect bias across different groups defined by sensitive attributes.
        
        Args:
            X_test: Test features
            y_test: Test targets
            sensitive_attr_name: Name of the sensitive attribute
            sensitive_attr_values: Values of the sensitive attribute
            
        Returns:
            dict: Bias metrics for each group
        """
        print(f"\n=== BIAS DETECTION FOR {sensitive_attr_name.upper()} ===")
        
        bias_metrics = {}
        y_pred = self.model.predict(X_test)
        
        # Calculate metrics for each group
        for value in np.unique(sensitive_attr_values):
            mask = sensitive_attr_values == value
            group_y_true = y_test[mask]
            group_y_pred = y_pred[mask]
            
            if len(group_y_true) > 0:
                group_accuracy = accuracy_score(group_y_true, group_y_pred)
                group_size = len(group_y_true)
                
                bias_metrics[value] = {
                    'accuracy': group_accuracy,
                    'size': group_size,
                    'error_rate': 1 - group_accuracy
                }
                
                print(f"\nGroup {value}:")
                print(f"  Size: {group_size}")
                print(f"  Accuracy: {group_accuracy:.4f}")
                print(f"  Error Rate: {1 - group_accuracy:.4f}")
        
        # Calculate fairness metrics
        if len(bias_metrics) >= 2:
            accuracies = [metrics['accuracy'] for metrics in bias_metrics.values()]
            max_acc = max(accuracies)
            min_acc = min(accuracies)
            
            # Statistical parity difference (simplified)
            parity_diff = max_acc - min_acc
            
            print(f"\nFairness Metrics:")
            print(f"  Accuracy Gap: {parity_diff:.4f}")
            print(f"  Relative Accuracy Gap: {parity_diff/max_acc:.2%}")
            
            # Flag potential bias
            if parity_diff > 0.1:  # 10% threshold
                print("  ⚠️  WARNING: Potential bias detected!")
                print("     Consider investigating data quality and model fairness.")
            else:
                print("  ✅ No significant bias detected in this analysis.")
        
        self.bias_metrics[sensitive_attr_name] = bias_metrics
        return bias_metrics
    
    def explain_prediction(self, X_sample, feature_names=None):
        """
        Explain a single prediction using SHAP values.
        
        Args:
            X_sample: Single sample to explain
            feature_names: Names of features for interpretability
        """
        if self.explainer is None:
            print("Model explainer not available. Train the model first.")
            return
        
        if feature_names is None:
            feature_names = self.feature_names
        
        print(f"\n=== PREDICTION EXPLANATION ===")
        
        # Get SHAP values
        shap_values = self.explainer.shap_values(X_sample)
        
        # Make prediction
        prediction = self.model.predict(X_sample)[0]
        prediction_proba = self.model.predict_proba(X_sample)[0]
        
        print(f"Prediction: {prediction}")
        print(f"Confidence: {prediction_proba.max():.4f}")
        
        # Show feature importance for this prediction
        if len(shap_values) > 1:  # For classification, get the predicted class
            class_idx = prediction
            shap_values = shap_values[class_idx]
        
        # Create feature importance summary
        feature_importance = list(zip(feature_names, shap_values[0]))
        feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
        
        print("\nTop features influencing this prediction:")
        for feature, importance in feature_importance[:5]:
            direction = "increases" if importance > 0 else "decreases"
            print(f"  {feature}: {importance:.4f} ({direction} prediction)")
    
    def generate_fairness_report(self):
        """
        Generate a comprehensive fairness report.
        
        Returns:
            str: Formatted fairness report
        """
        if not self.bias_metrics:
            return "No bias analysis performed yet."
        
        report = "\n" + "="*60 + "\n"
        report += "FAIRNESS ANALYSIS REPORT\n"
        report += "="*60 + "\n\n"
        
        report += "RESPONSIBLE AI CONSIDERATIONS:\n"
        report += "1. Data Quality: Ensure training data is representative\n"
        report += "2. Bias Monitoring: Regularly check for disparate impact\n"
        report += "3. Transparency: Document model decisions and limitations\n"
        report += "4. Continuous Evaluation: Monitor performance across groups\n"
        report += "5. Human Oversight: Don't rely solely on automated decisions\n\n"
        
        for attr_name, metrics in self.bias_metrics.items():
            report += f"BIAS ANALYSIS FOR {attr_name.upper()}:\n"
            report += "-" * 40 + "\n"
            
            for value, metric in metrics.items():
                report += f"Group {value}:\n"
                report += f"  Size: {metric['size']}\n"
                report += f"  Accuracy: {metric['accuracy']:.4f}\n"
                report += f"  Error Rate: {metric['error_rate']:.4f}\n\n"
        
        report += "LIMITATIONS OF THIS ANALYSIS:\n"
        report += "- Only considers accuracy-based fairness\n"
        report += "- May miss subtle forms of discrimination\n"
        report += "- Does not account for historical biases in data\n"
        report += "- Simplified metrics may not capture all concerns\n\n"
        
        report += "RECOMMENDATIONS:\n"
        report += "- Conduct regular bias audits\n"
        report += "- Include domain experts in model evaluation\n"
        report += "- Consider multiple fairness definitions\n"
        report += "- Monitor for concept drift and bias\n"
        report += "- Implement human-in-the-loop systems\n"
        
        return report


def create_synthetic_dataset(n_samples=1000, n_features=10, n_informative=5, 
                           n_redundant=2, n_classes=2, random_state=42):
    """
    Create a synthetic dataset for demonstration purposes.
    
    WARNING: This is synthetic data for educational purposes only.
    Real-world applications require careful consideration of data sources,
    privacy implications, and representativeness.
    """
    print("Creating synthetic dataset...")
    
    # Generate synthetic classification data
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_informative,
        n_redundant=n_redundant,
        n_classes=n_classes,
        random_state=random_state
    )
    
    # Convert to DataFrame for better interpretability
    feature_names = [f'feature_{i}' for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    
    # Add a synthetic sensitive attribute (for demonstration)
    # In real applications, this would be actual demographic data
    np.random.seed(random_state)
    sensitive_attr = np.random.choice(['group_A', 'group_B', 'group_C'], size=n_samples)
    
    # Introduce some bias for demonstration (this is artificial!)
    bias_mask = (sensitive_attr == 'group_C') & (y == 1)
    y[bias_mask] = np.random.choice([0, 1], size=bias_mask.sum(), p=[0.7, 0.3])
    
    print(f"Dataset created: {n_samples} samples, {n_features} features")
    print(f"Sensitive attribute distribution: {pd.Series(sensitive_attr).value_counts().to_dict()}")
    
    return df, y, sensitive_attr


def main():
    """
    Main function demonstrating responsible ML practices.
    """
    print("="*70)
    print("RESPONSIBLE MACHINE LEARNING DEMONSTRATION")
    print("="*70)
    print("\nThis program demonstrates how to train and evaluate ML models")
    print("while considering ethical implications, bias detection, and fairness.")
    
    # Create synthetic dataset
    X, y, sensitive_attr = create_synthetic_dataset()
    
    # Initialize responsible ML model
    model = ResponsibleMLModel(sensitive_features=['demographic_group'])
    
    # Prepare data
    X_train, X_test, y_train, y_test = model.prepare_data(X, y)
    
    # Train model
    model.train(X_train, y_train)
    
    # Evaluate performance
    performance = model.evaluate_performance(X_test, y_test)
    
    # Detect bias across demographic groups
    bias_metrics = model.detect_bias(X_test, y_test, 'demographic_group', sensitive_attr)
    
    # Explain a sample prediction
    sample_idx = 0
    model.explain_prediction(X_test[sample_idx:sample_idx+1])
    
    # Generate comprehensive fairness report
    fairness_report = model.generate_fairness_report()
    print(fairness_report)
    
    # Final warnings and recommendations
    print("\n" + "="*70)
    print("IMPORTANT DISCLAIMERS AND RECOMMENDATIONS")
    print("="*70)
    print("\n⚠️  THIS IS A DEMONSTRATION MODEL ⚠️")
    print("   - Not suitable for production use")
    print("   - Synthetic data may not reflect real-world patterns")
    print("   - Bias detection is simplified for educational purposes")
    
    print("\n🔒 RESPONSIBLE AI CHECKLIST:")
    print("   □ Validate data quality and representativeness")
    print("   □ Test for bias across different groups")
    print("   □ Document model limitations and assumptions")
    print("   □ Implement human oversight mechanisms")
    print("   □ Monitor for concept drift and bias")
    print("   □ Consider societal impact of predictions")
    print("   □ Regular bias audits and fairness evaluations")
    
    print("\n📚 FOR PRODUCTION SYSTEMS:")
    print("   - Use real, representative data")
    print("   - Implement comprehensive bias detection")
    print("   - Add multiple fairness metrics")
    print("   - Include domain experts in evaluation")
    print("   - Regular model retraining and validation")
    print("   - Human-in-the-loop decision making")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    main()
