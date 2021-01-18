from Agent import *
from GridWorld import *

env=GridWorld()
agent=Agent()

data=[[0 for _ in range(4)] for _ in range(4)]
gamma=1.0
alpha=10**(-4)

for k in range(50000):
    done=False
    history=list()
    
    while not done:
        action=agent.select_action()
        (x,y), reward, done=env.step(action)
        history.append((x,y,reward))
        
    env.reset()
    
    cum_reward=0
    
    for transition in history[::-1]:
        x,y,reward = transition
        
        data[x][y]=data[x][y]+alpha*(cum_reward-data[x][y])
        cum_reward+=gamma*reward
        
for row in data:
    print(row)