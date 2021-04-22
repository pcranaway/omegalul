# omegalul
A Python library for building omegle clients

# Credits
This library is mostly based on [nucular's omegle reverse engineering gist](https://gist.github.com/nucular/e19264af8d7fc8a26ece)

# Usage
```python3
import omegalul

# start a chat
chat = omegalul.start_chat()
print(chat)

while True:
    event = chat.fetch_event()

    print(event)

    if event[0] == omegalul.Event.GOTMESSAGE:
      chat.send_message(event[1])
      print('sent message back')
```
