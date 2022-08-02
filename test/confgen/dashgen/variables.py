import ipaddress
import macaddress
import os
ipp = ipaddress.ip_address


ENI_COUNT = 8  # 8
ENI_MAC_STEP = '00:00:00:08:00:00'
ENI_STEP = 1
ENI_L2R_STEP = 100


ACL_TABLE_MAC_STEP = '00:00:00:01:00:00'
ACL_POLICY_MAC_STEP = '00:00:00:00:00:40'

ACL_RULES_NSG = 1000  # 1000
ACL_TABLE_COUNT = 3


IP_MAPPED_PER_ACL_RULE = 40  # 40
IP_PER_ACL_RULE = 255  # 255

IP_STEP1 = int(ipp('0.0.0.1'))
IP_STEP2 = int(ipp('0.0.1.0'))
IP_STEP3 = int(ipp('0.1.0.0'))
IP_STEP4 = int(ipp('1.0.0.0'))
IP_STEPE = int(ipp('0.0.0.2'))


IP_L_START = ipaddress.ip_address('1.1.0.1')
IP_R_START = ipaddress.ip_address('1.128.0.1')


MAC_L_START = macaddress.MAC('00:1B:6E:00:00:01')
MAC_R_START = macaddress.MAC('00:1B:6E:80:00:01')

'''
IN
TB1 1.128.0.1
TB2 1.128.0.1 + 0.4.0.0=1.132.0.1
TB3 1.128.0.1 + 0.8.0.0=1.136.0.1



OUT
TB4 1.128.0.1 + 0.12.0.0 = 1.140.
TB5 1.128.0.1 + 0.16.0.0 = 1.144.0.1
TB6 1.128.0.1 + 0.20.0.0 = 1.148
'''
