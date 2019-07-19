import os
import zipfile
import pandas as pd

def zipdir(root ,df , ziph):
    for id, frame in zip(df['id'], df['frame']):
        path = os.path.join(root, id, frame)
        if os.path.exists(path):
            ziph.write(path)

if __name__ == '__main__':
    df = pd.read_csv('./good_samples.csv')[:10]
    zipf = zipfile.ZipFile('sampled_data.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./frames',df, zipf)
    zipf.close()