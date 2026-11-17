# Os Segredos da Chef

## Nome do Projeto

**Os Segredos da Chef**

## Descrição do Projeto

*Os Segredos da Chef* é um portal de receitas culinárias desenvolvido como Projeto Integrador para o curso Técnico em Informática do Instituto Federal de Rondônia (IFRO).

O sistema tem como objetivo solucionar a dificuldade de escolher refeições rápidas e práticas para o dia a dia, oferecendo uma plataforma intuitiva onde os usuários podem pesquisar receitas por nome, filtrar por categoria e ocasião de consumo, ordenar por tempo de preparo, consultar o modo de preparo completo e entrar em contato com a equipe, além de contar com sistema de autenticação para organização e gerenciamento do portal.

## Tecnologias Utilizadas

As tecnologias utilizadas no desenvolvimento do projeto são:

* **Python 3** — Linguagem de programação utilizada no back-end.
* **Django** — Framework web responsável pela arquitetura MTV (Models, Templates e Views), gerenciamento de rotas, painel administrativo e autenticação.
* **HTML5** — Estruturação semântica das páginas e templates do sistema.
* **CSS3** — Estilização das interfaces, identidade visual, responsividade e alinhamento dos cards em Flexbox.
* **JavaScript** — Interatividade no front-end, incluindo o controle de abertura e fechamento do modal de detalhes das receitas.
* **SQLite** — Banco de dados relacional utilizado no ambiente de desenvolvimento local.
* **Git e GitHub** — Controle de versão e colaboração da equipe por meio de branches individuais.

## Equipe

| Integrante                                  | Responsabilidade Geral no Projeto |
|:--------------------------------------------| :--- |
| **Mariana Nunes Mendes**                    | Desenvolvimento e manutenção dos apps `usuarios`, `core` e `web` (autenticação, funcionalidades centrais e integração web). |
| **Hemilly Eduarda Dellarmelino Oliveira**   | Configurações globais do projeto (`config`) e estilização visual das interfaces (`CSS`). |
| **Geovanna Favaleça Santos**                | Desenvolvimento e gerenciamento do app `receitas` (catálogo, destaques, busca e filtros). |
| **Jhennyfer dos Santos Rodrigues Lecheski** | Desenvolvimento do app `contato` e estruturação das páginas do portal em `HTML`. |

## Apps Django

O projeto é gerenciado pelo diretório de configurações `config/` e organizado nos seguintes aplicativos Django:

* **`receitas`** *(Responsável: Geovanna Favaleça)*: Aplicativo principal do catálogo culinário. Gerencia a página inicial com as receitas em destaque, a biblioteca completa de receitas, a busca por texto integrada entre as páginas, os filtros por categoria e ocasião de consumo e a ordenação dos resultados.
* **`usuarios`** *(Responsável: Mariana Nunes Mendes)*: Aplicativo responsável pela autenticação de contas e pelo modelo de usuário customizado do projeto (`AUTH_USER_MODEL = 'usuarios.Usuario'`), controlando os fluxos de login e logout.
* **`contato`** *(Responsável: Jhennyfer dos Santos L.)*: Aplicativo destinado ao recebimento, validação e armazenamento das mensagens enviadas pelos usuários por meio da página de contato.
* **`core`** *(Responsável: Mariana Nunes Mendes)*: Aplicativo central para organização de recursos base e funcionalidades compartilhadas entre os módulos do sistema.
* **`web`** *(Responsável: Mariana Nunes Mendes)*: Aplicativo voltado à camada de integração web do portal, reunindo rotas auxiliares (`receitas_urls.py`, `contato_urls.py`) e a estrutura de templates em `web/templates/web/`.

## Models e Views

Abaixo estão detalhados os Models e Views desenvolvidos para cada aplicativo e a respectiva integrante responsável:

### App `receitas` — *Responsável: Geovanna Favaleça*

* **Models:**
  * `Receita`: Armazena os dados das receitas cadastradas (`titulo`, `tempo_preparo`, `descricao`, `modo_preparo`, `imagem`, `categoria`, `ocasiao`).
  * `Categoria`: Armazena as categorias de classificação das receitas (`nome`, `slug`).
* **Views:**
  * `index` / `home_view`: Renderiza a página inicial (`index.html`) listando as receitas em destaque.
  * `receitas_view`: Renderiza a biblioteca de receitas (`receita.html`), aplicando busca textual (`s` / `busca`), filtros por categoria e ocasião e ordenação (mais recentes, menor tempo de preparo ou ordem alfabética).
  * `receita` / `detalhe_receita`: Recupera e exibe os dados de uma receita específica (`get_object_or_404`).

### App `usuarios` — *Responsável: Mariana Nunes Mendes*

* **Models:**
  * `Usuario`: Modelo de usuário customizado configurado em `AUTH_USER_MODEL = 'usuarios.Usuario'`.
* **Views:**
  * `LoginView` e views de autenticação (`usuarios/views.py`): Gerenciam a tela de login personalizada (`login.html`), autenticação de acesso e redirecionamentos de login e logout.

### App `contato` — *Responsável: Jhennyfer dos Santos L.*

* **Models:**
  * `Contato`: Armazena as mensagens enviadas pelo formulário de contato (substituindo o model inicial `MensagemContato`).
* **Views:**
  * Views de contato (`contato/views.py`): Renderizam a página de contato e processam os dados enviados pelo formulário.

### App `core` — *Responsável: Mariana Nunes Mendes*

* **Models e Views:** Estruturas e lógicas base compartilhadas do sistema definidas em `core/models.py` e `core/views.py`.

### App `web` — *Responsável: Mariana Nunes Mendes*

* **Models e Views:** Estruturas e controladores de camada web definidos em `web/models.py` e `web/views.py`, responsáveis pela integração de rotas e renderização dos templates da aplicação.

## Arquivos e Responsabilidades

| Arquivo(s) | Responsabilidade / Descrição | Integrante Responsável           |
| :--- | :--- |:---------------------------------|
| `config/settings.py`, `config/urls.py`, `config/wsgi.py`, `config/asgi.py`, `requirements.txt` e `.gitignore` | Configurações globais do Django, definição de `AUTH_USER_MODEL`, redirecionamentos de login/logout, diretórios estáticos/mídia, roteamento principal (`admin/`, `receitas/`, `contato/`, `usuarios/`) e gestão de dependências. | **Hemilly Eduarda Dellarmelino** |
| `static/css/layout.css`, `static/css/receita.css` e `static/css/form.css` | Identidade visual do portal, layout responsivo, alinhamento dos cards em Flexbox e estilização dos formulários e da página de login. | **Hemilly Eduarda Dellarmelino** |
| `receitas/models.py`, `receitas/views.py`, `receitas/urls.py` e `receitas/admin.py` | Definição dos models `Receita` e `Categoria`, lógica da página inicial, pesquisa integrada, filtros da biblioteca, rotas do app e registro no Django Admin. | **Geovanna Favaleça**            |
| `contato/models.py`, `contato/views.py`, `contato/urls.py` e `contato/admin.py` | Definição do model `Contato`, processamento das mensagens enviadas, rotas da página de contato e gestão no painel administrativo. | **Jhennyfer dos Santos L.**      |
| Templates HTML (`index.html`, `receita.html`, `login.html`, `contato.html`, `painel.html` em `web/templates/web/`) | Estruturação semântica das páginas, formulários de busca integrados entre a home e a biblioteca, modal de detalhes/modo de preparo (com JS embutido) e tela de login. | **Jhennyfer dos Santos L.**      |
| `usuarios/models.py`, `usuarios/views.py`, `usuarios/urls.py` e `usuarios/admin.py` | Implementação do model `Usuario`, controle de login/logout, rotas de autenticação e administração de usuários. | **Mariana Nunes Mendes**         |
| `core/models.py`, `core/views.py`, `core/urls.py` e `core/admin.py` | Desenvolvimento das funcionalidades centrais e recursos compartilhados no app `core`. | **Mariana Nunes Mendes**         |
| `web/models.py`, `web/views.py`, `web/urls.py`, `web/receitas_urls.py`, `web/contato_urls.py` e `web/admin.py` | Integração da camada web, organização de sub-rotas e ligação entre views e templates do diretório `web/templates/web/`. | **Mariana Nunes Mendes**         |

## Branches e Desenvolvimento Individual

Para manter o código organizado e evitar conflitos durante o desenvolvimento em equipe, **nenhuma integrante deve trabalhar diretamente na branch principal (`main`)**.

Cada integrante utiliza sua própria branch individual para implementar as atividades sob sua responsabilidade, permitindo identificar claramente a desenvolvedora de cada conjunto de alterações:

| Integrante                            | Branch Principal / Atual | Outras Branches Criadas no Repositório  |
|:--------------------------------------|:-------------------------|:----------------------------------------|
| **Mariana Nunes Mendes**              | `mari`                   | `mariana`                               |
| **Hemilly Eduarda De Oliveira D.**    | `duda`                   | `hemilly`                               |
| **Geovanna dos Santos Favaleça**      | `geovanna`               | `manana`                                |
| **Jhennyfer Rodrigues dos Santos L.** | `jhenn` /  `jhen`        | `jhenny`/ `jhe`                         |

### Fluxo recomendado no Git

1. **Atualizar a branch principal antes de iniciar:**

   ```bash
   git checkout main
   git pull origin main
   ```

2. **Acessar ou criar sua branch individual:**

   ```bash
   git checkout nome-da-sua-branch
   # ou, caso seja uma nova branch:
   git checkout -b nome-da-sua-branch
   ```

3. **Salvar e enviar alterações na sua branch:**

   ```bash
   git add .
   git commit -m "Descrição clara da alteração realizada"
   git push origin nome-da-sua-branch
   ```

4. **Integrar à branch principal:** após concluir e testar a funcionalidade na branch individual, abrir um **Pull Request** no GitHub para revisão do grupo antes de realizar o merge na `main`.

## Como Executar o Projeto Localmente

1. **Clone o repositório e acesse a pasta do projeto:**

   ```bash
   git clone <url-do-repositorio>
   cd segredos_da_chefe-main
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor local:**

   ```bash
   python manage.py runserver
   ```

   Acesse no navegador em `http://127.0.0.1:8000/`.
