import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import (
    PROCESSED_DEMAND_FILE,
    PROCESSED_SOLAR_FILE,
    PROCESSED_PRICE_FILE,
    plot_dir,
    PROCESSED_DATA_DIR
)

# Load cleaned data
demand_df = pd.read_csv(PROCESSED_DEMAND_FILE, parse_dates=['Datetime'])
solar_df = pd.read_csv(PROCESSED_SOLAR_FILE, parse_dates=['Datetime'])
price_df = pd.read_csv(PROCESSED_PRICE_FILE, parse_dates=['Datetime'])
battery_storage_df = pd.read_csv(f'{PROCESSED_DATA_DIR}/Battery_Storage.csv', parse_dates=['Datetime'])
surplus_deficit_df = pd.read_csv(f"{PROCESSED_DATA_DIR}/Surplus_Deficit.csv", parse_dates=['Datetime'])

# Set plot style
sns.set_theme(style="darkgrid")


# 🗓 Function to visualize **monthly** energy demand
def plot_monthly_energy_demand():
    monthly_demand = demand_df.resample('ME', on='Datetime').sum()
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_demand.index, monthly_demand['Consumption_kWh'], label='Monthly Energy Demand (kWh)', color='b')
    plt.title('Monthly Energy Demand')
    plt.xlabel('Date')
    plt.ylabel('Energy Demand (kWh)')
    plt.legend()
    plt.savefig(f'{plot_dir}/monthly_energy_demand.png')
    plt.close()
    print("Saved: plots/monthly_energy_demand.png")

# 🗓 Function to visualize **monthly** solar generation
def plot_monthly_solar_generation():
    monthly_solar = solar_df.resample('ME', on='Datetime').sum().sum(axis=1)
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_solar.index, monthly_solar, label='Monthly Solar Generation (kWh)', color='orange')
    plt.title('Monthly Solar Generation')
    plt.xlabel('Date')
    plt.ylabel('Solar Generation (kWh)')
    plt.legend()
    plt.savefig(f'{plot_dir}/monthly_solar_generation.png')
    plt.close()
    print("Saved: plots/monthly_solar_generation.png")

# 🗓 Function to visualize **monthly** battery storage levels
def plot_monthly_battery_storage_levels():
    battery_storage_df['Month'] = battery_storage_df['Datetime'].dt.to_period('M')
    monthly_battery = battery_storage_df.groupby('Month')['Battery_Level_kWh'].mean()
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_battery.index.to_timestamp(), monthly_battery, label='Monthly Battery Storage Level (kWh)', color='purple')
    plt.title('Monthly Battery Storage Levels')
    plt.xlabel('Date')
    plt.ylabel('Battery Level (kWh)')
    plt.legend()
    plt.savefig(f'{plot_dir}/monthly_battery_storage_levels.png')
    plt.close()
    print("Saved: plots/monthly_battery_storage_levels.png")



# 🗓 Function to plot monthly surplus/deficit with adjusted scale
def plot_monthly_surplus_deficit():
    monthly_data = surplus_deficit_df.resample('ME', on='Datetime').sum()

    plt.figure(figsize=(12, 6))
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot surplus on primary y-axis
    ax1.plot(monthly_data.index, monthly_data['Surplus_kWh'], color='green', label='Monthly Surplus (kWh)')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Surplus (kWh)', color='green')
    ax1.tick_params(axis='y', labelcolor='green')

    # Create secondary y-axis for deficit
    ax2 = ax1.twinx()
    ax2.plot(monthly_data.index, monthly_data['Deficit_kWh'], color='red', label='Monthly Deficit (kWh)')
    ax2.set_ylabel('Deficit (kWh)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Title and legend
    plt.title('Monthly Surplus/Deficit with Adjusted Scale')
    fig.tight_layout()
    plt.savefig(f"{plot_dir}/monthly_surplus_deficit.png")
    plt.close()
    print("Saved: monthly_surplus_deficit.png")



# 🕒 Function to visualize hourly energy demand (average across days)
def plot_hourly_energy_demand():
    demand_df['Hour'] = demand_df['Datetime'].dt.hour
    hourly_avg_demand = demand_df.groupby('Hour')['Consumption_kWh'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(hourly_avg_demand.index, hourly_avg_demand, label='Hourly Energy Demand (kWh)', color='b')
    plt.xticks(range(24), [f'{h:02d}:00' for h in range(24)])
    plt.title('Average Hourly Energy Demand')
    plt.xlabel('Hour of the Day')
    plt.xticks(rotation=45)
    plt.ylabel('Energy Demand (kWh)')
    plt.legend()
    plt.savefig(f'{plot_dir}/hourly_energy_demand.png')
    plt.close()
    print("Saved: plots/hourly_energy_demand.png")

# 🕒 Function to visualize hourly solar generation (average across days)
def plot_hourly_solar_generation():
    solar_df['Hour'] = solar_df['Datetime'].dt.hour
    hourly_avg_solar = solar_df.groupby('Hour')['Generation_kWh'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(hourly_avg_solar.index, hourly_avg_solar, label='Hourly Solar Generation (kWh)', color='orange')
    plt.xticks(range(24), [f'{h:02d}:00' for h in range(24)])
    plt.title('Average Hourly Solar Generation')
    plt.xlabel('Hour of the Day')
    plt.xticks(rotation=45)    
    plt.ylabel('Solar Generation (kWh)')
    plt.legend()
    plt.savefig(f'{plot_dir}/hourly_solar_generation.png')
    plt.close()
    print("Saved: plots/hourly_solar_generation.png")





# 🕒 Function to visualize hourly battery storage levels (average across days)
def plot_hourly_battery_storage_levels():
    battery_storage_df['Hour'] = battery_storage_df['Datetime'].dt.hour
    hourly_avg_battery = battery_storage_df.groupby('Hour')['Battery_Level_kWh'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(hourly_avg_battery.index, hourly_avg_battery, label='Hourly Battery Storage Level (kWh)', color='purple')
    plt.xticks(range(24), [f'{h:02d}:00' for h in range(24)])
    plt.title('Average Hourly Battery Storage Levels')
    plt.xlabel('Hour of the Day')
    plt.xticks(rotation=45)
    plt.ylabel('Battery Level (kWh)')
    plt.legend()
    plt.savefig(f'{plot_dir}/hourly_battery_storage_levels.png')
    plt.close()
    print("Saved: plots/hourly_battery_storage_levels.png")

# 🕒 Function to visualize hourly surplus/deficit with adjusted scale
def plot_hourly_surplus_deficit():
    hourly_data = surplus_deficit_df.groupby(surplus_deficit_df['Datetime'].dt.hour).mean()

    plt.figure(figsize=(12, 6))
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot surplus on the primary y-axis
    ax1.plot(hourly_data.index, hourly_data['Surplus_kWh'], color='green', label='Hourly Surplus (kWh)')
    ax1.set_xlabel('Hour of the Day')
    ax1.set_ylabel('Surplus (kWh)', color='green')
    ax1.tick_params(axis='y', labelcolor='green')

    # Create secondary y-axis for deficit
    ax2 = ax1.twinx()
    ax2.plot(hourly_data.index, hourly_data['Deficit_kWh'], color='red', label='Hourly Deficit (kWh)')
    ax2.set_ylabel('Deficit (kWh)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Title and legend
    plt.title('Average Hourly Surplus/Deficit with Adjusted Scale')
    fig.tight_layout()
    plt.savefig(f"{plot_dir}/hourly_surplus_deficit.png")
    plt.close()
    print("Saved: hourly_surplus_deficit.png")


# Main function to run all visualizations
def main():
    plot_hourly_energy_demand()
    plot_monthly_energy_demand()
    plot_hourly_solar_generation()
    plot_monthly_solar_generation()
    plot_hourly_battery_storage_levels()
    plot_monthly_battery_storage_levels()
    plot_hourly_surplus_deficit()
    plot_monthly_surplus_deficit()
    plot_hourly_solar_and_demand()

if __name__ == "__main__":
    main()
