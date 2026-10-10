# Projetos — Jonathan Sales Programming

Esta pasta `projects` organiza os projetos locais. Cada atividade fica em sua
própria pasta, com código, documentação, dependências e repositório próprios.

```text
projects/
├── README.md
├── AGENTS.md
└── 1-product-showcase/
    ├── app.py
    ├── README.md
    ├── requirements.txt
    ├── .venv/
    ├── models/
    ├── templates/
    ├── static/
    └── docs/
```

O primeiro projeto está em **[1-product-showcase](1-product-showcase/README.md)**.
Uma futura pasta `2-restaurant-menu` ficará ao lado dele, dentro de `projects`.
Por enquanto, a atividade 2 é apenas um modelo de README dentro dos documentos
do projeto 1; ainda não existe uma aplicação pronta para ela.

## Abrir o primeiro projeto no VS Code

Se o VS Code está aberto nesta pasta `projects`:

1. Abra **Terminal → New Terminal** (Novo Terminal).
2. Confira que está em `projects` com `Get-Location`.
3. Entre no primeiro projeto:

```powershell
cd .\1-product-showcase
```

4. Abra essa pasta no VS Code:

```powershell
code .
```

5. No terminal da pasta `1-product-showcase`, inicie a aplicação:

```powershell
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

6. Abra http://127.0.0.1:5000 no navegador.
7. Para parar, pressione Ctrl+C no terminal do servidor.

Se precisar instalar em outro computador, siga o
[README do projeto](1-product-showcase/README.md) e o
[roteiro guiado](1-product-showcase/docs/walkthrough.md). Cada clone cria sua
própria `.venv` dentro da pasta da atividade.

## Git e próximas atividades

Execute comandos de Git dentro da pasta do projeto escolhido. Para publicar o
primeiro esqueleto, entre em `1-product-showcase` e siga o
[guia do professor](1-product-showcase/docs/instructor-guide.md#publicar-o-esqueleto).
Não inicialize um único repositório Git nesta pasta `projects`.

No GitHub, cada atividade terá seu próprio repositório para receber forks.
O catálogo `jonathan-sales-programming` será um repositório separado com links;
veja o [guia de organização](1-product-showcase/docs/project-organization.md).

README e guias de orientação estão em português. Código, comentários,
interface, nomes de arquivos e repositórios permanecem em inglês.
