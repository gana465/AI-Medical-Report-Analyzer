import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("kidney_disease.csv")

# Remove unnecessary columns if present
if 'id' in df.columns:
    df.drop('id', axis=1, inplace=True)

# Convert target column
df['classification'] = df['classification'].map({
    'ckd': 1,
    'notckd': 0
})

# Keep only numeric columns
X = df.select_dtypes(include=['int64', 'float64'])

# Target
y = df['classification']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline
model = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('classifier', RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "kidney_model.pkl")

print("Model Saved Successfully!")