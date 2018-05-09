from time import sleep

class Computation():
    """
    TODO describe class

    """

    sender = None
    function = None
    result = None
  
    def __init__(self, sender, function):
        """
        :param sender: the address of the sender
        :param function: the compute job to be executed
        """
        
        self.sender = sender
        self.function = function

    def compute(self):
        self.result = self.function()