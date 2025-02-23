from celery import Celery
import celeryconfig
import redis
import time
import json
from communication.message_queue import send_message


# Initialize Celery
celery = Celery('tasks')
celery.config_from_object(celeryconfig)

# Redis for storing task metrics
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@celery.task
def process_recommendation(recommendation):
    """Background task to process treatment recommendations."""
    start_time = time.time()

    print(f"✅ Processing Recommendation: {recommendation}")
    
    result = {"status": "processed", "recommendation": recommendation}
    
    # Log processing time
    end_time = time.time()
    duration = end_time - start_time

    # Store data in Redis
    task_data = redis_client.get("task_metrics")
    if task_data:
        task_data = json.loads(task_data)
    else:
        task_data = {"timestamps": [], "durations": []}
    
    task_data["timestamps"].append(time.strftime("%H:%M:%S"))
    task_data["durations"].append(duration)

    redis_client.set("task_metrics", json.dumps(task_data))

    return result


from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_recommendation(data):
    print(f"📌 Task Started for Data: {data}")  # ADD THIS LINE
    result = sum(data) / len(data)  # Example processing
    print(f"✅ Task Completed: {result}")  # ADD THIS LINE
    return result





# from celery import Celery
# import celeryconfig

# # Initialize Celery
# celery = Celery('tasks')
# celery.config_from_object(celeryconfig)

# @celery.task
# def process_recommendation(recommendation):
#     """Background task to process treatment recommendations."""
#     print(f"✅ Processing Recommendation: {recommendation}")
#     return {"status": "processed", "recommendation": recommendation}
