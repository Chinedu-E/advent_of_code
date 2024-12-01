from collections import Counter


def read_input() -> list[tuple[int, int]]:
    with open("day1/input.txt") as f:
        data = f.read()
        data = data.splitlines()
        data = [(int(d.split()[0]), int(d.split()[1]))
                for d in data]
        return data


def main():
    vals = read_input()
    left = [val[0] for val in vals]
    right = [val[1] for val in vals]
    
    # Hashmap for frequency values on the right IDs
    right_freq = Counter(right)
    
    total_similarity = 0
    
    for val in left:
        freq = right_freq.get(val, 0)
        total_similarity += (val * freq)
        
    print(f"The total similarity between both lists is: {total_similarity}")

if __name__  == "__main__":
    main()