#!/usr/bin/env python3
import sys
import time

from probe_hdrs import *

def main():

    iface = 'h1-eth0'
    s = conf.L2socket(iface=iface)


    probe_pkt = Ether(src=get_if_hwaddr('h1-eth0'), dst='ff:ff:ff:ff:ff:ff') / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=2) / \
                ProbeFwd(egress_spec=2) / \
                ProbeFwd(egress_spec=1)

    while True:
    	#print(get_if_hwaddr('h1-eth0'))
        try:
            sendp(probe_pkt, iface=iface)
            #s.send(probe_pkt)
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()
