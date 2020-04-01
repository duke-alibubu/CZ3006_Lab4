import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

traffic_data = pd.read_csv('data.csv',header = None)
# traffic_data = traffic_data[traffic_data[0] == "FLOW"]

# 1. Top 5 senders
top_5_senders = traffic_data[9].value_counts().nlargest(5)

# 2. Top 5 receivers
top_5_receivers = traffic_data[10].value_counts().nlargest(5)

# 3. Top 5 applications
top_5_applications = traffic_data[15].value_counts().nlargest(5)

# 4. Traffic intensity
traffic_intensity = traffic_data[17].sum()

# 5. Proportion of TCP and UDP packets (optional)
num_tcp = traffic_data[traffic_data[11] == 6][11].count()
num_udp = traffic_data[traffic_data[11] == 17][11].count()
num_total = traffic_data[11].count()
tcp_percentage = (num_tcp/num_total) * 100
udp_percentage = (num_udp/num_total) * 100

# 6. Top 5 communication pairs (optional)
top_5_communication_pairs = traffic_data.groupby([9, 10])[9].count().nlargest(5)

# 7. Visualizing the communication between different IP hosts. (optional)