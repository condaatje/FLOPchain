from Controller import Controller
from Transaction import Transaction
from Miner import Miner
from User import User
from Block import Block
from time import sleep, time
import sys
from Computation import Computation
from random import random, randint


print "Please make sure to customize the simulation parameters to your machine."
difficulty = 2.0 * 10 ** 71 # NOTE: should customize these parameters to your 
num_users  = 5              # machine - e.g. increases in difficulty make mining 
num_miners = 5              # easier, but also make rejected blocks more common

print "Starting Simulation..."
c = Controller(num_users, num_miners, difficulty)

# an easy computation
def twoplustwo():
    return 2 + 2

# a difficult computation
def twotimestwo():
    sleep(2)
    return 2 * 2

c.users[0].broadcast_computation(twoplustwo)
c.users[0].broadcast_computation(twotimestwo)

print "FLOPchain is live!"
print

num_minutes = 1
t_end = time() + (60 * num_minutes)
while time() < t_end:
    sleep(random() * 3)
    
    sender = c.users[randint(0, num_users - 1)]
    recipient = c.users[randint(0, num_users - 1)]
    
    prev_transaction = Transaction(None, sender, "5") # bit of a cheat
    sender.create_transaction(prev_transaction, recipient, "2")
    

print
print "Final Blockchain: "
print

for block in c.blockchain:
    print "[", block.h(), "]"
    print "                                 ^"

print
print "Simulation Complete."
print
