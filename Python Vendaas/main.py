import streamlit as st
import pandas as pd
import plotly.express as px

## Pandas ler o csv
table = pd.read_csv("./CSV/vendas.csv")

st.write('## Sistema de Vendas')


## Cadastro de Vendas



st.sidebar.write('### Cadastrar Vendas')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Victoria'])
produto = st.sidebar.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantidade = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('Valor', step=0.5)
botao = st.sidebar.button('Cadastrar venda')

## Logica de cadastro 

if botao:
    if valor == 0 or quantidade == 0 or vendedor == 0:
        st.warning('Cadastro faltando informacoes')
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(table)
        table.loc[ultima_linha] = nova_venda
        table.to_csv('vendas.csv', index=False)
    st.success('Venda Cadastrada')

st.write('### Vendas Cadastradas')
st.dataframe(table)

## Dashboard
st.write('### Dashboard')

## Card/metrica - faturamento Total
faturamento = table['valor'].sum()
st.metric('Faturamento Total', faturamento)

## Grafico de coluna - venda por vendedor
column = px.bar(table, x='vendedor', y='valor', color='produto')
st.plotly_chart(column)
## Grafico de rosca - Venda por produto
rosca = px.pie(table, names='produto', values='valor', hole=0.5)
st.plotly_chart(rosca)