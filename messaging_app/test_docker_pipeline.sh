#!/bin/bash
echo "=== Testing Docker Pipeline Commands ==="
echo ""
echo "1. Testing Python Docker image..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim python --version
echo ""
echo "2. Testing pip installation..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim pip --version
echo ""
echo "3. Testing Django..."
docker run --rm -v $(pwd):/app -w /app python:3.8-slim bash -c "pip install django && python -c 'import django; print(django.__version__)'"
echo ""
echo "=== Docker Test Complete ==="
