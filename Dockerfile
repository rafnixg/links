# Multi-stage Dockerfile for LinkBioSite Static Site Generator
# Stage 1: Builder stage for installing dependencies
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.11-slim as runtime

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Install runtime system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Create app user
RUN useradd --create-home --shell /bin/bash linkbiosite

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install the package in editable mode for development
RUN pip install -e .

# Create directories for volume mounting
RUN mkdir -p /app/project /app/output && \
    chown -R linkbiosite:linkbiosite /app

# Switch to non-root user
USER linkbiosite

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import linkbiosite; print('LinkBioSite is healthy')" || exit 1

# Default command - can be overridden
CMD ["linkbiosite", "--help"]

# Stage 3: Production stage for serving built sites
FROM nginx:alpine as production

# Copy built site to nginx
COPY --from=runtime /app/output /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port
EXPOSE 80

# Health check for nginx
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]