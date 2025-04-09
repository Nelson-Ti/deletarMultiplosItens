
# 🗑️ Exclusão em Massa via API - Python

Este script em Python realiza exclusões em massa de registros através de requisições HTTP `DELETE` para uma API REST. A ferramenta é útil para remover diversos itens (como despesas, contratos, usuários etc.) de forma automatizada e segura, utilizando um intervalo de IDs e cabeçalhos personalizados de autenticação.

## 🚀 Funcionalidades

- Envia requisições `DELETE` para uma API REST com base em um intervalo de IDs.
- Permite configurar headers personalizados (como token de autorização, origem e user-agent).
- Exibe o status de cada exclusão no terminal (sucesso, não encontrado, erro).
- Pode ser facilmente adaptado para diferentes endpoints ou APIs.

## 📦 Requisitos

- Python 3.10+
- Biblioteca `requests` (instalável com `pip install requests`

## 🧰 Tecnologias Utilizadas

- Python 


## 📁 Estrutura do Projeto

```
📦 deletar_multiplos
 ┣ 📜 main.py
 ┣ 📜 README.md
```

## ✅ Exemplos de Uso

```python
url = f"URLAQUI/{id}"

# Excluindo itens específicas
ids_para_excluir = range(1, 100)  # de 1 até 100
```

## 📌 Observações

- Certifique-se de que os itens existem antes de tentar removê-los.
- O sistema pode ser integrado com um banco de dados ou rodar sobre dados em memória.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Feito com 💻 em Python.
