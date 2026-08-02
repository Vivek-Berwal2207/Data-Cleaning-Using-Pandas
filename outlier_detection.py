import numpy as np
import pandas as pd
scores = pd.Series([72, 88, 65, 91, 78, 200, 84, -5, 70, 82])

#Method 1: Z-score  (flag values > 3 std deviations from mean)
z_scores = (scores - scores.mean()) / scores.std()
outliers_z = scores[abs(z_scores) > 2]
print('Z-score outliers:', outliers_z.values)    # [200  -5]