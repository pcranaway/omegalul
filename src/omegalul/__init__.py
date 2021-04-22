import requests
import random
import json
import string
import enum

servers = []
server = ''

class Event(enum.Enum):
    """
    represents an event
    """
    GOTMESSAGE = 1
    STRANGERDISCONNECTED = 2
    TYPING = 3

class Chat:
    """
    represents a chat
    """

    def __init__(self, client_id):
        """
        creates a chat with a client id
        """

        self.client_id = client_id
        self.messages = []

    def fetch_event(self):
        """
        fetches the latest event of the chat
        returns only when a new event is received
        """

        event = json.loads(requests.post(server + '/events', data={'id': self.client_id}).text)[0]

        if event[0] == 'gotMessage':
            return (Event.GOTMESSAGE, event[1])

        if event[0] == 'strangerDisconnected':
            return (Event.STRANGERDISCONNECTED, None)

        if event[0] == 'typing':
            return (Event.TYPING, None)

        return event

    def send_message(self, message):
        """
        sends a message to a chat
        """

        requests.post(server + '/send', data={'msg': message, 'id': self.client_id})

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

def start_chat():
    """
    starts a chat using the specified server
    """

    response = requests.post('{}/start?rcs=1&firstevents=1&m=0&randid={}'.format(
        server,
        generate_randid()
    ))

    client_id = json.loads(response.text)['clientID']

    return Chat(client_id)

# hopefully this is called when the module is imported
servers = fetch_status()['servers']
server = get_random_server(servers)
