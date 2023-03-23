FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install --upgrade pip && \
  pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install --no-dev

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]