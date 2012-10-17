import os

infrastructure_files = ['LVWSSysAdmin', 'server.py', 'timeserver.py', 'timeserver.pyc', 'wsutils.py', 'wsutils.pyc']
global_services_header = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<UserServices>\n"
global_services_footer = "</UserServices>"
def generate_user_services_file():
	all_files = os.listdir(".")
	for f in infrastructure_files:
		all_files.remove(f)
	services = global_services_header
	f = open("./LVWSSysAdmin/GetAllUserServices", "w")
	for s in all_files:
		services = services+"<WSName>"+s+"</WSName>\n"	
	f.write(services+global_services_footer)
	f.close()
