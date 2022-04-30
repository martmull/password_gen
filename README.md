# Password generator
Attempt to create a hard to break easy to remember password generator.
Currently, we use:
- a ~3000 [english words dictionary](dictionaries/english_common_words.txt)
- a ~4400 [french words dictionary](dictionaries/french_common_words.txt)

See precisions [here](https://diceware.dmuth.org/)

![image](https://user-images.githubusercontent.com/29927851/166083159-792a4c3b-2646-468d-9833-d028febc3ddc.png)

# Installation
- `git clone https://github.com/martmull/password_gen.git`
- `cd password_gen`
- `pip install -r requirements.txt`

# Generate password
Generated password is capitalized and contains `0.` at the end in order to match common
password rules. e.g: `Johndoe0.`

- `python gen_password.py` to generate a 6 words password
- `python gen_password.py --length 5` to generate a 5 words password
- `python gen_password.py --length 5 --salt` to add 10 points of entropy
- `python gen_password.py --length 5 --salt --english_only` to use only english dictionary
- `python gen_password.py --help` to display help

# Usage
`python gen_password.py` returns:
> 2022-04-30 11:03:07.066 | INFO     | __main__:generate_password:75 - Rendit age lawyer cherche html taste 0. 
> (Entropy: 76 - Dictionary: 6544 words)

You can remove spaces and use this password `Renditagelawyercherchehtmltaste0.`
