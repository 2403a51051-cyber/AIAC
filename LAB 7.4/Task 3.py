with open("example.txt","w") as f:
    f.write("Hello,world!")
    f1=open("data1.txt","w")
    f2=open("data2.txt","w")
    f1.write("First file content\n")
    f2.write("Second file content\n")
    print("Files written successfully")
    import os
    if not os.path.exists("input.txt"):
        with open("input.txt", "w") as temp_input:
            temp_input.write("Sample input line 1\nSample input line 2\n")
            data = open("input.txt", "r").readlines()
            output = open("output.txt", "w")
            for line in data:
                output.write(line.upper())
                print("Processing done")
    
    
    import os
    if not os.path.exists("numbers.txt"):
        with open("numbers.txt", "w") as nf:
            nf.write("1\n2\n3\n4\n5\n")  # Example numbers

    with open("numbers.txt", "r") as f:
        nums = f.readlines()
    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))
    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")
    print("Squares written")