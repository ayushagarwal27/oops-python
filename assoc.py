class Engine:
    def start_engine(self):
        print('Starting engine')

    def stop_engine(self):
        print('Stopping engine')


class Car:
    def __init__(self, engine=Engine()):
        self.engine = engine

    def start(self):
        self.engine.start_engine()

    def stop(self):
        self.engine.stop_engine()


engine = Engine()
merc = Car(engine)
