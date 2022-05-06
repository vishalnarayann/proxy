from colorama import Fore
import time
import secrets
from random import randint
import random

a = random. randint(1,999)
b = random. randint(1,999)
c = random. randint(1,999)
d = random. randint(1,999)
e = random. randint(1000,9999)
f = (1)


continuing = True

import random
n = random.randint(0,999)

print(Fore.CYAN + (str(n) + " ACTIVE MEMBERS"))
time.sleep(0.75)
print(Fore.CYAN + "Connecting to Pub01 server")
time.sleep(0.75)
print(Fore.CYAN + "[Loading]")
time.sleep(1.0)
print(Fore.CYAN + "[Initialized]")
time.sleep(0.75)
print(Fore.CYAN + "[Loading Wallet List]")
time.sleep(1.25)
print(Fore.CYAN + "[Done]")
time.sleep(0.75)
print(Fore.CYAN + "[Matching Hash]")
time.sleep(1.25)
print(Fore.CYAN + "[Complete]")
time.sleep(0.75)
print(Fore.WHITE +"[Ready]")
time.sleep(0.75)

answer = input ("Enter a valid key license: ")
if answer.lower() == "v":
  continuing = True
time.sleep(1.5)
print("Your key expires on Friday, January 24, 2025")
time.sleep(1.5)
answers = input ("Thread amount (higher can cause ratelimits): ")
time.sleep(1.5)
print("Starting in proxy mode...")

time.sleep(4.0)
for _ in range(1):
  print(Fore.RED + "Priv | " + "5" + secrets.token_hex(27) + " | Proxy: " + str(a) + "." + str(b) + "." + str(c) + "." + str(d) + " : " + str(e))

while True:
  if continuing == True:
    for _ in range(100000):
      print(Fore.WHITE + "Balance: 0 BTC" + Fore.RED + " [X]" + " Trying 1" + secrets.token_hex(27) + " | Proxy: " + str(a) + "." + str(b) + "." + str(c) + "." + str(d) + " : " + str(e))
