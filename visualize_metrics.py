import redis
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Fetch task metrics from Redis
task_metrics = redis_client.get('task_metrics')

if task_metrics:
    data = json.loads(task_metrics)
    
    # Convert timestamps to datetime format
    timestamps = [datetime.strptime(ts, "%H:%M:%S") for ts in data['timestamps']]
    durations = data['durations']

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, durations, marker='o', linestyle='-', color='b', label="Execution Time")

    # Add labels for each point
    for i, txt in enumerate(durations):
        plt.annotate(f"{txt:.5f}", (timestamps[i], durations[i]), textcoords="offset points", xytext=(0,10), ha='center')

    # Formatting the plot
    plt.xlabel('Timestamp')
    plt.ylabel('Execution Duration (seconds)')
    plt.title('Task Execution Times')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig("task_execution_metrics.png")

    # Show the plot
    plt.show()

    print("✅ Chart saved as 'task_execution_metrics.png'.")

else:
    print("⚠️ No task metrics found in Redis.")
