import pandas as pd
import matplotlib.pyplot as plt

# Load the data
kmb_path = "results/kmb.csv"
og_path = "results/og.csv"
kmb = pd.read_csv(kmb_path)
og = pd.read_csv(og_path)
kmb_seq = pd.read_csv('results/kmb_seq_10.csv')
kmb_parallel = pd.read_csv('results/kmb_parallel_10.csv')


plt.figure(figsize=(10, 6))

# plt.plot(kmb['instance'], kmb['value'], color='blue', label='KMB')

# plt.plot(og['instance'], og['value'], color='green', label='OG')

# plt.title('Value Comparison between KMB and OG')
# plt.xlabel('Instance (ID)')
# plt.ylabel('Value')
# plt.grid(True)
# plt.legend()

# plt.show()


# plt.plot(kmb['instance'], kmb['time'], color='blue', label='KMB')

# plt.plot(og['instance'], og['time'], color='green', label='OG')

# plt.title('Value Comparison between KMB and OG')
# plt.xlabel('Instance (ID)')
# plt.ylabel('Time')
# plt.grid(True)
# plt.legend()

# plt.show()




# plt.plot(kmb_seq['instance'], kmb_seq['time'], color='blue', label='KMB Seq')

# plt.plot(kmb_parallel['instance'], kmb_parallel['time'], color='green', label='KMB Parallel')

# plt.title('Value Comparison between KMB Seq and Parallel')
# plt.xlabel('Instance (ID)')
# plt.ylabel('Time')
# plt.grid(True)
# plt.legend()

# plt.show()