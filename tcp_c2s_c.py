#C
import socket,os,time
c=0
while c==0:
    try:
        nam=input('Please input the name of the file which you want to upload it to your server />>> ')
        fil=open(nam,'rb')
        c=1
    except:
        print('no such file!\n\n')
fre=fil.read()
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('thatis.top',56889))
hea=b'tcp_c2s_by_python3\r\n\r\n'
soc.send(hea)
time.sleep(1)

rec=soc.recv(1024)
print(rec.decode('utf-8'))
if rec!=b'success\r\n\r\n':
	print('not connect successfully')
	soc.close()
	exit()
print('connect successfully!')
soc.send(nam.encode('utf-8'))
rec=soc.recv(1024)
print(rec.decode('utf-8'))
time.sleep(1)
rec=soc.recv(1024)
print(rec.decode('utf-8'))
soc.send(fre)
time.sleep(1)
end=b'end_of_tcp_c2s_by_python3\r\n\r\n'
soc.send(end)
rec=soc.recv(1024)
print(rec.decode('utf-8'))
if rec==b'Completed\r\n\r\n':
	print('\n')
	print('Completed!')

