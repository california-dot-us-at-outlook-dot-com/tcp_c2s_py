




#S
import socket,os,threading

def hand(cli):
	rec=cli.recv(1024)
	print(rec)
	if rec != b'tcp_c2s_by_python3\r\n\r\n' :
		cli.close()
		cli.send(b'incorrect_head!\r\n')
		print('head is not correct!')
		return 'head is not correct!'
	cli.send(b'success\r\n\r\n')
	dan=cli.recv(1024)
	try:
		dna=dan.rindex(b'/')
		nam=dan[dna+1:]
	except:
		nam=dan
	din='/home/neon/files/upload/'+nam.decode('utf-8')
	if os.path.isfile(din):
		cli.send(b'file_is_exist!\r\n')
		cli.close()
		print('file is exist!')
		return 'file is exist!'
	cli.send(b'new_file\r\n')
	try:
		fop=open(din,'wb')
	except:
		cli.send(b'cannot_write_file!\r\n')
		cli.close()
		print('cannot write file!')
		return 'cannot write file!'
	cli.send(b'open_file_successfully!\r\n')
	print('open file successfully!')
	rec=b''
	try:
		while rec != b'end_of_tcp_c2s_by_python3\r\n\r\n' :	
			fop.write(rec)
			rec=cli.recv(1024)
		fop.close()
		cli.send(b'Completed\r\n\r\n')
	except:
		cli.send(b'Something_Wrong!\r\n')
	cli.close()

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('172.19.64.36',56889))
soc.listen(6)
while 1:
	cli=soc.accept()
	threading.Thread(target=hand,args=(cli[0],)).start()
