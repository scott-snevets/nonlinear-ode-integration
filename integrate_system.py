import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define your system of ODEs
def system(t, y):
    x, y = y  # Unpack variables
    dxdt = np.sin(y) - x  # Replace with your equations
    dydt = np.cos(x) - y  # Replace with your equations
    return [dxdt, dydt]

# Set up initial conditions and time span
initial_conditions = [1.0, 0.5]  # Example initial values for x and y
t_span = (0, 10)  # Time range for integration
t_eval = np.linspace(t_span[0], t_span[1], 300)  # Points where solution is evaluated

# Integrate the system
solution = solve_ivp(system, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# Check if the integration was successful
if solution.success:
    # Plot results
    plt.plot(solution.t, solution.y[0], label='x(t)')
    plt.plot(solution.t, solution.y[1], label='y(t)')
    plt.xlabel('Time t')
    plt.ylabel('Solutions x(t), y(t)')
    plt.legend()
    plt.title('Numerical Integration of a Nonlinear 2x2 ODE System')
    plt.show()
else:
    print("Integration failed.")
