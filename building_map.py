"""
I was given this problem for a coding assessment.

"You are given an M x N grid marked by either a 1 or 0 representing buildings 
on a map.  1 marks the presence of a building and 0 marks free space. If two
or more 1's are adjacent to one another, then it is considered to be one
building.  If two or more 1's are diagonal to one another, then they are
considered to be two seperate buildings.  Count how many building exist."

After the end of 45 minutes, I had to move onto my second problem.
Because of trivial bugs, both my solutions were not accepted.  Judging by 
the speed at which I received a soul destroying email -- No one even look at 
my code.

"Thanks for completing the coding assessment. After reviewing the results it 
seems like the outcome was negative. Let’s stay in touch & hopefully we can 
start the process again sometime in near future."

Sure -- I enjoy crunching code for 90 minutes like my career and livelihood
depend on it.

I went back and decided to retry the problem, under time, again.  I completed 
the problem after ~hour.  I then puttered around with some minor changes and
optimizations before publishing. I don't dunno if its great, I just wanted to 
take back my dignity.  Thanks for ruining everything.
"""

def buildingDetector(maze :list, row :int, col :int, M :int, N :int):

    size = 0
    if row > 0 and maze[row - 1][col] == 1:
            maze[row - 1][col] -= 1
            size += buildingDetector(maze, row - 1, col, M, N) + 1

    if col > 0 and maze[row][col - 1] == 1:
            maze[row][col - 1] -= 1
            size += buildingDetector(maze, row, col - 1, M, N) + 1

    if row + 1 < M and maze[row + 1][col] == 1:
            maze[row + 1][col] -= 1
            size += buildingDetector(maze, row + 1, col, M, N) + 1

    if col + 1 < N and maze[row][col + 1] == 1:
            maze[row][col + 1] -= 1
            size += buildingDetector(maze, row, col + 1, M, N) + 1

    if maze[row][col] == 1:
        maze[row][col] -= 1
        size += 1

    return size

def main(maze :list, M :int, N :int):

    count = 0
    for row in range(M):
        for col in range(N):
            if (size := buildingDetector(maze, row, col, M, N)) > 0:
                print(f'found one! Size {size}.')
                count +=1

    return count

if __name__ == '__main__':

    TEST = [
        [1, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0]
    ]

    M = len(TEST)
    N = len(TEST[0])

    print(main(TEST, M, N))