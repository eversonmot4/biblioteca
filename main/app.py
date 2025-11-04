import banco_dados.b_d as db

cursor, conexao = db.iniciarbanco()
db.criar_tabela_cliente(cursor)
db.criar_tabela_livro(cursor)
db.criar_tabela_editora(cursor)
db.criar_tabela_Endereco(cursor)

db.inserir_cliente(cursor,conexao,"999.888.777-12","Rian","list_livros_comprados","99 91234-9856")

db.atualizar_dados(cursor,conexao,"clientes","nome","e",1)

db.apagar_dado(cursor, conexao, "clientes",1)