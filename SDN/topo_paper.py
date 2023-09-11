#!/usr/bin/python


"""
This ring topology have 5 switchs and each switch have 1 host

# static arp entry addition

h1 arp -s 192.168.1.2 00:00:00:00:00:02
...

ryu-manager group_table_lb.py

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', protocols='OpenFlow13')
        s5 = self.addSwitch('s5', protocols='OpenFlow13')
        s6 = self.addSwitch('s6', protocols='OpenFlow13')

        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")
        h5 = self.addHost('h5', mac="00:00:00:00:00:05", ip="192.168.1.5/24")
        h6 = self.addHost('h6', mac="00:00:00:00:00:06", ip="192.168.1.6/24")

        # add links between switch and host
        self.addLink(s1,h1,5,1)
        self.addLink(s2,h2,5,1)
        self.addLink(s3,h3,5,1)
        self.addLink(s4,h4,5,1)
        self.addLink(s5,h5,5,1)
        self.addLink(s6,h6,5,1)

        # add links between switch
        self.addLink(s1,s2,1,1)
        self.addLink(s1,s3,2,1)
        self.addLink(s2,s3,2,2)
        self.addLink(s3,s4,3,1)
        self.addLink(s3,s5,4,1)
        self.addLink(s4,s5,2,2)
        self.addLink(s4,s6,3,1)
        self.addLink(s5,s6,3,2)


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    # Add static arp 
    print("Add static arp")
    hosts = [net.get('h1'), net.get('h2'), net.get('h3'), net.get('h4'), net.get('h5'), net.get('h6')]

    # add ARP table of all host for each host
    for host in hosts:
        for h in hosts:
            host.setARP(h.IP(), h.MAC())
    #sleep(5)
    #net.pingAll()
    CLI(net)
    net.stop()
