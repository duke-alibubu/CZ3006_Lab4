import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

traffic_data = pd.read_csv('SFlow_Data_lab4.csv',header = None)
traffic_data = traffic_data[traffic_data[0] == "FLOW"]

# 4A. Top 5 talkers and listeners
top_5_talkers = traffic_data[9].value_counts().nlargest(5)
print ("------------TOP 5 TALKERS------------")
print (top_5_talkers)      # print out top 5 talkers
print ("-------------------------------------")


top_5_listeners = traffic_data[10].value_counts().nlargest(5)
print ("------------TOP 5 LISTENERS------------")
print (top_5_listeners)    # print out top 5 listeners
print ("-------------------------------------")

# 4B. Transport Protocol
all_transport_protocol = traffic_data[11].value_counts()
num_tcp = float(traffic_data[traffic_data[11] == 6][11].count())
num_udp = float(traffic_data[traffic_data[11] == 17][11].count())
num_total = float(traffic_data[11].count())
tcp_percentage = num_tcp * 100/num_total 
udp_percentage = num_udp * 100/num_total

print ("------------ALL TRANSPORT PROTOCOLS------------")
print (all_transport_protocol)      # print out all transport protocols and number of packets belonged to it
print ("------------TCP PERCENTAGE------------")
print (tcp_percentage)              # print out the proportion of packet that use TCP
print ("------------UDP PERCENTAGE------------")
print (udp_percentage)              # print out the proportion of packet that use UDP
print ("-------------------------------------")

# 4C. Applications Protocol
top_5_applications = traffic_data[15].value_counts().nlargest(5)
print ("------------TOP 5 APPLICATION PROTOCOLS------------")
print (top_5_applications)          # print out top 5 used application protocols
print ("-------------------------------------")

# 4D. Traffic
total_traffic = float(traffic_data[18].sum()) / math.pow(2, 20)
print ("------------TOTAL TRAFFIC------------")
print (total_traffic)               # print out total traffic  
print ("-------------------------------------")

# 4E. Additional analysis - Top 5 communication pairs
top_5_communication_pairs = traffic_data.groupby([9, 10])[9].count().nlargest(5)
print ("------------TOP 5 COMMUNICATION PAIRS------------")
print (top_5_communication_pairs)          # print out top 5 used application protocols
print ("-------------------------------------")