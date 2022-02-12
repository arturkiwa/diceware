from wordlistpl import wordlist
import secrets

ile_rzutow = 5
wynik_rzutu = []
lista_slow = []
ile_slow = 5

for r in range(ile_slow):
    kostka = ''.join(str(secrets.randbelow(6) + 1) for r in range(ile_rzutow))
    wynik_rzutu.append(kostka)

for i in wynik_rzutu:
    lista_slow.append(wordlist[i])

print('\n<--- TWOJE Słowa do zapamiętania --->\n')
for i in lista_slow:
    print(i, end=' ')

final_passphrase = " ".join(lista_slow).replace(" ", "")

print('\n\n<--- Twoje bezpieczne hasło --->\n')
print(final_passphrase)