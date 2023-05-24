

class Projects:
    def __init__(self, _id, name:str = None,
                 elements:list = None, num_of_pools=1):
        """
        """
        self.id = _id
        self.name = name
        self.elements = elements
        self.num_of_pools = num_of_pools


    def create(self):
        """
        """
