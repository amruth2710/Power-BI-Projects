# importing libraries
import pandas as pd
import glob
import os

# merging the files
joined_files = os.path.join("domestic_visitors", "domestic*.csv")
joined_files1 = os.path.join("foreign_visitors", "foreign*.csv")

# A list of all joined files is returned
joined_list = glob.glob(joined_files)
joined_list1 = glob.glob(joined_files1)

# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
df1 = pd.concat(map(pd.read_csv, joined_list1), ignore_index=True)
print(df)

# Export the DataFrame to csv
df.to_csv("domestic_combined.csv")
df1.to_csv("foreign_combined.csv")
