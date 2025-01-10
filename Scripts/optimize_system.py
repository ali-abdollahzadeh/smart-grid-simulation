import pandas as pd
import numpy as np
from config import PROCESSED_DATA_DIR

# Output file path
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Optimized_System.csv"

# Cost assumptions
PV_COST_PER_KW = 1200  # EUR per kW of PV
BATTERY_COST_PER_KWH = 300  # EUR per kWh of battery storage
ELECTRICITY_PRICE = 0.2  # EUR per kWh
FEED_IN_TARIFF = 0.1  # EUR per kWh for selling surplus to the grid

def optimize_system():
    # Load demand and solar generation data
    pv_system_df = pd.read_csv(f"{PROCESSED_DATA_DIR}/Optimal_PV_System.csv")
    surplus_deficit_df = pd.read_csv(f"{PROCESSED_DATA_DIR}/Surplus_Deficit.csv")

    # Calculate average daily demand and generation
    avg_daily_demand = pv_system_df['Demand_kWh'].mean()
    avg_daily_generation = pv_system_df['Generation_kWh'].mean()

    # Test different PV and battery sizes
    results = []
    for pv_size in range(5, 101, 5):  # PV sizes from 5 kW to 100 kW
        for battery_size in range(50, 2051, 50):  # Battery sizes from 50 kWh to 2050 kWh
            # Calculate investment costs
            pv_cost = pv_size * PV_COST_PER_KW
            battery_cost = battery_size * BATTERY_COST_PER_KWH
            total_cost = pv_cost + battery_cost

            # Calculate annual savings and feed-in earnings
            annual_savings = avg_daily_demand * 365 * ELECTRICITY_PRICE
            annual_surplus = max(avg_daily_generation * 365 - avg_daily_demand * 365, 0)
            feed_in_earnings = annual_surplus * FEED_IN_TARIFF

            # Calculate payback period and ROI
            payback_period = total_cost / (annual_savings + feed_in_earnings)
            roi = (annual_savings + feed_in_earnings) / total_cost * 100

            # Store the results
            results.append({
                'PV_Size_kW': pv_size,
                'Battery_Size_kWh': battery_size,
                'Total_Cost_EUR': total_cost,
                'Payback_Period_Years': payback_period,
                'ROI_Percent': roi
            })

    # Convert results to DataFrame and save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Optimized system configurations saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    optimize_system()
