import os
from prettytable.prettytable import NONE
from win10toast import ToastNotifier



def clrscr():
   if os.name == 'posix':
      os.system('clear')
   else:
      os.system('cls')


def notify(eligible_centers_count:int):
   try:
      toaster = ToastNotifier()
      toaster.show_toast("Vaccine Slots are available", f"You're eligible for total {eligible_centers_count} centers.", icon_path=None, duration=10)
   except Exception as e:
      print('[-] An Exception Occurred!')
      print(e)