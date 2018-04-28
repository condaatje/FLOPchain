from Crypto.PublicKey import RSA
import hashlib
from Controller import Controller
from Transaction import Transaction

class User():
    balance = 0
    parent = None
    key = None
    key_pair = None
    address = None

    def __init__(self, controller, starting):
        """
        Initialize a user. Generate public/private key.
        """
        self.parent = controller
        self.balance = starting
        self.key = self.generate_key()
        self.key_pair = (self.key.publickey().exportKey("PEM"), self.key.exportKey("PEM"))
        self.address = hashlib.sha256(self.key_pair[0].encode('utf-8')).hexdigest()

    def create_transaction(self, previous_transaction, recipient, amount):
        """
        Generate a transaction consisting of coins being sent to another user on the network
        :param previous_transaction: The previous transaction to be hashed for the signature
        :param recipient: The intended user to receive the transaction quantity
        :param amount: The quantity of coins being sent to the recipient from the current user in this transaction
        """
        transaction = Transaction(self.address, recipient, amount)
        # Transaction signature based on previous transaction and recipient's public key
        sign_string = previous_transaction.h() + recipient.key_pair[0]
        hash = hashlib.sha256(sign_string.encode('utf-8')).hexdigest()
        signature = self.key.sign(hash, '')
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
        return key_pair[0]

    def generate_key(self):
        """
        Helper method to generate public/private key pair
        :return Pair of keys (public and private)
        """
        # Generate the RSA key pair
        k = RSA.generate(2048)
        return k
