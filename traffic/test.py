import traffic
import os
cwd = os.getcwd()
data_dir = os.path.join(cwd, "gtsrb") 

traffic.load_data(data_dir)