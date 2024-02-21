import p2
from multiprocessing import Process

if __name__ == '__main__':
    freeze_support()
    Process(target=p2).start()