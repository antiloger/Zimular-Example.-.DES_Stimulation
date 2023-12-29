from simpy import Container
 
ContainerPool = {}

'''
1) can use ZContainerGenerator to create container pools and manage them 
2) use ZContainer to create a single container and manage it
''' 
class ZContainerGenerator():
    '''
    giving procedure is optional and default is 1 and 2 can be given
    '''
    def __init__(self,env,procedure=1):
        self.CPool = {}
        self.env = env
        self.procedure = procedure
    '''
        thsi shows how the containers are selected for populating and consuming items
        1 (default)- when populating the highest level is filled first then go for rest, consumed from lowest level container first
        (always there will be a full container mosly )
        2 - when populating the lowest level is filled first then go for rest, consumed from highest level container first
    '''
        
    '''
    must pass an array including container configs for each container in count[[capacity,initialValue],etc..]
    '''
    def createContainers(self,containerSlot):
        for key in range(containerSlot.keys()):
            #self.CPool.setdefault(key)
            ContainerPool.setdefault(key)
            number = 0
            for number in range(containerSlot[key][0]):
                #supposing inital value is 0, if not  give it as a parameter
                #self.CPool[key].append(ZContainer(self.env,key,number,containerSlot[key][1])) 
                ContainerPool[key].append(ZContainer(self.env,key,number,containerSlot[key][1]))
                number+=1

    def load(self,containerName,amount):
        if self.procedure == 1:
            chosenContainer = None
            highestContainerLevel = 0
            for container in ContainerPool[containerName]:
                if container.container.level > highestContainerLevel:
                    chosenContainer = container
                    highestContainerLevel = container.container.level
            chosenContainer.load(amount)
        else:
            chosenContainer = None
            lowestContainerLevel = ContainerPool[containerName][0].container.level
            for container in ContainerPool[containerName]:
                if container.container.level < lowestContainerLevel:
                    chosenContainer = container
                    lowestContainerLevel = container.container.level
            chosenContainer.load(amount)
        
    def consume(self,containerName,amount):
        if self.procedure == 1:
            chosenContainer = None
            lowestContainerLevel = ContainerPool[containerName][0].container.level
            for container in ContainerPool[containerName]:
                if container.container.level < lowestContainerLevel:
                    chosenContainer = container
                    lowestContainerLevel = container.container.level
            chosenContainer.consume(amount)
        else:
            chosenContainer = None
            highestContainerLevel = 0
            for container in ContainerPool[containerName]:
                if container.container.level > highestContainerLevel:
                    chosenContainer = container
                    highestContainerLevel = container.container.level
            chosenContainer.consume(amount)
        
    
            




        
    

class ZContainer():
    def __init__(self,env,name,number,Simpycontainer):
        self.env = env
        self.identity = {'name':name,'number':number}
        self.container = Simpycontainer
        self.monitor = {}
        #Later tis can be poltted in a graph which is unique for container instance
        self.usageSheet = {'title':f'{self.identity[name]}_{self.identity[number]}','data':{'Time':[],'level':[]}} 
        self.Trackusage = self.env.process(self.trackUsage())


    def trackUsage(self):
        while True:
            self.usageSheet['Time']=[self.env.now] 
            self.usageSheet['level']=[self.container.level]
            yield self.env.timeout(5) #every 5 time units, this will record its level and timeStamp

    def Full_fill(self):
        self.container.put(self.container.capacity-self.container.level)

    def Empty(self):
        self.container.get(self.container.level)

    def load(self,amount):
        self.container.put(amount)
    
    def consume(self,amount):
        self.container.get(amount)
    

    

