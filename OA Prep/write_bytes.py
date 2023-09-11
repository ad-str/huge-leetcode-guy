import os

def performTask(filename: str):
    a, b = 0, 0

    with open(filename) as file:
        for line in file.readlines():
            arr = line.strip().split()
            fsize = int(arr[-1])

            if fsize > 5000:
                a += 1
                b += fsize

    with open('bytes_' + filename, 'w') as file:
        file.write(str(a) + '\n' + str(b) + '\n')

if __name__ == "__main__":
    os.chdir('OA Prep')
    performTask("test.txt")