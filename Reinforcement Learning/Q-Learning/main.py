from QAgent import *
from GridWorld import *


env=GridWorld()
agent=QAgent()

for n_epi in range(10):
    done=False

    s=env.reset()
    while not done:
        a=agent.select_action(s)
        s_prime, r, done=env.step(a)
        agent.update_table((s,a,r,s_prime))
        s=s_prime
    agent.anneal_eps()

agent.show_table()