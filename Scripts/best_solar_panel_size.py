import pandas as pd
import numpy as np
from config import PROCESSED_DEMAND_FILE, PROCESSED_SOLAR_FILE, PROCESSED_DATA_DIR

# Output file path
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Best_Panel_Size_Analysis.csv"

# Function to calculate surplus/deficit for different solar panel sizes and find the best size
def find_best_panel_size(panel_sizes):
    # Load demand data
    demand_df = pd.read_csv(PROCESSED_DEMAND_FILE)
    demand_df['Datetime'] = pd.to_datetime(demand_df['Datetime'])
    demand_df.set_index('Datetime', inplace=True)

    # Load solar generation data
    solar_df = pd.read_csv(PROCESSED_SOLAR_FILE)
    solar_df['Datetime'] = pd.to_datetime(solar_df['Datetime'])
    solar_df.set_index('Datetime', inplace=True)

    best_size = None
    best_grid_dependency = float('inf')
    
    results = []

    for size in panel_sizes:
        # Calculate total solar generation for the given panel size
        solar_df['Total_Generation_kWh'] = solar_df['Generation_kWh'] * size

        # Merge demand and solar generation data
        combined_df = pd.merge(demand_df, solar_df, on='Datetime', how='left').fillna(0)

        # Calculate surplus and deficit
        combined_df['Surplus_kWh'] = np.maximum(combined_df['Total_Generation_kWh'] - combined_df['Consumption_kWh'], 0)
        combined_df['Deficit_kWh'] = np.maximum(combined_df['Consumption_kWh'] - combined_df['Total_Generation_kWh'], 0)

        # Calculate grid dependency ratio
        grid_dependency_ratio = combined_df['Deficit_kWh'].sum() / combined_df['Consumption_kWh'].sum()
        
        # Track the best size
        if grid_dependency_ratio < best_grid_dependency:
            best_grid_dependency = grid_dependency_ratio
            best_size = size

        # Collect results for all sizes
        results.append({
            'Panel_Size_m2': size,
            'Grid_Dependency_Ratio': grid_dependency_ratio
        })
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)

    # Save results to CSV
    results_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Results saved to {OUTPUT_FILE}")

    # Return the best size
    print(f"\nBest Solar Panel Size: {best_size} m²")
    return best_size

if __name__ == "__main__":
    # Define a range of panel sizes to test (from 10 m² to 100 m² in increments of 10 m²)
    panel_sizes_to_test = range(10, 101, 10)
    find_best_panel_size(panel_sizes_to_test)
