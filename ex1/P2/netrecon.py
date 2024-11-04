# PEP8 - NETRECON BY LEFSU
import argparse
import subprocess
import platform
import socket
import ipaddress


def reach_ip(host):
    """Ping a specific host to check if it's reachable."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        output = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return host, output.returncode == 0  # Check return code for success
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return host, False


def reach_network():
    def list_possible_ips():
        # Get the local IP address
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        # Get the subnet mask (assuming a typical class C network for simplicity)
        netmask = '255.255.255.0'
        # Create the network object
        network = ipaddress.ip_network(f"{local_ip}/{netmask}", strict=False)
        # List all possible IPs in the network
        possible_ips = list(network.hosts())
        return possible_ips

    # Print the possible IPs
    for ip in list_possible_ips():
        host, state = reach_ip(str(ip))
        print(f"Host '{host}' is {'reachable' if state else 'unreachable'}")


def reach_port(ip, port):
    # Create a socket to test the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection

    try:
        # Try to connect to the port
        result = sock.connect_ex((ip, port))
        if result == 0:
            # The port is open
            return f"Port {port} is open."
        else:
            # The port is closed
            return f"Port {port} is closed."
    except socket.error as e:
        return f"Error occurred: {e}"
    finally:
        sock.close()


def main():
    parser = argparse.ArgumentParser(description="Network connectivity and port checking tool.")

    # Mutually exclusive group for host/network argument
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--reach_host", type=str, help="The server address (IP or hostname) to verify connectivity.")
    group.add_argument("--reach_range_host", type=str, help="Range of hosts to verify connectivity. (ex: '200.1.1.20-50')")
    group.add_argument("--reach_network", action='store_true', help="Check the reachability of each machine on the local network.")

    # Port or Port Range argument for checking open ports
    parser.add_argument("--reach_port", type=str, help="IP and single port to check if it is open in the format 'IP PORT' (e.g., 192.168.1.1:80).")
    parser.add_argument("--reach_port_range", type=str, help="Range of ports to check if they are open (e.g., 20-80).")

    # Output argument
    parser.add_argument("--output", type=str, help="File to save the results (e.g., results.txt).")

    args = parser.parse_args()
    results = []

    # Check reachability for a specific host
    if args.reach_host:
        host, state = reach_ip(args.reach_host)
        print(f"Host '{host}' is {'reachable' if state else 'unreachable'}")

    if args.reach_range_host:
        ip_range = args.reach_range_host
        # Extract information from the variable
        base_ip, ip_range_end = ip_range.split('-')
        base_ip_prefix = base_ip.rsplit('.', 1)[0]
        start_ip = int(base_ip.rsplit('.', 1)[1])
        end_ip = int(ip_range_end)
        # Generate the list of IPs
        ip_list = [f"{base_ip_prefix}.{i}" for i in range(start_ip, end_ip + 1)]
        # Check the reachability of each IP
        for ip in ip_list:
            host, state = reach_ip(str(ip))
            print(f"Host '{host}' is {'reachable' if state else 'unreachable'}")

    if args.reach_network:
        reach_network()

    if args.reach_port:
        # Split the IP and port
        ip, port = args.reach_port.split(':')
        print(reach_port(ip, int(port)))

    if args.reach_port_range:
        ip, p1 = args.reach_port_range.split(':')
        p1, p2 = p1.split("-")
        for i in range(int(p1), int(p2) + 1):
            print(reach_port(ip, int(i)))


if __name__ == "__main__":
    main()
