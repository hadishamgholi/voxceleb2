import os
import zipfile

count = 3

def zipdir(path, ziph):
    global count
# ziph is zipfile handle
    for d in os.listdir(path):
        dir = os.path.join(path, d)
        if count <= 0:
            break
        count -= 1
        for file_name in os.listdir(dir):
            ziph.write(os.path.join(dir, file_name))

if __name__ == '__main__':
    
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)

    zipdir('./framess', zipf)

    zipf.close()