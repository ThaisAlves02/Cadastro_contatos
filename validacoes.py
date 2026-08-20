def validar_nome(nome):
    nome = nome.strip() # sem espaços no início ao fim
    
    if nome == "":
        return False
    else:
        return nome.isalpha() # sem números

def validar_telefone(telefone):
    telefone = telefone.strip() # sem espaços no início ao fim
    
    if telefone == "":
        return False
    else:
        return telefone.isdigit() and len(telefone) == 11
    
        