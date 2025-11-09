import unicodedata

def eh_palindromo(frase: str) -> str:

    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFKD', frase.lower())
                                if unicodedata.category(c) != 'Mn')
    
    texto_limpo = "".join(char for char in texto_sem_acentos if char.isalnum())
    

    if not texto_limpo:
        return "Não"

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

print(f"'Nerd': {eh_palindromo('Nerd')}")
print(f"'Tenet' : {eh_palindromo('Tenet')}")
print(f"'Python': {eh_palindromo('Python')}")
print(f"'Luke': {eh_palindromo('Luke')}")

print(f"'Radar': {eh_palindromo('Radar')}")
print(f"'Eve': {eh_palindromo('Eve')}")

print("-" * 20)

print(f"'ovo' :{eh_palindromo('ovo')}")
print(f"'Ada' : {eh_palindromo('Ada')}")
print(f"'Marvel': {eh_palindromo('Marvel')}")
print(f"'Matrix': {eh_palindromo('Matrix')}")

print("-" * 20)


print(f"'Socorram-me, subi no ônibus em Marrocos': {eh_palindromo('Socorram-me, subi no ônibus em Marrocos')}")