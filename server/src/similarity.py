from dtw import dtw
from .descriptors_extractor import extract_descriptors
from .db import songs


def find_most_sample(file_path):
    record_descriptors = extract_descriptors(file_path)
    print(record_descriptors.shape)

    distances = {}

    for song, ref_descriptors in songs.items():
        distance = dtw(ref_descriptors.T, record_descriptors.T).normalizedDistance

        distances[song] = distance  

    return min(distances, key=distances.get)
