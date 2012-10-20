import time, wsutils
from time import strftime

def current_time():
	current_time = time.localtime()
	updated_html = wsutils.standard_service_header
	updated_html = updated_html+wsutils.terminal_begin+"year"+wsutils.terminal_middle+strftime("%Y", current_time)+wsutils.terminal_end
	updated_html = updated_html+wsutils.terminal_begin+"month"+wsutils.terminal_middle+strftime("%m", current_time)+wsutils.terminal_end
	updated_html = updated_html+wsutils.terminal_begin+"day"+wsutils.terminal_middle+strftime("%d", current_time)+wsutils.terminal_end
	updated_html = updated_html+wsutils.terminal_begin+"hour"+wsutils.terminal_middle+strftime("%H", current_time)+wsutils.terminal_end
	updated_html = updated_html+wsutils.terminal_begin+"minute"+wsutils.terminal_middle+strftime("%M", current_time)+wsutils.terminal_end
	updated_html = updated_html+wsutils.terminal_begin+"second"+wsutils.terminal_middle+strftime("%S", current_time)+wsutils.terminal_end
	updated_html = updated_html+wsutils.terminal_begin+"fractional second"+wsutils.terminal_middle+"0.000"+wsutils.terminal_end
	updated_html = updated_html+wsutils.standard_service_footer
	f = open("./TimeServer/currentTime", "w")
	f.write(updated_html)
	f.close()
	return
