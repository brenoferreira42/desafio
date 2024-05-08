import random


class ImpulsivePlayer(object):
    def play(property: object, player) -> int:
        # NOTE: O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
        if property.owner is None and player.balance >= property.sell_value:
            player.balance -= property.sell_value
            property.owner = player
        else:
            player.balance -= property.rent_value
            property.owner.balance += property.rent_value


class DemandingPlayer(object):
    def play(property: int, player) -> int:
        # NOTE: O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
        if (
            property.owner is None
            and property.sell_value > 50
            and player.balance >= property.sell_value
        ):
            player.balance -= property.sell_value
            property.owner = player
        elif property.owner is not None:
            player.balance -= property.rent_value
            property.owner.balance += property.rent_value


class CautiousPlayer(object):
    def play(property: int, player) -> int:
        # NOTE: O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.

        if (
            property.owner is None
            and (player.balance - property.sell_value) >= 80
            and player.balance >= property.sell_value
        ):
            player.balance -= property.sell_value
            property.owner = player
        elif property.owner is not None:
            player.balance -= property.rent_value
            property.owner.balance += property.rent_value


class RandomPlayer(object):
    def play(property: int, player) -> int:
        # NOTE: O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
        buy_probability = random.random()

        if (
            property.owner is None
            and buy_probability < 0.5
            and player.balance >= property.sell_value
        ):
            player.balance -= property.sell_value
            property.owner = player
        elif property.owner is not None:
            player.balance -= property.rent_value
            property.owner.balance += property.rent_value
