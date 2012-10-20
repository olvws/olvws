import feedparser
import wsutils

def current_temp():
	updated_html = wsutils.standard_service_header
	d = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=12792335')
	updated_html = updated_html+wsutils.terminal_begin+"temp"+wsutils.terminal_middle+d.entries[0].description.split(" ")[6]+wsutils.terminal_end
	updated_html = updated_html+wsutils.standard_service_footer
	f = open("./Weather/currentTemp", "w")
	f.write(updated_html)
	f.close()


