import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# مسارات
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "telecom_kpi_data.csv"
VISUALS_DIR = BASE_DIR / "visuals"
VISUALS_DIR.mkdir(exist_ok=True)

# قراءة البيانات
df = pd.read_csv(DATA_FILE)
print("Data loaded successfully")
print(df.head())

# حساب KPIs
avg_drop_rate = df["call_drop_rate"].mean()
avg_throughput = df["throughput_mbps"].mean()
avg_latency = df["latency_ms"].mean()

print("\n--- Network KPIs ---")
print(f"Average Call Drop Rate: {avg_drop_rate:.2f}%")
print(f"Average Throughput: {avg_throughput:.2f} Mbps")
print(f"Average Latency: {avg_latency:.2f} ms")

# Visualization
# 1. Call Drop Rate Distribution
plt.figure()
plt.hist(df["call_drop_rate"], bins=15)
plt.xlabel("Call Drop Rate (%)")
plt.ylabel("Number of Cells")
plt.title("Call Drop Rate Distribution")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "call_drop_rate_distribution.png")
plt.close()

# 2. Throughput per Region
region_throughput = df.groupby("region")["throughput_mbps"].mean()
plt.figure()
region_throughput.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Average Throughput (Mbps)")
plt.title("Average Throughput per Region")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "throughput_per_region.png")
plt.close()

print("Analysis and visuals done!")
