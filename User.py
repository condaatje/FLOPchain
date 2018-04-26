from Crypto.PublicKey import RSA
import hashlib

class User():
    balance = 0
    parent = None
    key_pair = None
    address = None
    
    def __init__(self, controller, starting):
        """
        Initialize a user. Generate public/private key.
        """
        self.parent = controller
        self.balance = starting
        self.key_pair = self.generate_key_pair()
        self.address = hashlib.sha256(self.key_pair[0].encode('utf-8')).hexdigest()
    
    def create_transaction(self, recipient, amount):
        """
        Generate a transaction consisting of coins being sent to another user on the network
        :param recipient: The intended user to receive the transaction quantity
        :param amount: The quantity of coins being sent to the recipient from the current user in this transaction
        """
        transaction = None
        # TODO Actually create the transaction including encryption with key pair
        self.broadcast(transaction)
    
    def broadcast(self, transaction):
        """
        Transmits the transaction to the miners for verification to be added to the blockchain
        :param transaction: The transaction being broadcasted to the miners
        """
        parent.handle_new_transaction(transaction)
    
    def generate_key_pair(self):
        """
        Helper method to generate public/private key pair
        :return Pair of keys (public and private)
        """
        k = RSA.generate(2048, 65537) 
        public_key = k.publickey().exportKey("PEM") 
        private_key = k.exportKey("PEM") 
        return public_key, private_key