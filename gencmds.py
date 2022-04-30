#!/usr/bin/python3

import sys

_BANHAMMER_CMD = ' '.join((
    'iptables',
    '-t raw',
    '-I PREROUTING',
    '-p udp',
    '-m multiport',
    '--dports {ports}',
    '-m string',
    '--algo bm',
    '--hex-string "|{hex}|"',
    '-j DROP',
))
_CURVE25519_PUB_LEN = 32
_BASE58_ALPH = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def _reverse_base58_alph():
    rev_alph = [None] * 256
    for i, char in enumerate(_BASE58_ALPH):
        rev_alph[ord(char)] = i
    return rev_alph


_RBASE58_ALPH = _reverse_base58_alph()


def _base58_dec(str58):
    rev_alph = _reverse_base58_alph()
    result_num = 0
    for char in str58:
        result_num = result_num * len(_BASE58_ALPH) + rev_alph[ord(char)]
    return result_num.to_bytes(_CURVE25519_PUB_LEN, 'big')


def main():
    if len(sys.argv) != 3:
        print('Usage:', file=sys.stderr)
        print(f'    {sys.argv[0]} <file with public keys> <comma-separated list of UDP ports>', file=sys.stderr)
        exit(1)
    _, pubkeys_fname, udp_ports = sys.argv

    with open(pubkeys_fname, 'r') as pubkeys_f:
        for line in pubkeys_f.readlines():
            line = line.strip()
            if line.startswith('#'):
                # Comment.
                continue
            if not line:
                # Empty line.
                continue

            pubkey = _base58_dec(line)
            pubkey = pubkey.hex()

            cmd = _BANHAMMER_CMD.format(ports=udp_ports, hex=pubkey)
            print(cmd)


main()
