"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Laskafeld
email: ondrej.laskafeld@gmail.com
discord: khadnin
"""

# Importování knihovny pro náhodný výběr a čas
import random
import time

# Délka čísla, které se bude hádat (max 10!)
number_length = 4

# Seznam číslic na výběr
list_of_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generování prvního čísla (bez 0)
first_digit = random.randint(1, 9)

# Odstranění první číslice z možných číslic pro další výběr
list_of_digits.remove(first_digit)

# Převod prvního čísla na text, z důvodů budoucího spojování generovancýh číslic
final_number = str(first_digit)

# Pro zvolenou délku čísla náhodný výběr ze seznamu číslic, vymazaní vybrané číslice ze seznamu ať se neopakuje a připojení k existujícímu číslu
for i in range(number_length - 1):
    random_digit = random.choice(list_of_digits)
    final_number = final_number + (str(random_digit))
    list_of_digits.remove(random_digit)

# "Uvítání soutěžícího" :)  
print(
    "Hi there!\n"
    "-----------------------------------------------\n"
    "I've generated a random 4 digit number for you.\n"
    "Let's play a bulls and cows game.\n"
    "-----------------------------------------------\n"
    )

# Definování proměnných pro počítání počtu pokusů, času a podmínky ukončení while cyklu
attempts = 0
start_time = time.time()
x = 1

while x == 1:
    guess = input("Enter a number (in case you want to exit, wrote 'exit'): ")
    bulls = 0
    cows = 0
# Podmínka pro možné ukončení než člověk přijde na výsledek
    if guess == "exit":
        x = 0
        print("Terminating script. The number was:", final_number)
# Otestování zda je vstup číslo, zda jsou všechny číslice unikátní, zda délka má požadovanou délku, a zároveň že není první číslice nula
    elif guess.isdigit() and (len(set(str(guess))) == number_length) and (len(str(guess)) == number_length) and (guess[0] != "0") == True:
# Zjištění počtu "cows" skrz překrytí setů vstupu a generovaného čísla
        guess_set = set(guess)
        number_set = set(final_number)
        cows = len(guess_set.intersection(number_set))
        attempts += 1
# Zjištění počtu "bulls" procházením jednotlivých číslic/cifer
        for i in range(len(final_number)):
            if guess[i] == final_number[i]:
                bulls += 1
# Zjišťování zda je číslo uhádnuto celé a podle počtu pokusů "vytiskne" výsledek nebo vypíše počet bulls a cows a pokračuje se
        if bulls == number_length and attempts == 1:
            print(
                "Correct, you've guessed the right number in ", attempts, " quess!\n"
                "-----------------------------------------------------------------\n"
                "That's amazing!"
                )
            end_time = round(abs(start_time - time.time()), 1)
            print("It took you", end_time, "s.")   
            x = 0
        elif bulls == number_length and attempts > 1 and attempts <= 5:
            print(
                "Correct, you've guessed the right number in ", attempts, " quesses!\n"
                "-----------------------------------------------------------------\n"
                "That's amazing!"
                )
            end_time = round(abs(start_time - time.time()), 1)
            print("It took you", end_time, "s.")   
            x = 0
        elif bulls == number_length and attempts > 5 and attempts <= 15:
            print(
                "Correct, you've guessed the right number in ", attempts, " quesses!\n"
                "-----------------------------------------------------------------\n"
                "That's average!"
                )
            end_time = round(abs(start_time - time.time()), 1)
            print("It took you", end_time, "s.")       
            x = 0
        elif bulls == number_length and attempts > 15:
            print(
                "Correct, you've guessed the right number in ", attempts, " quesses!\n"
                "-----------------------------------------------------------------\n"
                "That's not so good!"
                )
            end_time = round(abs(start_time - time.time()), 1)
            print("It took you", end_time, "s.")        
            x = 0
        else:
            print(
                "Bulls:", bulls, "\n"
                "Cows:", cows, "\n"
                "-----------------------------------------------"
                )
# V případě, že je něco blbě se vstupem vypíše se následující
    else:
        attempts += 1
        print("\n"
            "--------------------------------------------------------------------------------------------------------------------------\n"
            "Entered number should be 4 digits long, not start with '0', do not have duplicated digits or contain nondigits characters.\n"
            "--------------------------------------------------------------------------------------------------------------------------\n"
            )