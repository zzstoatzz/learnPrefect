## Extract 
def extract(path):
    with open(path, "r") as f:
        txt = f.readline().strip()
    data = [int(i) for i in txt.split(",")]
    return data

## Transform 
def transform(data):
    newdata = [i+1 for i in data]
    return newdata

## Load
def load(data, path):
    import csv
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return