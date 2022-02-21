import sys
msg = sys.stdin.readlines()

def swap(txt):
    txt = list(txt)
    zm = {"??=":"#", "??/":"\ ", "??'":"^", "??(":"[", "??)":"]", "??!":"|", "??<":"{", "??>":"}", "??-":"~"}
    for char in txt:
        res = ''
        if char == '?':
            res += '?'
            i1 = txt.index(char)
            if str(txt[i1+1]) == '?':
                res += '?'
                res += txt[i1+2]
                if res in zm:
                    txt.remove(txt[i1+2])
                    txt.remove(txt[i1+1])
                    txt[i1] = zm[res]
    return txt




for item in msg:
    print(''.join(swap(item)))