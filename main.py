import pandas as pd

def main():
    tabela_clientes = pd.read_csv("ClientesBanco.csv", encoding="latin-1")
    print(tabela_clientes)

    tabela_clientes = tabela_clientes.dropna()
    print(tabela_clientes.info())
    print(tabela_clientes.describe().round(1))

if __name__ == "__main__": 
    main()