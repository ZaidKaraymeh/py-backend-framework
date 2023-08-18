from http import client, cookies, cookiejar, server
import logging
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger("server")


def home_controller(request):
    return "home"

def about_controller(request):
    return "about"


routes = {
    "/home": home_controller,
    "/about": about_controller,
}


class CustomHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        """Serve a GET request."""

        response = routes[self.path](self)
        # _logger.debug(msg=response)
        # f = self.send_head()
        # if f:
        #     try:
        #         self.copyfile(f, self.wfile)
        #     finally:
        #         f.close()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_str = 'Received: ' + response
        self.wfile.write(response_str.encode('utf-8'))
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode('utf-8')
        
        # Here, you can process the post_data_str as required

        # Responding to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_str = 'Received: ' + post_data_str
        self.wfile.write(response_str.encode('utf-8'))


PORT = 8000
HANDLER = CustomHTTPRequestHandler


with server.HTTPServer(("", PORT), HANDLER) as httpd:
    httpd.serve_forever()
