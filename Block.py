import hashlib

class Block():
    """
    TODO
    """
    
    nonce = None
    transactions = []
    tstring = None
    
    def __init__(self, transactions, prev_block_hash):
        """
        TODO
        :param transactions: TODO
        :param prev_block_hash: TODO
        """
        self.transactions = transactions
        self.tstring = str(prev_block_hash)
        
        for t in transactions:
            self.tstring += str(t.h())
    
    
    def h(self, nonce):
        """
        TODO
        :param nonce: TODO
        """
        self.nonce = nonce
        return hashlib.sha256(self.tstring + str(nonce)).hexdigest()
        