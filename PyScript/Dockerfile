# Step 1: Use the official Python image as the base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the script and other necessary files to the container
COPY PythonScript.py /app/PythonScript.py
COPY requirements.txt /app/requirements.txt

# Step 4: Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Specify the command to run the script
CMD ["python", "PythonScript.py"]
