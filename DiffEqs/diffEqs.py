import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Solve single first order differential equation
if(False):
    print("Solves dy(t)/dt = -ky(t) between 0 and 20. Need value for k and initial condition y(0).")
    print("For example k = 0.3 ad y0 = 5.")
    k = input('What is the value of k?\n') 
    y0 = input('What is the value of y(0)?\n') 
    k = float(k)
    y0 = float(y0)
    
    # function that returns dy/dt
    def model(y,t):
        dydt = -k * y
        return dydt

    # time points
    t = np.linspace(0,20)

    # solve ODE
    y = odeint(model,y0,t) #Saved as column of 1-unit arrays, to divide with analy must transpose and take 0th element
    analy = y0*np.e**(-k*t)

    # plot results
    #plt.plot(t,y,label="Numerical")
    #plt.plot(t,analy,label="Analytic")
    plt.plot(t,y.T[0]/analy,label="Num/Anal")
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

#Solve single first order differential equation, passing argument to odeint
if(False):
    print("Solves dy(t)/dt = -ky(t) between 0 and 20")
    
    # function that returns dy/dt
    def model(y,t,k):
        dydt = -k * y
        return dydt

    # time points
    t = np.linspace(0,20)

    y0 = 5
    k = 0.3
    # solve ODE
    y = odeint(model,y0,t,args=(k,)) #Saved as column of 1-unit arrays, to divide with analy must transpose and take 0th element

    # plot results
    plt.plot(t,y,label="Numerical")
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

#Solve coupled first order differential equation
if(False):
    print("Solves dy1(t)/dt = -k1*y1(t); dy2(t)/dt = -k1*y1(t)+k2*y2(t)")
    ts = 0 # where t starts
    tf = 2 # where t ends
    print("between t =", ts, " and t =", tf)
    k1 = -1 # 
    k2 = -1
    y10 = 1
    y20 = 2

    # function that returns dy/dt
    def model(t,y):
        dydt = [-k1*y[0] , -k1*y[0] + k2*y[1]]
        return dydt

    # time points
    t = np.linspace(0,2,num=200)

    # solve ODE, not that here model arguments need to be independent, dependent
    res = solve_ivp(model,(ts,tf),[y10,y20],t_eval=t)
    #analy = y0*np.e**(-k*t)

    #Analytic results with k1 = k2 = -1, y10 = 1, y20 = 2
    y1a = np.e**(t) 
    y2a = 0.5*np.e**(t) + 1.5*np.e**(-t)
    # plot results
    #plt.plot(res.t,res.y[0],label="Num $y_1$")
    #plt.plot(res.t,res.y[1],label="Num $y_2$")
    #plt.plot(t,y1a,label="Anal $y_1$")
    #plt.plot(t,y2a,label="Anal $y_2$")

    # plot ratios
    plt.plot(t,res.y[0]/y1a,label="y1 Num/Anal")
    plt.plot(t,res.y[1]/y2a,label="y2 Num/Anal")
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

# Catch up on the Black-Scholes model
# https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model

#I guess I want to plot a curves for geometric brownian motion


