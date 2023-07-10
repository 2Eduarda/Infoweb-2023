class Esporte:
    def __init__(self, nome, horarios, mensalidade):
        self.nome = nome
        self.horarios = horarios
        self.mensalidade = mensalidade

    def __str__(self):
        return f"Nome: {self.nome}\nHorários: {self.horarios}\nMensalidade: R${self.mensalidade:.2f}"

class Academia:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.esportes = []

    def inserir(self, esporte):
        self.esportes.append(esporte)

    def listar(self):
        return self.esportes

    def media_mensalidade(self):
        total_mensalidade = sum(esporte.mensalidade for esporte in self.esportes)
        media = total_mensalidade / len(self.esportes) if len(self.esportes) > 0 else 0
        return media

    def __str__(self):
        esportes_str = "\n".join(str(esporte) for esporte in self.esportes)
        return f"Academia: {self.nome}\nEndereço: {self.endereco}\nEsportes:\n{esportes_str}"

academia = Academia("Minha Academia", "Rua Principal, 123")

esporte1 = Esporte("Futebol", "Segunda a sexta, das 18h às 20h", 150.0)
academia.inserir(esporte1)

esporte2 = Esporte("Natação", "Terça e quinta, das 9h às 10h", 200.0)
academia.inserir(esporte2)

esporte3 = Esporte("Musculação", "Segunda a sexta, das 7h às 22h", 100.0)
academia.inserir(esporte3)

print(academia)
print("Média da mensalidade:", academia.media_mensalidade())
