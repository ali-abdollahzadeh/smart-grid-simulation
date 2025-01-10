import os

# Dynamically resolve the base directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

# Define data directories
RAW_DATA_DIR = os.path.join(BASE_DIR, "data/")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data/processed")
plot_dir = os.path.join(BASE_DIR, "plots")
# File paths
INVESTMENT_FILE = os.path.join(RAW_DATA_DIR, "investment_costs.csv")
PRICE_FILE = os.path.join(RAW_DATA_DIR, "electricity_prices.csv")
DEMAND_FILE = os.path.join(RAW_DATA_DIR, "energy_demand.csv")
SOLAR_FILE = os.path.join(RAW_DATA_DIR, "solar_generation.csv")




PROCESSED_INVESTMENT_FILE = os.path.join(PROCESSED_DATA_DIR, "Investment_Cost_Processed.csv")
PROCESSED_PRICE_FILE = os.path.join(PROCESSED_DATA_DIR, "Electricity_Price_Processed.csv")
PROCESSED_DEMAND_FILE = os.path.join(PROCESSED_DATA_DIR, "Energy_Demand_Processed.csv")
PROCESSED_SOLAR_FILE = os.path.join(PROCESSED_DATA_DIR, "Solar_Generation_Processed.csv")


