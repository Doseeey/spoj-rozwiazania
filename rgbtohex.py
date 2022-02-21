heks = {'#000000': 'black', '#C0C0C0': 'silver', '#808080': 'gray', '#FFFFFF': 'white',
        '#800000': 'maroon', '#FF0000': 'red', '#800080': 'purple', '#FF00FF': 'fuchsia',
        '#008000': 'green', '#00FF00': 'lime', '#808000': 'olive', '#FFFF00': 'yellow',
        '#000080': 'navy', '#0000FF': 'blue', '#008080': 'teal', '#00FFFF': 'aqua'}

def kolor(r, g, b):
    hr = hex(r)[2:].upper()
    hg = hex(g)[2:].upper()
    hb = hex(b)[2:].upper()

    if len(hr) == 1:
        t = hr
        hr = '0' + str(t)
    if len(hg) == 1:
        t = hg
        hg = '0' + str(t)
    if len(hb) == 1:
        t = hb
        hb = '0' + str(t)

    output = "#{}{}{}".format(hr,hg,hb)
    if output in heks:
        return heks[output]
    else:
        return output

n = int(input())
while n:
    n-=1
    r, g, b = map(int, input().split())
    print(kolor(r, g, b))