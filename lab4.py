import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

traffic_data = pd.read_csv('data.csv',header = None)

# 1. Top 5 senders
print traffic_data[9].value_counts().nlargest(5)