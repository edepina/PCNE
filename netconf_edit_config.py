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
        <interface>
            <name>Loopback99</name>
            <description>Created by NETCONF</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>99.99.99.99</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
'''

with manager.connect(**ios_xe) as devices:
    netconf_reply = devices.edit_config(netconf_filter, target='running')
    print(netconf_reply)