# **The Double Pendulum**
We have two massless rods both with length $L$, rod 1, one end if fixed from the origin, has a mass $m_1$ attached to it. Rod 2 has one end attached to $m_1$, the other end of the rod has a mass, $m_2$. Each of the rods make angles $\varphi_1$ and $\varphi_2$, respectively,  with the vertical, $\hat y$, axis.

## **The Lagrangian**
In this problem it is easier to consider the lagrangian for the angles $\varphi_1$ and $\varphi_2$

The lagrangian, $\mathcal{L}$, is defined as:

$$\begin{align}\mathcal{L} = T - U\\
 \end{align}$$

Where $T$ is the kinetic energy, and $U$ is the potential energy.

To find the kinetic energy we know $\frac{1}{2}m\textbf{v}^2$, to know the velocity we need to find the velocity vector $\textbf{v}$. Which can be found by the $x$ and $y$ positions.

$$
     \left \{ 
        \begin{aligned}
        &x_1 = L \sin\varphi_1 \\
        &y_1 = L \cos \varphi_1
        \end{aligned}
    \right. \, \& \,
    \left \{ 
        \begin{aligned}
        &x_2 = L\sin\varphi_2 + L \sin\varphi_1 \\
        &y_2 = L\cos\varphi_2 + L \cos \varphi_1
        \end{aligned}
    \right. 
$$


## Euler-Lagrange Equations
The Euler-Lagrange equations are defined as such,
$$
    \left \{ 
        \begin{aligned}
        &\frac{d}{dt}\left ( \frac{\partial\mathcal{L}}{\partial \dot\varphi_1} \right )- \frac{\partial \mathcal{L}}{\partial \varphi_1} = 0 \\
        &\frac{d}{dt}\left ( \frac{\partial\mathcal{L}}{\partial \dot\varphi_2} \right )- \frac{\partial \mathcal{L}}{\partial \varphi_2} = 0 
        \end{aligned}
    \right. .
$$
After solving the Lagrangian and solving for $\ddot\varphi_i$ we get 
$$
    \left \{ 
        \begin{aligned}
        &\ddot\varphi _ { 2 } (\varphi_1,\varphi_2,\dot\varphi_1,\dot\varphi_2,\ddot\varphi_1) = \frac { g } { L } \sin \varphi _ { 2 } - \ddot\varphi _ { 1 } \cos ( \varphi _ { 2 } - \varphi _ { 1 } ) + \dot\varphi_{1} \sin ( \varphi _ { 2 } - \varphi _ { 1 } ) ( \dot\varphi _ { 2 } -\dot \varphi _ { 1 } )\\ 
        &\ddot\varphi_1 (\varphi_1,\varphi_2,\dot\varphi_1,\dot\varphi_2,\ddot\varphi_2) = (\dot \varphi _ { 2 }  \sin ( \varphi _ { 2 } - \varphi _ { 1 } ) ( \dot\varphi _ { 2 } - \dot\varphi _ { 1 } ) + g ( m _ { 1 } + m _ { 2 } ) \sin \varphi _ { 1 } - m _ { 2 } L^ { 2 } \ddot\varphi _2 c o s ( \varphi _ { 2 } - \varphi _ { 1 } ) ) / L ^ { 2 } ( m _ { 1 } + m _ { 2 } )
        \end{aligned}
    \right. .
$$
Which next we need to start removing self-referencing term of $\ddot\varphi _ { 1 } (\varphi_1,\varphi_2,\dot\varphi_1,\dot\varphi_2,\ddot\varphi_1)$ to terms of $\ddot\varphi _ { 1 } (\varphi_1,\varphi_2,\dot\varphi_1,\dot\varphi_2)$, which yeilds

$$  
    \ddot\varphi_1 (\varphi_1,\varphi_2,\dot\varphi_1,\dot\varphi_2) = 
    \left (
    1+\frac{\cos^2(\varphi_2-\varphi_1)(\dot\varphi_1-\dot\varphi_2)}
    {m_1+m_2}
    \right )^{-1}
    \left [
        \frac{\dot\varphi_2 \sin(\varphi_2-\varphi_1)(\dot\varphi_1-\dot\varphi_2)}
        {L^2(m_1+m_2)}+\frac{g}{L^2}\sin(\varphi_1)+\frac{g}{L}\frac{m_2\cos(\varphi_2-\varphi_1)}{m_1+m_2}

    \right ]
    $$ .

## Casting to Runge Kutta (RK4) Integrator as a State Vector
In this step we preform casting, which is will be the proccess of reducing from our second-order differential equation system to behave as a first-order system. Through this we can plug into the Runge-Kutta.

To start we will cast our first angular velocity $\varphi_i \rightarrow \omega_i$, letting omega be our **angular** velocity as such.

$$\omega_i = \dot\varphi_i = \frac{d\varphi_i}{dt}$$

### State Vector
After we get the angular velocty we can express our pendulum as the following state:
$$
\textbf{Y}(t) = \left( \begin{matrix} \varphi_1 \\ \varphi_2 \\ \omega_1 \\ \omega_2  \end{matrix} \right)
$$
gives 
$$
\frac{d}{dt}\left( \begin{matrix} \varphi_1 \\ \varphi_2 \\ \omega_1 \\ \omega_2  \end{matrix}\right)
= \left( \begin{matrix} \omega_1 \\ \omega_2  \\ \ddot\varphi_1 \\ \ddot\varphi_2 \end{matrix}\right)
$$

or can be expressed as:
$$\textbf{Y}' = $$

## Runge-Kutta Method
Chapter 7 pg. 448, Nonlinear Systems of Differential Equations:
### Runge-Kutta for 2x2 DE Systems
$$
\begin{aligned}
x' = f(t,x,y), \qquad & x(t_0)=x_0\\
y' = g(t,x,y), \qquad & y(t_0)= y_0\\

\end{aligned}
$$
with step size h are as follows:
$$
x_{n+1} = x_n + \frac{h}{6}(k_{n1} + 2k_{n2} + 2k_{n3} + k_{n4}) \\[.2cm]
y_{n+1} = y_n + \frac{h}{6}(m_{n1} + 2m_{n2} + 2m_{n3} + m_{n4})
$$
Where 
$$
    \begin{aligned}
    k_{n1} &= f(t_n,x_n,y_n) \\
    k_{n2} &= f(t_n + \frac{h}{2}, x_n + \frac{h}{2}k_{n1},\, y_n + \frac{h}{2}m_{n1})\\
    k_{n3} &= f(t_n + \frac{h}{2}, x_n + \frac{h}{2}k_{n2},\, y_n + \frac{h}{2}m_{n2})\\
    k_{n4} &= f(t_n + h, x_n + hk_{n3},\, y_n +hm_{n3})
    \end{aligned}
$$
and
$$
    \begin{aligned}
    m_{n1} &= g(t_n,x_n,y_n) \\
    m_{n2} &= g(t_n + \frac{h}{2}, x_n + \frac{h}{2}k_{n1},\, y_n + \frac{h}{2}m_{n1})\\
    m_{n3} &= g(t_n + \frac{h}{2}, x_n + \frac{h}{2}k_{n2},\, y_n + \frac{h}{2}m_{n2})\\
    m_{n4} &= g(t_n + h, x_n + hk_{n3},\, y_n +hm_{n3})
    \end{aligned}
$$

## Analysis
![Graph](dp_graph.png)
