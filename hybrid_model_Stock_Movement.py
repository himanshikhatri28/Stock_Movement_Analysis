# Import required liabraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.decomposition import PCA
from textblob import TextBlob

# Load preprocessed stock signals data
df = pd.read_csv('c:/Users/Macbook/Desktop/ml stock project/processed_stock_signals.csv')
print(df.head()) # Display the first few rows to understand the dataset structure

# Step 1: Feature Engineering for the "Option" column
# Extract numeric part from "Option" (e.g., 49900 from 49900CE)
df['Option Numeric'] = df['Option'].str.extract(r'(\d+)', expand = False).astype(int)

# Extract text part from "Option" (e.g, CE or PE)
df['Option Type'] = df['Option'].str.extract(r'([A-Za-z]+)', expand = False)

# Encode "Option Type" using LabelEncoder
le = LabelEncoder()
df['Option Type Encoded'] = le.fit_transform(df['Option Type'])


# Step 2:  Convert "Stop Loss" column to numeric labels (1 for SL Paid, 0 for SL Unpaid)
df['Stop Loss'] = df['Stop Loss'].apply(lambda x : 1 if 'SL Paid' in x else 0)

# Step 3: Define feature variables (Trigger Price, Target price) and target variable (Stop Loss)
X = df[['Trigger Price', 'Target price','Option Numeric','Option Type Encoded']]
y = df['Stop Loss']

# Step 4: Split the data into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)


# Step 5: Apply PCA to reduce dimensions to 2 components
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Step 6: Train a Naive Bayes classifier on the PCA-transformed training data
naive_bayes_model = GaussianNB()
naive_bayes_model.fit(X_train_pca, y_train)

# Step 7: Predict using the trained model on the test data
nb_pred = naive_bayes_model.predict(X_test_pca)

# Step 8: Evaluate the model's performance using accuracy score
nb_accuracy = accuracy_score(y_test, nb_pred)
print(f"Naive Bayes Accuracy: {nb_accuracy * 100:.2f}%\n")

# Print the classification report
print("Naive Bayes Classification Report:")
print(classification_report(y_test, nb_pred, target_names=["SL Unpaid", "SL Paid"]))

# Compute the confusion matrix
cm = confusion_matrix(y_test, nb_pred)
print("\nConfusion Matrix:\n", cm)

# Step 9: Visualization
# Confusion Matrix Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=True, xticklabels=["0 (SL Unpaid)", "1 (SL Paid)"],
yticklabels=["0 (SL Unpaid)", "1 (SL Paid)"], linewidths=0.5, square=True, linecolor='black')
plt.title("Confusion Matrix Heatmap", fontsize = 16)
plt.xlabel("Predicted Label", fontsize = 12)
plt.ylabel("True Label", fontsize = 12)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.tight_layout()
plt.show()

# Visualize PCA Scatter Plot
plt.figure(figsize=(10,6))
scatter = plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c= y_test, cmap='viridis', edgecolors='k', alpha=0.8, s= 120)
plt.title('Scatter Plot of PCA Components', fontsize = 16)
plt.xlabel('Principal Component 1', fontsize = 12)
plt.ylabel('Principal Component 2', fontsize = 12)
plt.grid(color = 'grey', linestyle= '--', linewidth =0.5, alpha = 0.7)
colorbar = plt.colorbar(scatter)
colorbar.set_label("True Labels", fontsize = 12)
plt.tight_layout()
plt.show()

# Prediction vs. Actual Stock Movement line Chart
plt.figure(figsize=(12, 6))
plt.plot(range(len(y_test)), y_test, label="Actual Values", color="blue", linestyle="solid", linewidth=2)
plt.plot(range(len(nb_pred)), nb_pred, label="Predicted Values", color="orange", linestyle="dashed", linewidth=2, alpha=0.8)
plt.title("Stock Movement Prediction -- Actual vs Predicted", fontsize=16)
plt.xlabel("Data Points (Index)", fontsize=12)
plt.ylabel("Stock Movement (0 = SL Unpaid, 1 = SL Paid)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()

