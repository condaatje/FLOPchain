# Utility functions for cryptography such as hashing, public/private key encryption, etc.

from Crypto.PublicKey import RSA
import hashlib

def sha256hash(str):
    """
    SHA 256 hashing of properly encoded string
    :param str: string to be hashed
    :return SHA 256 hash
    """
    return hashlib.sha256(str.encode('utf-8')).hexdigest()

def generate_key():
    """
    Generate public/private key pair
    :return RSA key pair
    """
    # Generate the RSA key pair
    return RSA.generate(2048)

def extract_public_key(key):
    """
    Extract the public key from an RSA key pair
    :param key: the RSA key pair of interest
    :return the public key
    """
    return key.publickey().exportKey("PEM")

def extract_private_key(key):
    """
    Extract the private key from an RSA key pair
    :param key: the RSA key pair of interest
    :return the private key
    """
    return key.exportKey("PEM")
