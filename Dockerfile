# 1. Base image
FROM python:3.11

# 2. Set the working directory inside the container
WORKDIR /usr/src/app

# 3. Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all your actual code into the container
COPY . .

# 5. Command to run the application when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]