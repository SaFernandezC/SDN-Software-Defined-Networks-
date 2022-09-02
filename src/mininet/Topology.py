from mininet.topo import Topo
from mininet.log import info


class Topology(Topo):
    def build(self, hosts, switches, links):
        hosts_dict = {}
        switches_dict = {}

        for host, ip_host, mac_host in hosts:
            hosts_dict[host] = self.addHost(host, ip=ip_host, mac=mac_host)
            info(f'** Host {host}: IP {ip_host} - MAC {mac_host}\n')

        for switch in switches:
            switches_dict[switch] = self.addSwitch(switch)

        for link in links:
            self.addLink(link[0], link[1])
