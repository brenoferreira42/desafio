import random


class PlayerStrategy(object):
    def play(self, property, player):
        raise NotImplementedError("Method play must be implemented by its subclasses")

    def _buy_property(self, property, player):
        if property.owner is None:
            player.balance -= property.sell_value
            property.owner = player

    def _pay_rent(self, property, player):
        if property.owner is not None:
            player.balance -= property.rent_value
            property.owner.balance += property.rent_value


class ImpulsivePlayerStrategy(PlayerStrategy):
    # NOTE: O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
    def play(self, property, player):
        if player.balance >= property.sell_value:
            self._buy_property(property, player)

        self._pay_rent(property, player)


class DemandingPlayerStrategy(PlayerStrategy):
    # NOTE: O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    def play(self, property, player):
        if property.rent_value > 50 and player.balance >= property.sell_value:
            self._buy_property(property, player)

        self._pay_rent(property, player)


class CautiousPlayerStrategy(PlayerStrategy):
    # NOTE: O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
    def play(self, property, player):
        if (player.balance - property.sell_value) >= 80 and player.balance >= property.sell_value:  # fmt: skip
            self._buy_property(property, player)

        self._pay_rent(property, player)


class RandomPlayerStrategy(PlayerStrategy):
    # NOTE: O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
    def play(self, property, player):
        buy_probability = random.random()

        if buy_probability < 0.5 and player.balance >= property.sell_value:
            self._buy_property(property, player)

        self._pay_rent(property, player)
