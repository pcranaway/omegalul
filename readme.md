# omegalul
A Python library for building omegle clients

# Credits
This library is mostly based on [nucular's omegle reverse engineering gist](https://gist.github.com/nucular/e19264af8d7fc8a26ece)

# Usage
Right now, Omegalul is stateless, there are no classes, you pass your client's ID and your chosen server around
```python3
# get status and choose a random server
status = omegalul.fetch_status()
server = omegalul.get_random_server(status['servers'])

# start a chat and get your client's ID
chat = omegalul.start_chat(server)
id = chat['clientID']

while True:
    events = omegalul.fetch_events(server, id)
    print(events)
```
