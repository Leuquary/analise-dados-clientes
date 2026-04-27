import pandas as pd
import plotly.express as px

def main():
    tabela_clientes = pd.read_csv("ClientesBanco.csv", encoding="latin-1")
    print(tabela_clientes)
    
    tabela_clientes = tabela_clientes.dropna()

    print(tabela_clientes.info())
    print(tabela_clientes.describe().round(1))

    grafico_histograma = px.histogram(
        tabela_clientes, 
        x = "Contatos 12m", 
        color = "Categoria",
        barmode = "stack", 
        color_discrete_map = {
            "Cliente": "purple",
            "Cancelado": "orange"
        }
    )
    grafico_histograma.update_layout(
        title = "Contatos ao call center nos últimos 12 meses por categoria de cliente (cliente ativo / cliente cancelado)", 
        xaxis_title = "Contatos ao call center nos últimos 12 meses", 
        yaxis_title = "Quantidade de clientes", 
        bargap = 0.15
    )

    grafico_histograma.show()

    grafico_pizza = px.pie(
        tabela_clientes,
        names = "Categoria",
        title = "Proporção de clientes ativos e cancelados",
        color_discrete_map = {
            "Cliente": "green",
            "Cancelado": "red"
        }
    )

    grafico_pizza.show()

    grafico_barras_horizontais = px.histogram(
        tabela_clientes, 
        x = "Limite Consumido",
        y = "Faixa Salarial Anual",
        color = "Categoria",
        barmode = "group",
        color_discrete_map = {
            "Cliente": "green",
            "Cancelado": "red"
        }
    )

    grafico_barras_horizontais.update_layout(
        title = "Relação entre Limite Consumido e Faixa Salarial Anual por categoria de Cliente (cliente ativo / cliente cancelado)", 
        xaxis_title = "Limite Consumido", 
        yaxis_title = "Faixa Salarial Anual"
    )

    grafico_barras_horizontais.show()

if __name__ == "__main__": 
    main()