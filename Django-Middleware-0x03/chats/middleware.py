from datetime import datetime
import os

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Create the log file path
        self.log_file = os.path.join(os.path.dirname(__file__), 'requests.log')
        #Ensure the file exists
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write('--- Request Log Started ---\n')

        def __call__(self, request):
            user = getattr(request, 'user', 'Anonymous')
            log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
            # Append to log file
            with open(self.log_file, 'a') as f:
                f.write(log_entry)

            # Continue processing the request
            response = self.get_response(request)
            return response
