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
        :param function: TODO
        """
        
        self.sender = sender
        self.function = function

    def compute(self):
        self.result = self.function()

def twoplustwo():
    sleep(5)
    return 2 + 2
