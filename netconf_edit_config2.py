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
            <name>GigabitEthernet2</name>
            <description>Created by NETCONF</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>100.0.0.1</ip>
                    <netmask>255.255.255.0</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
'''

with manager.connect(**ios_xe) as devices:
    netconf_reply = devices.edit_config(netconf_filter, target='running')
    print(netconf_reply)