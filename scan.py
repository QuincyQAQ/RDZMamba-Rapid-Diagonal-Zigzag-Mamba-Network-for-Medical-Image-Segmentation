import numpy as np
import matplotlib.pyplot as plt

# Create an image matrix
img = np.arange(1, 65).reshape((8, 8))

print("Output Line1:\n", img)

def jieti(mat):
    m, n = mat.shape
    scan1 = np.zeros((m * n - m) // 2)
    t = 0
    for k in range(1, n // 2 + 1):
        for j in range(1, 1 + (k - 1) * 4 + 1):
            x_index = m - 2 * (k - 1) + (j // 2) - 1  # Adjusted for zero-based index
            y_index = (j + 1) // 2 - 1
            if x_index < m and y_index < n:
                scan1[t] = mat[x_index, y_index]
            t += 1

    scan2 = np.zeros(n)
    for i in range(n):
        if i < m:  # Ensuring the diagonal access is within the square matrix limits
            scan2[i] = mat[i, i]

    scan3 = np.zeros((m * n - m) // 2)
    t = 0
    for k in range((n - 2) // 2 + 1, 0, -1):
        for j in range(1, 4 * (k - 1) + 1 + 1):
            x_index = (j + 1) // 2 - 1
            y_index = 2 * (((n - 2) // 2 + 2) - k) + (j // 2) - 1
            if x_index < m and y_index < n:
                scan3[t] = mat[x_index, y_index]
            t += 1

    Line = np.concatenate((scan1, scan2, scan3))
    return Line


Line1 = jieti(img)


# Print the output line
print("Output Line1:", Line1)
