import pandas as pd
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
lap_thresh = 50
n_blurs = 25
n_nblurs = 5

df = pd.read_csv('/home/hadi/Documents/python/face-verification-proj/frame_to_lap.csv')

df['id'] = df['frame'].str[:7]
df['frame'] = df['frame'].str[8:]

df_res = pd.DataFrame(columns=list(df.columns.values))


# df_blur = df[df['laplacian'] <= lap_thresh]
# df_not_blur = df[df['laplacian'] > lap_thresh]

uniq_ids = pd.unique(df['id'])

for i, id in enumerate(uniq_ids):
    print(f'\r{i}/{len(uniq_ids)}', end='')
    df_id = df[df['id'] == id]
    df_id_blur = shuffle(df_id[df_id['laplacian'] <= lap_thresh]).reset_index(drop=True)
    df_id_notblur = shuffle(df_id[df_id['laplacian'] > lap_thresh]).reset_index(drop=True)
    
    blur_num = min([n_blurs, len(df_id_blur)])
    nblur_num = max([n_nblurs, blur_num])

    df_res = df_res.append(df_id_blur[:blur_num])
    df_res = df_res.append(df_id_notblur[:nblur_num])


df_res.to_csv('./good_samples.csv')



    
# df_blur = df[df['laplacian'] <= lap_thresh]

# frames_in_ids_dict = dict()
# size = len(df_blur)//100
# for i in range(size):
#     print('\rid {} of {}'.format(i, size), end='')
#     s = df_blur.iloc[i][1]
#     id = s[:7]
#     if id in frames_in_ids_dict:
#         frames_in_ids_dict[id] += 1
#     else:
#         frames_in_ids_dict[id] = 1

# print()
# plt.bar(frames_in_ids_dict.keys(), frames_in_ids_dict.values(), 1, color='b')
# plt.xticks(rotation=90, fontsize=6)
# plt.savefig('bar.png')