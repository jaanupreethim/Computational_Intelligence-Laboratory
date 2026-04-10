import math
import random
import csv
from collections import Counter

def distance_metric(v1, v2, c):
    if c == 1:
        distance = sum((a - b) ** 2 for a, b in zip(v1, v2))
        return math.sqrt(distance)
    else:
        return sum(abs(a - b) for a, b in zip(v1, v2))

def find_min_maxs(data):
    if not data:
        return [], []
    num_cols = len(data[0])
    mins = [min(row[i] for row in data) for i in range(num_cols)]
    maxs = [max(row[i] for row in data) for i in range(num_cols)]
    return mins, maxs

def min_max_normalization(point, mins, maxs):
    normalized = []
    for i in range(len(point)):
        denom = maxs[i] - mins[i]
        normalized.append((point[i] - mins[i]) / denom if denom != 0 else 0)
    return normalized

def load_user_file(file_path):
    dataset = []
    feature_names = []
    all_labels = set()
    try:
        with open(file_path, 'r') as f:
            content = f.read(2048)
            f.seek(0)
            try:
                dialect = csv.Sniffer().sniff(content, delimiters=',\t ')
                reader = csv.reader(f, dialect)
            except csv.Error:
                print("Could not guess delimiter. Defaulting to comma (',').")
                reader = csv.reader(f, delimiter=',')
            rows = [row for row in reader if row]
            if not rows:
                print("Error: File is empty or could not be read.")
                return None, None, None, None, None, None
            header = rows[0]
            data_rows = rows[1:]
            print(f"\nFile loaded. Each row has {len(header)} columns.")
            print("Detected Header:", header)
            label_col = int(input("Which column index is the Label? (e.g., 1): "))
            remove_id = input("Is there an ID column to ignore? (y/n): ").lower()
            id_col = int(input("Which column index is the ID? (e.g., 0): ")) if remove_id == 'y' else -1
            temp_feature_names = []
            for i, col_name in enumerate(header):
                if i != label_col and i != id_col:
                    temp_feature_names.append(col_name)
            feature_names = temp_feature_names
            for row in data_rows:
                try:
                    label = row[label_col]
                    features = [float(val) for i, val in enumerate(row) if i != label_col and i != id_col]
                    dataset.append({'label': label, 'features': features})
                    all_labels.add(label)
                except (ValueError, IndexError) as e:
                    print(f"Skipping row due to data conversion error or missing column: {row} - {e}")
                    continue
        return dataset, feature_names, sorted(list(all_labels)), id_col, label_col, header
    except Exception as e:
        print(f"Critical Error loading file: {e}")
        return None, None, None, None, None, None

print("--- Nearest Neighbour Processing ---")
user_file = input("Enter path to file: ")
full_dataset, feature_names, unique_labels, id_col, label_col, header = load_user_file(user_file)
if not full_dataset:
    exit()

print("\n" + "="*50)
print("             DATASET DESCRIPTION")
print("="*50)
print(f"Total entries loaded: {len(full_dataset)}")
print(f"Class Labels detected: {', '.join(unique_labels)}")
print(f"Number of Features: {len(feature_names)}")
print("Features and their raw ranges (approximate from sample):")
raw_feature_matrix = [item['features'] for item in full_dataset]
if raw_feature_matrix:
    raw_mins, raw_maxs = find_min_maxs(raw_feature_matrix)
    for i, name in enumerate(feature_names):
        print(f"  - {name}: Min={raw_mins[i]:.2f}, Max={raw_maxs[i]:.2f}")
else:
    print("  (No numerical features to display ranges for)")
print("="*50)

sample_size = 150
dataset = random.sample(full_dataset, min(len(full_dataset), sample_size))

print("\n" + "="*50)
print(f"             SAMPLED DATASET (Size: {len(dataset)})")
print("="*50)
if dataset:
    max_len_features_str = max(len(str(item['features'])) for item in dataset)
    print(f"{'FEATURES':<{max_len_features_str}} | LABEL")
    print("-" * (max_len_features_str + 8))
    for item in dataset:
        print(f"{str(item['features']):<{max_len_features_str}} | {item['label']}")
else:
    print("No data in the sampled dataset.")
print("="*50)


feature_matrix = [item['features'] for item in dataset]
mins, maxs = find_min_maxs(feature_matrix)
num_feat = len(feature_matrix[0]) if feature_matrix else 0

print(f"\nEnter {num_feat} values for prediction (corresponding to: {', '.join(feature_names)}):")
user_input = input("> ").split()
try:
    unknown_row = [float(x) for x in user_input]
    if len(unknown_row) != num_feat:
        print(f"Error: Expected {num_feat} values, but got {len(unknown_row)}. Exiting.")
        exit()
except ValueError:
    print("Error: Invalid input for prediction values. Please enter numbers separated by spaces. Exiting.")
    exit()


unknown_processed = min_max_normalization(unknown_row, mins, maxs)
print(f"\nUnknown data point RAW: {unknown_row}")
print(f"Unknown data point NORMALIZED (all features scaled to 0-1 range): {unknown_processed}")

print("\nChoose distance metric:\n1. Euclidean\n2. Manhattan")
dist_choice = int(input("Choice: "))

while True:
    try:
        k_input = input("\nEnter k value (or 0 to exit): ")
        k = int(k_input)
        if k <= 0:
            print("Exiting K-Nearest Neighbors analysis.")
            break
        if k > len(dataset):
            print(f"k cannot be greater than the sample size ({len(dataset)}). Please enter a smaller k.")
            continue

        results = []
        for item in dataset:
            norm_feat = min_max_normalization(item['features'], mins, maxs)
            dist = distance_metric(norm_feat, unknown_processed, dist_choice)
            results.append({'label': item['label'], 'distance': dist, 'features': item['features']})

        results.sort(key=lambda x: x['distance'])
        neighbors = results[:k]

        if not neighbors:
            print("No neighbors found for the given k value.")
            continue

        max_feat_str_len = max(len(str(n['features'])) for n in neighbors)
        total_width = max_feat_str_len + 14 + 10 + 6 + 10
        print("\n" + "="*total_width)
        print(f"             K-NEIGHBORS FOR K={k}")
        print("="*total_width)
        print(f"{'DATA POINTS':<{max_feat_str_len}} | {'DISTANCE':<10} | {'LABEL':<6} | {'RANK':<6}")
        print("-" * total_width)
        for i, n in enumerate(neighbors, start=1):
           print(f"{str(n['features']):<{max_feat_str_len}} | {n['distance']:.4f}     | {n['label']:<6} | {i:<6}")
        print("="*total_width)

        weights = {}
        print("\n--- Weighted Voting Prediction ---")
        for i, n in enumerate(neighbors, start=1):

            w = 1 / (n['distance'] + 1e-9)**2
            weights[n['label']] = weights.get(n['label'], 0) + w

        if weights:
            weighted_prediction = max(weights, key=weights.get)
            print("Final Accumulated Weights:")
            for label, total_w in weights.items():
                print(f"  - {label}: {total_w:.4f}")
            print(f"\n*** Weighted Prediction (k={k}): {weighted_prediction} ***")
        else:
            print("No neighbors with valid distances for weighted voting.")

        votes = [n['label'] for n in neighbors]
        vote_counts = Counter(votes)
        print("\n--- Unweighted Voting Prediction ---")
        if vote_counts:
            print("Intermediate Voting Counts:")
            for label, count in vote_counts.items():
                print(f"  - {label}: {count} votes")
            unweighted_prediction = vote_counts.most_common(1)[0][0]
            print(f"\n*** Unweighted Prediction (k={k}): {unweighted_prediction} ***")
        else:
            print("No neighbors for unweighted voting.")

        print("\n" + "="*50)

    except ValueError:
        print("Invalid input. Please enter an integer for k.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
