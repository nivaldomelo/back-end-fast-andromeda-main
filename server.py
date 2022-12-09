from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco
# Teste


@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal_id == animal_id:
            return animal
    return {'erro': 'Animal nao localizado'}


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal_id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'msg': 'Animal removido com sucesso'}

    return {'erro': 'Animal nao localizado'}


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None
