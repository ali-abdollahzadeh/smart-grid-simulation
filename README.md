# Smart Grid Simulation Project

## Project Overview

This project simulates energy demand, solar generation, and battery storage levels for a smart grid system. It includes a cost analysis and optimization of photovoltaic (PV) systems and battery storage to enhance energy management and return on investment (ROI). The simulation results are visualized through various plots.

## Folder Structure

- **data/**: Contains all the necessary datasets for the simulation.
  - `electricity_prices.csv`: Electricity price data.
  - `energy_demand.csv`: Energy demand data.
  - `investment_costs.csv`: Cost of PV systems and batteries.
  - `solar_generation.csv`: Solar generation data.

- **processed/**: Folder for processed datasets.

- **Docs/**: Contains project documentation.
  - `project_info.pdf`: Detailed information about the project.

- **plots/**: Contains generated plots from the simulation.
  - `hourly_*.png`: Hourly data plots.
  - `monthly_*.png`: Monthly data plots.
  - `payback_period_heatmap.png`: Payback period analysis.
  - `roi_heatmap.png`: Return on investment heatmap.

- **Scripts/**: Contains all the Python scripts used for data processing, simulation, optimization, and visualization.
  - `main.py`: Main script to run the entire simulation.
  - `clean_data.py`: Cleans and processes raw datasets.
  - `energy_demand_simulation.py`: Simulates energy demand.
  - `optimize_pv_system.py`: Optimizes the size of the PV system.
  - `optimize_battery_storage.py`: Optimizes the battery storage levels.
  - `visualize_data.py`: Generates plots.

## Prerequisites

- Python 3.9 or higher

### Required Python Libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

## Setup Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/ali-abdollahzadeh/smart-grid-simulation.git
cd smart-grid-simulation
```

### Step 2: Install Required Libraries
```bash
pip install -r requirements.txt
```

*Note: If a `requirements.txt` file is not available, manually install the required libraries:*
```bash
pip install pandas numpy matplotlib seaborn
```

### Step 3: Run the Simulation
```bash
python Scripts/main.py
```

### Step 4: View Results

Check the `plots` folder for the generated plots and visualizations.

## External Tools

If any external simulators or tools were used (e.g., GridLAB-D, HOMER), please ensure they are installed and configured properly. However, this project primarily uses Python-based simulation.

## Contribution Guide

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact

For any questions or issues, please contact Ali Abdollahzadeh at [al.abdollahzadeh@gmail.com].
