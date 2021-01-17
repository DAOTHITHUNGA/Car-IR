import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
#new
from flask_ngrok import run_with_ngrok
import pickle

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
# Read image features
fe = FeatureExtractor()

#TANDT
features = pickle.load(open('./static/feature/features_Pickle', 'rb'))
img_paths = pickle.load(open('./static/img_paths_Pickle', 'rb'))

#READ CAR INFO FILE
import pandas as pd
infos=pd.read_csv("./static/FINAL_TRAINDETAILS.csv")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']

        # Save query image
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        # Run search
        query = fe.extract(img)
        dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
        
        ids = np.argsort(dists)[:10]  # Top 10 results
        scores = [(dists[id], img_paths[id], (infos[infos["file name"] == str(img_paths[id]).split("/")[-1]])["car name"].values[0],(infos[infos["file name"] == str(img_paths[id]).split("/")[-1]])["link "].values[0]) for id in ids]        
        return render_template('index.html',
                               query_path=uploaded_img_path,
                               scores=scores)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run()
