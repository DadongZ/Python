i = 1

while i <= 10:
    print(i)
    i += 1

print('Done with loop')


secret_word = "Alex"

guess = ""
guess_count = 0
guess_limit = 3
out_of_guess =False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count +=1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN!")


