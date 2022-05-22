import torch

def main():
    print('Hello')

if __name__ == '__main__':

    entrypoints = torch.hub.list('ultralytics/yolov5', force_reload=True)
    print(entrypoints)

    for weight in entrypoints[5:8]:
        model = torch.hub.load('ultralytics/yolov5', weight)
        print(f'[INFO] Success load {weight.upper()}')
