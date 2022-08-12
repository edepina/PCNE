
# import NetConf Connection Manager
from ncclient import manager

# create dict with values
ios_xe = {
    'host' : '10.7.1.179',
    'username' : 'admin',
    'password' : 'cisco',
    'host' : '10.7.1.179',
    'hostkey_verify' : False,
    'port': 830
}

#initialise connection using dict values
devices = manager.connect(**ios_xe)

#print capabilities of device
for capability in devices.server_capabilities:
    print(capability)
