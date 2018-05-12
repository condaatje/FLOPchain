from time import sleep

class Computation():
    sender = None
    function = None
    result = None
  
    def __init__(self, sender, function):
        """
        A computation job on the FLOPchain network
        :param sender: the address of the sender
        :param function: the compute job to be executed
        """
        
        self.sender = sender
        self.function = function

    def compute(self):
        """
        Execute the computation
        """
        self.result = self.function()