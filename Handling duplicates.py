

import pandas as pd 

retail = pd.read_csv("C:/Users/hp/Desktop/DataSets/OnlineRetail.csv",header= 0, encoding= 'unicode_escape')

retail.info()   #For data types and non or null values
# data has no na or nall values 

retail.describe() # for mean ,min, max, IQR 


# check for count of NA'sin each column
retail.isna().sum()
retail.isnull().sum()

# for Mean,Meadian,Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer
import numpy as np
# Mode Imputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
retail["CustomerID"] = pd.DataFrame(mode_imputer.fit_transform(retail[["CustomerID"]]))
retail["Description"] = pd.DataFrame(mode_imputer.fit_transform(retail[["Description"]]))

retail.isnull().sum() 

retail.dtypes

#type casting
# Now we will convert 'float64' into 'int64' type. 

retail.UnitPrice = retail.UnitPrice.astype('int64')

retail.CustomerID = retail.CustomerID.astype('int64')

retail.dtypes
retail.nunique()

#Identify duplicates records in the data
duplicate = retail.duplicated()
sum(duplicate)

#Removing Duplicates
retail1 = retail.drop_duplicates() 


retail1.dtypes
retail1.dtypes
retail1.nunique()
 
########## EDA     

#1st moment of business decision 
#measure  of central tendency
#mean
retail1.Quantity.mean()
retail1.UnitPrice.mean()
#median
retail1.Quantity.median()
retail1.UnitPrice.median()

#2nd moment of business decision
#measure of dispersion

#variance
retail1.Quantity.var()
retail1.UnitPrice.var()
#standard deviation 
retail1.Quantity.std()
retail1.UnitPrice.std()
#Range 
range_Quantity = max(retail1.Quantity) - min(retail1.Quantity) 
range_Quantity

range_UnitPrice = max(retail1.UnitPrice)-min(retail1.UnitPrice)
range_UnitPrice


#3rd moment of business decision #skewness

retail1.Quantity.skew()
retail1.UnitPrice.skew()

#4th moment of business decision #kurtosis peakness of dataset 

retail1.Quantity.kurt()
retail1.UnitPrice.kurt() 
      
retail1.dtypes

retail.columns

boxplot = retail1.boxplot(column= [ 'Quantity','UnitPrice', 'CustomerID'])

# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(retail1.iloc[:, :])
