broker_url = 'redis://localhost:6379/0'  # Ensure Redis is set correctly
result_backend = 'redis://localhost:6379/0'  # Enable results tracking

task_routes = {
    'tasks.process_recommendation': {'queue': 'celery'}
}

accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'
timezone = 'UTC'
enable_utc = True
