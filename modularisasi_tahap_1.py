"""
PROGRAM MENGHITUNG LUAS SEGITIGA
LUAS SEGITIGA = ALAS * TINGGI / 2
"""

print('MENGHITUNG LUAS SEGITIGA')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'SEGITIGA DENGAN ALAS = {alas} DAN TINGGI = {tinggi} MEMILIKI LUAS = {luas_segitiga}')

print('\nMENGHITUNG LUAS SEGITIGA 2 DENGAN COPY PASTE')
alas = 20
tinggi = 15
luas_segitiga = alas * tinggi / 2
print(f'SEGITIGA DENGAN ALAS = {alas} DAN TINGGI = {tinggi} MEMILIKI LUAS = {luas_segitiga}')

print('\nFUNGSI MENGHITUNG LUAS SEGITIGA')


def menghitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


menghitung_luas_segitiga(10, 6)
menghitung_luas_segitiga(20, 15)

print('LOH KOK NGGAK KELIATAN ? \nIYA DONG KAN INTERPRETER NGGAK DISURUH NAMPILIN')
print('\nOKE DEH GUA TAMPILIN')
print(menghitung_luas_segitiga(10, 6))
print(menghitung_luas_segitiga(20, 15))

print('\nOKE BIAR KECE')
alas = 20
tinggi = 15
print(f'SEGITIGA DENGAN ALAS = {alas} DAN TINGGI = {tinggi} MEMPUNYAI LUAS = {menghitung_luas_segitiga(alas, tinggi)}')

print('\nDEVELOPED BY SETREN')


def luas_segitiga(alass, tinggii):
    luas_segitigaa = alass * tinggii / 2
    print(f'LUAS SEGITIGA DENGAN ALAS = {alass} DAN TINGGI = {tinggii} ADALAH = {luas_segitigaa}')


luas_segitiga(20, 15)
print('SETREN PANCEN JOSS')
