from threading import Thread


class MyThread(Thread):

    def run(self):
        print('Inside my thread class')


def execute():
    print('Execute ..')


for i in range(3):
    t = MyThread(target=execute())
    t.start()
