## Como executar o projeto no ambiente Windows

1. Instale o Python.
2. Clone o repositório:
    ```
    git clone https://github.com/Valdelainecristinaribeiro/PI-4-Petshop.git
    ```
3. Navegue até o diretório do projeto:
    ```
    cd PI-4-Petshop
    ```
4. Crie e ative o ambiente virtual:
    ```
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
5. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
6. Navegue até o diretório 'Shop':
    ```
    cd Shop
    ```
7. Execute as migrações do banco de dados:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Inicie o servidor:
    ```
    python manage.py runserver
    ```

## Como executar o projeto no ambiente Linux

1. Instale o Python.
2. Clone o repositório:
    ```
    git clone https://github.com/Valdelainecristinaribeiro/PI-4-Petshop.git
    ```
3. Navegue até o diretório do projeto:
    ```
    cd PI-4-Petshop
    ```
4. Crie e ative o ambiente virtual:
    ```
    virtualenv -p python3 venv
    source venv/bin/activate
    ```
5. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
6. Navegue até o diretório 'Shop':
    ```
    cd Shop
    ```
7. Execute as migrações do banco de dados:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Inicie o servidor:
    ```
    python manage.py runserver
    ```
### Integrantes
- [Valdelaine Ribeiro](https://github.com/Valdelainecristinaribeiro)
- [Marcel Araujo](https://github.com/araujomarcel)
- [Beatriz Honorato](https://github.com/BeatrizHonorato)
- [Larissa Volsi](https://github.com/Lvolsi)


| Função | Responsável |
| ------ | ------ |
| **Scrum Master** |Valdelaine Ribeiro |
| **Documentação** | Larissa Volsi |
| **Desenvolvedor Back-End** | Marcel Araujo e Beatriz Honorato |
| **Desenvolvedor Front-End** | Valdelaine Ribeiro e Larissa Volsi |
| **Banco de dados** | Marcel Araujo e Beatriz Honorato |
