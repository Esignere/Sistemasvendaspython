# 📊 Sistema de Vendas

Aplicação web desenvolvida em **Python** com **Streamlit** para cadastro, visualização e análise de vendas.

O projeto utiliza um arquivo CSV como banco de dados simples e apresenta um dashboard com métricas e gráficos para facilitar a análise das vendas cadastradas.

## 🚀 Tecnologias utilizadas

* **Python**
* **Streamlit** — interface da aplicação
* **Pandas** — leitura e manipulação dos dados
* **Plotly Express** — criação dos gráficos
* **CSV** — armazenamento dos dados

## 📌 Funcionalidades

### Cadastro de vendas

O sistema permite cadastrar:

* Data da venda
* Vendedor
* Produto
* Quantidade
* Valor

Os dados são adicionados ao arquivo `vendas.csv`.

### Dashboard

O sistema apresenta:

* 💰 Faturamento total
* 📊 Gráfico de vendas por vendedor
* 🥧 Gráfico de vendas por produto
* 📋 Tabela com todas as vendas cadastradas

## 📁 Estrutura do projeto

```text
Sistema-de-Vendas/
├── App.py
├── CSV/
│   └── vendas.csv
└── README.md
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd Sistema-de-Vendas
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install streamlit pandas plotly
```

Ou, caso o projeto possua um `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run App.py
```

O Streamlit abrirá a aplicação no navegador.

## 📊 Dashboard

O dashboard utiliza os dados cadastrados no CSV para calcular o faturamento total e gerar visualizações interativas.

### Faturamento total

Calcula a soma dos valores das vendas cadastradas.

### Vendas por vendedor

Gráfico de barras que permite visualizar o valor das vendas de cada vendedor, separado por produto.

### Vendas por produto

Gráfico de rosca que mostra a distribuição do valor das
