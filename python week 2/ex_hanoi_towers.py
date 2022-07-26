def hanoi(n, source, middle, dest):
    """
    Args:
        n(int): number of rings
        source, middle, dest = towers
    """
    if n == 1:
        print(f"Moving disk from tower {source} to tower {dest}")
    else:
        hanoi(n - 1, source, dest, middle)
        print(f"Moving disk from tower {source} to tower {dest}")
        hanoi(n - 1, middle, source, dest)

hanoi(3, 1, 2, 3)   #3 disks, source tower = 1, middle tower = 2, dest tower = 3
