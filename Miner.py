from random import randint
from Block import Block

class Miner():
    blockchain = None
    controller = None
    interrupt = False

    def __init__(self, controller, chain):
        """
        Initializes a miner on the Flopchain network. 
        :param controller: the simulation controller
        :param chain: the blockchain the miner starts with
        """
        self.controller = controller
        self.blockchain = chain
    
    
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
        
        # 1. Check if the block is valid
            # can check entire chain, but probably sufficient to just check
            # using the latest block. TODO this doesn't handle deviating chains...
        
        # If block is not valid:
            # return false
        
        # If new block is valid:
            # A. Stop mining
            # B. Append new block to local blockchain
            # C. Start mining on new chain (download new transactions)
            # D. return true
        
        # TODO logic for checking block validity (maybe not essential?)
        self.blockchain.append(block)
        self.interrupt = True # not really threadsafe but should work for us
    
    
    def mine(self):
        """
        Main mining loop $$$
        never returns, should be threaded.
        """
        transactions = self.controller.transactions.copy()
        prev_hash = self.blockchain[-1].h(self.blockchain[-1].nonce)
        new_block = Block(transactions, prev_hash)
        
        while True:
            if self.interrupt:
                transactions = self.controller.transactions.copy()
                prev_hash = self.blockchain[-1].h(self.blockchain[-1].nonce)
                new_block = Block(transactions, prev_hash)
                self.interrupt = False
            else:
                nonce = randint(1, 10000000) # TODO arbitrary
                hashstr = new_block.h(nonce)
                
                if int(hashstr, 16) <= self.controller.difficulty:
                    print("I mined a block!!$!")
                    self.interrupt = True
                    self.publish_block(new_block)