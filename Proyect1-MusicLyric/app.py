import time
from threading import Thread, Lock
import sys

lock = Lock()

def texto(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def letra_cancion(Letra, delay, speed):
    time.sleep(delay)
    texto(Letra, speed)

def cantar():
    letras = [
        ("'Cause you make me feel like", 0.05),
        ("I've been locked out of heaven", 0.05),
        ("For too long, for too long", 0.16),
        ("Yeah, you make me feel like", 0.05),
        ("I've been locked out of heaven", 0.05),
        ("For too long, for too long, oh, oh", 0.2),
        ("Whoa, whoa, whoa, yeah, yeah, yeah", 0.15),
        ("Can I just stay here?", 0.05),
        ("Spend the rest of my days here?", 0.1),
    ]
    delays = [0.3, 3.0, 7.0, 13.0, 17.3, 20.0, 28.0, 33.2, 36.5]


    threads = []
    for i in range(len(letras)):
        letra, speed = letras[i]
        t = Thread(target=letra_cancion, args=(letra, delays[i], speed))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

cantar()
