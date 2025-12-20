#!/bin/bash
echo "=== Testing Jenkins Commands Locally ==="
echo "Current directory: $(pwd)"
echo ""
echo "1. Python version:"
python3 --version
echo ""
echo "2. Pip version:"
pip3 --version
echo ""
echo "3. Installing requirements..."
pip3 install -r requirements.txt
echo ""
echo "4. Running migrations..."
python3 manage.py migrate --noinput
echo ""
echo "5. Running Django tests..."
python3 manage.py test chats.tests --verbosity=2
echo ""
echo "6. Running Pytest..."
python3 -m pytest chats/tests.py -v --tb=short
echo ""
echo "=== Local Test Complete ==="
