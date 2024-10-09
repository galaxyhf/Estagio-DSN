import json
caminho_arquivo = "C:\\Users\\06006330\\Desktop\\Target\\Faturamento.json"

with open(caminho_arquivo, 'r') as file:
    faturamento_diario = json.load(file)["faturamento_diario"]

faturamento_filtrado = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

print(f"Menor valor de faturamento em um dia do mês: {menor_faturamento}")
print(f"Maior valor de faturamento em um dia do mês: {maior_faturamento}")
print(f"Número de dias no mês com faturamento superior à média mensal: {dias_acima_media}")