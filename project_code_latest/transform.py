import json
import pandas as pd
import numpy as np
out = pd.read_csv('outs/taiwan/new_taiwan.csv')
# mat = json.load('homo_matrix/mat.json')


mat_path = 'homo_matrix/mat.json'
with open(mat_path) as f:
    data = json.load(f)
homo_matrix = np.array(data['mat']).reshape((3,3))

# center=[]
# center.append(1)
# center = np.array(center).reshape((3,1))
# transformed_center = np.matmul(homo_matrix, center)
# transformed_center = np.divide(transformed_center[:2], transformed_center[2]).astype(int)
center = {}
center["center"] = []
for row in out.itertuples():
    # cen_x = int(row.x + 0.5*row.w)
    # cen_y = int(row.y + 0.5*row.h)
    cen_x = int(row.x)
    cen_y = int(row.y)
    cen = [cen_x, cen_y]
    cen.append(1)
    cen = np.array(cen).reshape((3,1))
    
    transformed_center = np.matmul(homo_matrix, cen)
    transformed_center = np.divide(transformed_center[:2], transformed_center[2]).astype(int)

    tmp = {}
    # print(transformed_center[0][0],transformed_center[1][0])
    tmp["pt"] = [transformed_center[0][0].tolist(),transformed_center[1][0].tolist()]
    tmp["tag"] = int(row.tag)
    tmp["fid"] = int(row.fid)
    center["center"].append(tmp)

with open('final.json','w') as f:
    json.dump(center,f)
