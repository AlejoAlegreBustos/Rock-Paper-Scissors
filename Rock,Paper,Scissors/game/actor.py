import random

class Actor:

    """The class Actor have the responsability to provide a response to versus the user choose"""

    def __init__(self):
        self.r_p_s=["rock","paper","scissors"]

    def random_rps(self):
        machine_response=random.choice(self.r_p_s)

        return machine_response