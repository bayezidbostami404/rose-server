import os
import sys
import time
import hashlib
import requests

# আপনার নিজস্ব GitHub Raw ফাইলের লিংক এখানে বসাবেন (যেখানে Approved কী-গুলো থাকবে)
GITHUB_URL = "https://githubusercontent.com"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def check_approval():
    clear_screen()
    print('\033[38;5;46mROSE SERVER LOADING....\033[0m')
    time.sleep(1.5)
    clear_screen()

    # ডিভাইসের ইউনিক আইডি তৈরি (লকাল মেকানিজম)
    try:
        user_login = os.getlogin()
    except Exception:
        user_login = "user"
        
    try:
        user_uid = str(os.getuid())
    except AttributeError:
        user_uid = "1000"

    uuid_raw = user_login + user_uid
    generated_key = hashlib.md5(uuid_raw.encode()).hexdigest().upper()[:12]
    final_key = f"ROSE-{generated_key}"

    print('========================================')
    print(f"\033[1;37mYOUR KEY : \033[1;32m{final_key}\033[0m")
    print('========================================')
    print("\033[1;36m[*] Checking authorization with Rose Server...\033[0m")
    time.sleep(2)

    # আপনার গিটহাব রিপোজিটরি থেকে অনুমোদিত কী-র তালিকা যাচাইকরণ
    try:
        response = requests.get(GITHUB_URL, timeout=10)
        if response.status_code == 200:
            approved_list = response.text.splitlines()
            # ফাইলে কী-টি আছে কিনা তা চেক করা
            if final_key in [k.strip() for k in approved_list]:
                print("\033[1;32m[+] Access Granted! Welcome to Rose Server.\033[0m")
                time.sleep(2)
                main_tool()
            else:
                print("\033[1;31m[-] Access Denied! Your key is not approved.\033[0m")
                sys.exit()
        else:
            print("\033[1;31m[-] Server Error: Unable to fetch approval list.\033[0m")
            sys.exit()
    except requests.exceptions.RequestException:
        print("\033[1;31m[-] Network Error: Check your internet connection.\033[0m")
        sys.exit()

def main_tool():
    clear_screen()
    print("========================================")
    print("      ROSE SERVER MAIN TOOL MENU        ")
    print("========================================")
    # আপনার টুলের মূল কোড বা ফাংশনগুলো এখানে যুক্ত করুন
    print("[1] Start Task")
    print("[2] Exit")

if __name__ == "__main__":
    check_approval()
