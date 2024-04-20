import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,2,3,4,5],'B':[5,4,3,2,1]})

np.average(df.A)
np.mean(df.B)