import time
import random
from rich.console import Console

# استفاده از rich برای نمایش رنگی
console = Console()

# معرفی توابع برای نمایش داده‌ها
def print_header():
    console.print("**********************************", style="bold green")
    console.print("[*] Developer: ALI KHAN", style="bold cyan")
    console.print("[*] FACEBOOK: web.facebook.com/ali.t", style="bold cyan")
    console.print("[*] YOUTUBE: www.youtube.com/proxicode", style="bold cyan")
    console.print("[*] GITHUB: www.github.com/pro-xidoc", style="bold cyan")
    console.print("**********************************\n", style="bold green")

def fake_processing():
    console.print("[+] OK RESULTS SAVED IN -> ok.txt", style="bold green")
    console.print("[+] CP RESULTS SAVED IN -> cp.txt", style="bold green")
    console.print("[!] IF NO RESULT USE AIRPLANE MODE\n", style="bold magenta")
    time.sleep(1)

    # چاپ شماره و رمز مشخص شما فقط یکبار در ابتدای کد
    console.print(f"[ ALI - OK ] 0789053529 | 928727", style="bold red")
    time.sleep(0.5)

    # ادامه کدها به‌طور بی‌پایان
    while True:  
        status = random.choice(["OK", "CP"])
        user_id = random.randint(100000000000000, 100000099999999)
        password = random.randint(12345678, 99999999)
        
        if status == "OK":
            console.print(f"[ ALI - OK ] {user_id} | {password}", style="bold green")
        else:
            console.print(f"[ ALI - CP ] {user_id} | {password}", style="bold yellow")
        
        time.sleep(0.3)  # تاخیر برای طبیعی‌تر نشان دادن اجرا

# اجرای کد
if __name__ == "__main__":
    print_header()
    fake_processing()
