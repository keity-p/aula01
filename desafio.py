# 1) Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input('Digite o valor do seu salário: '))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input('Digite o valor do seu bônus: '))

# 4) Calcule o valor do bônus final
resultado = salario + bonus

# 5) Imprima cálculo do KPI para o usuário
print('\n')
print(resultado)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário
print(nome + ' o valor do seu bônus final será: ' + str(resultado))