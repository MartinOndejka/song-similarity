import librosa
import numpy as np


def extract_descriptors(file_path):
    y, sr = librosa.load(file_path)
    descriptors = librosa.feature.chroma_cqt(y=y, sr=sr)
    return descriptors
