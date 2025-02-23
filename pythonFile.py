from tasks import process_recommendation
process_recommendation.delay(1)  # Run the task directly

# from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//')

# # Force Celery to pull any available tasks
# app.control.revoke('celery', terminate=True)
