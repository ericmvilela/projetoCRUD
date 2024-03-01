# Desafio Desenvolvedor

CRUD de Produtos.


## Instalação

Certifique-se de ter o Python e o pip instalados em seu ambiente.

1. Clone o repositório:

   ```bash
   git clone https://github.com/ericmvilela/projetoDesenvolvedor
   ```

2. Crie um ambiente virtual

   - No Windows
      
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

   - No Linux/Mac
      
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```

3. Instale as dependências:

   `pip install -r requirements.txt`


## Configurações

1. Crie um Banco de Dados MySQL:
    ```mysql
    CREATE DATABASE produtosdb;
    ```
   
2. Configure as variáveis de ambiente:

    - Crie um arquivo '.env' no diretório do aplicativo.
    - Adicione as variáveis do Banco de Dados. Por exemplo:
        
        ```dotenv
        DB=mysql+pymysql
        USER_DB=root
        PASSWORD_DB=senha
        HOST_DB=localhost
        PORT_DB=3306
        NAME_DB=produtosdb
        SECRET_KEY=chave_secreta
        ```

3. Faça as migrações do Banco de Dados:
    
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Execução

Inicie o servidor:

```bash
flask run
```