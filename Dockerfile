FROM python:3.8-slim

# Install the dependencies for the app
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the app code into the image
COPY . .

# Run the app when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]