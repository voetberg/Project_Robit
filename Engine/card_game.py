from .player import Player

class CardGame:
    def __init__(self, day, winning_threshold):
        self.juniper = Player(day, "Juniper")
        self.citrus = Player(day, "Citrus")

    def draw_card(self, player):
        pass

    def play_card(self, player):
        pass

    def discard_card(self, player):
        pass

    def reveal_card(self, player):
        pass

    def game_finished(self):
        state = 1
        state *= self.juniper.hp <= 0
        state *= self.juniper.hp >= 12
        state *= self.citrus.hp <= 0
        state *= self.citrus.hp >= 12
        return state

    def play_turn(self):

        pass

    def play_game(self):
        for _ in range(10):
            if self.game_finished() == 1:
                pass
            else:
                self.play_turn()
        # TODO Optimize bc this is far too slow
        if self.juniper.hp > self.citrus.hp:
            self.winner = self.juniper
        elif self.juniper < self.citrus:
            self.winner = self.citrus
        else:
            self.winner.name = None

        return self.winner.name



