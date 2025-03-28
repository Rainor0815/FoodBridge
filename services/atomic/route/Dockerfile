FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Load environment variables from .env file
# Note: Ensure .env file is not committed to version control for security reasons.
# COPY .env .

# Run app.py when the container launches
CMD ["python", "route.py"]