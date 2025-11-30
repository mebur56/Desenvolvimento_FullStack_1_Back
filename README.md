# MVP Desenvolvimento FullStack Básico Backend

## Agenda
API para gerenciamento de agendamentos utilizando SQLite como banco


### Como executar

Navegue até a pasta src em um terminal e execute:
```
python -m pip install -r .\requirements.txt
```
Após a instalação dos pacotes com sucesso basta executar:
```
python -m flask run
```
ou para definir a porta execute:

```
python -m flask run --host=0.0.0.0 --port=5000
```

O banco SQLite tem suas tabelas inicializadas via código ao iniciar a API, não é necessária nenhuma ação


### Informações adicionais

O projeto contém a documentação swagger disponivél na url

http://localhost:5000/openapi/swagger

ou 

{sua_url}/openapi/swagger