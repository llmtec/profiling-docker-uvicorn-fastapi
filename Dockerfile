# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install fastapi uvicorn

# Define an argument for enabling profiling (this default value is overwritten by any env argument given at runtime)
ARG PROFILE_APP=false

# Make the ARG value available as an environment variable
ENV PROFILE_APP=${PROFILE_APP}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]