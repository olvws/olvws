import time
from time import strftime

standard_service_header = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Response>\n"
terminal_begin = "<Terminal><Name>"
terminal_middle = "</Name><Value>"
terminal_end = "</Value></Terminal>\n"
standard_service_footer = "</Response>"
def current_time():
	current_time = time.localtime()
	updated_html = standard_service_header
	updated_html = updated_html+terminal_begin+"year"+terminal_middle+strftime("%Y", current_time)+terminal_end
	updated_html = updated_html+terminal_begin+"month"+terminal_middle+strftime("%m", current_time)+terminal_end
	updated_html = updated_html+terminal_begin+"day"+terminal_middle+strftime("%d", current_time)+terminal_end
	updated_html = updated_html+terminal_begin+"hour"+terminal_middle+strftime("%H", current_time)+terminal_end
	updated_html = updated_html+terminal_begin+"minute"+terminal_middle+strftime("%M", current_time)+terminal_end
	updated_html = updated_html+terminal_begin+"second"+terminal_middle+strftime("%S", current_time)+terminal_end
	updated_html = updated_html+terminal_begin+"fractional second"+terminal_middle+"0.000"+terminal_end
	updated_html = updated_html+standard_service_footer
	f = open("./TimeServer/currentTime", "w")
	f.write(updated_html)
	f.close()
	return
