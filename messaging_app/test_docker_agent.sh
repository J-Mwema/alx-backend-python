#!/bin/bash
echo "=== Testing Docker Agent Commands ==="
echo ""
echo "1. Testing Python Docker image pull..."
docker pull python:3.8-slim
echo ""
echo "2. Testing Docker run with Python..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim python --version
echo ""
echo "3. Testing pip install..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim pip --version
echo ""
echo "4. Testing requirements installation..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim pip install -r requirements.txt
echo ""
echo "5. Testing Django..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim python manage.py --version
echo ""
echo "=== Docker Agent Test Complete ==="
