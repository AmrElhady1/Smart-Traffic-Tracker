FROM python:3.10-slim

# Create a non-root user (Required by Hugging Face Spaces)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Switch to root to install system dependencies for OpenCV
USER root
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev ffmpeg \
    && rm -rf /var/lib/apt/lists/*
    
# Switch back to user
USER user

# Install Python dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY --chown=user . .

# Expose the Gradio port
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]