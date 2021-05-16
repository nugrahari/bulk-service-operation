import os
import sys
import json
import pandas as pd
import numpy as np
from dotenv import load_dotenv



def create_service():


	for data in data_cctv:
		# print(data[0], data[1], data[2])
		s = open("template/service.txt").read()
		s = s.replace('codeDescription', data[1])
		s = s.replace('codeEngine', engine)
		s = s.replace('codeInput', data[2])
		s = s.replace('codeOutput', data[3])
		s = s.replace('codeDomain', domain)
		s = s.replace('codeApiKey', apiKey)
		f = open('/etc/systemd/system/' + initial + '_' + data[1] + '-' + str(data[0]) + '.service', 'w')
		f.write(s)
		f.close()

		# break 

	cmd = 'sudo systemctl daemon-reload'
	os.system(cmd)
	print(cmd)

def start_service():
	for data in data_cctv:
		cmd = 'sudo systemctl start ' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'
		print(cmd)
		os.system(cmd)
		# break

def stop_service():
	for data in data_cctv:
		cmd = 'sudo systemctl stop ' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'
		print(cmd)
		os.system(cmd)
		# break


def restart_service():
	for data in data_cctv:
		cmd = 'sudo systemctl restart ' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'
		print(cmd)
		os.system(cmd)
		# break

def delete_service():


	for data in data_cctv:
		
		cmd= 'rm /etc/systemd/system/' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'
		print(cmd)
		os.system(cmd)
		# break 

	cmd = 'sudo systemctl daemon-reload'
	print(cmd)
	os.system(cmd)

def status_service():

	for data in data_cctv:
		
		cmd= 'systemctl is-active --quiet ' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'

		print("\n"+cmd)
		cmd = os.system(cmd)

		if cmd == 0:
			print("service is running")
		else:
			print('service is not running')
		# break 

def enable_service():
	for data in data_cctv:
		cmd = 'sudo systemctl enable ' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'
		print(cmd)
		os.system(cmd)

def disable_service():
	for data in data_cctv:
		cmd = 'sudo systemctl disable ' + initial + '_' + data[1] + '-' + str(data[0]) + '.service'
		print(cmd)
		os.system(cmd)

def pm2_create():
	results = []
	for data in data_cctv:
		
		# break 
		data = {
		    "name"       : f"{initial}-{data[1]}",
		    "script"     : f"{engine} '{data[2]}' '{data[3]}' {domain} {apiKey}",
		}
		results.append(data)
		print(data)

	with open('template/pm2-config.json', 'w') as fp:
		json.dump(results, fp) 

def pm2_start(index):
	data = ""
	if index != 'all':
		index = int(index)-1
		data = {
	    "name"       : f"{initial}-{data_cctv[index][1]}",
	    "script"     : f"{engine} '{data_cctv[index][2]}' '{data_cctv[index][3]}' {domain} {apiKey}",
		}
		print(data)

		cmd = f"\npm2 start {initial}-{data_cctv[index][1]}"
	else:
		cmd = "pm2 start template/pm2-config.json"
	os.system(cmd)
	print(cmd)	

def pm2_status():
	cmd = "pm2 status template/pm2-config.json"
	os.system(cmd)

def pm2_stop(index):
	data = ""
	if index != 'all':
		index = int(index)-1
		data = {
	    "name"       : f"{initial}-{data_cctv[index][1]}",
	    "script"     : f"{engine} '{data_cctv[index][2]}' '{data_cctv[index][3]}' {domain} {apiKey}",
		}
		print(data)

		cmd = f"\npm2 stop {initial}-{data_cctv[index][1]}"
	else:
		cmd = "pm2 stop template/pm2-config.json"
	os.system(cmd)
	print(cmd)	

def pm2_delete():
	cmd = "pm2 delete template/pm2-config.json"
	os.system(cmd)
	cmd = "sudo rm template/pm2-config.json"
	os.system(cmd)

def pm2_logs(index):
	index = int(index)-1
	data = {
	    "name"       : f"{initial}-{data_cctv[index][1]}",
	    "script"     : f"{engine} '{data_cctv[index][2]}' '{data_cctv[index][3]}' {domain} {apiKey}",
	}
	print(data)

	cmd = f"\npm2 logs {initial}-{data_cctv[index][1]}"
	print(cmd)
	os.system(cmd)

def pm2_restart(index):
	data = ""
	if index != 'all':
		index = int(index)-1
		data = {
	    "name"       : f"{initial}-{data_cctv[index][1]}",
	    "script"     : f"{engine} '{data_cctv[index][2]}' '{data_cctv[index][3]}' {domain} {apiKey}",
		}
		print(data)

		cmd = f"\npm2 restart {initial}-{data_cctv[index][1]}"
	else:
		cmd = "pm2 restart template/pm2-config.json"
	os.system(cmd)
	print(cmd)	


load_dotenv('template/.env')

csv_cctv = pd.read_csv(os.getenv('CCTV_LIST_CSV'), delimiter=',', header=0)
data_cctv = np.array(csv_cctv)  

#print(os.getenv('INIT_SERVICE_NAME'))
initial = os.getenv('INIT_SERVICE_NAME')
engine = os.getenv('ENGINE')
domain = os.getenv('DOMAIN')
apiKey = os.getenv('APIKEY')
# print(csv_cctv.head())

if len(sys.argv) < 2 or len(sys.argv) > 3  :
	print("Error !!!")
	print("\tRun : python setup.py create-All > for create all service")
	print("\tRun : python setup.py start-All > for start all service")
	print("\tRun : python setup.py stop-All > for stop all service")
	print("\tRun : python setup.py restart-All > for restart all service")
	print("\tRun : python setup.py status-All > for check status all service")
	print("\tRun : python setup.py delete-All > for delete all service")
	print("\tRun : python setup.py enable-All > for enable startup all service")
	print("\tRun : python setup.py disable-All > for disable startup all service\n")
	
	print("\tRun : python setup.py pm2-create > for create all service by pm2")
	print("\tRun : python setup.py pm2-start > for start all service by pm2")
	print("\tRun : python setup.py pm2-status > for check status all service by pm2")
	print("\tRun : python setup.py pm2-stop > for stop all service by pm2")
	print("\tRun : python setup.py pm2-delete > for delete all service by pm2")
	print("\tRun : python setup.py pm2-logs no-index > for delete all service by pm2")
	print("\tRun : python setup.py pm2-restart > for start all service by pm2")
	sys.exit()

if sys.argv[1] == "create-All":
	create_service()

elif sys.argv[1] == "start-All":
	start_service()

elif sys.argv[1] == "stop-All":
	stop_service()

elif sys.argv[1] == "restart-All":
	restart_service()

elif sys.argv[1] == "delete-All":
	delete_service() 

elif sys.argv[1] == "status-All":
	status_service()

elif sys.argv[1] == "enable-All":
	enable_service()

elif sys.argv[1] == "disable-All":
	disable_service()  

elif sys.argv[1] == "pm2-create":
	pm2_create()  
elif sys.argv[1] == "pm2-start":
	pm2_start(sys.argv[2])  
elif sys.argv[1] == "pm2-status":
	pm2_status()
elif sys.argv[1] == "pm2-stop":
	pm2_stop(sys.argv[2])
elif sys.argv[1] == "pm2-delete":
	pm2_delete()
elif sys.argv[1] == "pm2-logs":
	pm2_logs(sys.argv[2])  
elif sys.argv[1] == "pm2-restart":
	pm2_restart(sys.argv[2])  

else:
	print("Error !!!")
	print("\tRun : python setup.py create-All > for create all service")
	print("\tRun : python setup.py start-All > for start all service")
	print("\tRun : python setup.py stop-All > for stop all service")
	print("\tRun : python setup.py restart-All > for restart all service")
	print("\tRun : python setup.py status-All > for check status all service")
	print("\tRun : python setup.py delete-All > for delete all service")
	print("\tRun : python setup.py enable-All > for enable startup all service")
	print("\tRun : python setup.py disable-All > for disable startup all service\n")

	print("\tRun : python setup.py pm2-create > for create all service by pm2")
	print("\tRun : python setup.py pm2-start > for start all service by pm2")
	print("\tRun : python setup.py pm2-status > for check status all service by pm2")
	print("\tRun : python setup.py pm2-stop > for stop all service by pm2")
	print("\tRun : python setup.py pm2-delete > for delete all service by pm2")
	print("\tRun : python setup.py pm2-logs no-index > for delete all service by pm2")
	print("\tRun : python setup.py pm2-restart > for start all service by pm2")
