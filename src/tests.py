from Controller import Controller
from Transaction import Transaction
from Miner import Miner
from User import User
from Block import Block
from time import sleep
import sys
from Computation import Computation

print("Testing Transactions...")
t = Transaction("a", "b", '1')
t.salt = '262' # don't do live
assert(t.h() == 'd074ebe1920ad0e6646b322ddafbd0a109f89e2415cb676373191c6b28d72fda')


print("Testing Blocks...")
b = Block([t], '262', nonce=None, computation=Computation("", None))
b.computation.sender = "" # not messing up the hash rn
b.computation.result = ""
assert(b.h('262') == '761f90d0e044abaf0198f5c17f15b60c527b4a453784b5797d2ee84c6b456d19')




# example compute job
def twoplustwo():
    return 2 + 2





# Controller:
# Test new transaction
# Test new block
print("Testing Controller...")
difficulty = 3.0 * 10 ** 71 # bigger = easier
c = Controller(1, 5, difficulty) # multithreaded mining simulation is a bit wonkly
u = c.users[0]
m = c.miners[0]

u.broadcast_computation(twoplustwo)
sleep(10)

print 
print "Blockchain after ~10 seconds:"
print

for block in c.blockchain:
    print "[", block.h(), "]"
    print "                                 ^"





# https://stackoverflow.com/a/47420863
sys.stdout.flush()
sys.stdout.close()

sys.stderr.flush()
sys.stderr.close()