import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = [5,8,7,10,6,7,9,3,8,2]
y = [6,9,8,10,5,7,8,4,6,2]

sum_X = sum(x)
sum_Y = sum(y)
mult_XY = sum([x[i]*y[i] for i in range(len(x))])
x2 = sum([x[i]**2 for i in range(len(x))])
y2 = sum([y[i]**2 for i in range(len(y))])


coeficiente = (len(x)*mult_XY - sum_X*sum_Y) / (len(x)*x2 - sum_X**2)   
linear = (sum_Y - coeficiente*sum_X) / len(x)

#plt.scatter(x, y)
#plt.plot([min(x), max(x)], [coeficiente*min(x) + linear, coeficiente*max(x) + linear], color='red')

sns.regplot(x=x, y=y, color='red',scatter=True )
plt.show()

print("somatória de x:", sum_X)
print("somatória de y:",sum_Y)
print("Multiplicacao  entre x e y:",mult_XY)
print("X elevado ao quadrado:", x2) 
print("Y elevado ao quadrado:", y2)
print("coficiente linear:", linear)
print("coeficiente angular:", coeficiente)