def validar_nome(nome):
    nome = nome.strip() # sem espaços no início ao fim
    
    if nome == "":
        return False
    else:
        return nome.isalpha() # sem números
