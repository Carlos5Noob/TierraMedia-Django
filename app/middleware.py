import time

class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        total_time = time.time() - start_time
        print(f"Tiempo de respuesta: {total_time:.4f} segundos")
        return response