#!/bin/bash
echo "=== Testing Jenkinsfile Commands ==="
echo ""
echo "1. Current directory and files:"
pwd
ls -la
echo ""
echo "2. Python and pip versions:"
python3 --version
pip3 --version
echo ""
echo "3. Installing requirements:"
pip3 install -r requirements.txt
echo ""
echo "4. Installing pytest:"
pip3 install pytest pytest-django
echo ""
echo "5. Running tests with pytest:"
python3 -m pytest chats/tests.py -v --tb=short
echo ""
echo "=== Test Complete ==="
