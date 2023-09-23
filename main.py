#!/usr/bin/env python3
"""
pip install prettytable
"""

import sys
from subnet_calculator import SubnetCalculator
from table_formatter import TableFormatter

def main():
    if len(sys.argv) < 3:
        print("Usage: main.py [CIDR] [Number of Subnets]")
        return

    cidr = sys.argv[1]
    num_subnets = int(sys.argv[2])
    
    try:
        calculator = SubnetCalculator(cidr)
        subnets_info = calculator.calculate_subnets(num_subnets)
        table_output = TableFormatter.format(subnets_info, cidr)
        print(table_output)
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
