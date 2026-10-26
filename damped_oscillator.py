# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

# Introduce mass and spring coefficients
m,k = 1,4 

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

zetas = [0.2, 1.0, 2.0]
for z in zetas:
    c = 2*z*np.sqrt(k*m)
    sol = solve_ivp(f, (0,10),y0, t_eval=t_eval, args=(c,))
    plt.plot(sol.t, sol.y[0],label = f"zeta = {z}")

plt.xlabel('time (s)')
plt.ylabel('x (m)')
plt.title('Free Response for Three Damping Ratios')
plt.legend()
plt.grid(True)

#Verify zeta = 0.2 against the exact solution
z = 0.2
c = 2*z*np.sqrt(k*m)
sol_check = solve_ivp(f, (0,10),y0, t_eval=t_eval, args=(c,), rtol=1e-8, atol=1e-10)
w_n = np.sqrt(k/m)
w_d = w_n*np.sqrt(1 - z**2)
x_exact = np.exp(-z*w_n*sol_check.t)*(np.cos(w_d*sol_check.t)+((z*w_n)/(w_d)*np.sin(w_d*sol_check.t)))
err = np.max(np.abs(sol_check.y[0]-x_exact))
print(f"max_error = {err:.2e}")
plt.show()
