import socket
import json

DNS_FILE = "dns_records.json"

def register_dns_record(data):
    try:
        with open(DNS_FILE, 'r') as file:
            dns_records = json.load(file)
    except FileNotFoundError:
        dns_records = {}

    dns_records[data['NAME']] = {'VALUE': data['VALUE'], 'TTL': data['TTL']}

    with open(DNS_FILE, 'w') as file:
        json.dump(dns_records, file)

def handle_registration_request(data):
    register_dns_record(data)

def handle_dns_query(data):
    with open(DNS_FILE, 'r') as file:
        dns_records = json.load(file)

    requested_record = dns_records.get(data['NAME'])

    if requested_record:
        dns_response = f"TYPE=A\nNAME={data['NAME']}\nVALUE={requested_record['VALUE']}\nTTL={requested_record['TTL']}"
    else:
        dns_response = ""

    return dns_response

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udp_socket.bind(('', 53533))  # Changed from ('0.0.0.0', 53533)

        print("Authoritative Server (AS) is running...")

        while True:
            data, addr = udp_socket.recvfrom(1024)
            data = data.decode().splitlines()

            request_type = data[0].split('=')[1]

            if request_type == 'A':
                registration_data = {line.split('=')[0]: line.split('=')[1] for line in data[1:]}
                handle_registration_request(registration_data)
                print("Registration successful:", registration_data)
            elif request_type == 'DNS Query':
                dns_query_data = {line.split('=')[0]: line.split('=')[1] for line in data[1:]}
                dns_response = handle_dns_query(dns_query_data)
                udp_socket.sendto(dns_response.encode(), addr)
                print("DNS Query response sent:", dns_response)

if __name__ == '__main__':
    main()