import requests, pyautogui, subprocess, selenium, time, os.path, os
import selenium.webdriver



def keygen():
    print("Generating key.\nMove your cursor around for 10 seconds.")
    x = 0
    y = 0
    for _ in range(1000):
        z = pyautogui.position()
        x += z[0]
        y += z[1]
        time.sleep(0.01)
    browser = selenium.webdriver.Chrome()
    
    browser.get("https://polarplunge.secureplayer.camzonecdn.com/v1.3/CamzoneStreamPlayer?iframe=yes&channel=polarplunge&muted=yes&mutebutton=no&czlogourl=&toolbar=always&backgroundcolor=000000&toolbarbgcolor=ffffff&toolbaralpha=100&toolbartextcolor=000000&epostcard=yes&toolbartype=new&toolbarposition=topright")
    time.sleep(x % 5 + y % 3)
    x = str(x)
    y = str(y)
    browser.save_screenshot("out.png")
    browser.close()
    imghash = subprocess.run("powershell -File run2.ps1 f out.png", capture_output=True).stdout.decode("utf-8").strip()
    subprocess.run("powershell rm out.png")
    xhash = subprocess.run("powershell -File run2.ps1 t " + x, capture_output=True).stdout.decode("utf-8").strip()
    yhash = subprocess.run("powershell -File run2.ps1 t " + y, capture_output=True).stdout.decode("utf-8").strip()
    out = subprocess.run("powershell -File run2.ps1 t " + (xhash + imghash), capture_output=True).stdout.decode("utf-8").strip() + subprocess.run("powershell -File run2.ps1 t " + (yhash + imghash), capture_output=True).stdout.decode("utf-8").strip()
    return out


def unlock():
    if not os.path.isfile("data/key.txt"):
        print("Create an account first.")
        exit()
    password = input("Enter your first password: ")
    password2 = input("Enter your second password: ")
    k = "0" * 128
    k = subprocess.run("powershell -File run2.ps1 t " + password, capture_output=True).stdout.decode("utf-8").strip() + subprocess.run("powershell -File run2.ps1 t " + password2, capture_output=True).stdout.decode("utf-8").strip()
    p = open("data/key.txt", "r").readlines()[0].strip()
    hashed = subprocess.run("powershell -File run.ps1 cipher.gls 2 " + p[:(int(len(p)/2))] + " " + k, capture_output=True).stdout.decode("utf-8").strip() + subprocess.run("powershell -File run.ps1 cipher.gls 2 " + p[(int(len(p)/2)):] + " " + k, capture_output=True).stdout.decode("utf-8").strip()
    d = [i.strip().split("|") for i in open("data/data.txt", "r").readlines()]
    with open("t.txt", "a+") as f:
        for i in d:
            x1 = subprocess.run("powershell -File run.ps1 cipher.gls 2 " + i[0] + " " + hashed, capture_output=True).stdout.decode("utf-8").strip()
            x2 = subprocess.run("powershell -File run.ps1 cipher.gls 2 " + i[1] + " " + hashed, capture_output=True).stdout.decode("utf-8").strip()
            x3 = subprocess.run("powershell -File run.ps1 cipher.gls 2 " + i[2] + " " + hashed, capture_output=True).stdout.decode("utf-8").strip()
            f.write(x1 + "|" + x2 + "|" + x3 + "\n")
    return hashed, password, password2, k

# site username password

def access():
    print("** Site|Username|Password **\n")
    with open("t.txt", "r") as f:
        d = f.readlines()
        for i in d:
            print(i)

def enter():
    site = input("Enter site name: ")
    user = input("Enter username: ")
    passw = input("Enter password: ")
    with open("t.txt", "a+") as f:
        f.write(f"{site}|{user}|{passw}\n")


def create():
    if os.path.isfile("data/key.txt"):
        print("Account already exists.")
        exit()
    pass1 = input("Enter first password: ")
    pass2 = input("Enter second: ")
    with open("data/key.txt", "a+") as f:
        f.write(subprocess.run("powershell -File run.ps1 cipher.gls 1 2 " + "a" * 128 + " poop", capture_output=True).stdout.decode("utf-8").strip() * 2)
    with open("data/data.txt", "a+") as f:
        pass
    return pass1, pass2


def main():
    a = input("(U)nlock, or (C)reate account: ")
    pass1 = ""
    pass2 = ""
    kee = "0"
    if a.upper() == "U":
        kee, pass1, pass2, u = unlock()
    elif a.upper() == "C":
        create()
        exit()
    else:
        exit()
    while True:
        b = input("(A)ccess passwords or (E)nter more (nothing to quit): ")
        if b.upper() == "A":
            access()
        elif b.upper() == "E":
            enter()
        else:
            break
    r = keygen()
    with open("data/data.txt", "w") as _:
        pass
    d = open("t.txt", "r").readlines()
    with open("data/data.txt", "a") as f:
        for i in d:
            x = i.strip().split("|")
            p1 = subprocess.run("powershell -File run.ps1 cipher.gls 1 2 " + r + " " + x[0], capture_output=True).stdout.decode("utf-8").strip()
            p2 = subprocess.run("powershell -File run.ps1 cipher.gls 1 2 " + r + " " + x[1], capture_output=True).stdout.decode("utf-8").strip()
            p3 = subprocess.run("powershell -File run.ps1 cipher.gls 1 2 " + r + " " + x[2], capture_output=True).stdout.decode("utf-8").strip()
            f.write(f"{p1}|{p2}|{p3}\n")
    with open("data/key.txt", "w") as _:
        pass
    with open("data/key.txt", "a") as f:
        l = subprocess.run("powershell -File run.ps1 cipher.gls 1 2 " + u + " " + r[:(int(len(r)/2))], capture_output=True).stdout.decode("utf-8").strip() + subprocess.run("powershell -File run.ps1 cipher.gls 1 2 " + u + " " + r[int((len(r)/2)):], capture_output=True).stdout.decode("utf-8").strip()
        f.write(l)
    with open("t.txt", "w") as _:
        pass
    os.remove("t.txt")




if __name__ == "__main__":
    #print(keygen())
    main()