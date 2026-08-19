import customtkinter as ctk
from tkinter import ttk, messagebox #ttk para fazer a tabela
import database

def adicionar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    
    
    #validação de string vazia ou espaços em branco
    if nome.strip() == "" or telefone.strip() == "" or email.strip() =="":
        return messagebox.showwarning('Atenção',"Os campos não podem estar em branco!")
    
    
    #Adiconar dados no banco
    database.adicionar_contato(nome,telefone,email)
    atualizar_tabela()
    #limpa os campos para o próximo cadastro
    entry_nome.delete(0,"end") # 0, end significa do começo ao fim
    entry_telefone.delete(0,"end")
    entry_email.delete(0,"end")
    

def atualizar_tabela():
    
    #1. limpa tudo que já está na tabela
    tabela.delete(*tabela.get_children())#pega todas linhas da tabela
    
    #2. Carregar os contatos atualizados do JSON
    contatos = database.carregar_contatos()
    
    #3. Inserir cada contato como uma linha nova na tabela
    for contato in contatos:
        tabela.insert("","end",values=(contato['nome'], contato['telefone'],contato['email']))
    
def excluir():
    dado_selecionado = tabela.selection()
    
    # pegar o índice do item selecionado
    indice = tabela.index(dado_selecionado[0])

    # janela de confirmação
    confirmar = messagebox.askyesno('Deseja excluir esse arquivo?')
    
    if confirmar == True:
         #carregar o arquivo JSON
            contatos = database.carregar_contatos()
            contatos.pop(indice)
            
            database.salvar_contatos(contatos)
            atualizar_tabela()
            



#==========================================
#Configurações da janela principal
#==========================================

janela = ctk.CTk()
janela.title('Cadastro de clientes')
janela.geometry('600x600')









#==========================================
#TITULO
#==========================================

cabecalho = ctk.CTkLabel(janela,
                      text='Cadastro',
                      font=('Arial',20,'bold'))
cabecalho.pack()

# ------------------------------------------------------------
# CAMPOS DE ENTRADA (Nome, Telefone, Email)
# ------------------------------------------------------------

frame_formulario = ctk.CTkFrame(janela)
frame_formulario.pack(padx=20, pady=20,fill='x')#fill ajusta o objeto ao eixo(x,y,both)

label_nome = ctk.CTkLabel(frame_formulario, text="Nome:")
label_nome.pack(padx=10, pady=(10, 0),anchor="w")#anchor ajusta a janela(w=esquerda,e=direita)
entry_nome = ctk.CTkEntry(frame_formulario, placeholder_text="Digite o nome")
entry_nome.pack(padx=10, pady=(0, 10),fill='x')

label_telefone = ctk.CTkLabel(frame_formulario, text="Telefone:")
label_telefone.pack(padx=10, pady=(10, 0),anchor="w")
entry_telefone = ctk.CTkEntry(frame_formulario, placeholder_text="Digite o Telefone")
entry_telefone.pack(padx=10, pady=(0, 10),fill='x')

label_email = ctk.CTkLabel(frame_formulario, text="email:")
label_email.pack(padx=10, pady=(10, 0),anchor="w")
entry_email = ctk.CTkEntry(frame_formulario, placeholder_text="Digite o email")
entry_email.pack(padx=10, pady=(0, 10),fill='x')


# ------------------------------------------------------------
# TREEVIEW (lista de contatos)
# ------------------------------------------------------------

colunas = ('Nome','Telefone','Email')
tabela = ttk.Treeview(janela,columns=colunas,show='headings')#Cria o objeto "tabela"

tabela.heading('Nome',text='Nome')
tabela.heading('Telefone',text='Tefone')
tabela.heading('Email',text='Email')

tabela.pack(fill='both',padx=20,pady=10)

# ------------------------------------------------------------
# BOTÕES
# ------------------------------------------------------------

frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
frame_botoes.pack(padx=20, pady=(0, 20), fill="x")

botao_adicionar = ctk.CTkButton(frame_botoes, text="Adicionar",command=adicionar)
botao_adicionar.pack(side="left", padx=5)

botao_editar = ctk.CTkButton(frame_botoes, text="Editar")
botao_editar.pack(side="left", padx=5)

botao_excluir = ctk.CTkButton(frame_botoes, 
                              text="Excluir", 
                              fg_color="#d9534f", 
                              hover_color="#c9302c", command=excluir)
botao_excluir.pack(side="left", padx=5)







atualizar_tabela()
janela.mainloop()