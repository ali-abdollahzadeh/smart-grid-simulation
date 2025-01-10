import pandas as pd
import os
from config import INVESTMENT_FILE, PRICE_FILE, DEMAND_FILE, SOLAR_FILE
from config import PROCESSED_INVESTMENT_FILE, PROCESSED_PRICE_FILE, PROCESSED_DEMAND_FILE, PROCESSED_SOLAR_FILE

# Function to clean electricity price data
def clean_price_data():
    # Load the electricity price data
    df = pd.read_csv(PRICE_FILE)

    # Convert Datetime to pandas datetime format
    df['Datetime'] = pd.to_datetime(df['Datetime'])

    # Convert EUR/MWh to EUR/kWh
    df['Price_EUR_kWh'] = df['Price_EUR_MWh'] / 1000

    # Drop the original EUR/MWh column
    df.drop(columns=['Price_EUR_MWh'], inplace=True)

    # Drop duplicates and save the cleaned data
    df.drop_duplicates(inplace=True)
    df.to_csv(PROCESSED_PRICE_FILE, index=False)
    print(f"Cleaned electricity price data saved to {PROCESSED_PRICE_FILE}")

# Function to clean energy demand data
def clean_demand_data():
    df = pd.read_csv(DEMAND_FILE)
    df.rename(columns={'Unnamed: 0': 'Datetime'}, inplace=True)
    df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')  # Convert to datetime
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.to_csv(PROCESSED_DEMAND_FILE, index=False)
    print(f"Cleaned energy demand data saved to {PROCESSED_DEMAND_FILE}")

# Function to clean solar generation data
def clean_solar_data():
    # Load the solar generation data
    df = pd.read_csv(SOLAR_FILE)

    # Convert wide format to long format
    df_long = df.melt(id_vars=["Unnamed: 0"], var_name="Month", value_name="Generation_kWh")

    # Rename the hour column
    df_long.rename(columns={"Unnamed: 0": "Hour"}, inplace=True)

    # Create a Datetime column
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
        "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
        "November": 11, "December": 12
    }
    df_long["Month"] = df_long["Month"].map(month_map)

    # Create a complete Datetime column
    df_long["Datetime"] = pd.to_datetime(
        "2022-" + df_long["Month"].astype(str) + "-01 " + df_long["Hour"]
    )

    # Drop unnecessary columns and sort by Datetime
    df_long = df_long[["Datetime", "Generation_kWh"]].sort_values(by="Datetime")

    # Save the cleaned file
    df_long.to_csv(PROCESSED_SOLAR_FILE, index=False)
    print(f"Cleaned solar generation data saved to {PROCESSED_SOLAR_FILE}")

# Function to clean investment cost data
def clean_investment_data():
    df = pd.read_csv(INVESTMENT_FILE)
    df.to_csv(PROCESSED_INVESTMENT_FILE, index=False)  # Save without changes
    print(f"Cleaned investment cost data saved to {PROCESSED_INVESTMENT_FILE}")

# Main function to clean all data
def main():
    print("Starting data cleaning process...")
    clean_price_data()
    clean_demand_data()
    clean_solar_data()
    clean_investment_data()
    print("Data cleaning process completed!")

if __name__ == "__main__":
    main()
