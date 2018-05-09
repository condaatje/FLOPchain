import thread
import Queue
import User
from Miner import Miner
from Transaction import Transaction
from Block import Block
from time import sleep
from Computation import Computation


    # TODO controller is a bit like a stand-in for the gossip protocol
class Controller():
                            # transactions pending in the network.
    transactions = set()    # This simulates the gossip protocol we would
                            # rather not implement.

                            # compute jobs issued to the network
    computations = set()    # many of the minor functionality details
                            # are disserviced by this simplification, but it works
                            
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
        
        def nullFunc():
                sleep(1)
                return 2**100

        nullJob = Computation("Null", nullFunc)
        
        self.difficulty = int(difficulty)
        self.computations.add(nullJob)
        
        for _ in range(0, num_users):
            self.users.append(User.User(self))

        t = Transaction("TODOondaatje", "TODOjason", "0") # sender, recipient, amount
        t.salt = '262'
        genesis = Block([t], "", computation=Computation("", None)) # takes in a list of transactions, and a hash of the previous block
        genesis.nonce = 832717007
        genesis.computation.sender = "" # not messing up the hash
        genesis.computation.result = ""
        
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
    
    def handle_new_computation(self, computation):
        """
        :param computation: the computation for the network to solve
        """
        self.computations.add(computation)

    def handle_new_block(self, block):
        """
        takes in a new block from a miner and alerts all other miners.
        Also removes the transactions processed from the transaction queue
        :param block: the newly mined block being broadcast
        """

        # simulate the network accepting/denying the new block
        # in real life it would be individual miners checking against the whole chain
        last_block = self.blockchain[-1]
        expected_block = Block(block.transactions, last_block.h(last_block.nonce), block.nonce, block.computation)
        
        if (expected_block.h(block.nonce) != block.h(block.nonce) 
            or int(block.h(block.nonce), 16) > self.difficulty 
            or block.transactions[0].data != self.reward
            or block.computation.result != block.computation.function()):
            
            # this is also where we would go through every transaction and
            # verify that the user was able to spend it, but better to leave it
            # out for this simulation...
            
            print "Bad block rejected by network!"
            print "Expected hashstr: ", expected_block.h()
            print "Actual hashstr: ", block.h()
            print "Expected coinbase reward: ", self.reward
            print "Actual coinbase reward: ", block.transactions[0].data
            print "Expected computation result: ", block.computation.function()
            print "Actual computation result: ", block.computation.result
            # later/in the paper we can think about methods to verify decentralized
            # or incentives for correctness
            
        else:
            print "Block", block.h(block.nonce), "accepted"
            self.blockchain.append(block)
            self.transactions = self.transactions - set(block.transactions)
            
            # computation completion would be way more in-depth irl
            # self.computations = self.computations - set([block.computation])
            
            for miner in self.miners:
                miner.handle_new_block(block)

