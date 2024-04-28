import pandas as pd

# Read CSV files into pandas DataFrames
both_df = pd.read_csv("bothParallel.csv")
inner_df = pd.read_csv("innerParallel.csv")
outer_df = pd.read_csv("outerParallel.csv")
sequential_df = pd.read_csv("Sequential.csv")

# Calculate performance for each method
def calculate_performance(df):
    # Calculate w (weight) for each row
    w = df['edges'] * df['nodes'] * (df['nodes']/df['terminals'] ** 2)
    # Calculate performance (p)
    df['performance'] = w * (df['value'] / df['time'])

# Calculate performance for each DataFrame
calculate_performance(both_df)
calculate_performance(inner_df)
calculate_performance(outer_df)
calculate_performance(sequential_df)

# Calculate the average performance across all methods
average_performance = (both_df['performance'].mean() + inner_df['performance'].mean() + outer_df['performance'].mean() + sequential_df['performance'].mean()) / 4

# Calculate the ratio of each performance value to the average performance
both_ratio = both_df['performance'].mean() / average_performance
inner_ratio = inner_df['performance'].mean() / average_performance
outer_ratio = outer_df['performance'].mean() / average_performance
sequential_ratio = sequential_df['performance'].mean() / average_performance

# Create a DataFrame to store the ratios
ratio_data = {
    'Method': ['bothParallel', 'innerParallel', 'outerParallel', 'Sequential'],
    'Ratio_to_Average_Performance': [both_ratio, inner_ratio, outer_ratio, sequential_ratio]
}

# Convert the data to a DataFrame
ratio_df = pd.DataFrame(ratio_data)

# Save the DataFrame to a CSV file
ratio_df.to_csv("performance_ratios.csv", index=False)

print("performance_ratios.csv")
