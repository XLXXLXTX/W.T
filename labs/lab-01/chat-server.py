#  Web Technologies Lab 1 | Author: Javier Pardos
import socket

def my_server(conn):
	#context resource manager to not forget 
	#to close socket & conn
	with conn:

		#print connections info
		print(f'{addr} connected.')
		conn.send(b'You are now connected.\n')

		while True: 
			#recive client msg and decode it 
			clientData = conn.recv(1024).decode('utf-8')
			##print(f'\t\tc - {len(clientData)}')
			
			#if msg from client is empty, end the loop
			#This will happen when client disconnect itself
			if not clientData:
				break
			
			print(f'client: {clientData}')

			#read msg from server and sent it encoded
			msg = input('server:')
			conn.send(msg.encode('utf-8'))

if __name__ == "__main__":
	#create socket ...
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#give ip, port ...
	s.bind(('localhost', 55555))

	#listen to incoming connections
	s.listen()

	#and accept all of then 
	conn, addr = s.accept()

	my_server(conn)