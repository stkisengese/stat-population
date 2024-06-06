import sys
from statistics import mean, median, pvariance, pstdev
from math import floor

def read_population_data(filename):
    """This function reads population data from a text file."""
    
    try:
        with open(filename) as file:
            # creating a list by iterating through every line of the file.
            population_data = [float(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        sys.exit(1)
    except ValueError as err:
        print(f"Error: {err}. File should contain only numbers")
        sys.exit(1)
    except Exception as err:
        print(f"Exception error occured: {err}.")
        sys.exit(1)

    return population_data

def calculate_statistics(data):
    """This function calculates basic statistics of list of numbers."""
    
    if not data:
        print("No data to calculate statistics.")
        return
        
    return {
        'average': floor(mean(data) + 0.5),
        'median': floor(median(data) + 0.5),
        'variance': round(pvariance(data)),
        'std_dev': round(pstdev(data))
    }    

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("Usage: python3 math_skills.py <filename.txt>")
        sys.exit(1)
    # try-except block to handle potential exceptions during function cals.    
    try:
        population_data = read_population_data(sys.argv[1])
        stats = calculate_statistics(population_data)
        
        print(f"Average: {stats['average']}")
        print(f"Median: {stats['median']}")
        print(f"Variance: {stats['variance']}")
        print(f"Standard Deviation: {stats['std_dev']}")
    except Exception as err:
        print(f"An error occured: {err}")
        sys.exit(1)
