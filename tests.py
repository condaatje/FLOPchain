from Controller import Controller
from Transaction import Transaction
from Miner import Miner
from User import User
from Block import Block
from time import sleep
import sys

print("Testing Transactions...")
t = Transaction("a", "b", '1')
t.salt = '262' # don't do live
assert(t.h() == 'd074ebe1920ad0e6646b322ddafbd0a109f89e2415cb676373191c6b28d72fda')


print("Testing Blocks...")
b = Block([t], '262')
assert(b.h('262') == '761f90d0e044abaf0198f5c17f15b60c527b4a453784b5797d2ee84c6b456d19')


print("TODO TEST USERS")
# User
# test create transaction
# test broadcast transaction


# Controller:
# Test new transaction
# Test new block
print("Testing Controller...")
difficulty = 5.0 * 10 ** 72 # bigger = easier
c = Controller(0, 5, difficulty) # multithreaded mining simulation is a bit wonkly
# u = c.users[0]
m = c.miners[0]


sleep(10)
print 
print "Blockchain after ~10 seconds:"
for block in c.blockchain:
    print "-> ", block.h()


print("TODO TEST MINER")
# thread this guy out and give him like 5 sec
# Miner
# test verify block
    # positive
    # negative
# test mine block




# https://stackoverflow.com/a/47420863
sys.stdout.flush()
sys.stdout.close()

sys.stderr.flush()
sys.stderr.close()