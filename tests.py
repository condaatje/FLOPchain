from Controller import Controller
from Transaction import Transaction
from Miner import Miner
from User import User

# Transactions:
t = Transaction("a", "b", 1)
t.salt = "262" # don't do live
assert(t.h() == 8698320300661017594)


# Controller:
# Test new transaction
# Test new block

# User
# test create transaction
# test broadcast transaction

# Miner
# test verify block
    # positive
    # negative
# test mine block


