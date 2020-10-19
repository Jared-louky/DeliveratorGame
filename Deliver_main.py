import sys, time 


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print("Hello, candidate. Welcome to CosaNostra Pizza Company, A 'Family' run 'corperate' conclomerant."
      "We are now using a simluation to find the right individuals to fill roles in our delivery department")


player_name = input("What is your name?  ")