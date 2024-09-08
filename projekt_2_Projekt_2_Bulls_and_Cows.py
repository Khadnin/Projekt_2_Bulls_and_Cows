"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Laskafeld
email: ondrej.laskafeld@gmail.com
discord: khadnin
"""

# Importování knihovny pro náhodný výběr a čas
import random
import time

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Všechny funkce

# Funkce na otestování zda je vstup číslo, zda jsou všechny číslice unikátní, zda délka má požadovanou délku, a zároveň že není první číslice nula
def guess_correct(num):
    if num.isdigit() and (len(set(str(num))) == number_length) and (len(str(num)) == number_length) and (num[0] != "0") == True:
        return True
    else:
        return False

# Funkce na vytvoření seznamu číslic ze zadaného čísla
def make_num_to_list(number):
    return [digit for digit in str(number)]

# Funkce na vrácení stráveného času hádáním
def time_result():
    end_time = round(abs(start_time - time.time()), 1)
    return(print("It took you", end_time, "s.\n") )

# Funkce pro zobrazení počtu pokusů (podle počtu pokusů)
def attempt_result(attempts_amount):
    if attempts_amount == 1:
        return(print(
            "Correct, you've guessed the right number in ", attempts, " quess!\n"
            "-----------------------------------------------------------------"
            )
        )
    elif attempts_amount > 1:
        return(print(
            "Correct, you've guessed the right number in ", attempts, " quesses!\n"
            "-----------------------------------------------------------------"
            )
        )

#--------------------------------------------------------------------------------------------------------------------------------------------------

# Délka čísla, které se bude hádat (max 10!)
number_length = 4

# Seznam číslic na výběr
list_of_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generování prvního čísla (bez 0)
first_digit = random.randint(1, 9)

# Odstranění první číslice z možných číslic pro další výběr
list_of_digits.remove(first_digit)

# Převod prvního čísla na text, z důvodů budoucího spojování generovaných číslic
final_number = str(first_digit)

# Pro zvolenou délku čísla náhodný výběr ze seznamu číslic, vymazaní vybrané číslice ze seznamu ať se neopakuje a připojení k existujícímu číslu
for i in range(number_length - 1):
    random_digit = random.choice(list_of_digits)
    final_number = final_number + (str(random_digit))
    list_of_digits.remove(random_digit)

print(final_number)

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
active_game = True

while active_game == True:
    guess = input("Enter a number (in case you want to exit, wrote 'exit'): ")
    bulls = 0
    cows = 0
# Podmínka pro možné ukončení než člověk přijde na výsledek
    if guess == "exit":
        active_game = False
        print("Terminating script. The number was:", final_number)
# Otestování vstupu
    elif guess_correct(guess):
        attempts += 1  
# Převedení zadaného vstupu a hádaného čísla na seznamy pro porovnání
        guess_list = make_num_to_list(guess)
        number_list = make_num_to_list(final_number)
# Cyklus pro procházení tolikrát jak je dlouhé hádané číslo 
        for i in range(len(final_number)):
# Kontrola "bulls" - zda je hádaná číslice v čísle rovna číslici na stejné pozici hádaného čísla
            if guess_list[i] == number_list[i]:
                bulls += 1
# Kontrola "cows" - zda je hádaná číslice v čísle v hádaném čísle (seznamu)
            elif guess_list[i] in number_list:
                cows += 1
# Zjišťování zda je číslo uhádnuto celé a podle počtu pokusů "vytiskne" výsledek nebo vypíše počet bulls a cows a pokračuje se
        if bulls == number_length:
            attempt_result(attempts)
            print("That's amazing!")
            time_result()  
            active_game = False
        elif bulls == number_length and attempts > 2 and attempts <= 5:
            attempt_result(attempts)
            print("That's amazing!")
            time_result()  
            active_game = False
        elif bulls == number_length and attempts > 6 and attempts <= 15:
            attempt_result(attempts)
            print("That's average!")
            time_result()  
            active_game = False
        elif bulls == number_length and attempts > 15:
            attempt_result(attempts)
            print("That's not so good!")
            time_result()  
            active_game = False
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