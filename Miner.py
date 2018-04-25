class Miner():
    blockchain = []
    controller = None

    def __init__(self, controller, chain):
        """
        Initializes a miner on the Flopchain network. 
        :param controller: the simulation controller
        :param chain: the blockchain the miner starts with
        """
        self.controller = controller
        self.blockchain = chain
        self.mine()
    
    
    def publish_block(self, block):
        """
        Publish a successfully mined block to the network
        :param block: the discovered block to publish
        """
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
        
        # If new block is valid:
            # A. Stop mining
            # B. Append new block to local blockchain
            # C. Start mining on new chain (download new transactions)
            # D. return true
        
        # If block is not valid:
            # return false
        
        pass
    
    
    def mine(self):
        """
        Main mining loop $$$
        """
        
        # 1. build a new block
            # 2.
        
        
        
        pass
    