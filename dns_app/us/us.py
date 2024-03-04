from flask import Flask, request, abort
import requests

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        abort(400)

    try:
        ip_address = resolve_hostname(hostname, as_ip, as_port)
    except Exception as e:
        return str(e), 500

    try:
        fibonacci_number = query_fibonacci_server(ip_address, fs_port, number)
    except Exception as e:
        return str(e), 500

    return str(fibonacci_number), 200


def resolve_hostname(hostname, as_ip, as_port):
    response = requests.get(f'http://{as_ip}:{as_port}/dns_lookup?hostname={hostname}')
    if response.status_code != 200:
        raise Exception(f"Failed to resolve hostname {hostname}: {response.text}")
    return response.text


def query_fibonacci_server(ip_address, fs_port, number):
    response = requests.get(f'http://{ip_address}:{fs_port}/fibonacci?number={number}')
    if response.status_code != 200:
        raise Exception(f"Failed to get Fibonacci number from server {ip_address}: {response.text}")
    return response.text


if __name__ == '__main__':
    app.run(port=8080)

