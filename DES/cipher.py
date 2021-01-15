
class Cipher:
    """
    Abstract module for any cipher 
    """
    def __init__(self, *args, **kwargs):
        raise NotImplementedError
    
    def encrpyt(self, *args, **kwargs):
        raise NotImplementedError
    
    def decrypt(self, *args, **kwargs):
        raise NotImplementedError

    
