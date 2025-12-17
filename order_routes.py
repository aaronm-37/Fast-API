from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_session
from schemas import PedidoSchema
from models import Pedidos

order_router = APIRouter(prefix='/order', tags=['order'])

# criando uma rota

@order_router.get('/')
async def pedidos():
    '''
    Docstring for pedidos
    '''
    return {'voce acessou a rota de pedidos'}

@order_router.post('/pedido')
async def criar_pedido(pedido_schema: PedidoSchema, session: Session =  Depends(get_session)):
    novo_pedido = Pedidos(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {'mensagem':f'Pedido criado com sucesso. ID do pedido: {novo_pedido.id}'}