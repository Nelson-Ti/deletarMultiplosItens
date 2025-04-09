import requests

# ID da despesa para testar
ids_para_excluir = range(1, 100)  # de 1 até 100

# Headers (troque pelo seu token real!)
headers = {
    "Authorization": "Bearer TOKENAQUI",
    "Origin": "Origin_do_sistemaweb",
    "User-Agent": "PostmanRuntime/7.43.3",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
} 

# Requisição GET
#response = requests.delete(url, headers=headers)

# Loop para deletar cada despesa
for despesa_id in ids_para_excluir:
    url = f"URL/{despesa_id}"
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ Despesa {despesa_id} excluída com sucesso.")
    elif response.status_code == 404:
        print(f"⚠️ Despesa {despesa_id} não encontrada.")
    else:
        print(f"❌ Erro ao excluir despesa {despesa_id}: {response.status_code} - {response.text}")
