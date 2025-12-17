from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import get_session
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    '''
    Docstring for autenticar
    '''
    return {
                'mensagem':'voce acessou a rota padrao de autenticacao',
                'autenticado': False
            }

# estrutura logica de criacao de usuario
@auth_router.post('/criar_conta')
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(get_session)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        # ja existe usuario com esse email
        raise HTTPException(status_code=400, detail='E-mail do usuário já cadastrado')
    else:
        senha_crypt = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_crypt, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {'mensagem':f'usuário cadastrado com sucesso { usuario_schema.email }'}
    