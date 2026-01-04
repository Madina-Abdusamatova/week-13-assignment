
import requests
from datetime import datetime

def get_random_dog_image():

    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        data = response.json()
        if response.status_code == 200:
            return data["message"]
        return None
    except (requests.RequestException, ValueError):
        return None


def get_random_cat_fact():

    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url, timeout=6)
        response.raise_for_status()
        data = response.json()
        return data.get("fact")
    except (requests.RequestException, ValueError):
        return None


def show_menu():
    print("\n" + "=" * 50)
    print("     Random Pet Fun Generator    ")
    print("=" * 50)
    print("1. Show a random dog picture")
    print("2. Tell me a random cat fact")
    print("3. Show BOTH! (dog picture + cat fact) + SAVE to file")
    print("4. Quit")
    print("-" * 50)


def main():
    print("Welcome to Pet Fun Generator!")
    print("Using real live APIs from the internet\n")

    while True:
        show_menu()
        
        choice_str = input("What would you like to do? (1-4): ").strip()
        
        try:
            choice = int(choice_str)
        except ValueError:
            print("Please enter a number between 1 and 4.\n")
            continue
        
        if choice == 4:
            print("\nThanks for playing!  ")
            print("Session ended:", datetime.now().strftime("%Y-%m-%d %H:%M"))
            break

        elif choice == 1:
            print("\nSearching for a cute dog... ", end="")
            image_url = get_random_dog_image()
            
            if image_url:
                print("Got it!")
                print("Dog picture link:", image_url)
                print("Paste it into your browser! ")
            else:
                print("Sorry... couldn't get a dog picture right now ")

        elif choice == 2:
            print("\nAsking the cats for wisdom...")
            fact = get_random_cat_fact()
            
            if fact:
                print("\nA fact from a VERY WISE CAT:\n")
                print(f"\"{fact}\"")
                
            else:
                print("The cats are keeping their secrets today...")

        elif choice == 3:
            print("\nMaximum cuteness loading...")
            
            dog_url = get_random_dog_image()
            cat_fact = get_random_cat_fact()
            
            print("\n" + "═" * 60)
            
            if dog_url:
                print(" Random Dog Picture:")
                print(dog_url)
            else:
                print(" Couldn't fetch a dog picture this time...")
                
            print()
            
            if cat_fact:
                print(" Cat Wisdom:")
                print(f"\"{cat_fact}\"")
            else:
                print(" No cat fact available right now...")
                
            print("═" * 60)

            if dog_url or cat_fact:
                filename = f"pet_fun_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                try:
                    with open(filename, "w") as file:
                        file.write("Pet Fun Session\n")
                        file.write("=" * 30 + "\n")
                        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
                        
                        if dog_url:
                            file.write("Dog Picture URL:\n")
                            file.write(f"{dog_url}\n\n")
                        if cat_fact:
                            file.write("Cat Fact:\n")
                            file.write(f"\"{cat_fact}\"\n")
                    
                    print(f"\nResults saved successfully to: {filename}")
                except :
                    print(f"\nCouldn't save file... sorry")
            else:
                print("\nNothing to save this time...")

        else:
            print("Please choose a number between 1 and 4.")

        input("\nPress Enter to continue... ")


print("Starting Pet Fun Generator...\n")
main()

