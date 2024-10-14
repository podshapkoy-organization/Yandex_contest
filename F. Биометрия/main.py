import os
import numpy as np
import pandas as pd
import librosa
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

train_folder = "train/"
test_folder = "test/"
train_labels = pd.read_csv("train/targets.tsv", sep='\t', header=None, names=['file', 'gender'])


def extract_features(file_path, n_mfcc=13):
    y, sr = librosa.load(file_path, sr=None)

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfcc.T, axis=0)
    mfcc_std = np.std(mfcc.T, axis=0)

    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = np.mean(chroma.T, axis=0)

    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_mean = np.mean(mel.T, axis=0)

    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_mean = np.mean(zcr)

    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_centroid_mean = np.mean(spectral_centroid)

    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    spectral_bandwidth_mean = np.mean(spectral_bandwidth)

    return np.hstack(
        [mfcc_mean, mfcc_std, chroma_mean, mel_mean, zcr_mean, spectral_centroid_mean, spectral_bandwidth_mean])


X = []
y = []
for index, row in train_labels.iterrows():
    file_path = os.path.join(train_folder, row['file'] + ".wav")
    features = extract_features(file_path)
    X.append(features)
    y.append(row['gender'])

X = np.array(X)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

xgb_clf = XGBClassifier(n_estimators=500, max_depth=6, learning_rate=0.01, random_state=42)
rf_clf = RandomForestClassifier(n_estimators=500, random_state=42)
svm_clf = SVC(probability=True, random_state=42)

ensemble_clf = VotingClassifier(estimators=[
    ('xgb', xgb_clf),
    ('rf', rf_clf),
    ('svm', svm_clf)
], voting='soft')

ensemble_clf.fit(X_train, y_train)
y_pred = ensemble_clf.predict(X_valid)
print("Accuracy:", accuracy_score(y_valid, y_pred))

test_files = [f.replace(".wav", "") for f in os.listdir(test_folder) if f.endswith(".wav")]
X_test = []
for file in test_files:
    file_path = os.path.join(test_folder, file + ".wav")
    features = extract_features(file_path)
    X_test.append(features)
X_test = np.array(X_test)
X_test = scaler.transform(X_test)
y_test_pred = ensemble_clf.predict(X_test)

results = pd.DataFrame({'file': test_files, 'gender': y_test_pred})
results.to_csv("answers.tsv", sep='\t', header=False, index=False)
