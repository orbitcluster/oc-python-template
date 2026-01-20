# Define the base image for Python environment
ARG PYTHON_BASE=python:3.13-slim

# Define the working directory
ARG WORKDIR="/app"
# Define the source path for the applicaion code
ARG SRC_PATH="src"

# Define the main executable file
ARG MAIN_EXECUTABLE="src/api/server.py"

# Define the container port
ARG CONTAINER_PORT=5000

# Builder stage
FROM ${PYTHON_BASE} AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --no-compile -r requirements.txt

# Final stage
FROM ${PYTHON_BASE}

# Re-declare ARGs to use them after FROM
ARG WORKDIR
ARG SRC_PATH
ARG MAIN_EXECUTABLE
ARG CONTAINER_PORT

# Set environment variables to use it downstream
ENV WORKDIR=${WORKDIR} \
    SRC_PATH=${SRC_PATH} \
    CONTAINER_PORT=${CONTAINER_PORT} \
    PORT=${CONTAINER_PORT} \
    MAIN_EXECUTABLE=${MAIN_EXECUTABLE} \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies and security updates
RUN apt-get update \
    && apt-get install -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set working directory
WORKDIR ${WORKDIR}
RUN chown appuser:appgroup ${WORKDIR}

# Copy installed dependencies from builder
COPY --from=builder /usr/local /usr/local

# Copy application code
COPY --chown=appuser:appgroup ${SRC_PATH}/ ./${SRC_PATH}/

USER appuser

EXPOSE ${CONTAINER_PORT}
CMD exec python ${MAIN_EXECUTABLE}
