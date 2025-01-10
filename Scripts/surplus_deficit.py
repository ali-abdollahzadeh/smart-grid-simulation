import pandas as pd
import numpy as np
from config import PROCESSED_DEMAND_FILE, PROCESSED_SOLAR_FILE, PROCESSED_DATA_DIR

# Output file path
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Surplus_Deficit.csv"

def calculate_surplus_deficit():
    # Load cleaned demand data
    demand_df = pd.read_csv(PROCESSED_DEMAND_FILE)
    demand_df['Datetime'] = pd.to_datetime(demand_df['Datetime'])
    demand_df.set_index('Datetime', inplace=True)

    # Load cleaned solar generation data
    solar_df = pd.read_csv(PROCESSED_SOLAR_FILE)
    solar_df['Datetime'] = pd.to_datetime(solar_df['Datetime'])
    solar_df.set_index('Datetime', inplace=True)

    # Extend solar data to match demand length
    num_repeats = -(-len(demand_df) // len(solar_df))  # Ceiling division
    solar_df_extended = pd.concat([solar_df] * num_repeats, ignore_index=True)
    solar_df_extended = solar_df_extended.iloc[:len(demand_df)]
    solar_df_extended['Datetime'] = demand_df.index

    # Merge demand and solar generation data
    combined_df = pd.merge(demand_df, solar_df_extended, on='Datetime', how='left').fillna(0)

    # Calculate surplus and deficit
    combined_df['Surplus_kWh'] = np.maximum(combined_df['Generation_kWh'] - combined_df['Consumption_kWh'], 0)
    combined_df['Deficit_kWh'] = np.maximum(combined_df['Consumption_kWh'] - combined_df['Generation_kWh'], 0)

    # Save the corrected data to CSV
    combined_df[['Datetime', 'Surplus_kWh', 'Deficit_kWh']].to_csv(OUTPUT_FILE, index=False)
    print(f"Corrected Surplus/Deficit data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    calculate_surplus_deficit()
