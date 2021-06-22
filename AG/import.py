import os
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### %matplotlib inline


user_name =os.environ.get("root")
password = os.environ.get('root')

connection = mysql.connector.connect(host='localhost',user = user_name,passwd = password,
db = 'statlog')
