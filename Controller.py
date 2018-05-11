import thread
import Queue
import User
from Miner import Miner
from Transaction import Transaction
from Block import Block
from time import sleep
from Computation import Computation


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
        :param num_users: Number of users in the network
        :param num_miners: Number of miners in the network
        :param difficulty: Mining difficulty
        """
        
        # A default function that miners can use to fill the requirement        
        def nullFunc():
                sleep(1)
                return 2**100
        
        nullJob = Computation("Null", nullFunc)
        self.computations.add(nullJob)
        self.difficulty = int(difficulty)
        
        # initialize users
        for _ in range(0, num_users):
            self.users.append(User.User(self))
            
        # set up the genesis block
        t = Transaction("Ondaatje", "Jason", "0")
        t.salt = '262'
        genesis = Block([t], "", computation=Computation("", None))
        self.blockchain.append(genesis)
        
        # initialize miners
        for i in range(0, num_miners):
            u = self.users[i % len(self.users)]
            m = Miner(self, [genesis], u)
            self.miners.append(m)
            thread.start_new_thread(m.mine, ())

    def handle_new_transaction(self, transaction):
        """
        Takes in a new transaction from a user and adds it to the un-mined 
        transaction queue
        :param transaction: the transaction being broadcast
        """
        self.transactions.add(transaction)
        print "Transaction ", transaction.h(), "broadcast to the network"
    
    def handle_new_computation(self, computation):
        """
        Takes in some compute job and puts it in the network simulation.
        :param computation: the computation for the network to solve
        """
        self.computations.add(computation)

    def handle_new_block(self, block):
        """
        Takes in a new block from a miner and alerts all other miners.
        Also removes the transactions processed from the transaction queue
        and verifies whether the block is valid.
        :param block: the newly mined block being broadcast/verified
        """

        # simulate the network accepting/denying the new block. In real
        # life it would be individual miners checking against the whole chain.
        last_block = self.blockchain[-1]
        expected_block = Block(block.transactions,
                               last_block.h(last_block.nonce),
                               block.nonce,
                               block.computation)
            
                                         # in it's current incarnation, 
        r = block.computation.function() # FLOPchain acts similarly to Ethereum,
                                         # where every miner computes and 
                                         # verifies every function
            
            # is the block valid?
        if (expected_block.h(block.nonce)    != block.h(block.nonce) 
            or int(block.h(block.nonce), 16)  > self.difficulty 
            or block.transactions[0].data    != self.reward
            or block.computation.result      != r):
            
            # this is also where we would go through every transaction and
            # verify that the user was able to spend it, but better to leave it
            # out for this simulation...
            
            
            
            print
            print "Bad block rejected by network!"
            print "Expected hashstr: ", expected_block.h()
            print "Actual hashstr: ", block.h()
            print "Expected coinbase reward: ", self.reward
            print "Actual coinbase reward: ", block.transactions[0].data
            print "Expected computation result: ", r
            print "Actual computation result: ", block.computation.result
            print
            
            # See discussion for some possible correctness incentives
            
        else: # the block passed verification! 
            
            print
            print "Block", block.h(block.nonce), "accepted"
            print 
            
            self.blockchain.append(block)
            self.transactions = self.transactions - set(block.transactions)
            
            # self.computations = self.computations - set([block.computation])
            # computation completion would be way more in-depth irl. 
            # See discussion.
            
            for miner in self.miners:
                # simulate network propogation. Note: this does not get into the 
                # nuances of "longest chain" mining.
                miner.handle_new_block(block)
