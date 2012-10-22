import feedparser
import wsutils

def current_temp_default():
	current_temp("woeid=12792335");
	return

def current_temp(parameter):
	updated_html = wsutils.standard_service_header
	woeid = parameter[parameter.index("=")+1:]
	d = feedparser.parse('http://weather.yahooapis.com/forecastrss?w='+woeid)
	updated_html = updated_html+wsutils.terminal_begin+"temp"+wsutils.terminal_middle+d.entries[0].description.split(" ")[7]+wsutils.terminal_end
	updated_html = updated_html+wsutils.standard_service_footer
	f = open("./Weather/currentTemp", "w")
	f.write(updated_html)
	f.close()
	return

