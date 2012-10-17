import cgi, SocketServer, SimpleHTTPServer
import wsutils, timeserver
 
class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
	if "/TimeServer/currentTime" in self.path: 
		timeserver.current_time()
                
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

wsutils.generate_user_services_file()
httpd = SocketServer.TCPServer(("", 8080), Handler)
print "serving at port", 8080
httpd.serve_forever()
