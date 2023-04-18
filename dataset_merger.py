import pandas as pd

# Read the first Excel file
df1 = pd.read_excel("softball_posts.xlsx")

# Read the second Excel file
df2 = pd.read_excel("softball_profile.xlsx")

# Merge the two DataFrames on 'ownerUsername' and 'username'
merged_df = pd.merge(df1, df2, left_on='ownerUsername', right_on='username')

# Save the merged DataFrame to a new Excel file
merged_df.to_excel("softball_dataset.xlsx", index=False)