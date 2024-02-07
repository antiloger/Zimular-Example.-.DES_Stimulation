# main.py
from componets import *


class Modeling_workspace:
    def __init__(self, env) -> None:
        self.env = env
        self.Modeling_Machien_Pool = [Modeling_Machien(env, f"Modeling_Machien_{i}") for i in range(5)]
        self.Modeling_Store = Modeling_Store(env)
        self.Inception_Machien_Pool = [Inspection_Machien(env, f"Inspection_Machien_{i}") for i in range(5)]
        self.Inception_Store = ZStore(env, simpy.Store(env, capacity=10), "Inception_Store")


    def run(self, entity):
        machien = self.choose_machien(self.Modeling_Machien_Pool)
        yield from machien.run(entity=entity)
        yield self.Modeling_Store.put(entity)
        yield self.env.timeout(2)

        if self.Modeling_Store.level() > 2:
            print("Inception_Store is full")
            b = yield self.Modeling_Store.get()
            machien2 = self.choose_machien(self.Inception_Machien_Pool)
            yield from machien2.run(entity=b)
            yield self.Inception_Store.put(b)
                
        

            

    def choose_machien(self, machien_pool):
        queue_length = [len(machien.res.queue) for machien in machien_pool]
        #print(f'queue_length -> {queue_length}')
        return machien_pool[queue_length.index(min(queue_length))]

    
        

