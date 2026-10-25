from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_csv(ROOT / "data" / "train.csv")

# Drop identifier columns, split features/target
df = df.drop(columns=[c for c in ["Unnamed: 0", "id"] if c in df.columns])
y = (df["satisfaction"] == "satisfied").astype(int)
X = df.drop(columns=["satisfaction"])

features = list(X.columns)  # exact input order
cat_cols = X.select_dtypes(exclude="number").columns.tolist()
num_cols = [c for c in features if c not in cat_cols]

num_pipe = Pipeline([("impute", SimpleImputer(strategy="median")),
                     ("scale", StandardScaler())])
cat_pipe = Pipeline([("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                     ("scale", StandardScaler())])
preprocess = ColumnTransformer([("num", num_pipe, num_cols),
                                ("cat", cat_pipe, cat_cols)])

model = HistGradientBoostingClassifier(
    max_iter=300, learning_rate=0.08, max_depth=12, random_state=42)
pipeline = Pipeline([("preprocess", preprocess), ("model", model)])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42)
pipeline.fit(X_train, y_train)

pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print("F1:", f1_score(y_test, pred))
print(classification_report(y_test, pred))

bundle = {
    "pipeline": pipeline,
    "features": features,
    "task": "classification",
    "labels": {0: "neutral or dissatisfied", 1: "satisfied"},
    "model_version": "1.0",
}
(ROOT / "backend" / "models").mkdir(parents=True, exist_ok=True)
joblib.dump(bundle, ROOT / "backend" / "models" / "model_bundle.joblib")

X_test.head(1).to_csv(ROOT / "data" / "sample_inputs.csv", index=False)
print("Saved bundle with", len(features), "features")