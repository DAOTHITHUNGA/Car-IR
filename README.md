###Run this project at goole colab###

Clone the repo into goole drive (recommended direction: /MyDrive/Colab Notebooks/"Car-IR")    
    
RUN "Truy Vấn-IR.ipynb" file in google colab

    SET UP
        1.Mount drive: drive.mount("/content/drive")
        2.Install flask-ngrok: !pip install flask-ngrok

    RUN SERVER

        1.Run server.py
        2.Waiting for a second
        3.Click the 2nd link to open web app (http://****.ngrok.io)

    SET UP NEW DATASET

        1.Copy new dataset into "./static/img" folder
        2.run offline.py
        3.rerun server.py
LINK DATASET:
https://drive.google.com/drive/folders/118gKytVYY3RO7JpxK34hF_pW0wlQ0ePJ?usp=sharing
