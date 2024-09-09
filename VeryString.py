text = str(input("Informe um texto ou palavra aqui: ")) #Recebe um input externo sendo string
text.lower() #Transforma tudo em minusculo para contar corretamente
count = text.count('a') #Conta quandos 'a' aparecem na variável text
if count > 0: #Se o contador for maior que 0...
    print("Existe a letra 'a'")
    print("A letra 'a' aparece ",count," vezes")
else: #Se não...
    print("A letra 'a' nao aparece por aqui :(")