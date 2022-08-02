from dashgen.variables import *


def generate():
    print('    ' + os.path.basename(__file__))
    routingappliances = []
    for eni_index in range(1, ENI_COUNT+1):
        j = eni_index+100
        IP_L = IP_L_START + (eni_index - 1) * IP_STEP3
        IP_R = IP_L_START + (j - 1) * IP_STEP3
        routingappliances.append(
            {
                "VTEP:%d" % eni_index: {
                    "appliance-id": "%d" % eni_index,
                    "routing-appliance-id": eni_index,
                    "routing-appliance-addresses": [
                        "%s/9" % IP_L
                    ],
                    "encap-type": "vxlan",
                    "vni-key": eni_index
                },
            }
        )
        routingappliances.append(
            {
                "VTEP:%d" % eni_index: {
                    "appliance-id": "%d" % j,
                    "routing-appliance-id": j,
                    "routing-appliance-addresses": [
                        "%s/9" % IP_R
                    ],
                    "encap-type": "vxlan",
                    "vni-key": j
                },
            }
        )
    return {"routing-appliances": routingappliances}
