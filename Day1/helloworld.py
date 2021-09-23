'''print("Jacob")
print("Vissering")
print("USA")
print("Let's begin 30 days of python")

type(10)
type(9.8)
type(3.14)
type(4-4j)
type(["Asabeneh","Python","Finland"])
type("Jacob")'''
import numpy as np
point_a = np.array((2,3))
point_b = np.array((10,8))
distance = np.linalg.norm(point_a - point_b)
print(distance)