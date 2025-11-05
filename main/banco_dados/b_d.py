import sqlite3

def iniciarbanco():
    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()
    return cursor, conexao

def criar_tabela_livro(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS livros(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                autor TEXT NOT NULL,
                titulo TEXT NOT NULL,
                editora TEXT NOT NULL,
                qnt_estoque INTEGER NOT NULL
            );
        """
    )
def criar_tabela_cliente(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                CPF TEXT NOT NULL,
                nome TEXT NOT NULL,
                list_livros_comprados TEXT NOT NULL,
                telefone TEXT NOT NULL
            );
        """
    )
def criar_tabela_editora(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS editora(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                gerente TEXT NOT NULL,
                contato TEXT NOT NULL,
                telefone TEXT NOT NULL
            );
        """
    )
def criar_tabela_Endereco(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS enderecos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                rua TEXT NOT NULL,
                bairro TEXT NOT NULL,
                CEP TEXT NOT NULL,
                num_casa INTEGER NOT NULL
            );
        """
    )
def fechar_conexao(conexao):
    conexao.close()


def inserir_livro(cursor,conexao, titulo, editora, autor, qnt_estoque):
    cursor.execute(
        """
            INSERT INTO  livros(titulo, editora, autor, qnt_estoque)
            VALUES (?, ?, ?, ?)
        
        """,
        (titulo, editora, autor, qnt_estoque)

    )
    conexao.commit()
def inserir_cliente(cursor,conexao,CPF,nome,list_livros_comprados,telefone):
    cursor.execute(
        """
            INSERT INTO clientes(CPF, nome, list_livros_comprados, telefone)
            VALUES (?, ?, ?, ?)
        
        """,
        (CPF, nome, list_livros_comprados, telefone)

    )
    conexao.commit()
def inserir_editora(cursor, conexao, gerente, contato, telefone):
    cursor.execute(
        """
            INSERT INTO editora(gerente, contato, telefone)
            VALUES (?, ?, ?)
        
        """,
        (gerente, contato, telefone)

    )
    conexao.commit() 
def endereco(cursor,conexao,rua,bairro,CEP,num_casa):
    #7 - Inserindo dados
    cursor.execute(
        """
            INSERT INTO  enderecos(rua, bairro, CEP, num_casa)
            VALUES (?, ?, ?, ?)
        
        """,
        (rua, bairro, CEP, num_casa)

    )
    conexao.commit()
    

def listar_dados(cursor,tabela):
    dados = cursor.execute(f"SELECT * FROM {tabela}")

    return dados

def atualizar_dados(cursor, conexao, tabela, atributo, valor, id):
    try:
        sql = f"UPDATE {tabela} SET {atributo} = ? WHERE id = ?"
        cursor.execute(sql, (valor, id))
        conexao.commit()
        print(f"Registro com ID {id} atualizado com sucesso!")
    
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao atualizar dados: {e}")

def apagar_dado(cursor, conexao, tabela, id):
    try:
        if not tabela.isidentifier():
            raise ValueError("Nome de tabela inválido!")
        sql = f"DELETE FROM {tabela} WHERE id = ?"
        cursor.execute(sql, (id,))
        conexao.commit()
        print(f"Registro com ID {id} removido com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao apagar dado: {e}")