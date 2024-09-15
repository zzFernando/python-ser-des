# Python Serialize/Deserialize

Este repositório contém um exemplo de como serializar e desserializar objetos em Python utilizando a biblioteca **Pykson** para conversão de objetos Python para JSON, e vice-versa. O projeto demonstra como salvar dados de objetos em arquivos e depois restaurá-los.

## Descrição

O projeto usa a biblioteca **Pykson** para realizar as seguintes tarefas:
- **Serialização**: Convertendo objetos Python para o formato JSON.
- **Desserialização**: Convertendo dados JSON de volta para objetos Python.
- Os dados serializados são armazenados em um arquivo (`data.json`) e posteriormente lidos para reconstruir os objetos Python.

## Estrutura do Repositório

- **`ser-des.py`**: Código Python que executa as operações de serialização e desserialização.
- **`data.json`**: Arquivo onde os dados serializados são armazenados.
- **`.gitignore`**: Arquivo para ignorar certos arquivos e diretórios durante commits no Git.
- **`LICENSE`**: Licença MIT para o repositório.
- **`README.md`**: Este arquivo de documentação.

## Como Usar

### Pré-requisitos

- **Python 3.x**
- Instalar a biblioteca **Pykson**:
  
  ```bash
  pip install pykson
  ```

### Passos para Executar

1. Clone o repositório:
   
   ```bash
   git clone https://github.com/zzFernando/python-ser-des.git
   cd python-ser-des
   ```

2. Execute o script `ser-des.py`:

   ```bash
   python ser-des.py
   ```

### O que o script faz

- **Serialização**: Um objeto da classe `Cliente` é criado e serializado em JSON. O JSON é armazenado no arquivo `data.json`.
- **Desserialização**: O conteúdo do arquivo `data.json` é lido, desserializado e restaurado como um objeto Python.

### Exemplo de Saída

```python
Serialize
{"nome": "Joazinho", "sobre_nome": "da silva", "idade": 12, "data_nasc": "1980-01-01", "endereco": "Rua ABC", "bairro": "Aquele", "cidade": "Porto Alegre", "estado": "RS", "profissao": "Estudante", "score": [10, 8, 9], "tags": ["aluno", "bom", "aprovado"]}
===============================================
Deserialize
<Cliente object at 0x7f9d1045c3a0>
```

## Estrutura da Classe `Cliente`

A classe `Cliente` possui os seguintes atributos:
- **nome**: Nome do cliente.
- **sobre_nome**: Sobrenome do cliente.
- **idade**: Idade do cliente.
- **data_nasc**: Data de nascimento do cliente.
- **endereco**: Endereço do cliente.
- **bairro**: Bairro do cliente.
- **cidade**: Cidade do cliente.
- **estado**: Estado do cliente.
- **pais**: País do cliente.
- **profissao**: Profissão do cliente.
- **score**: Lista de notas (exemplo: [10, 8, 9]).
- **tags**: Lista de tags relacionadas ao cliente (exemplo: ["aluno", "bom", "aprovado"]).

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
