import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

traffic_data = pd.read_csv('SFlow_Data_lab4.csv',header = None)
traffic_data = traffic_data[traffic_data[0] == "FLOW"]

# 1. Top 5 senders
top_5_senders = traffic_data[9].value_counts().nlargest(5)
# print (top_5_senders)

# 2. Top 5 receivers
top_5_receivers = traffic_data[10].value_counts().nlargest(5)
# print (top_5_receivers)

# 3. Top 5 applications
top_5_applications = traffic_data[15].value_counts().nlargest(5)
# print (top_5_applications)

# 4. Traffic intensity
traffic_intensity = float(traffic_data[18].sum()) / math.pow(2, 20)
print (traffic_intensity)

# 5. Proportion of TCP and UDP packets (optional)
transport_layer_protocol = traffic_data[11].value_counts()
num_tcp = float(traffic_data[traffic_data[11] == 6][11].count())
num_udp = float(traffic_data[traffic_data[11] == 17][11].count())
num_total = float(traffic_data[11].count())
tcp_percentage = num_tcp * 100/num_total 
udp_percentage = num_udp * 100/num_total

# print (transport_layer_protocol)
# print (tcp_percentage)
# print (udp_percentage)

# 6. Top 5 communication pairs (optional)
top_5_communication_pairs = traffic_data.groupby([9, 10])[9].count().nlargest(5)

# 7. Visualizing the communication between different IP hosts. (optional)