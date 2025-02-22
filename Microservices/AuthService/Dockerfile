FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .  # Copy dependency file
RUN pip install -r requirements.txt  # Install dependencies
COPY . .  # Copy application code
EXPOSE 5001
CMD ["python", "auth_service.py"]
