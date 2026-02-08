# 1. Use an official Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirement.txt .

RUN pip install --no-cache-dir --progress-bar off -r requirement.txt

# 4. Copy the rest of your application code
COPY . .

# 5. Expose the port Flask runs on
EXPOSE 5000

# 6. Command to run the application
CMD ["python", "app.py"]