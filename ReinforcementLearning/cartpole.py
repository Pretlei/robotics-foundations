import gymnasium as gym
import numpy as np
import random

env = gym.make("CartPole-v1")

# Number of bins to discretize the continuous state
# a group of numbers go into one bin... organize by number value
bins = (6, 6, 12, 12)

# Limits for state variables
# cart position max, cart value max, pole angle max, pole angular velocity max

upper_bounds = [4.8, 5, 0.418, 5]
lower_bounds = [-4.8, -5, -0.418, -5]

# Q-table, a table showing the best action at a specific state
q_table = np.zeros(bins + (env.action_space.n,))

# Learning parameters
alpha = 0.1 #learning rate, how much new information affects old
gamma = 0.99 #how much future rewards (long-term planning) matter
epsilon = 1.0 # starting value on "exploration meter" (random actions done by agent)
epsilon_decay = 0.995 # how much random actions decays
epsilon_min = 0.01 # least value on exploration metre

episodes = 5000 # number of iterations


def discretize(state):
    # converts each variable to between 0 and 1
    ratios = [(state[i] + abs(lower_bounds[i])) /
            (upper_bounds[i] - lower_bounds[i]) for i in range(4)]
    
    # categorize each variable to respective bins, discretize them
    new_state = [int(round((bins[i] - 1) * ratios[i])) for i in range(4)]
    new_state = [min(bins[i] - 1, max(0, new_state[i])) for i in range(4)] # ensures bin indices are valid

    return tuple(new_state)


for episode in range(episodes):

    state, _ = env.reset()
    state = discretize(state)

    done = False

    while not done:

        # exploration vs exploitation
        if random.uniform(0, 1) < epsilon: # if the random number is less than epsilon, 
            action = env.action_space.sample() # choose random action
        else:
            action = np.argmax(q_table[state]) # otherwise choose the best known action

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        next_state = discretize(next_state)

        # Q-learning update
        old_value = q_table[state][action]
        next_max = np.max(q_table[next_state])

        new_value = old_value + alpha * (reward + gamma * next_max - old_value)
        q_table[state][action] = new_value

        state = next_state

    epsilon = max(epsilon_min, epsilon * epsilon_decay)

env.close()

env = gym.make("CartPole-v1", render_mode="human")

for episode in range(50):

    state, _ = env.reset()
    state = discretize(state)

    done = False

    while not done:

        action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, _ = env.step(action)

        state = discretize(next_state)

        done = terminated or truncated