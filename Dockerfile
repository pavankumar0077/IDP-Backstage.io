FROM python:3.10-alpine

# Install build dependencies needed for psutil
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev linux-headers

# Copy and install Python dependencies
COPY requirements.txt /temp/
RUN pip install --no-cache-dir -r /temp/requirements.txt

# Copy application source code
COPY src /src
WORKDIR /src

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
