from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import User,Tokens, CONN
from secrets import token_hex

app = FastAPI()

def connectDB():
        engine = create_engine(CONN, echo=True)
        Session = sessionmaker(bind=engine)
        return Session()

@app.post('/cadastro')
def signin(nome:str, usuario:str, senha:str):
        session=connectDB()
        user = session.query(User).filter_by(user=usuario, password=senha).all()
        if len(user) == 0:
                x=User(name=nome, user=usuario, password=senha)
                session.add(x)
                session.commit()
                return {'status':'Usuario cadastrado com sucesso'}
        elif len(user)>0:
                return{'status':'Usuario já cadastrado'}

@app.post('/login')
def login(usuario:str, senha:str):
        session=connectDB()
        user = session.query(User).filter_by(user=usuario, password=senha).all()
        if len(user)==0:
                return {'status':'Usuario inexistente'}

        while True:
                token = token_hex(50)
                tokenExist = session.query(Tokens).filter_by(token=token).all()
                if len(tokenExist) == 0:
                        userExist = session.query(Tokens).filter_by(id_user=user[0].id).all()
                        if len(userExist)==0:
                                novoToken = Tokens(id_user=user[0].id, token=token)
                                session.add(novoToken)


                        elif len(userExist)>0:
                                userExist[0].token = token
                        session.commit()
                        break
        return token


                        