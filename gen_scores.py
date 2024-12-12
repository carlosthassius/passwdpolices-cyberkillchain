from zxcvbn import zxcvbn
import pandas as pd

passwds = pd.read_csv('passwd.csv',header=0)

print(f"\n\n|{'Password':<{16}}|{'Security Score':<{15}}|{'Feedback':<{55}}|{'Guesses':<{18}}|")

for i in passwds:
    score = zxcvbn(i)['score']
    feedback = zxcvbn(i)['feedback']['warning']
    if(len(feedback)==0): feedback = "-"
    guesses = zxcvbn(i)['guesses']
    #dic = zxcvbn(i)['dictionary_name']
    #print(zxcvbn(i))
    print(f'|{i:<{16}}|{score:<{15}}|{feedback:<{55}}|{guesses:<{18}}|')
print()
