import pandas as pd 
import numpy as np 
import os 


class LoadData:

    def __init__ (self, df):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = 'NASA_GISTEMP.data.csv'
        self.file_path = os.path.join(self.script_dir, self.filename)
        self.df = df
    
    def load_data (self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Successfully loaded the data!")
            
        
        except FileNotFoundError:
            print(f"ERROR: Could not find the file '{self.file_path}'.")
            print("Please check if the file is in the same folder as this script.")
        
        except Exception as e:
            print(f"An unexpected error has occured: {e}")
    
    def clean_data(self):
        if self.df is not None:
            if 'Date' in self.df.columns:
                self.df['Date'] = pd.to_datetime(self.df['Date'], format='mixed',
                                                dayfirst = False)
                self.df.set_index('Date', inplace = True)
            
            if 'GISTEMP' in self.df.columns:
                self.df['GISTEMP'] = pd.to_numeric(self.df['GISTEMP'], errors = 'coerce' )
                self.df.dropna(subset=['GISTEMP'], inplace = True)
            

    def remove_outliers(self):
        '''
        We group data values by month and check if they are an outlier
        compared to the same month in different years. 

        We use a seasonally-adjusted Z-score: 
        Z = (x - μ) /σ where x, μ, and σ  are values of that particular month.
        if |Z| > 3, then that value is considered a statistical outlier and
        the entire row will be removed
        '''
        if self.df is None:
            return None

        month_group = self.df.groupby(self.df.index.month)['GISTEMP']
        month_mean = month_group.transform('mean')
        month_std = month_group.transform('std')

        z_score = np.absolute((self.df['GISTEMP'] - month_mean)/month_std)

        outlier_mask = z_score >= 3
        removed_rows = self.df[outlier_mask]
        
        self.df = self.df[~outlier_mask] 
        
        print(f"\n Outlier Removal Report")
        if not removed_rows.empty:
            print(f"Removed {len(removed_rows)} statistical outliers:")
            for date, row in removed_rows.iterrows():
                print(f" > Date: {date.date()} | GISTEMP Anomaly: {row['GISTEMP']}°C")
        else:
            print("No outliers detected (all data points within 3 standard deviations).")

        return self.df
    

        
    
        
    