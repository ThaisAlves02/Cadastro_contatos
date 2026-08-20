import re

# validação de nome
# sem números
# sem espaços no início ao fim
# sem símbolos estranhos: Evite usar pontos ,:/@
# nome = input('Digite o nome:').strip()

# if nome.isalpha():
#     print(nome)
# else:
#     print('O nome não pode conter números ou caracteres especiais')
    
    
# # validação de telefone
# # Só pode números
# # Somente 11 números
# telefone = input('Digite o telefone:').strip()

# if telefone.isdigit() and len(telefone) == 11:
#     print(telefone)
# else:
#     print('Digite apenas números inteiros! O telefone deve ter 11 digitos.')


# validação de email
email = input('Digite o email:').strip()

email_padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_padrao, email):
    print(email)
else:
    print('Digite um email válido!')