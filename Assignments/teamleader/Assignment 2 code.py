#A python code assume you get temperature and humidity values generated with random function to a variable and write a condition to continuously detect alarm in case of high temperature
def temp_sensor(name):
    k=True
    print("PRESS ctrl+c SWITCH OFF THE ALARM ")
    while k==True:    
        import random
        import time
        temperature=random.uniform(35,90)
        print (f"The current temperature is {temperature:.2f}°C")
        humidity=random.randint(30,100)
        print(f"Humidity is {humidity}%")
        if temperature>60:
            print(f"🚨🚨 BEEP!!!!BEEP!!!!BEEP!!!!🚨🚨\n The temperature has exceeded to {temperature:.2f}°C \n press BREAK to stop the alarm")
        while temperature>60:
            k=str(input())
            k=k.upper()
            if k=="BREAK" :
                break
            else:
                print('''Uh-oh I guess you've used wrong word kindly type "BREAK" to stop the alarm ''')
                continue
            break

        if temperature>60:
            print("The alarm has been switched off successfully")
        else:
            print("The temperature is normal")
        time.sleep(7)
        k=True

name=str(input("ENTER YOUR USERNAME: "))
print("\tASSIGNMENT 2 - DETECTING ALARM IN CASE OF HIGH TEMPERATURE")
temp_sensor(name)
