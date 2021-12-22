# fastapi
---
## Levantar repo de forma local
```powershell

# 1. Instalar PostgreSQl
# 2. Crear base de datos llamada fastapi

# 3. Crear ambiente virtual
py -3 -m venv venv

# 4. Instalar dependencias
pip install -r requirements.txt
```
---
## Comando de inicio
```powershell
uvicorn app.main:app --reload
```