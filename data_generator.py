import os
import cv2
from time import time
counter = 0
jump_steps = 50


def get_clip_spec(clip_path):
    cap = cv2.VideoCapture(clip_path)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fr =  cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fr, (width, height)

def scene_to_frames(scene_path:str, clips: list, frames_folder):
    global counter
    global jump_steps
    # convert all clips into frames. save frames in folder named 'frames' in scene directory
    # frames_folder = os.path.join(scene_path, 'frames')
    if not os.path.exists(frames_folder):
        os.mkdir(frames_folder)
    for c in clips:
        cap = cv2.VideoCapture(os.path.join(scene_path, c))
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if counter % jump_steps == 0:
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # lap = cv2.Laplacian(gray, cv2.CV_64F).var()
                # file_name = '{}__{}.jpg'.format(counter // jump_steps, lap)
                file_name = '{}.jpeg'.format(counter // jump_steps)
                cv2.imwrite(os.path.join(frames_folder, file_name), frame)
            counter += 1
        cap.release()


def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main():
    frames_folder = './frames'
    create_dir_if_not_exists(frames_folder)
    frames_folder = os.path.abspath(frames_folder)
    data_path = './voxcelab/'
    ids = os.listdir(os.path.abspath(data_path))
    for i, id in enumerate(ids):
        counter = 0 # frame counter in one id
        create_dir_if_not_exists(os.path.join(frames_folder, id))
        id_path = os.path.join(data_path, id)
        scenes = os.listdir(id_path)
        for s, scene in enumerate(scenes):
            scene_path = os.path.join(id_path, scene)
            print("\r id {0} of {1}, scene {2} of {3}  ".format(i+1, len(ids), s+1, len(scenes)), end='')
            clips = os.listdir(scene_path)
            scene_to_frames(scene_path, clips, os.path.join(frames_folder, id))
            


if __name__ == "__main__":
    t1 = time()
    main()
    print('\n\ntime: ', time() - t1)