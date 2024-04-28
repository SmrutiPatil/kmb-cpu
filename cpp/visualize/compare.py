import pandas as pd
import matplotlib.pyplot as plt

# Define file names
both_parallel = "bothParallel.csv"
inner_parallel = "innerParallel.csv"
outer_parallel = "outerParallel.csv"
sequential = "Sequential.csv"

# Read CSV files into pandas DataFrames
both_df = pd.read_csv(both_parallel)
inner_df = pd.read_csv(inner_parallel)
outer_df = pd.read_csv(outer_parallel)
sequential_df = pd.read_csv(sequential)

# Plot time vs instance for each file
plt.figure(figsize=(10, 6))

plt.plot(both_df['instance'], both_df['time'], label='Both Parallel')
plt.plot(inner_df['instance'], inner_df['time'], label='Inner Parallel')
plt.plot(outer_df['instance'], outer_df['time'], label='Outer Parallel')
plt.plot(sequential_df['instance'], sequential_df['time'], label='Sequential')

plt.xlabel('Instance')
plt.ylabel('Time')
plt.title('Time vs Instance')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('time_vs_instance.png')
# plt.show()


# Sort DataFrames by nodes and edges
both_df_nodes_sorted = both_df.sort_values(by='nodes')
inner_df_nodes_sorted = inner_df.sort_values(by='nodes')
outer_df_nodes_sorted = outer_df.sort_values(by='nodes')
sequential_df_nodes_sorted = sequential_df.sort_values(by='nodes')

both_df_edges_sorted = both_df.sort_values(by='edges')
inner_df_edges_sorted = inner_df.sort_values(by='edges')
outer_df_edges_sorted = outer_df.sort_values(by='edges')
sequential_df_edges_sorted = sequential_df.sort_values(by='edges')

# Plot time vs nodes for each file
plt.figure(figsize=(10, 6))

plt.plot(both_df_nodes_sorted['nodes'], both_df_nodes_sorted['time'], label='Both Parallel')
plt.plot(inner_df_nodes_sorted['nodes'], inner_df_nodes_sorted['time'], label='Inner Parallel')
plt.plot(outer_df_nodes_sorted['nodes'], outer_df_nodes_sorted['time'], label='Outer Parallel')
plt.plot(sequential_df_nodes_sorted['nodes'], sequential_df_nodes_sorted['time'], label='Sequential')

plt.xlabel('Nodes')
plt.ylabel('Time')
plt.title('Time vs Nodes')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('time_vs_nodes.png')
# plt.show()

# Plot time vs edges for each file
plt.figure(figsize=(10, 6))

plt.plot(both_df_edges_sorted['edges'], both_df_edges_sorted['time'], label='Both Parallel')
plt.plot(inner_df_edges_sorted['edges'], inner_df_edges_sorted['time'], label='Inner Parallel')
plt.plot(outer_df_edges_sorted['edges'], outer_df_edges_sorted['time'], label='Outer Parallel')
plt.plot(sequential_df_edges_sorted['edges'], sequential_df_edges_sorted['time'], label='Sequential')

plt.xlabel('Edges')
plt.ylabel('Time')
plt.title('Time vs Edges')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('time_vs_edges.png')
# plt.show()




# 4. Histograms
# plt.figure(figsize=(10, 6))
# plt.hist(both_df['time'], bins=20, alpha=0.5, label='Both Parallel')
# plt.hist(inner_df['time'], bins=20, alpha=0.5, label='Inner Parallel')
# plt.hist(outer_df['time'], bins=20, alpha=0.5, label='Outer Parallel')
# plt.hist(sequential_df['time'], bins=20, alpha=0.5, label='Sequential')
# plt.xlabel('Time')
# plt.ylabel('Frequency')
# plt.title('Histogram of Time')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('time_histogram.png')
# plt.show()

# 5. Scatterplots
plt.figure(figsize=(10, 6))
plt.scatter(both_df['nodes'], both_df['edges'], label='Both Parallel')
plt.scatter(inner_df['nodes'], inner_df['edges'], label='Inner Parallel')
plt.scatter(outer_df['nodes'], outer_df['edges'], label='Outer Parallel')
plt.scatter(sequential_df['nodes'], sequential_df['edges'], label='Sequential')
plt.xlabel('Nodes')
plt.ylabel('Edges')
plt.title('Scatterplot of Nodes vs Edges')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('scatterplot_nodes_vs_edges.png')
plt.show()

# # 6. Boxplots
# plt.figure(figsize=(10, 6))
# plt.boxplot([both_df['time'], inner_df['time'], outer_df['time'], sequential_df['time']], labels=['Both Parallel', 'Inner Parallel', 'Outer Parallel', 'Sequential'])
# plt.ylabel('Time')
# plt.title('Boxplot of Time by Algorithm')
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('boxplot_time_by_algorithm.png')
# plt.show()

# 7. Correlation Matrix
all_data = pd.concat([both_df, inner_df, outer_df, sequential_df])

# Drop non-numeric columns
numeric_data = all_data.drop(columns=['instance'])

# Calculate correlation matrix
correlation_matrix = numeric_data.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 6))
plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)
plt.colorbar()
plt.title('Correlation Matrix')
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation='vertical')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.show()


# # 8. Heatmaps
# plt.figure(figsize=(10, 6))
# plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
# plt.colorbar()
# plt.title('Heatmap of Correlation Matrix')
# plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation='vertical')
# plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
# plt.tight_layout()
# plt.savefig('heatmap_correlation_matrix.png')
# plt.show()

# # 9. Line Plots with Multiple Y-Axes
# fig, ax1 = plt.subplots(figsize=(10, 6))

# ax1.plot(both_df['instance'], both_df['time'], label='Both Parallel', color='tab:blue')
# ax1.set_xlabel('Instance')
# ax1.set_ylabel('Time', color='tab:blue')
# ax1.tick_params('y', colors='tab:blue')
# ax1.legend(loc='upper left')

# ax2 = ax1.twinx()
# ax2.plot(both_df['instance'], both_df['nodes'], label='Nodes', color='tab:red', linestyle='--')
# ax2.set_ylabel('Nodes', color='tab:red')
# ax2.tick_params('y', colors='tab:red')
# ax2.legend(loc='upper right')

# plt.title('Time vs Instance with Nodes')
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('time_vs_instance_with_nodes.png')
# plt.show()

# # 10. Time Series Analysis (Example: Time vs Instance)
# plt.figure(figsize=(10, 6))
# plt.plot(both_df['instance'], both_df['time'], label='Both Parallel')
# plt.xlabel('Instance')
# plt.ylabel('Time')
# plt.title('Time Series Analysis: Time vs Instance')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('time_series_time_vs_instance.png')
# plt.show()




