#!/usr/bin/python

### topo ring gom 4 switch, moi switch co 1 host


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

        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")

        

        
        self.addLink(s1,h1,3,1)
        self.addLink(s2,h2,3,1)
        self.addLink(s3,h3,3,1)

        self.addLink(s1,s2,1,1)
        self.addLink(s1,s3,2,2) 
        self.addLink(s2,s3,2,1)
    

        

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()

    hosts = [net.get('h1'), net.get('h2'), net.get('h3')]

    # add ARP table of all host for each host
    for host in hosts:
        for h in hosts:
            host.setARP(h.IP(), h.MAC())
    #sleep(5)
    #print("Topology is up, lets ping")
    #net.pingAll()
    CLI(net)
    net.stop()
