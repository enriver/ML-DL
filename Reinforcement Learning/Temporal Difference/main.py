from Agent import *
from GridWorld import *

env=GridWorld()
agent=Agent()

data=[[0 for _ in range(4)] for _ in range(4)]
gamma=1.0
alpha=10**(-2) # larger than MC

for k in range(50000):
    done=False
    
    while not done:
        x,y=env.get_state()
        action=agent.select_action()
        (x_prime,y_prime), reward, done=env.step(action)
        x_prime, y_prime=env.get_state()
        
        # Update the data in the table as soon as step is taken
        data[x][y]+=alpha*(reward+gamma*data[x_prime][y_prime]-data[x][y])

    env.reset()

for row in data:
    print(row)
