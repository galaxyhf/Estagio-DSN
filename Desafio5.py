string_original = input("Digite a string que deseja inverter: ")

string_invertida = ""
for caractere in string_original:
    string_invertida = caractere + string_invertida

print(f"A string invertida é: {string_invertida}")