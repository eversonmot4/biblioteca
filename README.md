# 📚 Sistema de Gerenciamento de Biblioteca  
### Desenvolvido com Python + SQLite + Streamlit

Este projeto é um sistema simples e intuitivo para gerenciamento de biblioteca, permitindo realizar operações CRUD (Criar, Ler, Atualizar e Deletar) para Clientes, Livros e Editoras, utilizando uma interface gráfica construída com Streamlit e banco de dados SQLite.

---

## 🎯 Funcionalidades Principais

### 📖 Livros
- Adicionar novo livro  
- Listar livros cadastrados  
- Atualizar informações  
- Deletar por ID  

### 🧑‍💼 Clientes
- Registrar clientes  
- Atualizar CPF, nome, telefone e livros comprados  
- Excluir cliente  
- Visualização em tabela  

### 🏢 Editoras
- Cadastro de editoras  
- Atualização de dados  
- Remoção por ID  
- Visualização completa  

---

## 🛠 Tecnologias Utilizadas
- Python 3  
- Streamlit  
- SQLite3  
- Pandas  
- SQL (CRUD)

---

## 📂 Estrutura do Projeto

📁 projeto_biblioteca  
│  
├── banco_dados/  
│   └── b_d.py          # Funções do banco (CRUD)  
│  
├── app.py              # Interface Streamlit  
│  
└── README.md

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

### 2. Instale as dependências

### 3. Execute o sistema

### 4. Acesse no navegador
http://localhost:8501

---

## 🧠 Como o Sistema Funciona

- O arquivo b_d.py contém todas as funções de banco de dados.  
- O app.py monta a interface Streamlit, exibindo formulários, tabelas e abas de navegação.  
- O usuário pode gerenciar clientes, livros e editoras de forma rápida e visual.
