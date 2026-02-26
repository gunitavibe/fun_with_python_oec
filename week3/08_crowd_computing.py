import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()

plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

plt.xlabel("X values")
plt.ylabel("Y values")

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.show()
#'ro' → Red dots
#'r--' → Red dashed line
#'bs' → Blue squares
#'g^' → Green triangles