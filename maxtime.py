from datetime import datetime

# List of time strings
timelist = ['2024-08-30 11:20:33 PM', '2024-08-30 11:20:36 PM', '2024-08-30 11:20:39 PM']

# Convert the strings to datetime objects
datetime_list = [datetime.strptime(time, '%Y-%m-%d %I:%M:%S %p') for time in timelist]

# Find the maximum datetime
max_time = max(datetime_list)

# Convert back to string if needed
max_time_str = max_time.strftime('%Y-%m-%d %I:%M:%S %p')

# Print the result
print("The latest time is:", max_time_str)
