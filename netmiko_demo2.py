from netmiko import ConnectHandler

with open(r'G:\My Drive\Training\Koenig\PCNE\devices.txt') as f:
    devices_list = f.read().splitlines()

with open(r'G:\My Drive\Training\Koenig\PCNE\show_commands.txt') as f:
    show_commands_list = f.read().splitlines()

#print(devices_list, show_commands_list)


for device in devices_list:

    print('---------- Connecting to Device ' + device + '---------------')

    cisco_devices = {
    'device_type': 'cisco_ios',
    'host':   device,
    'username': 'admin',
    'password': 'cisco',
    }
    net_connect = ConnectHandler(**cisco_devices)

    for cmd in show_commands_list:
        output = net_connect.send_command(cmd)
        print(output)    

 

