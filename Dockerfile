# Use Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all the contents from your local directory into the container
COPY . /app

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
