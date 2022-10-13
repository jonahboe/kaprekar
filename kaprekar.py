'''
Code by: Jonah Boe
Date: 10/12/2022
'''

import sys

ERROR_TXT = "Program requires a four diget integer as the only parameter. Can include leading zeros."

def parse(val):
    vals = [0,0,0,0]
    vals[3] = val / 1000
    vals[2] = (val - vals[3] * 1000) / 100
    vals[1] = (val - vals[3] * 1000 - vals[2] * 100) / 10
    vals[0] = (val - vals[3] * 1000 - vals[2] * 100 - vals[1] * 10)
    return vals

def conjoin(vals):
    return vals[3] * 1000 + vals[2] * 100 + vals[1] * 10 + vals[0]

if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print(ERROR_TXT)
        sys.exit()

    try:
        val = int(sys.argv[1])
    except ValueError:
        print(ERROR_TXT + "\n")  

    if val > 9999:
        print(ERROR_TXT)
        sys.exit()

    vals = parse(val)
    if vals[0] == vals[1] and vals[0] == vals[2] and vals[0] == vals[3]:
        print("All four digits cannot be the same.")
        sys.exit()

    while val != 6174:
        vals = parse(val)
        hl = conjoin(sorted(vals))
        lh = conjoin(sorted(vals, reverse=True))
        print(str(val).rjust(4, '0') + "   ->   " + str(hl))
        print("          - " + str(lh).rjust(4, '0'))
        print("          ------")
        val = hl - lh
        print("            " + str(val).rjust(4, '0') + "\n")