import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom request handler for our simple API.
    """

    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        if self.path == '/':
            # Default endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # Data endpoint returning JSON
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))

        elif self.path == '/status':
            # Status endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Info endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # 404 Error handling for undefined endpoints
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server():
    """
    Start the HTTP server on port 8000.
    """
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
