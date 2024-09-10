
import numpy as np
import matplotlib.pyplot as plt
import copy
import math


data = np.array([
    [6.1101, 17.592], [5.5277, 9.1302], [8.5186, 13.662], [7.0032, 11.854],
    [5.8598, 6.8233], [8.3829, 11.886], [7.4764, 4.3483], [8.5781, 12.0],
    [6.4862, 6.5987], [5.0546, 3.8166], [5.7107, 3.2522], [14.164, 15.505],
    [5.734, 3.1551], [8.4084, 7.2258], [5.6407, 0.71618], [5.3794, 3.5129],
    [6.3654, 5.3048], [5.1301, 0.56077], [6.4296, 3.6518], [7.0708, 5.3893],
    [6.1891, 3.1386], [20.27, 21.767], [5.4901, 4.263], [6.3261, 5.1875],
    [5.5649, 3.0825], [18.945, 22.638], [12.828, 13.501], [10.957, 7.0467],
    [13.176, 14.692], [22.203, 24.147], [5.2524, -1.22], [6.5894, 5.9966],
    [9.2482, 12.134], [5.8918, 1.8495], [8.2111, 6.5426], [7.9334, 4.5623],
    [8.0959, 4.1164], [5.6063, 3.3928], [12.836, 10.117], [6.3534, 5.4974],
    [5.4069, 0.55657], [6.8825, 3.9115], [11.708, 5.3854], [5.7737, 2.4406],
    [7.8247, 6.7318], [7.0931, 1.0463], [5.0702, 5.1337], [5.8014, 1.844],
    [11.7, 8.0043], [5.5416, 1.0179], [7.5402, 6.7504], [5.3077, 1.8396],
    [7.4239, 4.2885], [7.6031, 4.9981], [6.3328, 1.4233], [6.3589, -1.4211],
    [6.2742, 2.4756], [5.6397, 4.6042], [9.3102, 3.9624], [9.4536, 5.4141],
    [8.8254, 5.1694], [5.1793, -0.74279], [21.279, 17.929], [14.908, 12.054],
    [18.959, 17.054], [7.2182, 4.8852], [8.2951, 5.7442], [10.236, 7.7754],
    [5.4994, 1.0173], [20.341, 20.992], [10.136, 6.6799], [7.3345, 4.0259],
    [6.0062, 1.2784], [7.2259, 3.3411], [5.0269, -2.6807], [6.5479, 0.29678],
    [7.5386, 3.8845], [5.0365, 5.7014], [10.274, 6.7526], [5.1077, 2.0576],
    [5.7292, 0.47953], [5.1884, 0.20421], [6.3557, 0.67861], [9.7687, 7.5435],
    [6.5159, 5.3436], [8.5172, 4.2415], [9.1802, 6.7981], [6.002, 0.92695],
    [5.5204, 0.152], [5.0594, 2.8214], [5.7077, 1.8451], [7.6366, 4.2959],
    [5.8707, 7.2029], [5.3054, 1.9869], [8.2934, 0.14454], [13.394, 9.0551],
    [5.4369, 0.61705]
])


x_train = data[:, 0]
y_train = data[:, 1]


plt.scatter(x_train, y_train, marker='x', c='r')
plt.title("Profits vs. Population per city")
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000')
plt.show()


def compute_cost(x, y, w, b):
    m = x.shape[0] 
    yp = np.dot(x, w) + b
    total_cost = (1 / (2 * m)) * np.sum((yp - y) ** 2)
    return total_cost


def compute_gradient(x, y, w, b):
    m = x.shape[0]
    yp = np.dot(x, w) + b
    dj_dw = (1 / m) * np.sum((yp - y) * x)
    dj_db = (1 / m) * np.sum(yp - y)
    return dj_dw, dj_db


def gradient_descent(x, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters):
    w = copy.deepcopy(w_in)
    b = b_in
    m = len(x)
    
    for i in range(num_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        
       
        if i % 100 == 0:
            cost = cost_function(x, y, w, b)
            print(f"Iteration {i}: Cost {cost:.3f}")
            
    return w, b


initial_w = 0.0
initial_b = 0.0
alpha = 0.001  
iterations = 20000 

w, b = gradient_descent(x_train, y_train, initial_w, initial_b, compute_cost, compute_gradient, alpha, iterations)
print(f"w, b found by gradient descent: {w}, {b}")


m = x_train.shape[0]
predicted = np.zeros(m)

for i in range(m):
    predicted[i] = w * x_train[i] + b

plt.plot(x_train, predicted, c="b")
plt.scatter(x_train, y_train, marker='x', c='r')
plt.title("Profits vs. Population per city")
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000')
plt.show()


predict1 = 3.5 * w + b
print(f"For population = 35,000, we predict a profit of ${predict1 * 10000:.2f}")

predict2 = 7.0 * w + b
print(f"For population = 70,000, we predict a profit of ${predict2 * 10000:.2f}")
