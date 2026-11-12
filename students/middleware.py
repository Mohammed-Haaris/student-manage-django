import time

class APILoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        print("API METHOD :", request.path)
        print("HTTP METHOD :", request.method)

        end_time = time.time()

        execution_time = end_time - start_time

        response = self.get_response(request)

        print("STATUS CODE :", response.status_code)
        print("EXECUTION TIME:", execution_time)

        return response