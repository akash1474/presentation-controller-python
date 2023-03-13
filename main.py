# Get the IP Address
# Update html and server with ip address
# start the server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pyautogui import press
HOST=""
PORT=8000
with open("ip.txt","r") as file:
	lines=file.readlines()
	word="IPv4 Address"
	for line in lines:
		if(word in line):
			idx=line.find("192")
			HOST=line[idx:-1]
			break

lines=[]
with open("index.html","r") as file:
	lines=file.readlines()
	word="URL="
	i=0;
	for line in lines:
		if(word in line):
			lines.pop(i)
			lines.insert(i,f"const URL=\"{HOST}:{PORT}\"\n")
			break
		i+=1;

with open("index.html","w") as f:
	f.writelines(lines)




class HTTPServerRequest(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type","text/html")
		self.end_headers()
		self.wfile.write(open('index.html','rb').read())

	def do_POST(self):
		self.send_response(200)
		press('right')

	def do_PATCH(self):
		self.send_response(200)
		press('left')

	def do_PUT(self):
		self.send_response(200)
		press('f5')

	def do_DELETE(self):
		self.send_response(200)
		press('escape')

server=HTTPServer((HOST,PORT),HTTPServerRequest)
print(f"http://{HOST}:{PORT}")
print("Server is running...")
server.serve_forever()
server.server_close()