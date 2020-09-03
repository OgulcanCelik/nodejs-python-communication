import redis
import base64

# initiliaze redis client
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe("send")

# set hello key to 'world'
r.set("hello", "world")

while True:
    for request in pubsub.listen():
        # on python the request is a dictionary including the type, pattern, channel and the data
        print("Received request: ", request)
        if request["data"] == "img":
            # open an image as bytes
            with open("test.jpg", "rb") as img_file:
                # ! you can base64 encode an image bytes to share between network easily
                my_string = base64.b64encode(img_file.read())
            r.publish("imageBase64", my_string)
