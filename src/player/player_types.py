import random


class PlayerType(object):
    def play(self, property, player):
        raise NotImplementedError("Method play must be implemented by its subclasses")

    def buy_property(self, property, player):
        if property.owner is None:
            player.balance -= property.sell_value
            property.owner = player

    def pay_rent(self, property, player):
        if property.owner is not None:
            player.balance -= property.rent_value
            property.owner.balance += property.rent_value


class ImpulsivePlayer(PlayerType):
    # NOTE: O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
    def play(self, property, player):
        if player.balance >= property.sell_value:
            self.buy_property(property, player)

        self.pay_rent(property, player)


class DemandingPlayer(PlayerType):
    # NOTE: O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    def play(self, property, player):
        if property.rent_value > 50 and player.balance >= property.sell_value:
            self.buy_property(property, player)

        self.pay_rent(property, player)


class CautiousPlayer(PlayerType):
    # NOTE: O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
    def play(self, property, player):
        if (player.balance - property.sell_value) >= 80 and player.balance >= property.sell_value:  # fmt: skip
            self.buy_property(property, player)

        self.pay_rent(property, player)


class RandomPlayer(PlayerType):
    # NOTE: O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
    def play(self, property, player):
        buy_probability = random.random()

        if buy_probability < 0.5 and player.balance >= property.sell_value:
            self.buy_property(property, player)

        self.pay_rent(property, player)
