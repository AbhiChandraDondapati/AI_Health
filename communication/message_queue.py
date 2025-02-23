from celery import Celery

# Configure Celery to use RabbitMQ
celery_app = Celery('AI_Health', broker='pyamqp://guest@localhost//')

@celery_app.task
def send_message(agent_name, data):
    print(f"📨 Message received by {agent_name}: {data}")
    return f"✅ Processed by {agent_name}"
