import time
import random
from rich.console import Console

console = Console()

def print_header():
    console.print("**********************************", style="bold green")
    console.print("[*] Developer: MANSOOR", style="bold cyan")
    console.print("[*] FACEBOOK: www.facebook.com/profile.php?id=100075435417249", style="bold cyan")
    console.print("[*] YOUTUBE: https://youtube.com/@technical_biktricks?si=GMkj0jawLyrLYdtt", style="bold cyan")
    console.print("[*] TELEGRAM: https://t.me/technical_bik", style="bold cyan")
    console.print("**********************************\n", style="bold green")

def fake_processing():
    console.print("[+] OK RESULTS SAVED IN -> ok.txt", style="bold green")
    console.print("[+] CP RESULTS SAVED IN -> cp.txt", style="bold green")
    console.print("[!] IF NO RESULT USE AIRPLANE MODE\n", style="bold magenta")
    time.sleep(1)

    while True:  
        status = random.choice(["OK", "CP"])
        user_id = random.randint(100000000000000, 100000099999999)
        password = random.randint(12345678, 99999999)
        
        if status == "OK":
            console.print(f"[ MANSOOR - OK ] {user_id} | {password}", style="bold green")
        else:
            console.print(f"[ MANSOOR - CP ] {user_id} | {password}", style="bold yellow")
        
        time.sleep(0.3) 

if __name__ == "__main__":
    print_header()
    fake_processing()
