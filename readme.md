# omegalul
A Python library for building omegle clients

# Credits
This library is mostly based on [nucular's omegle reverse engineering gist](https://gist.github.com/nucular/e19264af8d7fc8a26ece)

# Usage
```python3
# get status and choose a random server
status = omegalul.fetch_status()
server = omegalul.get_random_server(status['servers'])

# start a chat
chat = omegalul.start_chat(server)

while True:
    # fetch events
    # if the latest event is a gotMessage event, take the message and send it back
    events = chat.fetch_events()

    if events == None:
        break

    event = events[0]

    if event[0] == 'gotMessage':
        print('Stranger: ', event[1])
        
        chat.send_message(event[1])
        print('sent it back')
```
