import banco_dados.b_d as db
import sqlite3
import streamlit as st
import pandas as pd

cursor, conexao = db.iniciarbanco()

#transformar tabelas em lista de dicionarios
def listar_dados(cursor, tabela):
    tabela = cursor.execute(f"SELECT * FROM {tabela}")

    #transformar em lista de dicionarios
    lista_dados = []
    colunas = [descricao[0] for descricao in tabela.description]

    for linha in tabela.fetchall():
        dado_dict = {colunas[i]: linha[i] for i in range(len(colunas))}
        lista_dados.append(dado_dict)

    return lista_dados

print(listar_dados(cursor, "livros"))

def carregar_dados(tabela):
    try:
        data = db.listar_dados(cursor, tabela)
        if not data:
            st.info(f"Nenhum dado encontrado na tabela {tabela}.", icon="ℹ️")
            return []

        return data
    except Exception as e:
        st.error(f"Erro ao carregar {tabela}: {e}")
        return []



# # db.criar_tabela_cliente(cursor)
# # db.criar_tabela_livro(cursor)
# # db.criar_tabela_editora(cursor)
# # db.criar_tabela_Endereco(cursor)

# # db.inserir_cliente(cursor,conexao,"999.888.777-12","Rian","list_livros_comprados","99 91234-9856")

# # db.atualizar_dados(cursor,conexao,"clientes","nome","e",1)

# # db.apagar_dado(cursor, conexao, "clientes",1)

# st.title("Sistema de Gerenciamento de Biblioteca")
# st.write("Bem-vindo ao sistema de gerenciamento de biblioteca!")

# #fazer o load das tabelas
# def carregar_livros():
#     try:
#         data = db.listar_dados(cursor,"livros")
#         if not data:
#             st.info("Nenhum dado encontrado no banco de dados.", icon="ℹ️")
#             return []

#         livros = [
#             {
#                 "id": livro[0],
#                 "titulo": livro[2],
#                 "autor": livro[1],
#                 "editora": livro[3],
#                 "qnt_estoque": livro[4]
#             }
#                 for livro in data
#         ]
#         return livros
#     except Exception as e:
#         st.error(f"Erro ao carregar livros: {e}")
#         return []
    
# def carregar_clientes():
#     try:
#         data = db.listar_dados(cursor,"clientes")
#         if not data:
#             st.info("Nenhum dado encontrado no banco de dados.", icon="ℹ️")
#             return []

#         clientes = [
#             {
#                 "id": cliente[0],
#                 "nome": cliente[1],
#                 "cpf": cliente[2],
#                 "telefone": cliente[4],
#                 "list_livros_comprados": cliente[3]
#             }
#                 for cliente in data
#         ]
#         return clientes
#     except Exception as e:
#         st.error(f"Erro ao carregar clientes: {e}")
#         return []

# with st.sidebar:
#     st.header("Navegação")
#     pagina = st.selectbox("Ir para", ["Início", "Clientes", "Livros"])

# pagina = pagina.lower()

# if pagina == "início":
#     st.subheader("Página Inicial")
#     st.write("Aqui você pode gerenciar clientes, livros e editoras.")

#     escolha = st.selectbox("Selecione uma opção:", ["clientes", "livros", "editoras"])
#     if escolha == "clientes":
#         clientes_data = carregar_dados("clientes")
#         if clientes_data:
#             st.table(pd.DataFrame(clientes_data))

# elif pagina == "clientes":
#     st.subheader("Gerenciamento de Clientes")
#     st.write("Funcionalidades para gerenciar clientes serão implementadas aqui.")
    

# elif pagina == "livros":
#     st.subheader("Gerenciamento de Livros")
#     st.write("Funcionalidades para gerenciar livros serão implementadas aqui.")


# elif pagina == "editoras":
#     st.subheader("Gerenciamento de Editoras")
#     st.write("Funcionalidades para gerenciar editoras serão implementadas aqui.")

# st.subheader("📖 Lista de livros")
# if st.button("🔄 Recarregar livros"):
#     livros_data = carregar_clientes()
#     if livros_data:
#         st.table(livros_data)
# else:
#     livros_data = carregar_clientes()
#     if livros_data:
#         st.table(livros_data)
# # db.fecharbanco(cursor,conexao)            
