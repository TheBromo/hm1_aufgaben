# Verschiedene Scatterplots
import pandas as pd

# Scatterplot gleichsinniger Zusammenhang
df1 = pd.DataFrame({'x': [-1, -3, 4 ,1-2, 5, 11, -4, 4, -5, -12, 0, 8],

                    'y': [-12, 3, -12,0,-13,13,-1,2,2,-5,4,0]})
df = pd.concat([df1], axis=1)

r_xy_p = df.corr()
print(r_xy_p)

r_xy_s = df.corr(method='spearman')
print(r_xy_s)