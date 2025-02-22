# tasks.py
from celery import Celery

# Configure Celery to use Redis as a broker
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_data(data):
    # Simulate processing data
    result = f"Processed {data}"
    return result
