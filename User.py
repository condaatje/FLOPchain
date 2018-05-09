from Crypto.PublicKey import RSA
import hashlib
import crypto
import Controller
from Transaction import Transaction
from Computation import Computation

class User():
    parent = None
    encrypt_key = None
    address = None

    def __init__(self, controller):
        """
        Initialize a user. Generate public/private key.
        """
        self.parent = controller
        self.encrypt_key = crypto.generate_key()
        self.address = crypto.sha256hash(crypto.extract_public_key(self.encrypt_key))

    def create_transaction(self, previous_transaction, recipient, data):
        """
        Generate a transaction consisting of coins being sent to another user on the network
        :param previous_transaction: The previous transaction to be hashed for the signature
        :param recipient: The intended user to receive the transaction quantity
        :param amount: The quantity of coins being sent to the recipient from the current user in this transaction
        """
        transaction = Transaction(self.address, recipient, data)
        # Transaction signature based on previous transaction and recipient's public key
        sign_string = previous_transaction.h() + crypto.extract_public_key(recipient.encrypt_key)
        hsh = crypto.sha256hash(sign_string)
        signature = self.encrypt_key.sign(hsh, '')
        transaction.sign(signature)
        # Broadcast transaction after being created
        self.broadcast(transaction)

    def broadcast(self, transaction):
        """
        Transmits the transaction to the miners for verification to be added to the blockchain
        :param transaction: The transaction being broadcasted to the miners
        """
        self.parent.handle_new_transaction(transaction)

    def get_public_key():
        """
        Getter method for returning public key of a user
        :return the public key for this particular user
        """
        return crypto.extract_public_key(self.encrypt_key)

    def broadcast_computation(self, function):
        """
        :parameter function: the computation to be uploaded for the 
        network to solve
        """
        c = Computation(self.address, function)
        self.parent.handle_new_computation(c)
        
        