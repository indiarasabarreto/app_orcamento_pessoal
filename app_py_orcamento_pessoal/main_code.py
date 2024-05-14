#Obter valor total
renda_mensal = float(input('Renda mensal: '))


# (Percentagem a ser removida / 100) * renda_mensal


# Obtendo as percentagens
obter_50_porcento = ( 50 / 100) * renda_mensal
obter_30_porcento = ( 30 / 100) * renda_mensal
obter_20_porcento = ( 20 / 100) * renda_mensal
print("===================\nSeus números de 50%, 30%, 20%\n===================")

print("Necessidades: R${:,.2f}".format(obter_50_porcento))
print("Gastos: R${:,.2f}".format(obter_30_porcento))
print("Poupança: R${:,.2f}".format(obter_20_porcento))  

print("\n================================================================")