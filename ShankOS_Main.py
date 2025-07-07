#String library
#Only use tab indents and enter-key, nothing else

introscreendisplaytext = "Ima Shank you good if you dont work ya damn program!!!"

menuselectionlist = ["nano"]

def introscreendisplay():
	print(introscreendisplaytext)
def menu():
	print("enter selection that you would like to proceed in")
	print(menuselectionlist)
	menuselection = input()
	if menuselection == "nano":
		print("nano")
	else:
		print("else-output")

introscreendisplay()

menu()
