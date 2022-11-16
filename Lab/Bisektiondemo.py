#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector, Button
from math import copysign

# Display info about the program
print("-----------------------------------------------------")
print("The bisection method for the non-linear equation")
print("     f(x) = 0, where f(x) = x^2 - 4*sin(x) - 1")
print("-----------------------------------------------------")
print("The function y = f(x) and the line y = 0 are plotted in the figure. We are interested in the solution to the non-linear equation f(x) = 0. To solve the equation we will use the bisection method. The method starts with an interval in which a root lies and successively halves the interval with each iteration. Use the program as follows:")
print("1. Start by selecting an initial interval, use the cursor.")
print("2. Press \"Set initial interval\" to initialize the bisection method with chosen starting interval.")
print("3. Press \"Step once\" to perform one iteration, continue until the solution stops improving. The iteration number, current interval, function value at midpoint and estimated error are printed.")
print("4. Press \"Reset\" to reset the solver and try another initial interval. Quit the program by closing the figure window.")


def f(x):
    return x*x - 4*np.sin(x) - 1

def sign(x):
    return copysign(1,x)

# Setup the figure
xl, xr = -5, 5
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('Bisection method')

fig.subplots_adjust(left=0.10, bottom=0.15)
plt.xlabel('x')
plt.ylabel('y')

# Draw the initial plot. The 'line' variable is used for modifying the interval line later
xx = np.linspace(xl,xr,1000);
y = f(xx)
ax.plot(xx,y,label='y = f(x)',color='blue')
ax.plot(np.array([xl, xr]),np.array([0, 0]),'--',color='black',label='y = 0');
[line] = ax.plot([None,None],[0,0],'r*-',label='Bisection method');
ax.set_xlim([xl, xr])
ax.set_ylim([-10, 30])

# Define widgets and events
def onmove(vmin, vmax):
    line.set_xdata([vmin,vmax])
    plt.draw()
    
def onselect(vmin, vmax):
    return

start_guess_span_ax  = fig.add_axes([0.10, 0.10, 0.80, 0.03])
start_guess_span_ax.set_xlim(xl,xr)
start_guess_span_ax.set_xticks([])
start_guess_span_ax.set_yticks([])
start_guess_span_ax.set_frame_on(False)
start_guess_span_ax.set_position(ax.get_position())
start_guess_span = SpanSelector(start_guess_span_ax, direction='horizontal', useblit=True, span_stays=False, onselect=onselect, onmove_callback=onmove,rectprops=dict(alpha=1, facecolor='none', edgecolor='black'))

reset_button_ax = fig.add_axes([0.8, 0.03, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')
def reset_button_on_clicked(mouse_event):
    global iter_no
    start_guess_span.set_active(True)
    iter_no = 0
    line.set_xdata([None,None])
    line.set_ydata([0,0])
    step_button.label.set_text('Set initial interval')
    plt.draw()
    
reset_button.on_clicked(reset_button_on_clicked)

iter_no = 0
    
step_button_ax = fig.add_axes([0.10, 0.03, 0.25, 0.04])
step_button = Button(step_button_ax, 'Set initial interval', hovercolor='0.975', color='0.85')

def step_button_on_clicked(mouse_event):
    global iter_no
    xint,yint = line.get_data()
    a,b = xint
    if iter_no == 0:
        if a is None or b is None:
            print("\nNo interval chosen. Try again.")
            return
        if sign(f(a)) == sign(f(b)):
            print("\nThe interval [xl,xr] = [{:f},{:f}] won't work, the sign of f(x) must be different at the interval endpoints. Here f(xl) = {:f} and f(xr) = {:f} => same sign! Try again.".format(a,b,f(a),f(b)))
            return
        else:                
            print("\n{:^12s}\t{:^12s}\t{:^12s}\t{:^12s}\t{:^19s}".format("Iteration","xl","xr","f(xmid)","Estimated Error"))
            start_guess_span.set_active(False)
            step_button.label.set_text('Step once')
    else:
        c = (a+b)/2
        if sign(f(a)) == sign(f(c)):
            a = c
        else:
            b = c
             
    err = abs(b-a)
    iter_no += 1
    x = (a+b)/2
    print("{:^12d}\t{:^.12f}\t{:^.12f}\t{:^.12f}\t{:^.12e}".format(iter_no,a,b,f(x),err))
    line.set_xdata([a,b])
    
    plt.draw()
    
step_button.on_clicked(step_button_on_clicked)

ax.legend()
plt.show()


