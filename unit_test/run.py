import simpy

env = simpy.Environment()
res1 = simpy.Resource(env, capacity=1)
res2 = simpy.Resource(env, capacity=1)

def main():
    with res1.request() as req1:

        yield req1
        yield env.timeout(1)
        print('Resource 1 acquired', env.now)
        with res2.request() as req2:
            yield req2
            yield env.timeout(1)
            print('Resource 2 acquired', env.now)

for i in range(5):
    env.process(main())
env.run()
