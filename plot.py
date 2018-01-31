import matplotlib.pyplot as plt


def plot(dict):
    left = range(len(dict.keys()))
    right = dict.values()
    print right
    fig = plt.figure(figsize=(10, 8))
    plt.bar(left, right, color="#1E7F00", linewidth=0, align="center")
    plt.xticks(left, dict.keys())
    filename = "plot.png"
    plt.savefig(filename)
