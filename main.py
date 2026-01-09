from dataclean import LoadData
from analytics import Analytics
import matplotlib.pyplot as plt 

if __name__ == "__main__":
    loader = LoadData(None) 
    loader.load_data()
    loader.clean_data()
    loader.remove_outliers()


    analysis = Analytics(loader.df)

    monthly_report = analysis.get_monthly_summary()
    
    print("\n--- FINAL NASA GISTEMP REPORT ---")
    print(monthly_report[['Mean_Anomaly', 'Trend_Slope', 'Decadal_Rise_C', 'Correlation']])
    
    print("\n")
    
    print("Mean Anomaly: The average temperature deviation for each month relative to the 1951-1980 baseline.\n")
    print("Trend Slope: The yearly rate of change in the anomaly (positive values indicate warming).\n")
    print("Decadal Rise (°C): The predicted increase in temperature over a 10-year period based on current trends.\n")
    print("Correlation: Measures the strength of the relationship between Time and Warming (1.0 is a perfect match).\n")

    monthly_report['Mean_Anomaly'].plot(kind='bar', figsize=(10,5), color='skyblue')
    plt.ylabel("Mean Anomaly (°C)")
    plt.title("Monthly Mean GISTEMP Anomaly")
    plt.show()