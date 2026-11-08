from datetime import date, datetime, timezone

def register_session():
    training_date = datetime.today().strftime("%Y-%m-%d")
    training_type = input("What did you train today? ")
    duration = int(input("How long was your session? "))
    total_shots = int(input("How many shots taken? "))
    shots_on_targ = int(input("How many on target? "))
    intensity = int(input("Intensity (1-10): "))

    print("Summary:\n")
    print(f"Date: {training_date}")
    print(f"Training Type: {training_type}")
    print(f"Duration: {duration}")
    print(f"Total Shots: {total_shots}")
    print(f"Shots on Target: {shots_on_targ}")
    print(f"Intensity: {intensity}")
    
def menu():
        while True:
            print("===== SOCCER TRACKER =====")
            print("1. Register training")
            print("2. View statistics")
            print("3. Exit")

            option = input("Choose an option: ")

            if option == "1":
                register_session()
            elif option == "2":
                print("View statistics")
            elif option == "3":
                print("Exit")
            
                break

            else:
                print("Invalid option")

if __name__ == "__main__":
    menu()






