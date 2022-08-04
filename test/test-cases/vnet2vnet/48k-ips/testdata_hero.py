import pandas as pd
import os




allow  = pd.read_csv(os.path.join(os.path.dirname(__file__),'MAC_ALLOW.csv'),usecols=['MAC_ALLOW',"IP_ALLOW"])
deny   = pd.read_csv(os.path.join(os.path.dirname(__file__),'MAC_DENY.csv'),usecols=['MAC_DENY',"IP_DENY"])
all_ad = pd.read_csv(os.path.join(os.path.dirname(__file__),'MAC_ALL.csv'),usecols=['MAC_ALL',"IP_ALL"])



testdata = {
    "val_map": {
        1: {
            "underlay_routing":"STATIC",#"BGP"
            "oeth": {"mac": "80:09:02:01:00:01", },
            "oipv4": {"ip": "220.0.1.2", "gip": "220.0.1.1", "mac": "00:ae:cd:10:7e:c6", },
            "obgp": {"ip": "220.0.1.2", "dip": "220.0.1.1", "bid": "194.0.0.1", "type": "External", "las": 200, },
            "oipv4pool": {"ip": "221.0.1.1", "multiplier": 8},
            "dg_b_ong_eth": {"mac": '00:12:01:00:00:01', },
            "dg_b_ong_ipv4": {"ip": "221.0.1.1", "gip": "101.1.0.1"},
            "vxlan": {"RemoteVmStaticMac": list(all_ad['MAC_ALL']), "RemoteVtepIpv4": '221.0.0.2', "StaticInfoCount": 6000, "Vni": 1, "RemoteVmStaticIpv4": list(all_ad['IP_ALL'])},
            "ieth_local": {"mac": "00:1b:6e:00:00:01",'step':'00:00:00:00:00:01'},
            "iipv4_local": {"ip": "1.1.0.1", "gip": "1.128.0.1","prefix":9,'ip_step':'0.0.0.1','ip_ng1_step':'1.0.0.0','gip_step':'0.0.0.0','gip_ng1_step':'1.0.0.0'},
        },
        2: {
            "oeth": {"mac": "80:09:02:02:00:01", },
            "oipv4": {"ip": "220.0.2.2", "gip": "220.0.2.1", "mac": "00:ae:cd:10:7e:c6", },
            "obgp": {"ip": "220.0.2.2", "dip": "220.0.2.1", "bid": "194.0.0.1", "type": "External", "las": 200, },
            "oipv4pool": {"ip": "221.0.2.101", "multiplier": 8},
            "dg_b_ong_eth": {"mac": '00:15:01:00:00:01', },
            "dg_b_ong_ipv4": {"ip": "221.0.2.101", "gip": "104.1.0.1"},
            "vxlan": {"RemoteVmStaticMac": '00:1b:6e:00:00:01', "RemoteVtepIpv4": '221.0.0.2', "StaticInfoCount": 1, "Vni": 101, "RemoteVmStaticIpv4": "1.1.0.1"},
            "ieth_allow": {"mac": list(allow['MAC_ALLOW'])},
            "iipv4_allow": {"ip": list(allow['IP_ALLOW']), "gip": "1.1.0.1","prefix":9,"multiplier": 3000},
            "ieth_deny": {"mac": list(deny['MAC_DENY'])},
            "iipv4_deny": {"ip": list(deny['IP_DENY']), "gip": "1.1.0.1","prefix":9,"multiplier": 3000},

        }
    },
    "acl_policies": [
        {
            'src_ip': ['222.0.0.2/32', '222.0.0.2/32'],
            'dst_ip':['222.0.0.1/32', '222.0.0.1/32'],
            'priority':0,
            'action':'allow',
        },
    ]
}



#VNI need increment

