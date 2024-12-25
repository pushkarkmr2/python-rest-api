# Use Python 3.11 image as base
FROM python:3.11-slim
#FROM python:alpine3.6

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/
COPY appFlask.py /app/
COPY appAiohttp.py /app/
#COPY . /

# Install the required Python dependencies
RUN pip install flask==0.10.1
RUN pip install --no-cache-dir aiohttp


# Expose the port the app runs on
#EXPOSE 8080

ENTRYPOINT ["python"]

# Command to run the application
CMD ["-u", "appFlask.py"]
#CMD ["-u", "appAiohttp.py"]
#CMD ["-u", "app.py"]



