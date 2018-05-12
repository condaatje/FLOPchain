import User
from Transaction import Transaction
from Controller import Controller
import sys

difficulty = 1.0 * 10 ** 72 # bigger = easier
print "Initializing Controller..."
c = Controller(1, 0, difficulty)

print "Initializing some test users..."
u1 = User.User(c) # RSA Keygen takes a while on t2.micro?
u2 = User.User(c)

t = Transaction(None, u1, "5") # heads up transactions are initialized with a salt
                                # so if you want deterministic tests use t.salt = "something"
u1.create_transaction(t, u2, "10")














# https://stackoverflow.com/a/47420863
sys.stdout.flush()
sys.stdout.close()

sys.stderr.flush()
sys.stderr.close()