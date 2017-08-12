# iota_seed_generator
Random seed generator for Iota


To generate a random iota_string:

1. Clone this repo
2. cd into the iota_seed_generator repo
3. run python generate.py

This will generate two files:

1. iota.seed -- which is your new seed, and will be overwritten each time you run the program.
2. .iota_history -- which is a log of the seeds you have created.

Run python generate.py -h for the help menu.

This script uses the secrets module that was introduced in Python 3.6, which uses a more cryptographically
secure method of randomness which is provided by your operating system.  As such this must be used with
Python versions >= 3.6   

