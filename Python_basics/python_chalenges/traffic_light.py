# I will try to design a scrip that emulatesa traffic light an its logic to control a data flux.


from tqdm import tqdm
import time

def traffic_light():

    while True:
        print("Red")
        time.sleep(5)

        print("Green")
        time.sleep(10)
   
        print("Yellow")
        time.sleep(2)

traffic_light()

for i in tqdm(range(10)):
    time.sleep(1)