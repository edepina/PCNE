from ncclient import manager

ios_xe = {
    'host' : '10.7.1.179',
    'username' : 'admin',
    'password' : 'cisco',
    'hostkey_verify' : False,
    'port': 830
}

netconf_filter = '''
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation = "delete">
            <name>Loopback99</name>
        </interface>
    </interfaces>
</config>
'''

with manager.connect(**ios_xe) as devices:
    netconf_reply = devices.edit_config(netconf_filter, target='running')
    print(netconf_reply)