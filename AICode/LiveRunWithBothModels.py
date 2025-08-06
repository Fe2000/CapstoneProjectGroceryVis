# Imports
import mariadb
import sys
import time
import datetime
import torch
from tensorflow import keras
import cv2
from PIL import Image, ImageOps
from matplotlib import pyplot as plt   
import cv2
import math
import sys
import numpy as np
import smtplib


import glob
import os

# Load Models
model = torch.hub.load('ultralytics/yolov5', 'custom', 'bestV5.pt')
modelCap = modelTest = keras.models.load_model('CapacityDetectionV8Binary')

feCount = 130

print('Start')

userId = 51

# Connect to DB
try:
    conn = mariadb.connect(
        user="testUser",
        password="password123",
        host="74.117.171.96",
        port=3306,
        database="groceryOfficial"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
print("Connection Good")

lastPre = []

swap = True

print("makeing camera")
cam = cv2.VideoCapture(0)
print("camera made")
while True:

    print(lastPre)

    print("Pic taken")
    print(str(feCount) + "THIS DA SPOT" )
   # list_of_files = glob.glob('/home/uafsadmin/Desktop/yolov5/runs/detect/exp22/crops/fe/*') # * means all if need specific format then *.csv
    latest_file = sorted(glob.iglob('/home/uafsadmin/Desktop/yolov5/runs/detect/exp27/crops/fe/*.jpg'), key=os.path.getctime)[-2]
    print("************************************" + latest_file)

    print('Pic FOUND imwrite')

    results = model(latest_file)

    results.crop()

    fe = results.pandas().xyxy[0]

    temp = []
    for x in fe['name']:
        temp.append(x)

    if lastPre == temp:

        print('same')

    else:

        #cur.execute("DELETE FROM user_ingredients WHERE u_id = (?)" , (userId,))
        cur.execute("DELETE w FROM user_ingredients w INNER JOIN ingredients e ON i_id=ing_id WHERE u_id=? AND is_detectable='T'", (userId,)) 
        print("found diff")
        lastPre = temp

        itemp = temp
        dReady = {x: itemp.count(x) for x in itemp}

        for t in dReady:
            predict = t

            if predict == 'Milk':
                fir = 1077

            elif predict == 'Container':

                fir = 8034
                results.crop(save_dir='tempCropSpot/tempF')

                newlat = latest_file[58: ]
                print(newlat)

                im = Image.open("tempCropSpot/tempF" + str(feCount)+ "/crops/Container/"+  newlat)

                feCount+= 1

                imResize = im.resize((300, 420), Image.ANTIALIAS)
                imResize.save("tempFolder/TempPic" +
                              '.jpg', 'JPEG', quality=90)

                image1 = np.asarray(
                    (Image.open("tempFolder/TempPic.jpg")), dtype='float32') / 255

                image1 = np.asarray(image1)
                image1 = image1.reshape(1, 300, 420, 3)

                result = modelCap.predict(image1)

                tClass = result.max()

                if tClass == result[0][0] and swap == True:

                    print('Low')

                   # cur.execute("SELECT user_email FROM users WHERE user_id=?", (userId,))
                    cur.execute("INSERT INTO user_notifications(u_id, notif_description, notif_item) VALUES (?, 'Your container is low! Run and restock your cereal', 'Milk')" , (userId,))

                    tempE = ''

                    # for user_email in cur: 
                    #         print(f"First name: {user_email}")
                    #         tempE = user_email

                    # print('Email Pulled')        
                    # print(tempE[0])
                    
                    gmail_user = 'fimpeldaegan@gmail.com'
                    gmail_password = 'hkwwarwyxpwpsjbi'
                    sent_from = gmail_user
                    to = ['dfimpe00@g.uafs.edu']
                    subject = 'GroceryVis'
                    body = 'consectetur adipiscing elit'

                    email_text = "Subject: GroceryVis \nRun and grab some more milk your container is low!"
                    (sent_from, ", ".join(to), subject, body)

                    try:
                        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        smtp_server.ehlo()
                        smtp_server.login(gmail_user, gmail_password)
                        smtp_server.sendmail(sent_from, to, email_text)
                        smtp_server.close()
                        print("Email sent successfully!")
                        swap = False
                    except Exception as ex:
                        print("Something went wrong….", ex)

                elif tClass == result[0][1]:

                    print('High')
                    swap = True

            elif predict == 'Peanut':
                fir = 16098

            elif predict == 'Eggs':
                fir = 1123

            elif predict == 'Noodles':
                fir = 6982

            elif predict == 'Apple':
                fir = 9003

            elif predict == 'Bread':
                fir = 18064

            ohH = str(dReady[t])
            print(predict + ": " + ohH)
            cur.execute("INSERT INTO user_ingredients (u_id,i_id,ing_name,on_hand) VALUES (?, ?,?,?)",(userId, fir, t,ohH ))
            conn.commit()
            print('commit')

    time.sleep(2)

conn.close()

print("close")