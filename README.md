# Biblioteca saber infinito

## Site da aplicação: https://randu.pythonanywhere.com/

![Image](https://github.com/user-attachments/assets/9f5e3489-410b-432f-a760-f36a0b579f00)

### Sobre as limitações atuais do projeto.
- Foi feito o deploy, mas nesse processo acabou acumulando alguns problemas, que serão corrigidos posteriormente.
- Não foi feito uma interface gráfica, amigável, apenas o HTML e formatação do banco de dados.
- Não foi desenvolvida uma lógica ainda para cadastrar os emprestimos, a não ser pela área administrativa do django.

## Como a aplicação funciona na máquina

### Página inicial
- Na página inicial temos as seguintes opções:

![image](https://github.com/user-attachments/assets/593a450f-2bdf-40f0-ae33-a7fbc03d308b)

### Listar livros 
- Nessa página serão mostrados os livros que já foram cadastrados no banco de dados:

![image](https://github.com/user-attachments/assets/dc0ca250-bc63-4200-9f26-2fee5063128e)

### Listar membros
- Nessa página serão mostrados os usuários dessa biblioteca.
  - Entendemos que essas são informações privadas da biblioteca, mas estamos somente estraindo dados do banco de dados no momento.
 
![image](https://github.com/user-attachments/assets/e144a686-df4b-4fdb-9f30-92024519a78f)

### Cadastrar Livro
- Essa página também será destinada apenas aos administradores da aplicação.

![image](https://github.com/user-attachments/assets/8fb444a8-645c-4e43-b540-e1b4acf21c7f)

- Cadastrando mais um livro hipotético:
![image](https://github.com/user-attachments/assets/bc72b661-4599-4d80-bdb1-69fafc8fd69c)

- Logo após o cadastro, será retornado todos os livros:
![image](https://github.com/user-attachments/assets/ab4309c8-cd75-43b0-9efc-64047caafb10)


### Cadastrar Usuário
- Essa página se destina ao cadastro de usuários no banco de dados
![image](https://github.com/user-attachments/assets/18d40930-108a-4e0f-9135-63dbc3dd1821)
- Logo após o cadastro, aparece os nomes dos membros.
  - Essa é uma prática apenas para o debug da aplicação.
![image](https://github.com/user-attachments/assets/8b6e970b-c7a9-415c-beee-1607f1e97c65)
  
### Listar emprestimos
- Essa página apresenta todos os empréstimos e os seus dados
![image](https://github.com/user-attachments/assets/99291fd1-24ba-4329-97f5-9db75b0ecbcb)
