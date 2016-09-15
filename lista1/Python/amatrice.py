from agents import *

class Human(Thing):
    pass

class Rock(Thing):
    pass

class Droid(Agent):
    "An agent that keeps track of the direction it has"
    #holding = []
    actualDirection = Direction("down") #you can specify in which direction do you prefer to start

    def can_grab(self, thing):
        '''Explorer can only grab Humans'''
        return isinstance( thing, Human().__class__)
    

    
class amatriceEnvironment(XYEnvironment): ## TAKE A LOOK AT XY AND WUMPUS ENVIRONMENT Line 376 and 678 agents.py
    rock_probability = 0.2 # Probability to find a rock in a location. (From Chapter 7.2)
    humans_quantity = 2 # Probability to find a human in a location. (From Chapter 7.2)
    maxSteps = 30 # calculate the maximium steps (squares) to the agent end
    steps = 0;
    
    def __init__(self, agent, width=3, height=13): #vector, is gonna be matrix
        super(amatriceEnvironment, self).__init__(width, height) 
        self.init_world(agent)
        
        
    def init_world(self, agent):

        "WALLS"
        self.add_walls()

        "ROCKS"
        for x in range(self.x_start, self.x_end):
            for y in range(self.y_start, self.y_end):
                if random.random() < self.rock_probability:
                    self.add_thing(Rock(), (x, y), True)
        
        "AGENT"
        self.add_thing(agent, (1, 1), True)
        
        "HUMANS"
        for w in range(self.humans_quantity):
            w_x, w_y = self.random_location_inbounds()
            self.add_thing(Human(), (w_x, w_y), True)
    
    #overrides the function in agents.py because of a bug - Function in line 
    def random_location_inbounds(self, exclude=None):
        '''Returns a random location that is inbounds (within walls if we have walls)'''
        location = (random.randint(self.x_start, self.x_end-1), random.randint(self.y_start, self.y_end-1))
        if exclude is not None:
            while(location == exclude):
                location = (random.randint(self.x_start, self.x_end), random.randint(self.y_start, self.y_end))
        return location

    #Returns a matrix of the world (with or without the walls)    
    def get_world(self, show_walls=True):
        '''returns the items in the world'''
        result = []
        x_start, y_start = (0, 0) if show_walls else (1, 1)
        x_end, y_end = (self.width, self.height) if show_walls else (self.width - 1, self.height - 1)
        for x in range(x_start, x_end):
            row = []
            for y in range(y_start, y_end):
                row.append(self.list_things_at((x, y)))
            result.append(row)
        return result
    
    
    ## TAKE A LOOK AT Line 729 agents.py 
    def percepts_from(self, agent, location, tclass=Thing):
        '''Returns percepts from a given location, and replaces some items with percepts from chapter 7.'''
        thing_percepts = {
            Human: Human(),
            Wall: Wall(),
            Rock: Rock()
            }

        '''Human'''
        if location != agent.location:
            thing_percepts[Human] = None


        result = [thing_percepts.get(thing.__class__, thing) for thing in self.things
                  if thing.location == location and isinstance(thing, tclass) and not isinstance(thing, agent.__class__)]
        return result if len(result) else [None]
    
    
    def is_done(self):
        if self.steps >= self.maxSteps:
            return 1
        return 0
    
    ## TAKE A LOOK AT Line 748 and 767 agents.py 
    def percept(self, agent):
        '''Returns things in the cell of the agent.
            Result format: [Proximity wall sensor / human sensor / take off]'''
        x, y = agent.location
        d = Direction(agent.actualDirection.direction)
        xW, yW = d.move_forward( (x,y) )
        result = []
        result.append(self.percepts_from(agent, (xW,yW) )) #Proximity sensor
        result.append(self.percepts_from(agent, (x, y) )) #Human Sensor 
        result.append(self.is_done())   #take off Sensor
        return result
    
    def execute_action(self, agent, action):
        self.steps += 1
        '''Modify the state of the environment based on the agent's actions
            Performance score taken directly out of the book

        if action == 'TurnRight':
            agent.direction = agent.direction + Direction.R
            agent.performance -= 1
        elif action == 'TurnLeft':
            agent.direction = agent.direction + Direction.L
            agent.performance -= 1
        elif'''
        if action == 'Forward':
            agent.bump = self.move_to(agent, agent.actualDirection.move_forward(agent.location))
            agent.performance -= 1
        elif action == 'Grab':
            things = [thing for thing in self.list_things_at(agent.location)
                      if agent.can_grab(thing)]
            if len(things):
                print("Grabbing", things[0].__class__.__name__)
                agent.performance += 1000
                #agent.holding.append(things[0])
                self.delete_thing(things[0])
            agent.performance -= 1
        elif action == 'TakeOff':
            agent.performance -= 1
            self.delete_thing(agent)
            self.maxSteps=0
            
            
def ReflexDroid():
    def program(percept):
        proximityS, humanS, takeOffS = percept;
        if takeOffS:
            return 'TakeOff'
        elif isinstance( humanS[0], Human().__class__):
            return 'Grab'
        elif isinstance( proximityS[0], Wall().__class__):
            return 'TakeOff'
        else:
            return 'Forward'
        '''elsif.....
        return 'TurnRight':
            
        return 'TurnLeft':
        '''
    return Droid(program)



########Testing try your code here         
### try to create a droid from ReflexDroid type. Reflex Can you image how to make another type of agent (model Based, table based)?
### try to create an amatriceEnvironment within the droid of the ReflexDroid type 
### try to see - understand the Enviroment/world hint: REMEBER 'get_world'
### try to execute step by step the world. Hint function step() of the environment.
### try to view the state of the world in each step
### Image changing the dimensions of the world, execute_action would be changed? Any other change?
