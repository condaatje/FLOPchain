from User import User
from Transaction import Transaction
from Controller import Controller

c = Controller(1, 1, 1000000096959000000000058095962450186640908945459952075351825212422645853)
u1 = User(c, 100)
u2 = User(c, 200)

t = Transaction(None, u1, 5)
u1.create_transaction(t, u2, 10)
