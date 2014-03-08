#!/usr/bin/env python 
import cgi, SocketServer, SimpleHTTPServer
import wsutils, timeserver, weather
 
class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
	if "/TimeServer/currentTime" in self.path: 
		timeserver.current_time()
	if "/Weather/currentTemp" in self.path:
		try:
			weather.current_temp(self.path[self.path.index('?')+1:])
		except ValueError:
			weather.current_temp_default()
                
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

wsutils.generate_user_services_file()
httpd = SocketServer.TCPServer(("", 8080), Handler)
print "serving at port", 8080
httpd.serve_forever()
