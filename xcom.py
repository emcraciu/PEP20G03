import communicator

client = communicator.Client('localhost', 1234)
server = communicator.Server('localhost', 1234)
server.start()
client.start()
server.stop()
