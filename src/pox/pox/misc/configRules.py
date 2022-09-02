from misc.Rule import Rule
import pox.lib.packet as pkt

"""
    ip_src: str = IP de destino. Ejemplo: '10.0.0.1'
    port_src: int = Puerto de destino. Ejemplo: 80.
    mac_src: str = MAC de destino. Ejemplo: '00:00:00:00:00:04'
    ip_dst: str = IP de destino.
    port_dst: int = Puerto de destino.
    mac_dst: str = MAC de destino.
    protocol: str = Opciones: 'UDP', 'TCP', 'ICMP'.
    type_ethernet: str = Opciones: pkt.ethernet.IP_TYPE, pkt.ethernet.ARP_TYPE
    description: str = Descripción que se quiera cuando se filtra el paquete.
"""


rules = [
    Rule(
        ip_src='10.0.0.1',
        ip_dst='10.0.0.4',
        type_ethernet=pkt.ethernet.ARP_TYPE,
        description='Dropping: IP src 10.0.0.1, IP dst 10.0.0.4, protocol=ARP'
    ),
    Rule(
        ip_src='10.0.0.4',
        ip_dst='10.0.0.1',
        type_ethernet=pkt.ethernet.ARP_TYPE,
        description='Dropping: IP src 10.0.0.4, IP dst 10.0.0.1, protocol=ARP'
    ),
    Rule(
        ip_src='10.0.0.1',
        ip_dst='10.0.0.4',
        type_ethernet=pkt.ethernet.IP_TYPE,
        description='Dropping: IP src 10.0.0.1, IP dst 10.0.0.4, protocol=IP'
    ),
    Rule(
        ip_src='10.0.0.4',
        ip_dst='10.0.0.1',
        type_ethernet=pkt.ethernet.IP_TYPE,
        description="Dropping: IP src 10.0.0.4,"
        "IP dst 10.0.0.1,"
        "protocol=IP"
    ),
    Rule(
        mac_src="00:00:00:00:00:04",
        mac_dst="00:00:00:00:00:01",
        description="Dropping: MAC src 00:00:00:00:00:04, "
        "MAC dst 00:00:00:00:00:01"
    ),
    Rule(
        mac_src="00:00:00:00:00:01",
        mac_dst="00:00:00:00:00:04",
        description="Dropping: MAC src 00:00:00:00:00:01,"
        "MAC dst 00:00:00:00:00:04"
    ),
    Rule(
        ip_src='10.0.0.1',
        port_dst=5001,
        protocol='UDP',
        description="Dropping: UDP port 5001"
        "for messages sent by host 10.0.0.1"
    ),
    Rule(
        port_dst=80,
        protocol='UDP',
        description='Dropping: PORT dst 80, protocol=UDP'
    ),
    Rule(
        port_dst=80,
        protocol='TCP',
        description='Dropping: PORT dst 80, protocol=TCP'
    ),
]