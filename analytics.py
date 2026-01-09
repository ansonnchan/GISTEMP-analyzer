import numpy as np
import pandas as pd

class Analytics:
    def __init__(self, df):
        self.df = df

    def get_monthly_summary(self):

        results = []
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for m in range(1, 13):
            month_data = self.df[self.df.index.month == m]
            years = month_data.index.year.to_numpy()
            temps = month_data['GISTEMP'].to_numpy()

            mean_val = np.mean(temps)
    
            slope, _ = np.polyfit(years, temps, 1)
            correlation = np.corrcoef(years, temps)[0, 1]

            results.append({
                'Month': month_names[m-1],
                'Mean_Anomaly': mean_val,         
                'Trend_Slope': slope,            
                'Decadal_Rise_C': slope * 10,    
                'Correlation': correlation
            })

        
        summary_df = pd.DataFrame(results)
        summary_df.set_index('Month', inplace=True)
        
        return summary_df