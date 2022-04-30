# Password generator
Attempt to create a hard to break easy to remember password generator
Currently we use ~3000 french words to create passwords
See precisions [here](https://diceware.dmuth.org/)

# Installation
- `git clone https://github.com/martmull/password_gen.git`
- `cd password_gen`

# Generate password
- `python gen_password.py --lenght 5` to generate a 5 words password
- `python gen_password.py --lenght 5 --salt` to add 10 points of entropy
- `python gen_password.py --help` to display help

