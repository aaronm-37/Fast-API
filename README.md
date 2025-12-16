## comando para rodar aplicacao
```bash 
 uvicorn main:app --reload
 ```

## comandos para migracao e criacao do banco de dados
```bash
alembic revision --autogenerate -m 'Initial Migration'  
alembic upgrade head  
```