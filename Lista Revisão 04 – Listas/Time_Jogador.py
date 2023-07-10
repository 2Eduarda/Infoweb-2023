class Jogador:
    def __init__(self, nome, camisa, gols):
        self.nome = nome
        self.camisa = camisa
        self.gols = gols

    def __str__(self):
        return f"Nome: {self.nome}, Camisa: {self.camisa}, Gols: {self.gols}"


class Time:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado
        self.jogadores = []

    def inserir_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.jogadores:
            print(jogador)

    def artilheiro(self):
        if not self.jogadores:
            return None
        return max(self.jogadores, key=lambda jogador: jogador.gols)

    def __str__(self):
        return f"Nome do time: {self.nome}, Estado: {self.estado}"

time1 = Time("Time A", "Estado A")
jogador1 = Jogador("Jogador 1", "Camisa 11", 5)
jogador2 = Jogador("Jogador 2", "Camisa 9", 8)
jogador3 = Jogador("Jogador 3", "Camisa 3", 3)

time1.inserir_jogador(jogador1)
time1.inserir_jogador(jogador2)
time1.inserir_jogador(jogador3)

print(time1)  # Imprime as informações do time
time1.listar_jogadores()  # Imprime os jogadores cadastrados

artilheiro = time1.artilheiro()
if artilheiro:
    print("Artilheiro:", artilheiro)
else:
    print("Nenhum jogador cadastrado")

  

#Cadastrar um time e seus respectivos jogadores. As informações de cada jogador são: nome, camisa e número de gols realizados. A classe Time deve permitir inserir os jogadores, listar os jogadores cadastrados e obter o jogador com o maior número de gols (método Artilheiro).
#     Time
# - nome: string
# - estado: string
# - jogadores: Jogador[]
# + Inserir(j: Jogador) : void
# + Listaro(): Jogador[]
# + Artilheiro(): Jogador
# + ToString(): string

#    jogador
# - nome: string
# - camisa: string -gols: int
# + ToString(): string