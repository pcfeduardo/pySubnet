#!/usr/bin/env python3

import ipaddress
import math

class SubnetCalculator:

    def __init__(self, cidr):
        self.network = ipaddress.ip_network(cidr, strict=False)

    def calculate_subnets(self, num_subnets):
        new_prefix_increment = int(math.ceil(math.log2(num_subnets)))
        subnet_prefixlen = self.network.prefixlen + new_prefix_increment

        subnets = list(self.network.subnets(new_prefix=subnet_prefixlen))
        
        if len(subnets) < num_subnets:
            raise ValueError("Number of resulting subnets is less than requested. Please choose a wider CIDR or fewer subnets.")

        result = []
        for subnet in subnets[:num_subnets]:
            info = {
                'Address': str(subnet.network_address),
                'Netmask': str(subnet.netmask),
                'Wildcard': str(subnet.hostmask),
                'Network': str(subnet),
                'HostMin': str(subnet.network_address + 1),
                'HostMax': str(subnet.broadcast_address - 1),
                'Broadcast': str(subnet.broadcast_address),
                'Hosts/Net': subnet.num_addresses - 2,
            }
            result.append(info)
        return result
