########## Final Exam - Yellow Taxi

import pandas as pd

### 2019 (Pre-Covid)
# Read in csv file
YTPC = pd.read_csv("yellow_tripdata_2019-06.csv")

YTPC.dtypes

# Converting Time format
YTPC[['tpep_pickup_datetime','tpep_dropoff_datetime','store_and_fwd_flag']].dtypes

YTPC['pickup'] = pd.to_datetime(YTPC['tpep_pickup_datetime'],
                              infer_datetime_format=True)

del YTPC['tpep_pickup_datetime']

YTPC['dropoff'] = pd.to_datetime(YTPC['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del YTPC['tpep_dropoff_datetime']

YTPC['duration'] = YTPC['dropoff'] - YTPC['pickup']

YTPC[['pickup','dropoff','duration']].head()

del YTPC['store_and_fwd_flag']


## Eliminate Outlier Observations
# trip_distance <= 100
YTPC['valid'] = YTPC['trip_distance'] <= 100

YTPC = YTPC[YTPC.valid == True]

YTPC['trip_distance'].describe()


# delete any rows where passengers = 0 
YTPC['valid'] = YTPC['passenger_count'] > 0

YTPC = YTPC[YTPC.valid == True]

YTPC['passenger_count'].describe()


# delete trip distance = 0
YTPC['valid'] = YTPC['trip_distance'] != 0

YTPC = YTPC[YTPC.valid == True]

YTPC['trip_distance'].describe()


# keep only rows where "extra" >= 0
YTPC['valid'] = YTPC['extra'] >= 0

YTPC = YTPC[YTPC.valid == True]

YTPC['extra'].describe()


# for total_amount, keep only rows where it is greater than zero but less than 1,000
YTPC['valid'] = YTPC['total_amount'] > 0

YTPC = YTPC[YTPC.valid == True]

YTPC['valid'] = YTPC['total_amount'] <1000

YTPC = YTPC[YTPC.valid == True]

YTPC['total_amount'].describe()

YTPC.describe()

YTPC.to_csv('Yellow_PreCovid_Saved.csv', index = False)




### 2020 (After-Covid)
# Read in csv file
YTAC = pd.read_csv("yellow_tripdata_2020-06.csv")

YTAC.dtypes

# Converting Time format
YTAC[['tpep_pickup_datetime','tpep_dropoff_datetime','store_and_fwd_flag']].dtypes

YTAC['pickup'] = pd.to_datetime(YTAC['tpep_pickup_datetime'],
                              infer_datetime_format=True)

del YTAC['tpep_pickup_datetime']

YTAC['dropoff'] = pd.to_datetime(YTAC['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del YTAC['tpep_dropoff_datetime']

YTAC['duration'] = YTAC['dropoff'] - YTAC['pickup']

YTAC[['pickup','dropoff','duration']].head()

del YTAC['store_and_fwd_flag']



## Eliminate Outlier Observations
# trip_distance <= 100
YTAC['valid'] = YTAC['trip_distance'] <= 100

YTAC = YTAC[YTAC.valid == True]

YTAC['trip_distance'].describe()


# delete any rows where passengers = 0 
YTAC['valid'] = YTAC['passenger_count'] > 0

YTAC = YTAC[YTAC.valid == True]

YTAC['passenger_count'].describe()

# delete trip distance = 0
YTAC['valid'] = YTAC['trip_distance'] != 0

YTAC = YTAC[YTAC.valid == True]

YTAC['trip_distance'].describe()

# for total_amount, keep only rows where it is > 0 but < 1,000
YTAC['valid'] = YTAC['total_amount'] > 0

YTAC = YTAC[YTAC.valid == True]

YTAC['valid'] = YTAC['total_amount'] <1000

YTAC = YTAC[YTAC.valid == True]

YTAC['total_amount'].describe()

# keep only rows where "extra" >= 0
YTAC['valid'] = YTAC['extra'] >= 0

YTAC = YTAC[YTAC.valid == True]

YTAC['extra'].describe()
YTAC.describe()

YTAC.to_csv('Yellow_AfterCovid_Saved.csv', index = False)


### Comparisson between 2019 & 2020 Averages
import statistics 

# Distance
print("2019 vs 2020 Avg Distance Dec = ",(statistics.mean(YTPC['trip_distance'])-statistics.mean(YTAC['trip_distance'])))
                                                  
# Amount
print("2019 vs 2020 Average Fare Dec = ",(statistics.mean(YTPC['total_amount'])-statistics.mean(YTAC['total_amount'])))

# Duration
print("2019 vs 2020 Avg Duration Dec = ",(statistics.mean(YTPC['duration'])-statistics.mean(YTAC['duration'])))
          

                  


