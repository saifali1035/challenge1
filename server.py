import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML form
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
            <html>
            <head><title>Enter Your Name</title></head>
            <body>
                <form method="post">
                    <label for="name">Enter your name:</label>
                    <input type="text" id="name" name="name" required>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
        """
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        # Handle the form submission
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = parse_qs(post_data.decode('utf-8'))

        # Get the submitted name
        name = params.get('name', [''])[0]

        # Send a personalized greeting back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = f"Hello {name}"
        self.wfile.write(response.encode('utf-8'))

def start_server():
    host = 'localhost'
    port = 9098
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server is listening on http://{host}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()
