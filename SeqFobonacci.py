vOne = int(0) #Convertendo o valor para inteiro e seu resultado será 0
vTwo= int(1) #Convertendo o valor para inteiro e seu resultado será 1
vThree = int(0) #Convertendo o valor para inteiro e seu resultado será 0

result = int(input("Informe um numero: ")) #Resultado irá receber um comando externo e inteiro
while result > vThree: #Enquanto o resultado for menor que o valor 3...
    vThree = vOne + vTwo #Somando os valores
    vOne = vTwo #Valor 1 vai ficar com o valor 2
    vTwo = vThree #Valor 2 vai ficar com o resultado da soma
if result == 0 or result == 1: #Se o resultado for igual a 0 ou o resultado igual a 1...
    print('O número informado faz parte da sequencia.')
elif result == vThree: #Se não se o resultado for igual ao valor total (valor três)...
    print('O número informado faz parte da sequencia.')
else: #Se não...
    print("O número informado não faz parte da sequencia.")
