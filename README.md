# GISTEMP Analyzer

A Python tool to analyze NASA GISTEMP global temperature anomaly data. This project loads, cleans, and processes temperature anomaly records, removes statistical outliers, and generates monthly summaries including mean anomaly, trend slopes, decadal rise, and correlation. Users can also visualize the anomalies in a simple bar chart.

The project leverages **Pandas** and **NumPy** for data manipulation and analysis, and optionally **Matplotlib** for data visualization.

NASA GISTEMP data was retrieved from: https://psl.noaa.gov/data/timeseries/month/DS/NASAGLBLT/

## Features
- Load and clean GISTEMP CSV data
- Remove seasonal outliers
- Compute monthly statistics:
  - Mean Anomaly
  - Trend Slope
  - Decadal Rise
  - Correlation
- Visualize monthly mean anomalies with Matplotlib

## Dependencies
This project requires the following Python packages:
- **Pandas** – for data loading, cleaning, and manipulation
- **NumPy** – for numerical calculations
- **Matplotlib** – for plotting and visualization of data

### Check if you have the dependencies
Open a terminal or Anaconda Prompt and run:

```pip list```

or

`conda list`

If `pandas`, `numpy`, and `matplotlib` are listed, you’re ready to go.

### Install dependencies
Using Conda (recommended):
```
conda create -n gistemp python=3.11
conda activate gistemp
conda install pandas numpy matplotlib
```
Using Pip:

`pip install pandas numpy matplotlib`

## Installation
1. Clone the repository:

```
git clone https://github.com/ansonnchan/GISTEMP-analyzer.git
cd GISTEMP-analyzer
```

2. Ensure `NASA_GISTEMP.data.csv` is in the project folder.

3. Run the main script:

`python main.py`

This will display the monthly summary in the console and optionally generate a bar chart of mean anomalies.


