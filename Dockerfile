# Use slim Python base image to reduce build time and image size
FROM python:3.9-slim AS builder

WORKDIR /app

# Install only required build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment to isolate our package dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install wheel for building packages
RUN pip install --no-cache-dir --upgrade pip wheel setuptools

# Copy requirements file
COPY requirements.txt .

# Install dependencies in a specific order to resolve conflicts
# First, install core dependencies
RUN pip install --no-cache-dir -r requirements.txt
    
# Clean up to reduce image size
RUN find /opt/venv -name "*.pyc" -delete && \
    find /opt/venv -name "__pycache__" -exec rm -rf {} \; 2>/dev/null || true && \
    rm -rf /root/.cache /tmp/*

# Final stage with minimal image size
FROM python:3.9-slim AS final

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Make sure we use the virtual environment:
ENV PATH="/opt/venv/bin:$PATH"

# Copy application files (only what's needed)
COPY main.py ./
COPY config/ ./config/
COPY services/ ./services/
COPY routes/ ./routes/
COPY models/ ./models/
COPY repositories/ ./repos/

# Expose the port FastAPI runs on
EXPOSE 8000

# Set environment for production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run the application with dotenvx to handle encrypted environment variables
# The DOTENV_PRIVATE_KEY will be provided as an environment variable when running the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]