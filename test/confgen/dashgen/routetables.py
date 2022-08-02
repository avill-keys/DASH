import ipaddress
from dashgen.variables import *


def generate():
    print('    ' + os.path.basename(__file__))
    routetable = []

    for eni_index in range(1, ENI_COUNT+1):
        routes = []
        ip_prefixes = []
        ip_prefixes_append = ip_prefixes.append

        IP_L = IP_L_START + (eni_index - 1) * IP_STEP4
        r_vpc = eni_index + ENI_L2R_STEP
        IP_R = IP_R_START + (eni_index - 1) * IP_STEP4
        routes.append(
            {
                "ip-prefixes": ["%s/32" % IP_L],
                "action": {
                    "routing-type": "vpc",
                    "vpc-id": "vpc-%d" % eni_index
                }
            }
        )

        for table_index in range(1, (ACL_TABLE_COUNT*2+1)):
            #table_id = eni_index * 1000 + table_index

            for ip_index in range(1, (ACL_RULES_NSG+1)):
                remote_ip = IP_R_START + (eni_index - 1) * IP_STEP4 + (table_index - 1) * 4 * IP_STEP3 + (ip_index - 1) * IP_STEP2
                ip_prefixes_append("%s/32" % remote_ip)

        routes.append(
            {
                "ip-prefixes": ip_prefixes,
                "action": {
                    "routing-type": "vpc",
                    "vpc-id": "vpc-%d" % r_vpc
                }
            }
        )

        routetable.append(
            {
                "ROUTE-TABLE:%d" % eni_index: {
                    "route-table-id": "route-table-%d" % eni_index,
                    "ip-version": "IPv4",
                    "routes": routes
                }
            }
        )

    return {"route-tables": routetable}
