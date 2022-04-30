# Password generator
Attempt to create a hard to break easy to remember password generator.
Currently we use ~4400 french words to create passwords.

See precisions [here](https://diceware.dmuth.org/)

![image](https://user-images.githubusercontent.com/29927851/166083159-792a4c3b-2646-468d-9833-d028febc3ddc.png)

# Installation
- `git clone https://github.com/martmull/password_gen.git`
- `cd password_gen`
- `pip install -r requirements.txt`

# Generate password
- `python gen_password.py` to generate a 6 words password
- `python gen_password.py --length 5` to generate a 5 words password
- `python gen_password.py --length 5 --salt` to add 10 points of entropy
- `python gen_password.py --help` to display help
