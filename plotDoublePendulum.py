import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8  # acceleration due to gravity (m/s^2)
L = 1.0  # length of the pendulum rods (m)
m1 = 1.0  # mass of the first pendulum (kg)
m2 = 1.0  # mass of the second pendulum (kg)

# Define the system of differential equations
def derivs(t, state):
    # Unpack the state vector
    phi1, phi2, omega1, omega2 = state
    
    # Equations of motion (from the Euler-Lagrange equations)
    delta_phi = phi2 - phi1
    
    # First-order derivatives
    dphi1_dt = omega1
    dphi2_dt = omega2
    
    # Second-order derivatives (angular accelerations)
    domega1_dt = ((m2 * L * omega2**2 * np.sin(delta_phi) * np.cos(delta_phi)
                   + m2 * g * np.sin(phi2) * np.cos(delta_phi)
                   - (m1 + m2) * g * np.sin(phi1)) 
                   / (L * (m1 + m2)))
    
    domega2_dt = ((-m2 * L * omega1**2 * np.sin(delta_phi) * np.cos(delta_phi)
                   + (m1 + m2) * g * np.sin(phi1) * np.cos(delta_phi)
                   - (m1 + m2) * g * np.sin(phi2)) 
                   / (L * (m1 + m2)))
    
    return [dphi1_dt, dphi2_dt, domega1_dt, domega2_dt]

# Define the Runge-Kutta method
def runge_kutta(func, y0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    
    for i in range(1, len(t)):
        k1 = np.array(func(t[i-1], y[i-1]))
        k2 = np.array(func(t[i-1] + 0.5*dt, y[i-1] + 0.5*dt*k1))
        k3 = np.array(func(t[i-1] + 0.5*dt, y[i-1] + 0.5*dt*k2))
        k4 = np.array(func(t[i-1] + dt, y[i-1] + dt*k3))
        
        y[i] = y[i-1] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    return t, y

# Initial conditions
phi1_0 = np.pi / 2  # initial angle of the first pendulum (radians)
phi2_0 = np.pi / 2  # initial angle of the second pendulum (radians)
omega1_0 = 0.0  # initial angular velocity of the first pendulum (rad/s)
omega2_0 = 0.0  # initial angular velocity of the second pendulum (rad/s)

# Initial state vector
state0 = [phi1_0, phi2_0, omega1_0, omega2_0]

# Time parameters
t0 = 0.0  # start time
tf = 10.0  # end time
dt = 0.01  # time step

# Solve the system using Runge-Kutta
t, sol = runge_kutta(derivs, state0, t0, tf, dt)

# Extract solutions
phi1 = sol[:, 0]
phi2 = sol[:, 1]

# Plot the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, phi1, label=r'$\phi_1$ (angle 1)')
plt.plot(t, phi2, label=r'$\phi_2$ (angle 2)')
plt.xlabel('Time [s]')
plt.ylabel('Angle [rad]')
plt.legend()
plt.title('Pendulum Angles')

plt.subplot(1, 2, 2)
plt.plot(t, sol[:, 2], label=r'$\omega_1$ (angular velocity 1)')
plt.plot(t, sol[:, 3], label=r'$\omega_2$ (angular velocity 2)')
plt.xlabel('Time [s]')
plt.ylabel('Angular velocity [rad/s]')
plt.legend()
plt.title('Pendulum Angular Velocities')

plt.tight_layout()
plt.show()