# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

# Introduce spring, mass, and damping coefficients
m,k = 1,4 
zeta = 0.2 
c = 2*zeta*np.sqrt(k*m)
print(c)

# Function
def f(t, y, c):
    # 1. unpack y into x and v 
    x,v = y
    # 2. compute the acceleration a from the ODE
    a = (-k/m)*x + (-c/m)*v 
    # 3. return [v,a]
    return [v,a]

#Define time points
t_eval = np.linspace(0, 10, 500)
x0, v0 = 1,0
y0 = [x0,v0]

#Compute ivp
sol = solve_ivp(f, (0,10),y0, t_eval=t_eval, args=(c,))

#Plot
plt.plot(sol.t, sol.y[0])
plt.show()





