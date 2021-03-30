import os
import sys
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

load_dotenv('template/.env')

csv_cctv = pd.read_csv(os.getenv('CCTV_LIST_CSV'), delimiter=',', header=0)
data_cctv = np.array(csv_cctv)  

#print(os.getenv('INIT_SERVICE_NAME'))
initial = os.getenv('INIT_SERVICE_NAME')
engine = os.getenv('ENGINE')
domain = os.getenv('DOMAIN')
apiKey = os.getenv('APIKEY')
# print(csv_cctv.head())

if len(sys.argv) != 2 :
	print("Error !!!")
	print("\tRun : python setup.py create-All > for create all service")
	print("\tRun : python setup.py start-All > for start all service")
	print("\tRun : python setup.py stop-All > for stop all service")
	print("\tRun : python setup.py restart-All > for restart all service")
	print("\tRun : python setup.py status-All > for check status all service")
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

else:
	print("Error !!!")
	print("\tRun : python setup.py create-All > for create all service")
	print("\tRun : python setup.py start-All > for start all service")
	print("\tRun : python setup.py stop-All > for stop all service")
	print("\tRun : python setup.py restart-All > for restart all service")
	print("\tRun : python setup.py status-All > for check status all service")