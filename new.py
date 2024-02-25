# -*- coding: utf-8 -*-
"""Dropshot / StoneDrill Decrypter

This is a r2pipe based script which will be used to demonstrate the capabilities
of radare2 and r2pipe (@r2gui). The script will be oficially published on a blogpost
on https://www.megabeets.net as part of series of article about radare2.

"""

__author__ = "Itay Cohen, aka Megabeets"
__copyright__ = "Do whatever you want with this code"
__website__ = "https://www.megabeets.net"

import r2pipe
import zlib

# Rotate right lambda


def ror(val, r_bits, max_bits): return \
    ((val & (2**max_bits-1)) >> r_bits % max_bits) | \
    (val << (max_bits-(r_bits % max_bits)) & (2**max_bits-1))


def decode_strings(verbose=True):
    if verbose:
        print("\n%s\n\tStarting the decode of the encrypted strings\n%s\n\n" %
              ('~'*60, '~'*60))

    # Declaration of decryption-table related variables
    decryption_table = 0x41BA3C
    decryption_table_end = 0x41BA77
    decryption_table_len = decryption_table_end - decryption_table
    decryption_function = 0x4012A0

    # Analyze the binary to better detect functions and x-refs
    r2.cmd('aa')

    # Rename the decryption function
    r2.cmd('afn decryption_function %d' % decryption_function)

    # Dump the decryption table to a variable
    decryption_table_content = [65, 97, 67, 99, 100, 68, 101, 70, 102, 71, 104, 105, 75, 76, 108, 77, 109, 110, 78, 111, 79, 112, 80, 114, 82, 115,
                                83, 84, 116, 85, 117, 86, 118, 119, 87, 120, 121, 90, 122, 51, 50, 46, 92, 69, 98, 103, 106, 72, 73, 32, 95, 89, 81, 66, 58, 34, 47, 64, 10]

    # Iterate x-refs to the decryption function
    for xref in r2.cmdj('axtj %d' % decryption_function):
        # Get the arguments passed to the decryption function: length and encrypted string
        length_arg, offsets_arg = r2.cmdj('pdj -2 @ %d' % (xref['from']))

        # String variable to store the decrypted string
        decrypted_string = ""

        # Guard rail to avoid exception
        if (not 'val' in length_arg):
            continue

        # Manually decrypt the encrypted string
        for i in range(0, length_arg['val']):
            decrypted_string += chr(decryption_table_content[r2.cmdj(
                'pxj 1 @ %d' % (offsets_arg['val'] + (i*2)))[0]])

        # Print the decrypted and the address it was referenced to the console
        if verbose:
            print(decrypted_string + " @ " + hex(xref['from']))

        # Add comments to each call of the decryption function
        r2.cmd('CC Decrypted: %s @ %d' % (decrypted_string, xref['from']))

# This function was added in the 2nd part of the series about dropshot


def decrypt_resource(verbose=True):
    if verbose:
        print("\n%s\n\tStarting the decryption of the resource\n%s\n" %
              ('~'*60, '~'*60))
    # Get information on all resources in JSON format
    rsrcs = r2.cmdj('iRj')
    rsrc_101 = {}

    # Locate resource 101 and dump it to an array
    for rsrc in rsrcs:
        if rsrc['name'] == 101:
            rsrc_101 = r2.cmdj("pxj %d @ %d" %
                               (rsrc['size'], rsrc['vaddr']))

    # Decompress the zlibbed array
    print(rsrc_101)
    decompressed_data = zlib.decompress(bytes(rsrc_101))

    decrypted_payload = []

    # Decrypt the payload
    for b in decompressed_data:
        decrypted_payload.append((ror(b, 3, 8)))

    # Write the payload (a PE binary) to a file
    open(r'./decrypted_rsrc.bin', 'wb').write(bytearray(decrypted_payload))

    if verbose:
        print("Saved the PE to ./decrypted_rsrc.bin")


r2 = r2pipe.open("dropshot.exe.vir")
decode_strings()
decrypt_resource()

# # Refresh the interface to load changes
# r2.refresh()
