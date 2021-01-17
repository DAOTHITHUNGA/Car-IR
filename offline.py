from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np
import pickle

if __name__ == '__main__':
    fe = FeatureExtractor()
    img_paths=[]
    features=[]
    for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        features.append(feature)
        img_paths.append(img_path)
    features = np.array(features)
    print(len(img_paths),len(features))
    img_paths_Pickle = open('./static/img_paths_Pickle', 'wb') 
    pickle.dump(img_paths, img_paths_Pickle)
    features_Pickle = open('./static/feature/features_Pickle', 'wb') 
    pickle.dump(features, features_Pickle)