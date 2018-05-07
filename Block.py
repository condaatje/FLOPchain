from hashlib import sha256

class Block():
    """
    TODO
    """
    
    nonce = None
    transactions = []
    tstring = None
    
    def __init__(self, transactions, prev_block_hash, nonce=None):
        """
        TODO
        :param transactions: TODO
        :param prev_block_hash: TODO
        """
        self.transactions = transactions
        self.tstring = str(prev_block_hash)
        self.nonce = nonce
        
        for t in transactions:
            self.tstring += str(t.h())
    
    
    def h(self, new_nonce=None):
        """
        TODO
        :param nonce: TODO
        """
        if new_nonce != None:
            self.nonce = new_nonce
        
        if sha256 != None: 
            return sha256(self.tstring + str(self.nonce)).hexdigest()
        else: # not sure why this is happening w/ multithreading
            return -1
            # raise Exception("ERROR NO SHA!")