import random
from sys import argv
import datetime
import secrets


now = datetime.datetime.now()
iota_seed_length = 81
history_excempt = False

# Generate seed
def iota_seed_generator(seed_length=iota_seed_length):
    population = "ABCDEFGHIJKLMNOPQRSTUVWXYZ9"
    out_string = ""
    for x in range(seed_length):
        out_string = out_string + secrets.choice(population)
    return out_string


# Handle system arguments
try:
    custom_length = int(argv[1])
    if custom_length < 81:
        iota_seed_length = custom_length

except:
    try:
        if argv[1] == '-e':
            history_excempt = True
        if argv[1] == '-h':
            with open('.options') as options:
                print(options.read())
    except:
        pass
try:
    if argv[2] == '-e':
        history_excempt = True
except:
    pass


# Generate iota.seed file
iota_seed = iota_seed_generator()
out_file = open('iota.seed', 'w')
out_file.write(iota_seed)
out_file.close()


# Handle history file
if not history_excempt:
    try:
        with open('.iota_history', 'a') as hist_file:
            hist_file.write("\n" + iota_seed + " " + now.strftime("%Y-%m-%d %H:%M:%S"))
    except:
        hist_file = open('.iota_history', 'w')
        hist_file.write(iota_seed + " " + now.strftime("%Y-%m-%d %H:%M:%S"))
        hist_file.close()
