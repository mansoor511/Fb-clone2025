import time
import random
from rich.console import Console

console = Console()

def print_header():
    console.print("**********************************", style="bold green")
    console.print("[*] Developer: MANSOOR", style="bold cyan")
    console.print("[*] FACEBOOK: https://www.facebook.com/profile.php?id=100075435417249", style="bold cyan")
    console.print("[*] YOUTUBE: https://youtube.com/@technical_biktricks?si=VkQbDFzj9HHEujai", style="bold cyan")
    console.print("[*] TELEGRAM: https://t.me/technical_bik", style="bold cyan")
    console.print("**********************************\n", style="bold green")

def fake_processing():
    console.print("[+] OK RESULTS SAVED IN -> ok.txt", style="bold green")
    console.print("[+] CP RESULTS SAVED IN -> cp.txt", style="bold green")
    console.print("[!] IF NO RESULT USE AIRPLANE MODE\n", style="bold magenta")
    time.sleep(1)

    while True:
        status = random.choice(["OK", "CP"])

        
        random_id = str(random.randint(10000000000000, 99999999999999))  

        
        random_password = str(random.randint(10000000, 99999999)) 

        if status == "OK":
            console.print(f"[ MANSOOR - OK ] {random_id} | {random_password}", style="bold green")
        else:
            console.print(f"[ MANSOOR - CP ] {random_id} | {random_password}", style="bold yellow")
        
        time.sleep(0.3)

if __name__ == "__main__":
    print_header()
    fake_processing()
