import glob
from .descriptors_extractor import extract_descriptors


songs = {}

step = 428

def load_songs():
    print("Loading songs...")

    for file_name in glob.glob("../data/*"):
        song = file_name.split("/")[-1]
        print(f"Loading {song}")
        descriptors = extract_descriptors(file_name)

        i = 0
        while i < descriptors.shape[1]:
            songs[f"{song}_{i}"] = descriptors[:, i:i+step]
            i += int(step / 4)
    
    print("Songs loaded!")
