import os
import pandas as pd
import numpy as np
import cv2
from time import time
frame_to_lap_dict = dict()
# df = pd.DataFrame(columns=['id', 'frame', 'laplacian'])

def calc_frame_lap(path):
    global df
    # frame_count = 0
    ids = os.listdir(path)
    for i, d in enumerate(ids):
        print('\rid {} of {}'.format(i, len(ids)), end='')
        dir = os.path.join(path, d)
        for file_name in os.listdir(dir):
            img = cv2.imread(os.path.join(dir, file_name))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            lap = cv2.Laplacian(gray, cv2.CV_64F).var()
            frame_to_lap_dict[f'{d}/{file_name}'] = lap
            # frame_count += 1

if __name__ == '__main__':
    t1 = time()
    calc_frame_lap('./frames')
    df = pd.DataFrame(frame_to_lap_dict.items(), columns=['frame', 'laplacian'])
    df.to_csv('./frame_to_lap.csv')

    print('\n\ntime: ', time() - t1)

