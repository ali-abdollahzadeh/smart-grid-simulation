import os
import logging
from config import PROCESSED_DATA_DIR, plot_dir

# Import your scripts
from clean_data import clean_price_data ,clean_demand_data, clean_solar_data, clean_investment_data
from surplus_deficit import calculate_surplus_deficit
from best_solar_panel_size import find_best_panel_size
from optimize_battery_storage import optimize_battery_storage
from optimize_pv_system import optimize_pv_system
from optimize_system import optimize_system
from cost_analysis import perform_cost_analysis
from energy_demand_simulation import HouseholdEnergyEnv
from visualize_data import main as visualize_data_main
from visualize_optimized_system import main as visualize_optimized_system_main

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
panel_sizes_to_test = range(10, 101, 10)
# Function to run the energy demand simulation
def run_energy_demand_simulation():
    print("Running energy demand simulation...")
    env = HouseholdEnergyEnv()
    obs = env.reset()
    for _ in range(24 * 365):
        action = env.action_space.sample()  # Random actions
        obs, reward, done, _ = env.step(action)
        if done:
            break
    # Export the generated load profile
    output_file = "../data/energy_demand.csv"
    env.load_profile.to_csv(output_file)
    print(f"Energy demand data exported to {output_file}")


def main():
    try:
        logging.info("Step 1: Cleaning all data...")
        clean_price_data()
        clean_demand_data()
        clean_solar_data()
        clean_investment_data()

        logging.info("Step 2: Simulating energy demand...")
        run_energy_demand_simulation()

        logging.info("Step 3: Calculating surplus/deficit...")
        calculate_surplus_deficit()

        logging.info("Step 4: Finding the best solar panel size...")
        find_best_panel_size(panel_sizes_to_test)

        logging.info("Step 5: Optimizing battery storage...")
        optimize_battery_storage()

        logging.info("Step 6: Optimizing PV system...")
        optimize_pv_system()

        logging.info("Step 7: Optimizing the entire system...")
        optimize_system()

        logging.info("Step 8: Performing cost analysis...")
        perform_cost_analysis()

        logging.info("Step 9: Generating visualizations...")
        visualize_data_main()
        visualize_optimized_system_main()

        logging.info("✅ All steps completed successfully!")

        logging.info(f"Processed data saved in: {PROCESSED_DATA_DIR}")
        logging.info(f"Plots saved in: {plot_dir}")

    except Exception as e:
        logging.error(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
