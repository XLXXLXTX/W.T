#  Web Technologies Lab 1 | Author: Javier Pardos
import socket 

def my_client(s): 
	#loop condition
	chatting = True

	#loop to read and send msg to server 
	while chatting:

		#recive the initial msg of the server ('you are now connected')
		#decode the msg, because it was send in bytes from the server
		#conn.send(b ...) 
		serverData = s.recv(1024).decode('utf-8')
		##print(f'\t\ts - {len(serverData)}')
		print(f'server: {serverData}')

		#read the client message
		msg = input('client: ')
		
		#send the msg,
		s.sendall(msg.encode('utf-8'))

		#if message equal bye, clients close the chat session
		if msg == 'bye':
			chatting = False
			print(msg)

	#at the end fo the loop, close socket
	s.close()

if __name__ == "__main__":
	#create socker with IPV4 and TCP/IP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#connect to given ip, localhost:8081
	s.connect(('localhost', 55555))

	my_client(s)