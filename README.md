# EX01 Developing a Simple Webserver

# Date:10-10-2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
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
```

# OUTPUT:
![alt text](<../Screenshot 2025-10-04 231736.png>)
![alt text](<../Screenshot 2025-10-04 231816.png>)


# RESULT:
The program for implementing simple webserver is executed successfully.
