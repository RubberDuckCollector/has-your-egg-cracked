import datetime as dt
from datetime import date


current_year = date.today().year
current_month = date.today().month
current_day = date.today().day
next_year = current_year + 1

today = dt.datetime(current_year, current_month, current_day)

# today = dt.datetime(current_year, 1, 1)

next_egg_day = dt.datetime(next_year, 3, 31)

print(f"The next egg day is {next_egg_day}.")

if today >= dt.datetime(current_year, 1, 1) and today < dt.datetime(current_year, 3, 31):
    print("""
                ████████
              ██        ██
            ██▒▒▒▒        ██
          ██▒▒▒▒▒▒      ▒▒▒▒██
          ██▒▒▒▒▒▒      ▒▒▒▒██
        ██  ▒▒▒▒        ▒▒▒▒▒▒██
        ██                ▒▒▒▒██
      ██▒▒      ▒▒▒▒▒▒          ██
      ██      ▒▒▒▒▒▒▒▒▒▒        ██
      ██      ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒██
      ██▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒██
        ██▒▒▒▒  ▒▒▒▒▒▒    ▒▒▒▒██
        ██▒▒▒▒            ▒▒▒▒██
          ██▒▒              ██
            ████        ████
                ████████""")
    print("Your egg has not cracked!")
else:
    print("""
                  ▒▒
          ▓▓██░░▒▒▓▓▓▓░░░░██
          ▓▓                ██
        ▓▓░░▓▓██              ▓▓██
        ██░░░░██                  ████
      ▓▓░░░░▓▓░░                  ░░██
      ██░░░░░░██░░                    ▓▓██
      ██░░░░░░░░██░░░░                    ██████████
    ██░░░░░░▒▒██░░░░░░░░░░░░                        ██
    ██░░░░▒▒░░░░██░░░░░░░░░░░░░░░░  ░░░░        ░░░░██
    ██░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░▓▓██
    ██░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░░░░░██░░██
    ██░░░░░░░░░░░░░░▒▒░░░░░░██░░░░▓▓████░░░░░░██░░██
    ██░░░░░░░░░░░░░░▒▒░░░░░░░░██▓▓░░░░░░████░░██░░██
      ██░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒▒░░░░░░░░██░░██
      ██░░░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░██
        ██░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
        ░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██
            ████░░░░░░░░░░░░░░░░░░░░████
                ██▓▓██░░░░░░░░██████
                      ████████
    """)
    print("Your egg has cracked!")
    