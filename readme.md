# Nodejs - Python

This repository includes simple Nodejs and Python scripts to show different communication ways between Nodejs and Python.

Let's install dependencies first:

# Dependencies

## Redis

Redis currently is not supported in Windows.

For Ubuntu-based distros:

```
sudo apt install Redis
```

For macOS via Homebrew:

```
brew install Redis
```

You can check if Redis working by

```
redis-cli ping
```

You should see

```
PONG
```

# Packages

## Nodejs

```
npm i
```

## Python

```
pip install -r requirements.txt
```

# Communicating via Redis

Redis is an amazing tool that can be used as a database, message broker, cache purposes, and more awesome stuff. Redis lives in memory, so it's very fast compared to the other databases and it can serve 1 million requests per second!

Most common languages have Redis bindings including Python and Nodejs.

You can store values in key:value format just like in JSON.

You can access redis-cli via this command:

```
redis-cli
```

Then you can start executing Redis commands and examine how it works!

Here is an awesome quick-guide: https://www.tutorialspoint.com/redis/redis_quick_guide.htm

Please read it carefully and understand the basic data types, keys, values, and pub/sub.

On Redis folder, you have two scripts, one for Python and one for Nodejs. Start Python one `main.py` first and then Nodejs `main.js`.

Python script is going to set `hello` key to `world` and wait for messages in `send` channel.
When Nodejs script runs, it is going to read the `hello` key value from the Redis store and print it to the console. Then, it is going to set `send` command as `img`. Python is going to capture this and start the process.

First, Python script going the read the test image in bytes, then convert it to base64 encoded string so it will become easier to share with Nodejs. On the last line, you can see that Python publishes the encoded string to the `imageBase64` channel.

When Nodejs subscriber gets a message on `imageBase64`, it will decode the base64 string to bytes and then going to write the image as `out_from_redis.jpg`. This is a very basic way of transferring images between Nodejs and Python using Redis.

# Communicating via ZeroMQ

ZeroMQ is a popular socket framework that uses in-process, inter-process, TCP, and multicast. You can easily create connections like N-to-N, fan-out, pub-sub, request-reply, and more.

You can check these links for more information:

https://zeromq.org/

https://www.tutorialspoint.com/unix_sockets/what_is_socket.htm

ZeroMQ is using network communication, you have to specify ports for different sockets. In this example, we are going to use `5556` for the request-response socket and `5557` for the publisher/subscriber socket.

Python script is going to create two sockets and start a listening message from the req socket. When a message is received, it is going to validate if the message is `sendImage` and then starts the same process just like Redis one.
