from dataclasses import dataclass
from pox.lib.addresses import IPAddr, EthAddr
import pox.lib.packet as pkt


@dataclass
class Rule:
    ip_src: str = None
    port_src: int = None
    mac_src: str = None
    ip_dst: str = None
    port_dst: int = None
    mac_dst: str = None
    protocol: str = None
    type_ethernet: str = pkt.ethernet.IP_TYPE
    description: str = ''

    def _asign_ip_addrs(self, block):
        if (self.ip_src):
            block.nw_src = IPAddr(self.ip_src)
        if (self.ip_dst):
            block.nw_dst = IPAddr(self.ip_dst)

    def _asign_ports(self, block):
        if (self.port_src):
            block.tp_src = self.port_src
        if (self.port_dst):
            block.tp_dst = self.port_dst

    def _asign_mac_addrs(self, block):
        if (self.mac_src):
            block.dl_src = EthAddr(self.mac_src)
        if (self.mac_dst):
            block.dl_dst = EthAddr(self.mac_dst)

    def _asign_protocols(self, block):
        if (self.protocol):
            if (self.protocol == 'UDP'):
                block.nw_proto = pkt.ipv4.UDP_PROTOCOL
            elif (self.protocol == 'TCP'):
                block.nw_proto = pkt.ipv4.TCP_PROTOCOL
            else:
                block.nw_proto = pkt.ipv4.ICMP_PROTOCOL
        
        block.dl_type = self.type_ethernet

    def set_flow_table(self, block):
        self._asign_ip_addrs(block)
        self._asign_ports(block)
        self._asign_mac_addrs(block)
        self._asign_protocols(block)
