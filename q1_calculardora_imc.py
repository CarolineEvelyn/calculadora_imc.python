
# entrada
peso = float(input('digite seu peso (kg):\n-> '))
altura = float(input('digite sua altura (metros):\n-> ' ))

# processamente 
imc = peso / (altura ** 2)

# saída
print('seu imc é: ', imc)

if imc <= 18.4:
    print('classificação: Magreza')

if imc >= 18.5 and imc <= 24.9:
    print('classificação: Adequado') 
    
if imc >= 25.0 and imc <= 29.9:
    print('classificação: Pré-Obeso')
    
if imc >= 30.0:
    print('classificação: Obesidade')