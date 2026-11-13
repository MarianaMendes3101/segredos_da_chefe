# Pendências do MVP — Segredos da Chef

A lista abaixo deve ser revisada pelo grupo após executar o projeto no computador com Django instalado.

- [ ] **Executar os testes automatizados localmente.** Os testes de receitas, categorias, contatos e cadastro de usuário foram preparados, mas não foi possível executá-los neste ambiente porque o pacote Django não está instalado e a rede para instalá-lo está indisponível.
- [ ] **Conferir o cadastro com upload de imagem.** O formulário aceita imagem e o projeto configura a pasta `media/`; testar com um arquivo de imagem pequeno no navegador.
- [ ] **Cadastrar dados reais de demonstração.** Criar algumas categorias e receitas para que a página inicial tenha conteúdo. Não foram inseridos dados fictícios automaticamente no banco.
- [ ] **Criar uma conta administrativa.** Executar `python manage.py createsuperuser` para acessar o Django Admin e as telas restritas de gerenciamento de usuários e mensagens.
- [ ] **Configuração para produção não incluída.** O projeto está configurado para desenvolvimento local (`DEBUG=True`). Não deve ser publicado na internet sem configurar segredo, hosts, HTTPS e demais medidas de segurança.

## Itens implementados para a atividade

- CRUD de categorias e receitas: cadastrar, listar, visualizar receita, editar e excluir com confirmação.
- Busca de receitas por título e filtro por categoria.
- Slug gerado automaticamente quando não informado e validação para evitar duplicidades.
- Relacionamento Receita–Categoria com `on_delete=PROTECT`, evitando excluir categoria que ainda possui receitas vinculadas.
- Cadastro de usuário com validação de e-mail e senha usando os validadores do Django.
- CRUD administrativo de usuários e mensagens de contato (restrito a staff).
- Formulário público de contato com validação de e-mail.
- Migrações iniciais para os modelos de receitas, categorias e contatos.
