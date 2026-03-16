import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#Entrada
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual (%) ')) / 100
perc_cdb = float(input('Percentual do CDI (%) ')) / 100
perc_lci = float(input('Percentual do LCI (%) ')) / 100
taxa_fii = float(input('Rentabilidade mesal FII (%) ')) / 100
meta = float(input('Meta finnanceira (R$) '))

#CONVERSAO CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) -1

#TOTAL INVESTIDO
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses) + (aporte * meses)) 
lucro_cdb = montante_cdb - total_investido
montante_cbd_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses))

#POUPANÇA
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses) + (aporte * meses))

#FII
fii1 = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii2 = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii3 = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii4 = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii5 = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))

simulacoes_fii = [fii1, fii2, fii3, fii4, fii5]

media_fii = statistics.mean(simulacoes_fii)
mediana_fii = statistics.median(simulacoes_fii)
desvio_fii = statistics.stdev(simulacoes_fii)

montante_fii = media_fii

# DATAS
data_simulacao = datetime.date.today()
dias = meses * 30
data_resgate = data_simulacao + datetime.timedelta(days=dias)


# META FINANCEIRA
meta_atingida = montante_fii >= meta

# FORMATAÇÃO MONETÁRIA
f_total = locale.currency(total_investido, grouping=True)
f_cdb = locale.currency(montante_cdb_liquido, grouping=True)
f_lci = locale.currency(montante_lci, grouping=True)
f_poup = locale.currency(montante_poupanca, grouping=True)
f_fii = locale.currency(montante_fii, grouping=True)

f_media = locale.currency(media_fii, grouping=True)
f_mediana = locale.currency(mediana_fii, grouping=True)
f_desvio = locale.currency(desvio_fii, grouping=True)

# GRÁFICOS ASCII
graf_cdb = "█" * int(montante_cdb_liquido/1000)
graf_lci = "█" * int(montante_lci/1000)
graf_poup = "█" * int(montante_poupanca/1000)
graf_fii = "█" * int(montante_fii/1000)

# RELATÓRIO FINAL
print("\n======== RELATÓRIO DE INVESTIMENTOS ========")

print("Data da simulação:", data_simulacao)
print("Data estimada de resgate:", data_resgate)

print("\nTotal investido:", f_total)

print("\n----- VALORES FINAIS -----")

print("CDB:", f_cdb)
print("LCI:", f_lci)
print("Poupança:", f_poup)
print("FII:", f_fii)

print("\n----- ESTATÍSTICAS FII -----")

print("Média:", f_media)
print("Mediana:", f_mediana)
print("Desvio padrão:", f_desvio)

print("\nMeta financeira atingida:", meta_atingida)

print("\n----- GRÁFICO COMPARATIVO -----")
print("CDB      ", graf_cdb)
print("LCI      ", graf_lci)
print("POUPANÇA ", graf_poup)
print("FII      ", graf_fii)
