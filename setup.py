import os
import sys
import pandas as pd
import numpy as np
from dotenv import load_dotenv



def create_service():


	for data in data_cctv:
		# print(data[0], data[1], data[2])
		s = open("template/service.txt").read()
		s = s.replace('codeDescription', data[0])
		s = s.replace('codeEngine', engine)
		s = s.replace('codeInput', data[1])
		s = s.replace('codeOutput', data[2])
		s = s.replace('codeDomain', domain)
		s = s.replace('codeApiKey', apiKey)
		f = open('/etc/systemd/system/' + initial + '_' + data[0] + '.service', 'w')
		f.write(s)
		f.close()

		break 

	cmd = 'sudo systemctl daemon-reload'
	os.system(cmd)
	print(cmd)

def start_service():
	for data in data_cctv:
		cmd = 'sudo systemctl start ' + initial + '_' + data[0] + '.service'
		print(cmd)
		os.system(cmd)
		break

def stop_service():
	for data in data_cctv:
		cmd = 'sudo systemctl stop ' + initial + '_' + data[0] + '.service'
		print(cmd)
		os.system(cmd)
		break


def restart_service():
	for data in data_cctv:
		cmd = 'sudo systemctl restart ' + initial + '_' + data[0] + '.service'
		print(cmd)
		os.system(cmd)
		break

def delete_service():


	for data in data_cctv:
		
		cmd= 'rm /etc/systemd/system/' + initial + '_' + data[0] + '.service'
		print(cmd)
		os.system(cmd)
		break 

	cmd = 'sudo systemctl daemon-reload'
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