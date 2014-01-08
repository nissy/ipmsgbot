#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import random
import argparse

# http://smart-pda.net/isourou/ipmsg/doc/ipmsg_protocol.html
def getMsgFormat(user, host, command_no, message):
    return "1:%d:%s:%s:%d:%s" % (
        random.randint(1, 1000),
        user,
        host,
        command_no,
        message
    )

def main():
    parser = argparse.ArgumentParser(description='ipmsg')
    parser.add_argument('ipaddress', type=str, help='remote ip address')
    parser.add_argument('-u', type=str, help='source user name')
    parser.add_argument('-m', required=True, type=str, help='message')
    parser.add_argument('--port', type=str, help='port')
    args = parser.parse_args()

    command_no = 32
    source_host = 'localhost'

    # Set ipaddress
    ipaddress = args.ipaddress

    # Set port
    port = 2425
    if not args.port is None:
        port = args.port

    # Set source_user
    source_user = socket.gethostname()
    if not args.u is None:
        source_user = args.u.decode("utf-8").encode('cp932')

    # Set message
    message = args.m.decode("utf-8").encode('cp932')

    # Send message
    try:
        sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sc.sendto(getMsgFormat(source_user, source_host, command_no, message), (ipaddress, port))
    except:
        print 'Send Error'

if __name__ == "__main__":
    main()
