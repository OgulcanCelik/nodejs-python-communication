const { Subscriber, Request } = require("zeromq");
const fs = require("fs");

// initialize different types of zeromq clients for different types of use cases
const reqSock = new Request();

const subSock = new Subscriber();

// use different ports for different use cases
reqPort = 5556;
// 127.0.0.1 == localhost
reqSock.connect(`tcp://127.0.0.1:${reqPort}`);

subPort = 5557;
subSock.connect(`tcp://127.0.0.1:${subPort}`);
subSock.subscribe();

reqSock.send("sendImage");

subSock.receive().then((message) => {
  fs.writeFileSync(
    "./out_from_zmq.jpg",
    new Buffer(message.toString("utf-8"), "base64")
  );
});
