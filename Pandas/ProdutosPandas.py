import pandas as pd
import IPython as ip

tabela = pd.read_excel("Produtos.xlsx")

tabela.loc[tabela["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5

tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Multiplicador Imposto"]

tabela.to_excel("ProdutosPandas.xlsx", index = False)
