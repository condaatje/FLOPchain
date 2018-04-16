import thread
import Queue

class Controller():
    self.transactions = Set()

    def __init__(self):
        """
        Initialization of controller for the FLOPchain network
        Simulates the role of nodes in a Blockchain system. Should preserve all
        decentralization logic, just makes simulation simpler.
        """

        # thread 'em out
        #thread.start_new_thread(f, (arg1, arg2))


    def handle_new_transaction(self, transaction):
        """
        takes in a new transaction from a user and adds it to the 
        un-mined transaction queue
        :param transaction: the transaction being broadcast
        """
        self.transaction_queue.append(transaction)
    
    
    def handle_new_block(self, block):
        """
        takes in a new block from a miner and alerts all other miners.
        Also removes the transactions processed from the transaction queue
        :param block: the newly mined block being broadcast
        """
        
    
        # if block is ok and all that
        self.transactions = self.transactions - block.transactions
        
        # TODO byzantine stuff