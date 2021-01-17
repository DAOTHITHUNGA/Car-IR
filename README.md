ĐỒ ÁN TRUY VẤN ĐA PHƯƠNG TIỆN

    Sinh viên thực hiện
    Đào Thị Thu Nga 18521135
    Nguyễn Khánh Toàn 18521509
Link slide báo cáo: https://docs.google.com/presentation/d/1TvNVV9LOqzLWyRgsVkUVMf7Wa7kspsIE5MTLsd3ZPGY/edit?usp=sharing


###Run this project at google colab###

Clone the repo into goole drive (recommended direction: /MyDrive/Colab Notebooks/Car-IR)    
    
RUN "Truy Vấn-IR.ipynb" file in google colab

![image](https://user-images.githubusercontent.com/61963734/104850612-aa8c1780-5922-11eb-9b41-e3d64d21868c.png)

Connect to a Runtime with GPU

    SET UP
        1.Mount drive: drive.mount("/content/drive")
        2.Install flask-ngrok: !pip install flask-ngrok

    RUN SERVER

        1.Run server.py
        2.Waiting for a second
        3.Click the 2nd link to open the web app (http://****.ngrok.io)
![image](https://user-images.githubusercontent.com/61963734/104850763-9268c800-5923-11eb-9b0b-cba1035ead8b.png)
![image](https://user-images.githubusercontent.com/61963734/104850986-c690b880-5924-11eb-8a41-c337c2f19e5b.png)
![image](https://user-images.githubusercontent.com/61963734/104851038-0a83bd80-5925-11eb-8d9f-5844cd2fdf63.png)
![image](https://user-images.githubusercontent.com/61963734/104851074-4c146880-5925-11eb-9f7b-b17d4c82369d.png)
![image](https://user-images.githubusercontent.com/61963734/104851143-c93fdd80-5925-11eb-96c5-0d7d07a0de38.png)

    SET UP NEW DATASET

        1.Copy new dataset into "./static/img" folder
        2.run offline.py
        3.rerun server.py

LINK DATASET:
https://drive.google.com/drive/folders/118gKytVYY3RO7JpxK34hF_pW0wlQ0ePJ?usp=sharing
