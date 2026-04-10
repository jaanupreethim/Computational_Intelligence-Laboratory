import math

def read_data(filename):
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n")
    headers = lines[0].split(",")
    data = [line.split(",") for line in lines[1:]]
    return headers, data

def entropy(values):
    total = len(values)
    if total == 0: return 0
    ent = 0
    unique = list(set(values))
    for u in unique:
        p = values.count(u) / total
        ent -= p * math.log2(p)
    return ent

def information_gain(data, attr_index, target_index, total_entropy, attr_name):
    print(f"\nAttribute: {attr_name}")
    values = sorted(list(set(row[attr_index] for row in data)))
    total_records = len(data)
    weighted_entropy = 0

    print("Value\tYes\tNo\tEntropy Formula")

    for val in values:
        subset = [row[target_index] for row in data if row[attr_index] == val]
        y = subset.count("yes")
        n = subset.count("no")
        t = len(subset)

        ent = entropy(subset)
        weight = t / total_records
        weighted_entropy += (weight * ent)


        if y == 0 or n == 0:
            formula = f"0.0"
        else:
            formula = f"-({y}/{t}log2({y}/{t})) - ({n}/{t}log2({n}/{t})) = {round(ent, 4)}"

        print(f"{val}\t{y}\t{n}\t{formula}")

    print(f"\nWeighted Entropy = {round(weighted_entropy, 4)}")
    gain = total_entropy - weighted_entropy
    print(f"Information Gain = {round(gain, 4)}")
    return gain

def find_root_node(filename):
    headers, data = read_data(filename)
    target_index = len(headers) - 1
    target_values = [row[target_index] for row in data]
    total_entropy = entropy(target_values)

    print(f"Target Attribute: {headers[target_index]}")
    print(f"Total Entropy = {round(total_entropy, 4)}")

    gains = {}
    for i in range(target_index):
        gain = information_gain(data, i, target_index, total_entropy, headers[i])
        gains[headers[i]] = gain

    print("\nSummary of Information Gain")
    for attr in gains:
        print(f"{attr} : {round(gains[attr], 4)}")

    root = max(gains, key=gains.get)
    print(f"\nRoot Node: {root}")

find_root_node("data.txt")
