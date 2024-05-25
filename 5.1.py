import tkinter as tk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
red_led=17
green_led=27
blue_led=22
GPIO.setup(red_led,GPIO.OUT)
GPIO.setup(green_led,GPIO.OUT)
GPIO.setup(blue_led,GPIO.OUT)
def turn_off_all_led():
	GPIO.output(red_led,GPIO.LOW)
	GPIO.output(green_led,GPIO.LOW)
	GPIO.output(blue_led,GPIO.LOW)
def turn_on_red():
	turn_off_all_led()
	GPIO.output(red_led,GPIO.HIGH)
def turn_on_green():
	turn_off_all_led()
	GPIO.output(green_led,GPIO.HIGH)
def turn_on_blue():
	turn_off_all_led()
	GPIO.output(blue_led,GPIO.HIGH)
def handle_input():
	color=entry.get().strip().lower()
	if color=='red':
		turn_on_red()
	elif color=='green':
		turn_on_green()
	elif color=='blue':
		turn_on_blue()
	else:
		messagebox.showerror("Error","invalid")
def on_closing():
	turn_off_all_led()
	GPIO.cleanup()
	root.destroy()
root=tk.Tk()
root.title("Led controller")

label=tk.Label(root,text="enter color")
label.pack(anchor=tk.W)

entry=tk.Entry(root)
entry.pack(anchor=tk.W)

submit_button=tk.Button(root,text="Submit",command=handle_input)
submit_button.pack(anchor=tk.W)

exit_button=tk.Button(root,text="exit",command=on_closing)
exit_button.pack(anchor=tk.W)
root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()


	
	
