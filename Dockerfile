# Use Python 3.10 base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy local code into container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI’s port
EXPOSE 8000

# Command to run API server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
