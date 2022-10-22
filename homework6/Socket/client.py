import socket
from DH import dh_
import json


class ClientSocket:
	def __init__(self, debugflag):
		self.__dh = dh_.DH()
		self.__debugflag = debugflag

	def initDiffieHellman(self, socket):
		socket.send("connected".encode())
		step1 = socket.recv(1024)
		if self.__debugflag:
			print(step1)
		jsonData = json.loads(step1.decode())
		jsonData = jsonData["dh-keyexchange"]
		self.__dh.base = int(jsonData["base"])
		self.__dh.sharedPrime = int(jsonData["prime"])
		publicSecret = int(jsonData["publicSecret"])
		calcedPubSecret = str(self.__dh.calcPublicSecret())
		step2 = "{"
		step2 += "\"dh-keyexchange\":"
		step2 += "{"
		step2 += "\"step\": {},".format(2)
		step2 += "\"publicSecret\": {}".format(calcedPubSecret)
		step2 += "}}"
		socket.send(step2.encode())
		self.__dh.calcSharedSecret(publicSecret)

	def start_client(self, ip):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((ip, 50000));
			self.initDiffieHellman(sock)
			print("The secret key is {}".format(self.__dh.key))
		finally:
			sock.close()
