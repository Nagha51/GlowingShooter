

class DefaultCallbackManager:
    def __init__(self):
        self.update = []
        self.delete = []


class PlayerCallBackManager(DefaultCallbackManager):
    def __init__(self):
        super().__init__()
        self.shoot = []
