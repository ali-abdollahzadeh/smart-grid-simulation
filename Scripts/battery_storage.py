import pandas as pd
from config import PROCESSED_DEMAND_FILE, PROCESSED_SOLAR_FILE, PROCESSED_DATA_DIR

# Define battery parameters
BATTERY_CAPACITY_KWH = 500  # Total battery capacity in kWh
BATTERY_EFFICIENCY = 0.9  # Charging/discharging efficiency (90%)

# Output file path
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Battery_Storage.csv"

def calculate_battery_storage():
    # Load cleaned demand data
    demand_df = pd.read_csv(PROCESSED_DEMAND_FILE)
    demand_df['Datetime'] = pd.to_datetime(demand_df['Datetime'])
    demand_df.set_index('Datetime', inplace=True)

    # Resample to hourly demand
    hourly_demand = demand_df['Consumption_kWh'].resample('h').sum()

    # Load cleaned solar generation data
    solar_df = pd.read_csv(PROCESSED_SOLAR_FILE)
    solar_df['Datetime'] = pd.to_datetime(solar_df['Datetime'])
    solar_df.set_index('Datetime', inplace=True)

    # Ensure both dataframes have the same hourly index
    hourly_demand = hourly_demand.reindex(solar_df.index, fill_value=0)

    # Calculate hourly surplus energy
    hourly_surplus = solar_df['Generation_kWh'] - hourly_demand

    # Calculate battery storage levels and grid dependency
    battery_level = 0
    battery_storage = []
    grid_drawn = 0
    total_demand = 0
    self_consumed = 0

    for surplus, demand in zip(hourly_surplus, hourly_demand):
        total_demand += demand

        if surplus > 0:
            # Charge the battery with surplus energy
            battery_level += surplus * BATTERY_EFFICIENCY
            if battery_level > BATTERY_CAPACITY_KWH:
                battery_level = BATTERY_CAPACITY_KWH

            # Self-consume the energy surplus
            self_consumed += min(surplus, demand)

        else:
            # Use battery energy to cover deficit
            battery_level += surplus
            if battery_level < 0:
                grid_drawn += abs(battery_level)  # Draw from the grid
                battery_level = 0

        battery_storage.append(battery_level)

    # Calculate self-consumption ratio
    self_consumption_ratio = self_consumed / total_demand
    grid_dependency_ratio = grid_drawn / total_demand

    # Convert to DataFrame and save to CSV
    battery_storage_df = pd.DataFrame({
        'Datetime': hourly_surplus.index,
        'Battery_Level_kWh': battery_storage
    })
    battery_storage_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Battery storage data saved to {OUTPUT_FILE}")
    print("\nSelf-Consumption Ratio:", round(self_consumption_ratio * 100, 2), "%")
    print("Grid Dependency Ratio:", round(grid_dependency_ratio * 100, 2), "%")

if __name__ == "__main__":
    calculate_battery_storage()
