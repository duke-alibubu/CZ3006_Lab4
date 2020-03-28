import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

traffic_data = pd.read_csv('data.csv',header = None)

# 1. Top 5 senders
top_5_senders = traffic_data[9].value_counts().nlargest(5)

# 2. Top 5 receivers
top_5_receivers = traffic_data[10].value_counts().nlargest(5)

# 3. Top 5 applications
top_5_applications = traffic_data[15].value_counts().nlargest(5)

# 4. Traffic intensity

# 5. Proportion of TCP and UDP packets (optional)

# 6. Top 5 communication pairs (optional)
top_5_communication_pairs = traffic_data.groupby([9, 10])[9].count().nlargest(5)

# 7. Visualizing the communication between different IP hosts. (optional)
