from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from Topology import Topology


class Network:
    def __init__(self, log_level, hosts, switches, links):
        self.log_level(log_level)
        self.net = Mininet(
            topo=Topology(hosts=hosts, switches=switches, links=links),
            build=False,
            ipBase='10.0.0.0/24'
        )

        self.switches = switches

        info('*** Adding controller\n')
        self.controller = self.net.addController(
            name='controller',
            controller=RemoteController,
            ip='0.0.0.0',
            protocol='tcp',
            port=6633
        )

    def log_level(self, log_level):
        setLogLevel(log_level)

    def run(self):
        info('*** Starting network\n')
        self.net.start()

        info('*** Starting controllers\n')
        for controller in self.net.controllers:
            controller.start()

        for switch in self.switches:
            self.net.get(switch).start([self.controller])

        info('*** Post configure switches and hosts\n')
        CLI(self.net)
        self.net.stop()
