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
def on_closing():
	turn_off_all_led()
	GPIO.cleanup()
	root.destroy()
root=tk.Tk()
root.title("Led controller")
radio_var=tk.IntVar()
radio_red=tk.Radiobutton(root,text="red",variable=radio_var,value=1,command=turn_on_red)
radio_red.pack(anchor=tk.W)
radio_green=tk.Radiobutton(root,text="green",variable=radio_var,value=2,command=turn_on_green)
radio_green.pack(anchor=tk.W)
radio_blue=tk.Radiobutton(root,text="blue",variable=radio_var,value=3,command=turn_on_blue)
radio_blue.pack(anchor=tk.W)
exit.button=tk.Button(root,text="exit",command=on_closing)
exit.button.pack(anchor=tk.W)
root.protocol("WM_delete_window",on_closing)
root.mainloop()


	
	
