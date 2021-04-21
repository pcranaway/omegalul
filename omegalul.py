import requests
import random
import json
import string

def fetch_status():
    """
    fetches status of omegle, parses it into JSON and returns it
    """
    return json.loads(requests.get('http://omegle.com/status').text)

def get_random_server(servers):
    """
    gets a random omegle server
    """

    return 'https://{}.omegle.com'.format(random.choice(servers))

def generate_randid():
    """
    generates a randid which is a random string containing 8 2-9 and A-Z without I and O
    """

    chars = string.digits + string.ascii_uppercase
    chars = chars.replace('I', '')
    chars = chars.replace('O', '')

    return ''.join(random.choice(chars) for i in range(8))

def start_chat(server):
    """
    starts a chat using the specified server
    """

    response = requests.post('{}/start?rcs=1&firstevents=1&m=0&randid={}'.format(
        server,
        generate_randid()
    ))

    return json.loads(response.text)

def fetch_events(server, id):
    """
    fetches events of a chat
    """

    return json.loads(requests.post(server + '/events', data={'id': id}).text)

def send_message(server, id, message):
    """
    sends a message to a chat
    """

    requests.post(server + '/send', data={'msg': message, 'id': id})
