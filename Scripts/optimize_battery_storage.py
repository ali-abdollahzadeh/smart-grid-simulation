import pandas as pd
import numpy as np
from config import PROCESSED_DATA_DIR

# Load the surplus/deficit data
surplus_deficit_file = f"{PROCESSED_DATA_DIR}/Surplus_Deficit.csv"
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Optimal_Battery_Storage.csv"

def optimize_battery_storage():
    # Load the surplus/deficit data
    surplus_deficit_df = pd.read_csv(surplus_deficit_file, parse_dates=['Datetime'])

    # Calculate cumulative surplus and deficit over time
    cumulative_surplus = surplus_deficit_df['Surplus_kWh'].cumsum()
    cumulative_deficit = surplus_deficit_df['Deficit_kWh'].cumsum()

    # Calculate the maximum storage needed to cover deficits
    max_deficit = cumulative_deficit.max()
    max_surplus = cumulative_surplus.max()

    # Calculate recommended battery size (to cover peak deficit)
    recommended_battery_size = max_deficit

    # Save results to a CSV file
    result_df = pd.DataFrame({
        'Cumulative_Surplus_kWh': cumulative_surplus,
        'Cumulative_Deficit_kWh': cumulative_deficit
    })
    result_df.to_csv(OUTPUT_FILE, index=False)

    # Print summary
    print(f"Optimal Battery Storage size: {recommended_battery_size:.2f} kWh")
    print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    optimize_battery_storage()
