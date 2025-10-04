from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>  
    <head>
        <title>Simple Web server</title>
    </head>
    <body bgcolor="lightgrey">
        <center>
            <h1>Welcome to NKK's Simple Web Server</h1>
        </center>
        <table border="15" align="center" cellpadding="25" cellspacing="0">
            <tr bgcolor="yellow">
                <th>S.NO</th>
                <th>NAME</th>
                <th>AGE</th>
            </tr>
            <tr bgcolor="cyan">
                <td>1.</td>
                <td>NARENDRA KRISHNAN KS</td>
                <td>17</td>
            </tr>
            <tr bgcolor="pink">
                <td>2.</td>
                <td>MERLIN</td>
                <td>17</td>
            </tr>
            <tr bgcolor="lightgreen">
                <td>3.</td>
                <td>ADITYA</td>
                <td>18</td>
            </tr>
            <tr bgcolor="orange">
                <td>4.</td>
                <td>ARUN</td>
                <td>18</td>   
            </tr>
            <tr bgcolor="lightblue">
                <td>5.</td>
                <td>DHANUSH</td>
                <td>18</td>
            </tr>
           
        </table>
    </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received from:", self.client_address)
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running on http://localhost:8000 ...")
httpd.serve_forever()