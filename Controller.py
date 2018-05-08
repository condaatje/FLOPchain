import thread
import Queue
import User
from Miner import Miner
from Transaction import Transaction
from Block import Block


    # TODO controller is a bit like a stand-in for the gossip protocol
class Controller():
                            # transactions pending in the network.
    transactions = set()    # This simulates the gossip protocol we would
                            # rather not implement.

    users = []
    miners = []
    reward = "10"
    difficulty = None
    blockchain = []

    def __init__(self, num_users, num_miners, difficulty):
        """
        Initialization of controller for the FLOPchain network
        Simulates the role of nodes in a Blockchain system. Should preserve all
        decentralization logic, just makes simulation simpler.
        :param num_users: TODO
        :param num_miners: TODO
        :param difficulty: TODO
        """

        self.difficulty = int(difficulty)

        for _ in range(0, num_users):
            self.users.append(User.User(self))

        t = Transaction("TODOondaatje", "TODOjason", "0") # sender, recipient, amount
        t.salt = '262'
        genesis = Block([t], "") # takes in a list of transactions, and a hash of the previous block
        genesis.nonce = 832717007
        
        self.blockchain.append(genesis)
        
        for i in range(0, num_miners):
            u = self.users[i % len(self.users)]
            m = Miner(self, [genesis], u)
            self.miners.append(m)
            thread.start_new_thread(m.mine, ())

    def handle_new_transaction(self, transaction):
        """
        takes in a new transaction from a user and adds it to the
        un-mined transaction queue
        :param transaction: the transaction being broadcast
        """
        self.transactions.add(transaction)
        print(transaction)


    def handle_new_block(self, block):
        """
        takes in a new block from a miner and alerts all other miners.
        Also removes the transactions processed from the transaction queue
        :param block: the newly mined block being broadcast
        """

        # simulate the network accepting/denying the new block
        # in real life it would be individual miners checking against the whole chain
        last_block = self.blockchain[-1]
        expected_block = Block(block.transactions, last_block.h(last_block.nonce), block.nonce)
        
        if (expected_block.h() != block.h() 
            or int(block.h(), 16) > self.difficulty 
            or block.transactions[0].data != self.reward):
            
            # this is also where we would go through every transaction and
            # verify that the user was able to spend it, but better to leave it
            # out for this simulation...
            
            print "Bad block rejected by network!"
            print "Expected hashstr: ", expected_block.h()
            print "Actual hashstr: ", block.h()
            print "Expected coinbase reward: ", self.reward
            print "Actual coinbase reward: ", block.transactions[0].data
        else:
            print "Block", block.h(block.nonce), "accepted"
            self.blockchain.append(block)
            # 1. Distribute new block to other miners.
            self.transactions = self.transactions - set(block.transactions)
            for miner in self.miners:
                miner.handle_new_block(block)

