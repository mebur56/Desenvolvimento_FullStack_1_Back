# MVP Desenvolvimento FullStack Básico Backend

## Agenda
API para gerenciamento de agendamentos utilizando SQLite como banco

### Requisitos
É necessário a instalação do python e o pip para funcionamento da api

Python: https://www.python.org/downloads/

Após instalar o python em seu ambiente basta rodar o comando 
```
python -m ensurepip --upgrade
```

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

O projeto contém a documentação swagger disponível na url

http://localhost:5000/openapi/swagger

ou 

{sua_url}/openapi/swagger

Existe um front end complementar ao projeto disponível em [Desenvolvimento FullStack Básico FrontEnd](https://github.com/mebur56/Desenvolvimento_FullStack_1_Front)
