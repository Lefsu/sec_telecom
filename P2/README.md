```markdown
# NETRECON

NETRECON is a network connectivity and port checking tool. It allows you to determine if a host is reachable, analyze the range of IP addresses on the local network, and check if specific ports or port ranges are open.

## Features

- Check the connectivity of a specific host (IP address or hostname).
- Analyze the range of IP addresses on the local network.
- Check the status of a specific port on a host.
- Check the status of a range of ports on a host.

## Prerequisites

- Python 3.x
- Standard Python libraries (no additional installation required)

## Installation

Clone this repository or download the Python file `netrecon.py` to your machine.

## Usage

Run the script from the command line with the appropriate arguments:

```bash
python netrecon.py [OPTIONS]
```

### Options

- `--reach_host <address>`: Check the connectivity of a specific host (IP or hostname).
- `--reach_range_host <range>`: Check the connectivity of a range of hosts (e.g., '192.168.1.20-50').
- `--reach_network`: Check the connectivity of each machine on the local network.
- `--reach_port <IP:PORT>`: Check if a specific port is open on a host (e.g., '192.168.1.1:80').
- `--reach_port_range <IP:RANGE>`: Check if ports in a range are open on a host (e.g., '192.168.1.1:20-80').
- `--output <file>`: Specify a file to save the results (e.g., `results.txt`). (coming soon)

### Examples

1. Check the connectivity of a host:

    ```bash
    python netrecon.py --reach_host 192.168.1.1
    ```

2. Check the connectivity of a range of hosts:

    ```bash
    python netrecon.py --reach_range_host 192.168.1.20-50
    ```

3. Check the connectivity of all hosts on the local network:

    ```bash
    python netrecon.py --reach_network
    ```

4. Check if a port is open on a host:

    ```bash
    python netrecon.py --reach_port 192.168.1.1:80
    ```

5. Check a range of ports:

    ```bash
    python netrecon.py --reach_port_range 192.168.1.1:20-80
    ```

## Help

To display available options and help, run:

```bash
python netrecon.py --help
```


## License

This project is licensed under the [MIT License](LICENSE).