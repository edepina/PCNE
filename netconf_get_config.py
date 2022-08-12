# import NetConf Connection Manager
from operator import ne
from ncclient import manager
from xml.dom.minidom import parseString

# create dict with values
ios_xe = {
    'host' : '10.7.1.179',
    'username' : 'admin',
    'password' : 'cisco',
    'host' : '10.7.1.179',
    'hostkey_verify' : False,
    'port': 830
}
# Create a filter to retrieve interface information
netconf_filter = """
<filter>
    <interfaces xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
</filter>
"""

# Connect to device and retrieve config using get_config method
with manager.connect(**ios_xe) as device:
    netconf_reply = device.get_config(source = 'running', filter = netconf_filter)
    print(parseString(netconf_reply.xml).toprettyxml()) # Print output in readable format