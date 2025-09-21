# Use official Python image
FROM python:3.10-slim

WORKDIR /app

# Copy dependencies files
COPY . ./

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the default Chainlit port
EXPOSE 8000

# Terminal Command to run the app
CMD ["python", "-m", "chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8000", "-w"]