from ZIM.ZGen import EntityGenerator
from run import Modeling_workspace
from ZIM.output_table import System_Output
import simpy
from ZIM.ZResource import ResourcePool
from ZIM.ZContainer import ContainerPool
from ZIM.ZStore import StorePool

env = simpy.Environment()
workinit = Modeling_workspace(env)

entity_format = {
    "type": "item",
    "id": 0,
    "priority": 0,
}


generator = EntityGenerator(env, workinit, entity_format, init_count=1)


def customer_generator():
    
    # for _ in range(5):
    #     env.process(generator.generate_entity())
    #     yield env.timeout(1)
    for _ in range(20):
        entity = generator.generate_entity()
        env.process(workinit.run(entity))
        yield env.timeout(1)

# def customer_generator1():

#     env.process(workinit.work(
#         generator.enter_format(
#             priority=0
#         )
#     ))
#     yield env.timeout(1)

#     env.process(workinit.work(
#         generator.enter_format(
#             priority=0
#         )
#     ))
#     yield env.timeout(1)


#     env.process(workinit.work(
#         generator.enter_format(
#             priority=-1
#         )
#     ))



def run_simulation():
    print("Running simulation...")
    print("creating resources...")
    print("creating entities...")
    env.process(customer_generator())
    env.run()
    print("Simulation done.")

    print("---------RESOURCE1----------")
    for i in workinit.Modeling_Machien_Pool:
        print(f'name:-> {i.res_name}')
        print(f'entertime ->>>>{i.enter_time}')
        print(f'leavetime ->>>>{i.leave_time}')
        print(f'user_time ->>>>{i.user_time}')
        print(f'queue_time ->>>>{i.queue_time}')
        print('-------------------')
    
    print("---------RESOURCE2----------")
    for i in workinit.Inception_Machien_Pool:
        print(f'name:-> {i.res_name}')
        print(f'entertime ->>>>{i.enter_time}')
        print(f'leavetime ->>>>{i.leave_time}')
        print(f'user_time ->>>>{i.user_time}')
        print(f'queue_time ->>>>{i.queue_time}')
        print('-------------------')

    print('---------STORE----------')
    print(f'put->> {StorePool["Modeling_Store"].put_output}')
    

if __name__ == "__main__":
    run_simulation()
