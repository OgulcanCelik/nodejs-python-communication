const redis = require("redis");
const fs = require("fs");

// initiliaze redis clients for different use cases
const subscriber = redis.createClient();
const client = redis.createClient();

// get hello key from redis
client.get("hello", (err, reply) => {
  console.log(`hello ${reply}`);
});

// subscribe to a channel to listen base64 encoded image
subscriber.subscribe("imageBase64");

// publish send command as image for subscriber to listen
client.publish("send", "img");

// set a callback function to execute when a new message pushed to the subscribed channel
subscriber.on("message", (channel, message) => {
  console.log(`got message from channel: ${channel}`);
  fs.writeFileSync("./out_from_redis.jpg", new Buffer(message, "base64"));
});
