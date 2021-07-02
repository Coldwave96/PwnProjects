badchars = '\x62\x69\x63\x2f\x20\x66\x6e\x73'

sh_string = '/bin/sh\x00'

def xor(sh_str):
    i = 0
    for j in range(len(sh_str)):
        tmp = chr(ord(sh_str[j]) ^ i)
        if tmp in badchars:
            i = i + 1
    print i

xor(sh_string)