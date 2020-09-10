# CARA IMPORT FUNGSI LUAS SEGITIGA DARI MODUL SEGITIGA DARI PACKAGE GEOMETRI
from geometri.persegipanjang import luas_persegipanjang, info as persegipanjang_info
from geometri.segitiga import luas_segitiga, info as segitiga_info

luas_segitiga(20, 15)
print(segitiga_info())

luas_persegipanjang(20, 15)
print(persegipanjang_info())