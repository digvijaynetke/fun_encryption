#!/usr/bin/env python3
##
##First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge).
##Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. 
###The numbers can be combined together, into one long hex string.

##
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print(bytes.fromhex(63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d))
print("Here is your flag:")
print("".join(chr(o ^ 0x0) for o in ords))
