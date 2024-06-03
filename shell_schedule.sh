#!/bin/bash

# Function to convert current time to EST
get_current_time_est() {
  date +'%H:%M' -d "$(date -u) -5 hours"
}

# Desired time to trigger the Python script (10:30 PM EST)
target_time="22:30"

while true; do
  current_time=$(get_current_time_est)
  
  if [ "$current_time" == "$target_time" ]; then
    # Run the Python script
    python3 /path/to/your_script.py
    break
  fi
  
  # Wait for 1 minute before checking the time again
  sleep 60
done
