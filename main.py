import os
import torch
import torch.nn as nn
import torch.optim as optim
from termcolor import colored
from gui import GUI

# AI Advisor model
class Advisor(nn.Module):
    def __init__(self):
        super(Advisor, self).__init__()
        self.linear1 = nn.Linear(3, 10)
        self.linear2 = nn.Linear(10, 3)

    def forward(self, x):
        x = torch.relu(self.linear1(x))
        return self.linear2(x)

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.territories = 1
        self.resources = {"gold": 100, "wood": 50}
        self.production_rate = {"gold": 10, "wood": 5}

# Game class
class Game:
    def __init__(self):
        self.gui = GUI()
        self.players = [Player(os.getlogin()), Player("A.I.")]
        self.ai_advisor = Advisor()
        self.optimizer = optim.Adam(self.ai_advisor.parameters(), lr=0.001)
        self.loss_fn = nn.MSELoss()

    def play(self):
        for _ in range(10):
            for player in self.players:
                current_state = torch.tensor([player.resources["gold"], player.resources["wood"], player.territories], dtype=torch.float32)

                if player == self.players[0]:
                    player_input = self.gui.get_player_input(player)
                    if player_input:
                        player.resources["gold"] -= 50
                        player.resources["wood"] -= 30
                        player.territories += 1
                else:
                    with torch.no_grad():
                        suggested_actions = self.ai_advisor(current_state)
                        build_territory_prob = torch.sigmoid(suggested_actions[2])
                        build_territory = torch.bernoulli(build_territory_prob).item()

                    if build_territory:
                        player.territories += 1
                        print(f"{player.name} builds a territory!")
                    else:
                        player.resources["gold"] -= suggested_actions[0].item()
                        player.resources["wood"] -= suggested_actions[1].item()

                for resource in player.resources:
                    player.resources[resource] += player.production_rate[resource]

                self.gui.draw(self.players[0].name, self.players[1].name, self.players[0].territories, self.players[1].territories)

                print(colored(f"{player.name} territories:", "yellow"))
                print(player.territories)
                print("=" * 20)

        self.gui.run()

    def train_ai_advisor(self):
        for _ in range(1000):
            for player in self.players[1:]:
                current_state = torch.tensor([player.resources["gold"], player.resources["wood"], player.territories], dtype=torch.float32)
                suggested_actions = self.ai_advisor(current_state)
                target_territory = torch.tensor([0, 0, 1], dtype=torch.float32)

                self.optimizer.zero_grad()
                loss = self.loss_fn(suggested_actions, target_territory)
                loss.backward()
                self.optimizer.step()

if __name__ == "__main__":
    print(colored("Welcome to Civilization Conquest Game!", "cyan"))
    print("In this game, you are a leader of a civilization competing against an AI opponent.")
    print("Your goal is to build structures, gather resources, and conquer territories.")
    print("The player with the most territories under their control wins!")
    print("=" * 40)

    game = Game()
    game.train_ai_advisor()
    game.play()

    territories = [player.territories for player in game.players]
    winner_idx = territories.index(max(territories))
    print(colored("Game Over!", "red"))
    print(f"{game.players[winner_idx].name} wins with {territories[winner_idx]} territories!")
