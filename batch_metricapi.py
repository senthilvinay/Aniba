from datetime import datetime

data = {
    "HumanReadableDate": "Apr 30 2025",
    "MonthLabel": 1745971200,
    "EarliestStart": 8611,
    "LatestEnd": 8777,
    "Start": 8611,
    "End": 8777,
    "Consumption": 0.0,
    "AverageDuration": 166,
    "JobCond": "C"
}

# Function to safely convert timestamp
def convert_timestamp(ts):
    try:
        # Assume seconds (Unix Epoch)
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return "Invalid timestamp"

# Convert possible timestamps
timestamp_fields = ["MonthLabel", "EarliestStart", "LatestEnd", "Start", "End"]
for field in timestamp_fields:
    human_readable = convert_timestamp(data[field])
    print(f"{field}: {human_readable}")
