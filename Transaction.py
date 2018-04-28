from random import random
import hashlib

class Transaction():
    """

    "We define an electronic coin as a chain of digital signatures.  Each owner
    transfers the coin to the next by digitally signing a hash of the previous
    transaction and the public key of the next owner and adding these to the end
    of the coin.  A payee can verify the signatures to verify the chain of
    ownership" - Satoshi Nakamoto

    ^ this is cool, but instead of using UTXOs we're just going to use balances
    for the sim, I think.

    """
    signature = None

    sender = None
    recipient = None
    amount = None
    salt = None

        # TODO actual cryptography? lol
        # right now anyone could say they are the sender and move coins
        # from any account. need to sign the message with sender's private key
    def __init__(self, sender, recipient, amount):
        """
        :param sender: the address of the sender
        :param recipient: the address of the recipient
        :param amount: the amount of FLOP to be transferred
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.salt = random() # makes transactions unique

    def h(self):
        """
        Return a deterministic hash of the transaction
        """
        m = hashlib.sha256()
        hstr = str(self.sender) + str(self.recipient) + str(self.amount) + str(self.salt)
        return hashlib.sha256(hstr).hexdigest()

    def sign(self, signature):
        """
        Signature of this transaction by the sender
        :param signature: the signature created by the sender based on their private key encryption
        """
        self.signature = signature
    # Note: miners verify transactions. No verify() method in here.
