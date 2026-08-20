def validar_nome(nome):
    nome = nome.strip() # sem espaços no início ao fim
    
    if nome.isalpha(): # sem números
        return True
    else:
        return False

