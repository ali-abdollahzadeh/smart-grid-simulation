import gym
from gym import spaces
import numpy as np
import pandas as pd

class HouseholdEnergyEnv(gym.Env):
    def __init__(self):
        super(HouseholdEnergyEnv, self).__init__()

        # Observation space: [hour, day, month, season]
        self.observation_space = spaces.Box(low=0, high=23, shape=(4,), dtype=np.int32)
        
        # Action space: [usage level for appliances, heating, lights, etc.]
        self.action_space = spaces.Discrete(5)  # 0: Very low, 1: Low, 2: Medium, 3: High, 4: Very high
        
        self.current_hour = 0
        self.current_day = 0
        self.current_month = 0
        self.total_consumption = 0

        # Initialize a yearly load profile DataFrame
        self.load_profile = pd.DataFrame(index=pd.date_range("2022-01-01", "2022-12-31 23:00", freq="h"), columns=['Consumption_kWh'])

    def reset(self):
        self.current_hour = 0
        self.current_day = 0
        self.current_month = 0
        self.total_consumption = 0
        return np.array([self.current_hour, self.current_day, self.current_month, self.get_season()])

    def step(self, action):
        # Calculate energy consumption based on action taken
        base_consumption = self.get_base_consumption()
        consumption = base_consumption * (0.5 + action * 0.5)
        
        self.total_consumption += consumption
        self.load_profile.iloc[self.current_hour, 0] = consumption
        
        # Update time
        self.current_hour += 1
        if self.current_hour % 24 == 0:
            self.current_day += 1
        if self.current_day % 30 == 0:
            self.current_month += 1

        done = self.current_hour >= len(self.load_profile)

        reward = -consumption  # The goal is to minimize consumption

        return np.array([self.current_hour % 24, self.current_day % 7, self.current_month % 12, self.get_season()]), reward, done, {}

    def get_base_consumption(self):
        # Define a base consumption profile based on the hour of the day
        base_profile = [0.4, 0.3, 0.25, 0.2, 0.2, 0.25, 0.35, 0.7, 0.8, 0.85, 0.9, 0.8, 0.75, 0.7, 0.8, 1.0, 1.2, 1.4, 1.3, 1.1, 0.8, 0.6, 0.5, 0.4]
        return base_profile[self.current_hour % 24]

    def get_season(self):
        if self.current_month in [12, 1, 2]:
            return 0  # Winter
        elif self.current_month in [3, 4, 5]:
            return 1  # Spring
        elif self.current_month in [6, 7, 8]:
            return 2  # Summer
        else:
            return 3  # Fall

# Testing the environment
env = HouseholdEnergyEnv()
obs = env.reset()
for _ in range(24 * 365):
    action = env.action_space.sample()  # Random actions
    obs, reward, done, _ = env.step(action)
    if done:
        break

# Export the generated load profile
env.load_profile.to_csv("../data/energy_demand.csv")
print("Energy demand data exported successfully!")