#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Display info about the program
print("-----------------------------------------------------")
print("The Newton-Raphson method for the non-linear equation")
print("     f(x) = 0, where f(x) = x^2 - 4*sin(x) - 1")
print("-----------------------------------------------------")
print("The function y = f(x) and the line y = 0 are plotted in the figure. We are interested in the solution to the non-linear equation f(x) = 0. To solve the equation we will use the Newton-Raphson method. The method starts with an initial guess and successively improves the solution with each iteration. Use the program as follows:")
print("1. Start by selecting an initial guess by moving the red dot.")
print("2. Press \"Set initial guess\" to initialize the Newton-Raphson method with the chosen starting guess.")
print("3. Press \"Step once\" to perform one iteration, continue until the solution stops improving. The iteration number, solution value, function value and estimated error are printed.")
print("4. Press \"Reset\" to reset the solver and try another initial guess. Quit the program by closing the figure window.")

def f(x):
    return x*x - 4*np.sin(x) - 1

def fprim(x):
    return 2*x - 4*np.cos(x)

# Setup the figure
xl, xr = -5, 5
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('Newton-Raphson method')

fig.subplots_adjust(left=0.10, bottom=0.15)

xx = np.linspace(xl,xr,1000);
yy = f(xx)

# Draw the initial plot. The 'line' variable is used for modifying the interval line later
ax.plot(xx,yy,label='y = f(x)',color='blue')
ax.plot(np.array([xl, xr]),np.array([0, 0]),'--',color='black',label='y = 0');
[line] = ax.plot([0],[0],'r*',label='Newton-Raphson');
ax.set_xlim([xl, xr])
ax.set_ylim([-10, 30])

# Define widgets and events
start_guess_slider_ax  = fig.add_axes([0.10, 0.10, 0.80, 0.03])
start_guess_slider_ax.set_frame_on(False)
start_guess_slider_ax.set_position(ax.get_position())
start_guess_slider = Slider(start_guess_slider_ax, '', xl, xr, valinit=0, facecolor='none', edgecolor='none')
start_guess_slider.valtext.set_visible(False)
start_guess_slider.vline.set_alpha(0)
def slider_on_changed(val):
    line.set_xdata(start_guess_slider.val)
    plt.draw()
    
start_guess_slider.on_changed(slider_on_changed)

reset_button_ax = fig.add_axes([0.8, 0.03, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')
def reset_button_on_clicked(mouse_event):
    global x, xvec, iter_no
    start_guess_slider.reset()
    if not iter_no == 0:
        start_guess_slider.set_active(True)
        iter_no = 0
        x = start_guess_slider.val
        xvec = []
        line.set_xdata(0)
        line.set_ydata([0])
        step_button.label.set_text('Set initial guess')
        plt.draw()
    
reset_button.on_clicked(reset_button_on_clicked)

iter_no = 0
err = float("NaN")
x = start_guess_slider.val
xvec = []
    
step_button_ax = fig.add_axes([0.10, 0.03, 0.2, 0.04])
step_button = Button(step_button_ax, 'Set initial guess', hovercolor='0.975', color='0.85')
def step_button_on_clicked(mouse_event):
    global x, iter_no, err, xvec, xl, xr
    if iter_no == 0:
        x = start_guess_slider.val
        err = float("NaN")
        print("\n{:^16s}\t{:^16s}\t{:^16s}\t{:^23s}".format("Iteration","x","f(x)","Estimated Error"))
        start_guess_slider.set_active(False)
        step_button.label.set_text('Step once')
    else:
        diff = f(x)/fprim(x)
        x = x - diff
        err = abs(diff)
             
    iter_no += 1
    xvec.append(x)
    print("{:^16d}\t{:^.16f}\t{:^.16f}\t{:^.16e}".format(iter_no,x,f(x),err))
    line.set_xdata(xvec)
    line.set_ydata(iter_no*[0])
    
    plt.draw()
    
step_button.on_clicked(step_button_on_clicked)

ax.legend()
plt.show()


