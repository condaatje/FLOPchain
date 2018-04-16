import Controller
import Miner
import User



num_users = 5
num_miners = 5

users = []
miners = []

control = Controller()

for _ in (range 1, num_users):
    users.append(User(control))

for _ in range(1, num_miners):
    miners.append(Miner(control))


# TODO run the network