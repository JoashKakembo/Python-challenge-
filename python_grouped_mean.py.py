import numpy as np

# Implement your solution here
def get_grouped_mean():
    # Load the data
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_data = np.genfromtxt(url, delimiter=',', dtype='object')
    
    # Extract the sepal width and species columns
    sepal_width = iris_data[:, 1].astype(float)
    species = iris_data[:, 4]
    
    # Get unique species values
    unique_species = np.unique(species)
    
    # Calculate grouped mean using list comprehension
    grouped_mean = [[sp, np.mean(sepal_width[species == sp])] for sp in unique_species]
    
    return grouped_mean

# Calculate grouped mean and print
grouped_mean = get_grouped_mean()
for i in grouped_mean:
    print(i)
