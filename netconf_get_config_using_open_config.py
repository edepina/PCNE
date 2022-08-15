from ncclient.manager import connect
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

netconf_filter = '''
<filter>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
</filter>
'''

with connect(**ios_xe) as devices:
    netconf_reply = devices.get_config(source = 'running', filter = netconf_filter)
    print(parseString(netconf_reply.xml).toprettyxml())

    