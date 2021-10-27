import argparse

import gym

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Run an environment')
    parser.add_argument('--input-env', dest='input_env',required=True,
            choices=['cartpole', 'mountaincar', 'pendulum'],
            help='Specify the name of the environment')
    return parser

if __name__ == '__main__':
    args = build_arg_parser().parse_args()
    input_env = args.input_env

    name_map = {
        'cartpole': 'CartPole-v0',
        'mountaincar': 'MountainCar-v0',
        'pendulum': 'Pendulum-v0'
    }

    # creating the environment
    env = gym.make(name_map[input_env])

    # start iterating by resetting the environment
    for _ in range(20):
        # reset the env
        observation = env.reset()

        # iterating 100 times for each reset, starting w/ rendering the env
        for i in range(20):
            # rendering
            env.render()

            # printing the current observation
            print(observation)

            # taking an action based on the available action space
            action = env.action_space.sample()

            # extracting the consequences of taking the action
            observation, reward, done, info = env.step(action)

            # check if goal has been achieved
            if done:
                print("Episode finished after {} timesteps".format(i+1))
                break