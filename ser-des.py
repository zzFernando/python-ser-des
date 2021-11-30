from pykson import Pykson,JsonObject, IntegerField, StringField, ObjectListField, DateField, ListField
import pickle


class Cliente(JsonObject):
    nome = StringField()
    sobre_nome = StringField()
    idade = IntegerField()
    data_nasc = DateField()
    endereco = StringField()
    bairro = StringField()
    cidade = StringField()
    estado = StringField()
    profissao = StringField()
    score = ListField(int)
    tags = ListField(str)


teste = Cliente(
    nome='Joazinho',
    sobre_nome='da silva',
    idade=12,
    data_nasc='1980-01-01',
    endereco='Rua ABC',
    bairro='Aquele',
    cidade='Porto Alegre',
    estado='RS',
    profissao='Estudante',
    score = [10, 8, 9],
    tags = ['aluno', 'bom', 'aprovado'],

)
#Serialize
print('Serialize')
teste1 = Pykson().to_json(teste)
with open('data.json', 'wb') as fp:
    pickle.dump(teste1, fp)

with open('data.json', 'rb') as fp:
    data = pickle.load(fp)
print(data)
print(type(data))

print('===============================================')

#Deserialize
print('Deserialize')
teste = Pykson().from_json(data, Cliente)
print(teste)