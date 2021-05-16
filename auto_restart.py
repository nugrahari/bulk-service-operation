import sys
import os
import time
import random
from datetime import datetime

minutes_restart = ['00', '10', '20', '30', '40', '50']

if getattr(sys, 'frozen', False):
	application_path = os.path.dirname(os.path.realpath(sys.executable))
elif __file__:
	application_path = os.path.dirname(os.path.realpath(__file__))

python_path = os.path.join(application_path, "Env/bin/python")
# python_path = "/usr/bin/python3"
application_path = os.path.join(application_path, "setup.py")
print(application_path)
print(python_path)

while True:
	now = datetime.now()
	# current_time = now.strftime("%H:%M:%S")
	current_time = now.strftime("%H:%M")
	# current_time = now.strftime("%H")
	if current_time == '00:00':
	# if current_time in minutes_restart:
		print(current_time,"Restarting Engine")

		cmd = f"{python_path} {application_path} pm2-stop all"
		print(cmd)
		os.system(cmd)

		cmd = f"killall kecilin"
		print(cmd)
		os.system(cmd)

		cmd = f"{python_path} {application_path} pm2-start all"
		print(cmd)
		os.system(cmd)


	else:
		print(current_time)

	time.sleep(49)
