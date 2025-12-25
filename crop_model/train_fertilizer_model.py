import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# ==============================
# LOAD CSV SAFELY
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "Fertilizer Prediction.csv")

data = pd.read_csv(csv_path)

# ==============================
# RENAME COLUMNS FIRST ✅
# ==============================
# ✅ Fix wrong column names
data.rename(columns={
    'Temparature': 'Temperature',
    'Humidity ': 'Humidity'
}, inplace=True)


# ✅ DEBUG: CHECK COLUMN NAMES
print("✅ Available columns:", list(data.columns))

# ✅ NOW THIS WILL WORK
print("\n✅ Fertilizer class distribution:\n")
print(data['Fertilizer_Name'].value_counts())

# ==============================
# ENCODE CATEGORICAL COLUMNS
# ==============================
le_crop = LabelEncoder()
le_soil = LabelEncoder()

data['Crop_Type'] = le_crop.fit_transform(data['Crop_Type'])
data['Soil_Type'] = le_soil.fit_transform(data['Soil_Type'])

# ==============================
# FEATURES & TARGET
# ==============================
X = data.drop('Fertilizer_Name', axis=1)
y = data['Fertilizer_Name']

# ==============================
# TRAIN-TEST SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y   # ✅ VERY IMPORTANT for imbalance
)

# ==============================
# BALANCED DECISION TREE ✅
# ==============================
model = DecisionTreeClassifier(
    class_weight="balanced",
    max_depth=6,
    min_samples_split=10,
    random_state=42
)

model.fit(X_train, y_train)

# ==============================
# SAVE MODEL & ENCODERS
# ==============================
with open(os.path.join(BASE_DIR, "fertilizer_model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(BASE_DIR, "crop_encoder.pkl"), "wb") as f:
    pickle.dump(le_crop, f)

with open(os.path.join(BASE_DIR, "soil_encoder.pkl"), "wb") as f:
    pickle.dump(le_soil, f)

print("\n✅ Fertilizer model trained & saved successfully")
