def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def find_highest(scores):
    return max(scores) if scores else None

def find_lowest(scores):
    return min(scores) if scores else None

def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

if __name__ == "__main__":
    try:
        scores = list(map(float, input("Enter scores separated by spaces: ").split()))
        if scores:
            process_scores(scores)
        else:
            print("No scores entered.")
    except ValueError:
        print("Error: Please enter valid numeric scores.")