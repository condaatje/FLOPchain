class Miner():
    self.blockchain = []
    self.controller = None

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
        
        pass
        
    
    def handle_new_block(self, block):
        """
        Takes in a new block from a miner and alerts all other miners
        :param block: the newly mined block being broadcast
        """
        
        pass
    
    
    def mine(self):
        """
        Main mining loop $$$
        """
        
        pass
    