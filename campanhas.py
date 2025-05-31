from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://sayderbr:Robson002@cluster0.ixr9nj2.mongodb.net/')
db = client['meubanco']
colecao_campanhas = db['campanhas']
colecao_sessoes = db['sessoes']

class SistemaCampanhas:
    @staticmethod
    def criar_campanhas():
        nome_da_campanha = input('\nDigite o nome da campanha: ')
        mestre = input('Nome do mestre da campanha: ')
        participantes = input('Quais jogadores irão jogar esta campanha: ')
        descricao = input('Descrição da campanha: ')
        
        campanha = {
            'nome': nome_da_campanha,
            'mestre': mestre,
            'participantes': participantes,
            'descricao': descricao,
            'sessoes': []
        }
        colecao_campanhas.insert_one(campanha)
        print("\n✅ Campanha criada com sucesso!\n")

    @staticmethod
    def listar_campanhas():
        print("\n=== CAMPANHAS ===")
        for campanha in colecao_campanhas.find():
            print(f"ID: {campanha['_id']} | Nome: {campanha['nome']} | Mestre: {campanha.get('mestre', 'Não informado')}")
        print()

    @staticmethod
    def criar_sessoes():
        SistemaCampanhas.listar_campanhas()
        id_campanha = input('Digite o ID da campanha: ')
        titulo = input('Digite o nome da sessão: ')
        resumo = input('Digite o resumo da sessão: ')

        sessao = {
            'titulo': titulo,
            'resumo': resumo,
            'campanha_id': ObjectId(id_campanha)
        }

        colecao_sessoes.insert_one(sessao)

        colecao_campanhas.update_one(
            {"_id": ObjectId(id_campanha)},
            {"$push": {"sessoes": {'titulo': titulo, 'resumo': resumo}}}
        )

        print("\n✅ Sessão criada com sucesso!\n")
    
    @staticmethod
    def listar_sessoes():
        print("\n=== SESSÕES CADASTRADAS ===")
        for sessao in colecao_sessoes.find():
            campanha = colecao_campanhas.find_one({"_id": sessao["campanha_id"]})
            nome_campanha = campanha["nome"] if campanha else "Campanha desconhecida"
            print(f"Título: {sessao['titulo']} | Resumo: {sessao['resumo']} | Campanha: {nome_campanha}")
        print()


