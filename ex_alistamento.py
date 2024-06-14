from datetime import datetime
nascimento = int(input('Ano de nascimento: '))

idade = 2023 - nascimento
#anos passados sem se alistar alistar:
alistamento = idade - 18
ano_atual = datetime.now().year
#ano em que a pessoa vai precisar se alistar:
ano_alistamento = idade - ano_atual
# ano em que a pessoa deveria ter se alistado:
alistamento_atrasado = ano_atual - alistamento
# anos que faltam para se alistar
faltam = ano_atual - nascimento
alistamento_futuro = ano_atual + faltam


if idade == 18:
    print(f'Quem nasceu em {nascimento}, tem {idade} anos de idade')
    print('Você precisa se alistar o mais rápido possível!')

elif idade > 18:
    print(f'Quem nasceu em {nascimento}, tem {idade} anos de idade')
    print(f'Você já deveria ter se alistado em {alistamento_atrasado}.')
    print('Você precisa se alistar urgentemente!')

elif idade < 18:
    print(f'Quem nasceu em {nascimento}, tem {idade} anos de idade')
    print(f'Ainda faltam {faltam} ano(s) para o seu alistamento.')
    print(f'Seu alistamento será em {alistamento_futuro}')


