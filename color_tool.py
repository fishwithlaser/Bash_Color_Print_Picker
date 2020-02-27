
"""
Black        0;30     Dark Gray     1;30
Red          0;31     Light Red     1;31
Green        0;32     Light Green   1;32
Brown/Orange 0;33     Yellow        1;33
Blue         0;34     Light Blue    1;34
Purple       0;35     Light Purple  1;35
Cyan         0;36     Light Cyan    1;36
Light Gray   0;37     White         1;37
"""

if __name__ == '__main__':
    color_list = [(30, 'Black'), (90, 'Dark Grey'), (31, 'Red'), (91, 'Bright Red'), (32, 'Green'), (92, 'Bright Green'),  (33, 'Bworange'), (93, 'Light Yellow'),  (34, 'Blue'), (94, 'Light Blue'), (35, 'Purple'), (95, 'Light Magenta'),  (36, 'Cyan'), (96, 'Bright Cyan'),  (37, 'Light Grey'), (97, 'White')]

    Bkgd = [x for x in range(41, 50)]
    Bkgd += [x for x in range(100, 107)]
    for codeY in Bkgd:
    
        _str = f'{codeY}'
        if len(str(codeY)) == 2:
            _str += ' '
        for code, color in color_list:
            _str += f"\033[{code}m\033[{codeY}m \\033[{code}m \033[0m "
        print(_str)

    print('print fun colours forever?')
    input()
    from random import randint
    bkdg_len = len(Bkgd) - 1
    j = 0
    str = ""
    while True:
        j += 1
        i = randint(0, bkdg_len)
        code = Bkgd[i]
        str += f"\033[{code}m "
        if j % 80 == 0:
            str += f"\033[0m "
            print(str)
            str = ""






