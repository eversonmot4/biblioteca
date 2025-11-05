import banco_dados.b_d as db
import streamlit as st
import pandas as pd

cursor, conexao = db.iniciarbanco()
db.criar_tabela_cliente(cursor)
db.criar_tabela_livro(cursor)
db.criar_tabela_editora(cursor)

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

def carregar_tabela_para_dataframe(cursor, tabela):
    try:
        dados = listar_dados(cursor, tabela)
        if not dados:
            st.info("Nenhum dado encontrado no banco de dados.", icon="ℹ️")
            return pd.DataFrame()  # Retorna um DataFrame vazio

        df = pd.DataFrame(dados)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados da tabela {tabela}: {e}")
        return pd.DataFrame()

def tabela_dados(tabela):
    st.subheader(f"📖 Lista de {tabela}")
    if st.button(f"🔄 Recarregar {tabela}"):
        data = listar_dados(cursor, tabela)
        if data:
            st.table(data)
        else:
            st.info(f"Nenhum dado encontrado na tabela {tabela}.", icon="ℹ️")
    else:
        data = listar_dados(cursor, tabela)
        if data:
            st.table(data)
        else:
            st.info(f"Nenhum dado encontrado na tabela {tabela}.", icon="ℹ️")

st.title("Sistema de Gerenciamento de Biblioteca")
st.write("Bem-vindo ao sistema de gerenciamento de biblioteca!")

with st.sidebar:
    st.header("Navegação")
    pagina = st.selectbox("Ir para", ["Início", "Clientes", "Livros", "Editoras"])

pagina = pagina.lower()

# Conteúdo das páginas
if pagina == "início":
    st.subheader("Página Inicial")
    st.write("Aqui você pode gerenciar clientes, livros e editoras.")

    sel = st.selectbox("Selecione a tabela para visualizar:", ["Clientes", "Livros", "Editoras"])
    if sel == "Clientes":
        df_clientes = carregar_tabela_para_dataframe(cursor, "clientes")
        if not df_clientes.empty:
            st.dataframe(df_clientes)


    elif sel == "Livros":
        df_livros = carregar_tabela_para_dataframe(cursor, "livros")
        if not df_livros.empty:
            st.dataframe(df_livros)
    elif sel == "Editoras":
        df_editoras = carregar_tabela_para_dataframe(cursor, "editora")
        if not df_editoras.empty:
            st.dataframe(df_editoras)

elif pagina == "clientes":
    st.subheader("Gerenciamento de Clientes")

    sec1, sec2, sec3 = st.tabs(["Adicionar Cliente", "Atualizar Cliente", "Deletar Cliente"])

    with sec1:
        st.write("Adicionar um novo cliente:")
        cpf = st.text_input("CPF:")
        nome = st.text_input("Nome:")
        lista_livros = st.text_input("Lista de Livros Comprados (separados por vírgula):")
        telefone = st.text_input("Telefone:")
        if st.button("Adicionar Cliente"):
            db.inserir_cliente(cursor, conexao, cpf, nome, lista_livros, telefone)
            st.success("Cliente adicionado com sucesso!")
    with sec2:
        st.write("Atualizar um cliente existente:")
        id_atualizar = st.number_input("ID do Cliente a ser atualizado:", min_value=1, step=1)
        atributo = st.selectbox("Atributo a ser atualizado:", ["CPF", "nome", "list_livros_comprados", "telefone"])
        valor = st.text_input("Novo valor:")
        if st.button("Atualizar Cliente"):
            db.atualizar_dados(cursor, conexao, "clientes", atributo, valor, id_atualizar)
            st.success("Cliente atualizado com sucesso!")
    with sec3:
        st.write("Deletar um cliente:")
        id_deletar = st.number_input("ID do Cliente a ser deletado:", min_value=1, step=1)
        if st.button("Deletar Cliente"):
            db.apagar_dado(cursor, conexao, "clientes", id_deletar)
            st.success("Cliente deletado com sucesso!")

    tabela_dados("clientes")

    

elif pagina == "livros":
    st.subheader("Gerenciamento de Livros")

    sec1, sec2, sec3 = st.tabs(["Adicionar Livro", "Atualizar Livro", "Deletar Livro"])

    with sec1:
        st.write("Adicionar um novo Livro:")
        titulo = st.text_input("Título:")
        editora = st.text_input("Editora:")
        autor = st.text_input("Autor:")
        qnt_estoque = st.number_input("Quantidade em Estoque:", min_value=0, step=1)
        if st.button("Adicionar Livro"):
            db.inserir_livro(cursor, conexao, titulo, editora, autor, qnt_estoque)
            st.success("Livro adicionado com sucesso!")
    with sec2:
        st.write("Atualizar um livro existente:")
        id_atualizar = st.number_input("ID do Livro a ser atualizado:", min_value=1, step=1)
        atributo = st.selectbox("Atributo a ser atualizado:", ["titulo", "editora", "autor", "qnt_estoque"])
        valor = st.text_input("Novo valor:")
        if st.button("Atualizar Livro"):
            db.atualizar_dados(cursor, conexao, "livros", atributo, valor, id_atualizar)
            st.success("Livro atualizado com sucesso!")
    with sec3:
        st.write("Deletar um livro:")
        id_deletar = st.number_input("ID do Livro a ser deletado:", min_value=1, step=1)
        if st.button("Deletar Livro"):
            db.apagar_dado(cursor, conexao, "livros", id_deletar)
            st.success("Livro deletado com sucesso!")

    tabela_dados("livros")


elif pagina == "editoras":
    st.subheader("Gerenciamento de Editoras")

    sec1, sec2, sec3 = st.tabs(["Adicionar Editora", "Atualizar Editora", "Deletar Editora"])
    with sec1:
        st.write("Adicionar uma nova Editora:")
        gerente = st.text_input("Gerente:")
        contato = st.text_input("Contato:")
        telefone = st.text_input("Telefone:")
        if st.button("Adicionar Editora"):
            db.inserir_editora(cursor, conexao, gerente, contato, telefone)
            st.success("Editora adicionada com sucesso!")
    with sec2:
        st.write("Atualizar uma editora existente:")
        id_atualizar = st.number_input("ID da Editora a ser atualizada:", min_value=1, step=1)
        atributo = st.selectbox("Atributo a ser atualizado:", ["gerente", "contato", "telefone"])
        valor = st.text_input("Novo valor:")
        if st.button("Atualizar Editora"):
            db.atualizar_dados(cursor, conexao, "editora", atributo, valor, id_atualizar)
            st.success("Editora atualizada com sucesso!")
    with sec3:
        st.write("Deletar uma editora:")
        id_deletar = st.number_input("ID da Editora a ser deletada:", min_value=1, step=1)
        if st.button("Deletar Editora"):
            db.apagar_dado(cursor, conexao, "editora", id_deletar)
            st.success("Editora deletada com sucesso!")

    tabela_dados("editora")