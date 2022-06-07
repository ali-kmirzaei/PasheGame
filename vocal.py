from playsound import playsound
from random import randint
from multiprocessing import Process

path = 'vocals/'

def sprocess(arg):
    P = Process(target=playsound, args=(arg,))
    P.start()  


def comming():
    i = str(randint(1, 2))
    name = 'bedebezanim'+i+'.mp3'
    sprocess(path+name)

def correlation():
    # print('correlation')
    name = 'gish.wav'
    sprocess(path+name)

def escape():
    i = randint(1, 4)
    if i > 2 :
        name = 'sefti.mp3'
    else:
        name = 'bedebezanim'+str(i)+'.mp3'
    sprocess(path+name)
