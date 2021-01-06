import pandas as pd
import itertools
import makeProbs as prob

gdata = pd.read_csv("graph_data_bool.csv")
num_rows = gdata.shape[0]
gdata['Count'] = [1.0] * num_rows
gdata = gdata.groupby(['G','L','R','S','E', 'O', 'T']).count()
gdata['Count'] = [count/num_rows for count in gdata['Count']]
print(sum(gdata.iloc[(gdata.index.get_level_values('G') == False) & (gdata.index.get_level_values('L')==False)]['Count']))
# print(gdata)

parent_pool = []
for x in 'GLRSEOT':

    print("Current variable is " + x)
    print("Current parent pool:")
    print(parent_pool)
    print("Parent candidates:")
    for k in range(min(3, len(parent_pool))):
        for candidate_parents in itertools.combinations(parent_pool, k):
            # test for (conditional) independence here
            # x_prob = query(x is true)
            # depend_prob = query(x and y and z are true)
            # normal_prob = query(all vars before x(1 -> k - 1) are true)
            # if (x_prob / depend_prob) == (x_prob / normal_prob):
            #     then dependent
            print(candidate_parents)
    parent_pool.append(x)
    print()

