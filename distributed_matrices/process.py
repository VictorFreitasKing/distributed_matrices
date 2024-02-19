from multiprocessing import Process
import time

p = Process(target=print, args=[1])

p.run()