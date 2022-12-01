from dtw import dtw
from .descriptors_extractor import extract_descriptors
from .db import songs
from .dtw import dtw_distance


def find_best_sample(file_path, dtw_implementation="dtw-python"):
    record_descriptors = extract_descriptors(file_path)

    distances = {}

    for song, ref_descriptors in songs.items():
        match dtw_implementation:
            case "custom":
                distance = dtw_distance(ref_descriptors.T, record_descriptors.T)
            case _:
                distance = dtw(ref_descriptors.T, record_descriptors.T).normalizedDistance

        distances[song] = distance  

    return min(distances, key=distances.get)
