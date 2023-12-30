# Use the official Python image as the base image
FROM python:3.11-slim

ENV THRESHOLD_VALUE=0.5

# Set the working directory in the container
WORKDIR /app

# Copy the local requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the local code to the container
COPY main_module.py .
COPY server.py .
COPY index.html .
COPY favicon.ico .

# Expose the port that the FastAPI application will run on (adjust as needed)
EXPOSE 80

# Start the FastAPI application
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]