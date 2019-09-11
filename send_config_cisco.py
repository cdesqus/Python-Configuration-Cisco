# Import program dependencies
from netmiko import ConnectHandler
import getpass

# Read from a list of hostnames to connect to
hosts = open('hosts.txt','r')
hosts = hosts.read()
hosts = hosts.strip().splitlines()

# Get UserName and password from input
userName = input('Username: ')
passWord = getpass.getpass()

# Loop to process hosts in hosts.txt file
for host in hosts:
	# Define device type and connection attributes
	deciso = {
		 "host": host,
    	"username": userName,
    	"password": passWord,
    	"device_type": 'cisco_ios',
	}

	# Netmiko SSH Connection Handler
	net_connect = ConnectHandler(**deciso)

	#open file to write command output
	file = open(host + '_config-output.txt', 'w')

	# Execute commands
	output = net_connect.send_config_set('configure terminal')
	# Command Configuration Here
	output = net_connect.send_config_set('hostname CDESQUS-OFFICE')
	output = net_connect.send_config_set('do write')

	# Print output to console screen
	print('-------------- Output from ' + host + '------------------')
	print(output)
	print()
	print()

	# Write output to file above
	file.write(output)
	file.close()
