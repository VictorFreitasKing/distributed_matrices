from multiprocessing import Process

p = Process(target=print, args=[1])

p.run()