#!/usr/bin/env python3

from prettytable import PrettyTable

class TableFormatter:

    @staticmethod
    def format(subnets_info, vpc_cidr):
        table = PrettyTable()
        
        headers = ['Subnet', 'Address', 'Netmask', 'Wildcard', 'Network', 'HostMin', 'HostMax', 'Broadcast', 'Hosts/Net']
        table.field_names = headers
        
        for index, subnet in enumerate(subnets_info, 1):
            row_data = [index]
            for header in headers[1:]:
                row_data.append(subnet[header])
            table.add_row(row_data)
        
        return f"VPC CIDR: {vpc_cidr}\n" + str(table)