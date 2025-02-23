
from tasks import process_recommendation
import time

# Sample patients' data (each list represents one patient)
patients_data = [
    [0.8, 0.6, 0.7, 0.9, 0.5],  # Patient 1
    [0.3, 0.2, 0.4, 0.1, 0.5],  # Patient 2
    [0.6, 0.9, 0.8, 0.3, 0.7],  # Patient 3
    [0.5, 0.7, 0.6, 0.2, 0.8],  # Patient 4
    [0.9, 0.4, 0.3, 0.6, 0.7],  # Patient 5
]

# Send tasks for each patient's data
for i, data in enumerate(patients_data):
    task = process_recommendation.delay(data)
    print(f"Task sent for Patient {i+1} with ID: {task.id}")
    time.sleep(1)  # Small delay to avoid overloading

print("✅ All patient tasks sent successfully!")
