import matplotlib.pyplot as plt
from solar_objects import Star, Planet
def graph(space_objects):
    for obj in space_objects:
        B=[]
        B=obj.A[:1000:5]
        T=[]
        for i in range(100):
          T.append(i)
        plt.plot(B,T)
        plt.show()
