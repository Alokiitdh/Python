# Pascal Trinage

def pascal_triangle(n): # n number of rows
    triangle = []
    for i in  range(n):
        row = [1]*(i+1) # starting each roe element as 1
        # updating elements in the middle of the row
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle

n = 5
tri = pascal_triangle(n)
for r in tri:
    print(r)
