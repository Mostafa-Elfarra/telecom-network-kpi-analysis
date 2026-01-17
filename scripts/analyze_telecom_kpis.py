import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# تحديد مسار المشروع
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "telecom_kpi_data.csv"
VISUALS_DIR = BASE_DIR / "visuals"

# إنشاء مجلد الرسومات إن لم يكن موجودًا
VISUALS_DIR.mkdir(exist_ok=True)

# قراءة البيانات
df = pd.read_csv(DATA_FILE)

print("Data loaded successfully")
print(df.head())
