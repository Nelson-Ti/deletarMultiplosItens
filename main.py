import requests

# ID do registro para testar
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

# Loop para deletar cada registro
for id in ids_para_excluir:
    url = f"URL/{id}"
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ Registro {id} excluída com sucesso.")
    elif response.status_code == 404:
        print(f"⚠️ Registro {id} não encontrada.")
    else:
        print(f"❌ Erro ao excluir registro {id}: {response.status_code} - {response.text}")
