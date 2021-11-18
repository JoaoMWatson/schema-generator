# Gerador de schemas registry

## Requisitos
    - Python instalado >3.6.~

## Para utilizar siga esses passos
1. ```$ python -m venv .venv```
2. ```$ source .venv/bin/activate```
3. ```$ pip install -t requirements.txt```
4. ```$ python main.py <file> <sheet-number> <topic-name> <schema-description>```

**Parametros:**
 file: caminho do arquivo, recomenda-se colocar na pasta do projeto para minimizar erros
 sheet-number: numero da planilha que contem o mapping, começando o 0
 topic-name: nome do tópico para preenchimento de informações do schema
 schema-description: descrição do schema para preenchimento do header

**Para mais informações e em caso de duvida** 
```$ python main.py --help```