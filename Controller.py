import thread
import Queue
from User import User
from Miner import Miner
from Transaction import Transaction
from Block import Block

class Controller():
                            # transactions pending in the network. 
    transactions = set()    # This simulates the gossip protocol we would 
                            # rather not implement.

    users = []
    miners = []
    
    difficulty = None
    

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
            # self.users.append(User(self, 0)) TODO wait for user class to be ready
            pass
        
        t = Transaction("TODOondaatje", "TODOjason", "0") # sender, recipient, amount
        genesis = Block([t], "") # takes in a list of transactions, and a hash of the previous block
        
        for _ in range(0, num_miners):
            self.miners.append(Miner(self, [genesis]))
        
        
        # thread 'em out
        # thread.start_new_thread(f, (arg1, arg2))


    def handle_new_transaction(self, transaction):
        """
        takes in a new transaction from a user and adds it to the 
        un-mined transaction queue
        :param transaction: the transaction being broadcast
        """
        self.transactions += transaction
    
    
    def handle_new_block(self, block):
        """
        takes in a new block from a miner and alerts all other miners.
        Also removes the transactions processed from the transaction queue
        :param block: the newly mined block being broadcast
        """
        
        # 1. Distribute new block to other miners.
        
        # 2. If they accept it, remove transactions from pending transaction queue
        #    (simulates what would happen in decentralized network)
        self.transactions = self.transactions - block.transactions
        
        # 3. All miners start mining new block
        
        