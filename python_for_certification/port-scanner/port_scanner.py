import socket
import re
import common_ports


"""
input: port_scanner.get_open_ports("www.freecodecamp.org", [75, 85])
"""
def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", target)

    target_ip = target
    target_name = target
    if (bool(match)):
        try:
            socket.inet_aton(target)
        except OSError:
            return str("Error: Invalid IP address")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return str("Error: Invalid hostname")

    # must be include last number, so +1.
    for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target_ip, port)) == 0:
            open_ports.append(port)
        s.close()
    if (verbose == False):
        return(open_ports)
    else:
        try:
            target_name = socket.gethostbyaddr(target_ip)[0]
        except socket.herror:
            target_name = target_ip
        if (target_name == target_ip):
            retval = "Open ports for {0}\n".format(target)
        else:
            retval = "Open ports for {0} ({1})\n".format(target_name, target_ip)
        retval += "PORT     SERVICE"
        for port in open_ports:
            name = common_ports.ports_and_services[port]
            retval += "\n" + str(port).ljust(9, ' ') + name
        return(retval)
