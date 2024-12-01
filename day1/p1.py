

def read_input() -> list[tuple[int, int]]:
    with open("day1/input.txt") as f:
        data = f.read()
        data = data.splitlines()
        data = [(int(d.split()[0]), int(d.split()[1]))
                for d in data]
        return data

def main():
    vals = read_input()
    pair_1 = [val[0] for val in vals]
    pair_2 = [val[1] for val in vals]
    
    pair_1.sort()
    pair_2.sort()
    
    total = 0
    
    for p1, p2 in zip(pair_1, pair_2):
        diff = abs(p1 - p2)
        total += diff
    
    print(f"The total difference is {total}")    
    

if __name__  == "__main__":
    main()