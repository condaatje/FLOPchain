from Controller import Controller
from Transaction import Transaction
from Miner import Miner
from User import User
from Block import Block

# Transactions:
t = Transaction("a", "b", '1')
t.salt = '262' # don't do live
assert(t.h() == 'd074ebe1920ad0e6646b322ddafbd0a109f89e2415cb676373191c6b28d72fda')


# Blocks:
b = Block([t], '262')
assert(b.h('262') == '761f90d0e044abaf0198f5c17f15b60c527b4a453784b5797d2ee84c6b456d19')

# User
# test create transaction
# test broadcast transaction

# Controller:
# Test new transaction
# Test new block
c = Controller(1, 1, 1000000096959000000000058095962450186640908945459952075351825212422645853)
# u = c.users[0]
m = c.miners[0]
m.mine()

# Miner
# test verify block
    # positive
    # negative
# test mine block


