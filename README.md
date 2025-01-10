# Smart Grid Simulation Project

## Project Overview

This project is part of the ICT4SM course at Politecnico di Torino. It focusWes on capacity planning and optimization of photovoltaic (PV) systems and battery storage for a smart grid household energy management system. The goal is to reduce costs, improve energy self-sufficiency, and optimize financial returns through efficient solar energy usage.

## Group Members
- **Ali Abdollahzadeh** ([@ali-abdollahzadeh](https://github.com/ali-abdollahzadeh))
- **Arezou Shadkam**
- **Kiyana Sabet**

## Project Objectives
The project aims to answer three key questions:
1. How can a household use solar energy to meet its energy demand?
2. What is the optimal size for a solar panel system and battery storage to minimize costs?
3. How long will it take to recover the investment and start making savings?

## Methodology
The project followed a structured approach:
1. Data collection from sources like GSE, PVGIS, and Statista.
2. Simulation of energy demand using a custom Gym environment to model household consumption patterns.
3. Calculation of energy surplus and deficit by comparing solar generation with household demand.
4. Optimization of PV system size and battery storage.
5. Cost analysis, including ROI and payback period calculations.
6. Visualization of results through heatmaps and plots.

## Folder Structure
- **data/**: Contains all the necessary datasets for the simulation.
  - `electricity_prices.csv`: Electricity price data.
  - `energy_demand.csv`: Energy demand data.
  - `investment_costs.csv`: Cost of PV systems and batteries.
  - `solar_generation.csv`: Solar generation data.
  - **processed/**: Folder for processed datasets.

- **Docs/**: Contains project documentation.
  - `project_info.pdf`: Detailed project report.

- **plots/**: Contains generated visualizations.
  - `hourly_energy_demand.png`: Hourly energy demand plot.
  - `hourly_solar_generation.png`: Hourly solar generation plot.
  - `hourly_surplus_deficit.png`: Hourly surplus/deficit plot.
  - `payback_period_heatmap.png`: Payback period heatmap.
  - `roi_heatmap.png`: Return on investment (ROI) heatmap.

- **Scripts/**: Contains all Python scripts used for data processing, simulation, and visualization.
  - `main.py`: Main script to run the simulation.
  - `clean_data.py`: Cleans and processes raw datasets.
  - `energy_demand_simulation.py`: Simulates energy demand.
  - `optimize_pv_system.py`: Optimizes PV system size.
  - `optimize_battery_storage.py`: Optimizes battery storage levels.
  - `visualize_data.py`: Generates plots.

## Results Summary
### Key Insights:
- The optimal combination is a **10-15 kW PV system** with a **750-1,000 kWh battery**.
- This configuration provides:
  - A short payback period (20-23 years).
  - High ROI (~35-40%).
  - Significant grid dependency reduction.

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


## Contribution Guide

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact

For any questions or issues, please contact Ali Abdollahzadeh at [al.abdollahzadeh@gmail.com].
