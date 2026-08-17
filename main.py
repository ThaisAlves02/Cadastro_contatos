import customtkinter as ctk
from tkinter import ttk, messagebox #ttk para fazer a tabela

def adicionar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    




#==========================================
#Configurações da janela principal
#==========================================

janela = ctk.CTk()
janela.title('Cadastro de clientes')
janela.geometry('600x500')

#==========================================
#TITULO
#==========================================

titulo = ctk.CTkLabel(janela,text='Cadastro',font=('Arial', 28, 'bold'))
titulo.pack()


#==========================================
#CAMPOS DE ENTRADA(Nome,Telefone,Email)
#==========================================

frame_formulario = ctk.CTkFrame(janela)
frame_formulario.pack(padx=20, pady=20, fill='x')

label_nome = ctk.CTkLabel(frame_formulario, text='Nome')
label_nome.pack(padx=10, pady=(10, 0), anchor='w')
entry_nome = ctk.CTkEntry(frame_formulario, placeholder_text='Digite o seu nome')
entry_nome.pack(padx=10, pady=(0, 10), fill='x')

label_telefone = ctk.CTkLabel(frame_formulario, text='Telefone', anchor='w')
label_telefone.pack(padx=10, pady=(10, 0), anchor='w')
entry_telefone = ctk.CTkEntry(frame_formulario, placeholder_text='Digite o seu telefone')
entry_telefone.pack(padx=10, pady=(0, 10), fill='x')

label_email = ctk.CTkLabel(frame_formulario, text='Email')
label_email.pack(padx=10, pady=(10, 0), anchor='w')
entry_email = ctk.CTkEntry(frame_formulario, placeholder_text='Digite o seu Email')
entry_email.pack(padx=10, pady=(0, 10), fill='x')

#==========================================
#TREEVIEW (Lista de contatos)
#==========================================

colunas = ('Nome', 'Telefone', 'Email')
tabela = ttk.Treeview(janela, columns=colunas, show='headings') #Cria o objeto 'tabela'

tabela.heading('Nome', text='Nome')
tabela.heading('Telefone', text='Telefone')
tabela.heading('Email', text='Email')

tabela.pack(fill='both', padx=20, pady=10)


#==========================================
#BOTÕES
#==========================================

frame_botoes = ctk.CTkFrame(janela,fg_color='transparent')
frame_botoes.pack()

botao_adicionar = ctk.CTkButton(frame_botoes, text='Adicionar')
botao_adicionar.pack(padx=5, side='left')

botao_editar = ctk.CTkButton(frame_botoes, text='Editar')
botao_editar.pack(padx=5, side='left')

botao_excluir = ctk.CTkButton(frame_botoes, text='Excluir', hover_color='red')
botao_excluir.pack(padx=5)










janela.mainloop()