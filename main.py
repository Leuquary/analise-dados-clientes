import pandas as pd

def main():
    tabela_clientes = pd.read_csv("ClientesBanco.csv", encoding="latin-1")
    print(tabela_clientes)

if __name__ == "__main__": 
    main()