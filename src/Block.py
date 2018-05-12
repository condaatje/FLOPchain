from hashlib import sha256

class Block():
    nonce = None
    transactions = []
    tstring = None
    computation = None
    
    def __init__(self, transactions, prev_block_hash, nonce=None, computation=None):
        """
        A block on the FLOPchain network. The basic unit in the blockchain.
        :param transactions: The transactions to be included in the block
        :param prev_block_hash: The previous block to be linked (via hashing) 
            to this one.
        """
        self.transactions = transactions
        self.tstring = str(prev_block_hash)
        self.nonce = nonce
        self.computation = computation
        
        for t in transactions:
            self.tstring += str(t.h())
    
    
    def h(self, new_nonce=None):
        """
        Calculate a block's hash with a given nonce
        :param nonce: the nonce to be hashed in
        """
        if new_nonce != None:
            self.nonce = new_nonce
        
        if sha256 != None: 
            return sha256(self.tstring 
                        + str(self.computation.sender) # doesn't hash the func 
                        + str(self.computation.result) # itself, which it should
                        + str(self.nonce)).hexdigest()
        else: # not sure why this is happening w/ multithreading
            return -1
            # raise Exception("ERROR NO SHA!")