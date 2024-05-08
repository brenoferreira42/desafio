class ImpulsivePlayer(object):
    def play(self, property: int) -> int:
        # TODO: O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
        ...


class DemandingPlayer(object):
    def play(self, property: int) -> int:
        # TODO: O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
        return ...


class CautiousPlayer(object):
    def play(self, property: int) -> int:
        # TODO: O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
        return property


class RandomPlayer(object):
    def play(self, property: int) -> int:
        # TODO: O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
        return property
