from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.misc.configRules import rules
from pox.lib.util import dpid_to_str
log = core.getLogger()


class SDNController(object):
    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_ConnectionUp(self, event):
        log.debug("Installing rules... \n\n")
        for rule in rules:
            block = of.ofp_match()
            rule.set_flow_table(block)
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            try:
                event.connection.send(flow_mod)
                log.debug(f'Rule sent: {rule.description}')
            except Exception as e:
                log.debug(e)
        log.debug("All rules sent.\n\n")
        

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if (packet.type != 34525):
            log.debug(f"Packet arrived from switch: {dpid_to_str(event.dpid)}"
                    f" interface {event.port}: {packet.src} --> {packet.dst}\n")
    
    # Para que se cierre bien todo (matar topología).
    def _handle__ConnectionDown(self, event):
        event.connection.disconnect()


def launch():
    core.registerNew(SDNController)
