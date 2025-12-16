from fastapi import APIRouter

order_router = APIRouter(prefix='/order', tags=['order'])

# criando uma rota

@order_router.get('/')
async def pedidos():
    '''
    Docstring for pedidos
    '''
    return {'voce acessou a rota de pedidos'}