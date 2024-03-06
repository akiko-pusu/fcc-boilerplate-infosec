import socket
import re


"""
input: port_scanner.get_open_ports("www.freecodecamp.org", [75, 85])
"""
def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", target)

    if (bool(match)):
        try:
            socket.inet_aton(target)
        except OSError:
            return str("Error: Invalid IP address")

    if (verbose == False):
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            return str("Error: Invalid hostname")

        for port in range(port_range[0], port_range[1]):
            # ipv4 and tcp
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target_ip, port)):
                print("The port is closed %s" % port )
            else:
                print("The port is open %s" % port)
                open_ports.append(port)

            s.close()
    return(open_ports)
