from random import randint
from Block import Block
from Transaction import Transaction

class Miner():
    blockchain = None
    controller = None
    interrupt = False
    benefactor = None

    def __init__(self, controller, chain, benefactor):
        """
        Initializes a miner on the Flopchain network. 
        :param controller: the simulation controller
        :param chain: the blockchain the miner starts with
        :param benefactor: the miner's User model
        """
        self.controller = controller
        self.blockchain = chain
        self.benefactor = benefactor
    
    
    def publish_block(self, block):
        """
        Publish a successfully mined block to the network
        :param block: the discovered block to publish
        """
        self.blockchain.append(block)
        self.controller.handle_new_block(block)
        
    
    def handle_new_block(self, block):
        """
        Some other miner on the network has discovered a new block.
        Stop mining on the current one, build a new block, and start noncing.
        :param block: the newly mined block being received
        """
        
        # If new block is valid:
            # A. Stop mining
            # B. Append new block to local blockchain
            # C. Start mining on new chain (download new transactions)

        self.blockchain.append(block)
        self.interrupt = True # not really threadsafe but should work for us
        # mine loop going on in the background will listen to self.interrupt        
    
    def mine(self):
        """
        Main mining loop $$$
        never returns, should be threaded.
        """
        
        coinbase = Transaction(None, self.benefactor, "10") # miner reward
        transactions = [coinbase] + list(self.controller.transactions.copy())
        prev_hash = self.blockchain[-1].h(self.blockchain[-1].nonce)
        new_block = Block(transactions, prev_hash)
        
        while True:
            if self.interrupt:
                transactions = [coinbase] + list(self.controller.transactions.copy())
                prev_hash = self.blockchain[-1].h(self.blockchain[-1].nonce)
                new_block = Block(transactions, prev_hash)
                self.interrupt = False
            else:
                if randint != None:
                    nonce = randint(1, 1 * 10 ** 11) # TODO arbitrary?
                    
                    if nonce != None: # again, strange multithreading suff
                        hashstr = new_block.h(nonce)
                            
                        if int(str(hashstr), 16) <= self.controller.difficulty and hashstr != -1:
                            self.interrupt = True
                            self.publish_block(new_block)
                    else:
                        pass
                        
                else:
                    pass
                    # raise Exception("ERROR NO RANDINT!")