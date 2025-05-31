from pymongo import MongoClient
from bson import ObjectId
from campanhas import SistemaCampanhas

client = MongoClient('mongodb+srv://sayderbr:Robson002@cluster0.ixr9nj2.mongodb.net/')
db = client['meubanco']
colecao_usuarios = db['usuarios_rpg']
colecao_personagens = db['usuarios']
colecao_itens = db['inventario']

# ======================= SISTEMA PRINCIPAL =======================
class sistema:
    # ======================= CADASTRO =======================
    def cadastrar_usuario(self):
        print("=== Cadastro de Novo Usuário ===")
        usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        tipo = input("Tipo (mestre/player): ").lower()

        if tipo not in ["mestre", "player"]:
            print("Tipo inválido. Digite 'mestre' ou 'player'.")
            return

        if colecao_usuarios.find_one({"usuario": usuario}):
            print("Usuário já existe. Tente outro nome.")
            return

        colecao_usuarios.insert_one({"usuario": usuario, "senha": senha, "tipo": tipo})
        print("Usuário cadastrado com sucesso!\n")

    # ======================= LOGIN =======================
    def login_usuario(self):
        print("=== Login ===")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        user = colecao_usuarios.find_one({"usuario": usuario, "senha": senha})
        if user:
            print(f"\nBem-vindo, {usuario}!")
            return user
        else:
            print("Usuário ou senha incorretos.\n")
            return None

    # ======================= MENU DO MESTRE =======================
    def menu_mestre(self):
        while True:
            print("\n==== MENU DO MESTRE ====")
            print("1. Cadastrar personagem")
            print("2. Listar personagens")
            print("3. Atualizar personagem")
            print("4. Deletar personagem")
            print("5. Inserir item")
            print("6. Listar itens")
            print("7. Atualizar item")
            print("8. Deletar item")
            print("9. Gerenciar campanhas")
            print("10. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar_personagem()
            elif opcao == "2":
                self.listar_personagens()
            elif opcao == "3":
                self.atualizar_personagem()
            elif opcao == "4":
                self.deletar_personagem()
            elif opcao == "5":
                self.inserir_item()
            elif opcao == "6":
                self.listar_itens()
            elif opcao == "7":
                self.atualizar_item()
            elif opcao == "8":
                self.deletar_item()
            elif opcao == "9":
                self.menu_campanhas()
            elif opcao == "10":
                print("Saindo do menu do mestre.\n")
                break
            else:
                print("Opção inválida.\n")

    # ======================= MENU DO PLAYER =======================
    def menu_player(self):
        while True:
            print("\n==== MENU DO PLAYER ====")
            print("1. Listar personagens")
            print("2. Listar itens")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.listar_personagens()
            elif opcao == "2":
                self.listar_itens()
            elif opcao == "3":
                print("Saindo do menu do player.\n")
                break
            else:
                print("Opção inválida.\n")

    # ======================= FUNÇÕES DE PERSONAGEM =======================
    def cadastrar_personagem(self):
        nome = input("Nome do personagem: ")
        classe = input("Classe: ")
        nivel = int(input("Nível: "))
        colecao_personagens.insert_one({"nome": nome, "classe": classe, "nivel": nivel})
        print("Personagem cadastrado!\n")

    def listar_personagens(self):
        print("\n=== Lista de Personagens ===")
        for p in colecao_personagens.find():
            print(f"ID: {p['_id']} | Nome: {p.get('nome')} | Classe: {p.get('classe')} | Nível: {p.get('nivel')}")
        print()

    def atualizar_personagem(self):
        self.listar_personagens()
        id_personagem = input("ID do personagem a atualizar: ")
        try:
            novo_nivel = int(input("Novo nível: "))
            colecao_personagens.update_one(
                {"_id": ObjectId(id_personagem)},
                {"$set": {"nivel": novo_nivel}}
            )
            print("Personagem atualizado!\n")
        except Exception as e:
            print(f"Erro: {e}\n")

    def deletar_personagem(self):
        self.listar_personagens()
        id_personagem = input("ID do personagem a deletar: ")
        try:
            personagem = colecao_personagens.find_one({"_id": ObjectId(id_personagem)})
            if personagem:
                confirmacao = input(f"Apagar {personagem['nome']}? (s/n): ").lower()
                if confirmacao == "s":
                    colecao_personagens.delete_one({"_id": ObjectId(id_personagem)})
                    print("Personagem deletado!\n")
                else:
                    print("Operação cancelada.")
            else:
                print("Personagem não encontrado.")
        except Exception as e:
            print(f"Erro: {e}\n")

    # ======================= FUNÇÕES DE ITEM =======================
    def inserir_item(self):
        nome = input("Nome do item: ")
        raridade = input("Raridade: ")
        descricao = input("Descrição: ")
        colecao_itens.insert_one({"item": nome, "raridade": raridade, "descricao": descricao})
        print("Item adicionado!\n")

    def listar_itens(self):
        print("\n=== Lista de Itens ===")
        for i in colecao_itens.find():
            print(f"ID: {i['_id']} | Item: {i.get('item')} | Raridade: {i.get('raridade')} | Descrição: {i.get('descricao')}")
        print()

    def atualizar_item(self):
        self.listar_itens()
        id_item = input("ID do item a atualizar: ")
        try:
            nova_desc = input("Nova descrição: ")
            colecao_itens.update_one(
                {"_id": ObjectId(id_item)},
                {"$set": {"descricao": nova_desc}}
            )
            print("Item atualizado!\n")
        except Exception as e:
            print(f"Erro: {e}\n")

    def deletar_item(self):
        self.listar_itens()
        id_item = input("ID do item a deletar: ")
        try:
            item = colecao_itens.find_one({"_id": ObjectId(id_item)})
            if item:
                confirmacao = input(f"Apagar {item['item']}? (s/n): ").lower()
                if confirmacao == "s":
                    colecao_itens.delete_one({"_id": ObjectId(id_item)})
                    print("Item deletado!\n")
                else:
                    print("Operação cancelada.")
            else:
                print("Item não encontrado.")
        except Exception as e:
            print(f"Erro: {e}\n")

    # ======================= MENU DE CAMPANHAS =======================
    def menu_campanhas(self):
        while True:
            print("\n=== MENU DE CAMPANHAS ===")
            print("1. Criar campanha")
            print("2. Listar campanhas")
            print("3. Criar sessão")
            print("4. Listar sessões")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                SistemaCampanhas.criar_campanhas()
            elif opcao == "2":
                SistemaCampanhas.listar_campanhas()
            elif opcao == "3":
                SistemaCampanhas.criar_sessoes()
            elif opcao == "4":
                SistemaCampanhas.listar_sessoes()
            elif opcao == "5":
                break
            else:
                print("Opção inválida.\n")

    # ======================= INÍCIO DO SISTEMA =======================
    def iniciar_sistema(self):
        while True:
            print("=== SISTEMA DE RPG ===")
            print("1. Cadastrar novo usuário")
            print("2. Fazer login")
            print("3. Sair")

            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                self.cadastrar_usuario()
            elif escolha == "2":
                user = self.login_usuario()
                if user:
                    if user['tipo'] == 'mestre':
                        self.menu_mestre()
                    else:
                        self.menu_player()
            elif escolha == "3":
                print("Encerrando sistema.")
                break
            else:
                print("Opção inválida.\n")

if __name__ == "__main__":
    sistema().iniciar_sistema()
