from GridWorld import *
from QAgent import *


env=GridWorld()
agent=QAgent()

for n_epi in range(1000): # 1000번 시행
    done=False
    history=list()

    s=env.reset()
    while not done:
        a=agent.select_action(s)
        s_prime, r, done=env.step(a)
        history.append((s,a,r,s_prime))
        s=s_prime

    agent.update_table(history)
    agent.anneal_epas

agent.show_table()