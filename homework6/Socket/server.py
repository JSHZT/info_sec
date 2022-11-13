import socketserver
from DH import dh_
from BasicMathImplementation.Math import Prime
import json


class ServerSocket(socketserver.BaseRequestHandler):

	def initDiffieHellman(self):
		if self.request.recv(1024).decode() != "connected":
			print("Error while connecting")
		publicSecret = self.__dh.calcPublicSecret()
		step1 = "{"
		step1 += "\"dh-keyexchange\":"
		step1 += "{"
		step1 += "\"step\": {},".format(1)
		step1 += "\"base\": {},".format(self.__dh.base)
		step1 += "\"prime\": {},".format(self.__dh.sharedPrime)
		step1 += "\"publicSecret\": {}".format(publicSecret)
		step1 += "}}"
		self.request.send(step1.encode())
		step2 = self.request.recv(1024)
		if self.__debugflag:
			print(step2)
		jsonData = json.loads(step2.decode())
		jsonData = jsonData["dh-keyexchange"]
		publicSecret = int(jsonData["publicSecret"])
		self.__dh.calcSharedSecret(publicSecret)
	def handle(self):
		self.__debugflag = self.server.conn
		self.__dh = dh_.DH()
		print("[{}] Client connected.".format(self.client_address[0]))
		self.initDiffieHellman()
		print("> The secret key is {}\n".format(self.__dh.key))

def start_server(debugflag):
	server = socketserver.ThreadingTCPServer(("", 50000), ServerSocket)
	server.conn = debugflag
	server.serve_forever()
