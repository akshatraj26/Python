import threading


class SquareGeneratorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Launching...")


th = SquareGeneratorThread()
th.start()
print(dir(th))

print('Dict:', vars(th))