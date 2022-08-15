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
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
            <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <id>1</id>
                <network>
                    <ip>99.99.99.99</ip>
                    <mask>0.0.0.0</mask>
                    <area>0</area>
                </network>
            </ospf>
        </router>
    </native>
</config>
'''

with manager.connect(**ios_xe) as devices:
    netconf_reply = devices.edit_config(netconf_filter, target='running')
    print(netconf_reply)