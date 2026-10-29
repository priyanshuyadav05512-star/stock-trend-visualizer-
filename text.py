import yfinance as yf
import matplotlib.pyplot as plt

#  Stock symbol (add .NS for NSE-listed companies)
stock = "RELIANCE.NS"

# yfinance returns multi-level column names; keep only the top level (Close, Volume, etc.)
data = yf.download(stock, period="1y", auto_adjust=True)
data.columns = data.columns.get_level_values(0)

# Calculate moving averages (average of the last N days' closing prices)
data["MA20"] = data["Close"].rolling(20).mean()
data["MA50"] = data["Close"].rolling(50).mean()

#  Create a figure with 2 charts stacked vertically
# The top chart is 3x taller than the bottom one, and both share the same x-axis (dates)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8),
                               sharex=True,
                               gridspec_kw={"height_ratios": [3, 1]})

# Top chart: closing price with both moving averages
ax1.plot(data["Close"], label="Close Price", color="black")
ax1.plot(data["MA20"], label="20-Day MA", color="blue")
ax1.plot(data["MA50"], label="50-Day MA", color="red")
ax1.set_title(f"{stock} - Price Trend (1 Year)")
ax1.set_ylabel("Price (₹)")
ax1.legend()
ax1.grid(alpha=0.3)

# Bottom chart: trading volume as bars
ax2.bar(data.index, data["Volume"], color="gray")
ax2.set_ylabel("Volume")

plt.tight_layout()
plt.show()