class Subject():
    def __init__(self):
        self.obervers = []

    def add_observer(self, observer):
        self.obervers.append(observer)

    def notify(self):
        for observer in self.obervers:
            observer.update(self)