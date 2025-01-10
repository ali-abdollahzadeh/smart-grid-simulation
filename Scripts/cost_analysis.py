import pandas as pd
from config import PROCESSED_DATA_DIR

# Output file path
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Cost_Analysis.csv"

# Assumptions
PV_COST_PER_KW = 1200  # Cost in EUR per kW of installed PV
BATTERY_COST_PER_KWH = 300  # Cost in EUR per kWh of battery storage
ELECTRICITY_PRICE = 0.2  # EUR per kWh (average electricity price)
FEED_IN_TARIFF = 0.1  # EUR per kWh (for surplus energy sold to the grid)

def perform_cost_analysis():
    # Load necessary data
    pv_system_df = pd.read_csv(f"{PROCESSED_DATA_DIR}/Optimal_PV_System.csv")
    battery_storage_df = pd.read_csv(f"{PROCESSED_DATA_DIR}/Optimal_Battery_Storage.csv")

    # Extract recommended PV system size and battery size
    optimal_pv_size = pv_system_df['Ratio'].mean() * 1000  # Convert to kW
    recommended_battery_size = battery_storage_df['Cumulative_Deficit_kWh'].max()

    # Calculate investment costs
    pv_investment_cost = optimal_pv_size * PV_COST_PER_KW
    battery_investment_cost = recommended_battery_size * BATTERY_COST_PER_KWH
    total_investment_cost = pv_investment_cost + battery_investment_cost

    # Calculate annual savings
    annual_energy_demand = pv_system_df['Demand_kWh'].sum()  # Total annual demand
    annual_savings = annual_energy_demand * ELECTRICITY_PRICE

    # Calculate potential earnings from selling surplus energy
    annual_surplus_energy = pv_system_df['Generation_kWh'].sum() - annual_energy_demand
    feed_in_earnings = max(annual_surplus_energy, 0) * FEED_IN_TARIFF

    # Calculate payback period
    payback_period = total_investment_cost / (annual_savings + feed_in_earnings)

    # Calculate ROI
    roi = (annual_savings + feed_in_earnings) / total_investment_cost * 100

    # Save results to CSV
    result_df = pd.DataFrame({
        'Metric': ['PV Investment Cost', 'Battery Investment Cost', 'Total Investment Cost', 'Annual Savings', 'Feed-In Earnings', 'Payback Period (Years)', 'ROI (%)'],
        'Value': [pv_investment_cost, battery_investment_cost, total_investment_cost, annual_savings, feed_in_earnings, payback_period, roi]
    })

    result_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Cost analysis results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    perform_cost_analysis()
