print("Bu benim ilk ödevim")

yazi= 'MERYEM'
print(yazi)
print(yazi[0])
print(yazi[1:3])
print(yazi[3])
print(yazi *3)
print(yazi + 'ÜNALDI')

liste1 = [100, 'Meryem']
liste2 = [150, 'Ayşe']
print(liste1)
print(liste1[0])
print(liste2 * 2)
print(liste1 + liste2)

liste = [2, 4, 5, 7]
liste.append(8)
print(liste)

liste = [2, 4, 5, 7]
liste.remove(2)
print(liste)

liste.sort()
print(liste)

uzunluk = len(liste)
print(liste)
print("Güncel Liste:", liste)
print("Listenin uzunluğu:", uzunluk)
print("Listenin ilk elemanı:", liste[0])