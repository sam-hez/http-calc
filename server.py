import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


HOST = "localhost"
PORT = 5000


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


class CalculatorHandler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)

        if path == "/":
            self.send_json(200, {
                "message": "Simple calculator server",
                "example": "/add?a=5&b=3"
            })
            return

        if path not in ["/add", "/subtract", "/multiply", "/divide"]:
            self.send_json(404, {"error": "Page not found"})
            return

        if "a" not in query or "b" not in query:
            self.send_json(400, {"error": "Enter both a and b"})
            return

        try:
            a = float(query["a"][0])
            b = float(query["b"][0])
        except ValueError:
            self.send_json(400, {"error": "a and b must be numbers"})
            return

        if path == "/add":
            result = add(a, b)
        elif path == "/subtract":
            result = subtract(a, b)
        elif path == "/multiply":
            result = multiply(a, b)
        else:
            if b == 0:
                self.send_json(400, {"error": "Cannot divide by zero"})
                return
            result = divide(a, b)

        self.send_json(200, {"result": result})


server = HTTPServer((HOST, PORT), CalculatorHandler)
print(f"Server running at http://{HOST}:{PORT}")
print("endpoints :")
print(f"http://{HOST}:{PORT}/add?a=5&b=3")
print(f"http://{HOST}:{PORT}/subtract?a=5&b=3")
print(f"http://{HOST}:{PORT}/multiply?a=5&b=3")
print(f"http://{HOST}:{PORT}/divide?a=5&b=3")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped")
    server.server_close()

