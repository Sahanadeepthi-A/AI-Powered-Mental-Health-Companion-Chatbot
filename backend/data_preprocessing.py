import pandas as pd
import os

# Ensure output directory exists
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/student_mental_health.csv")

print("Columns found in dataset:")
print(df.columns)

# Keep only required columns
df = df[["statement", "status"]]

# Normalize labels into controlled categories
def normalize_label(label):
    label = label.lower()
    if label == "suicidal":
        return "Severe Distress"
    elif label in ["depression", "depressed"]:
        return "Depression"
    elif label in ["anxiety", "stress"]:
        return "Anxiety"
    else:
        return "Normal"

df["label"] = df["status"].apply(normalize_label)

# Rename for ML pipeline consistency
df.rename(columns={"statement": "text"}, inplace=True)

df = df[["text", "label"]]

# Save processed data
df.to_csv("data/processed/training_data.csv", index=False)

print("✅ Data preprocessing completed successfully")
print("\nLabel distribution:")
print(df["label"].value_counts())

