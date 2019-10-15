from subprocess import call

'''
command = "find /tmp -name '*.jpg'"
subprocess.call(command.split())
'''
'''
imagepath  = "~/temp/scrot.png"
outfile = "~/temp/gocres.txt"
call(["scrot"], ['scrot.png'], ["-s"], ["-e"], ['mv $f ~/temp'])
call(["gocr"], ["-i"], ["~/temp/scrot.png"], ["-o"], ["~/temp/gocres.txt"])
call(["cat"],["~/temp/gocres.txt"])

shang mian [] taiduo, wrong
'''
def printfile(file,ifchi):
    res = ''
    with open(file,'r') as f:
        for line in f.readlines():
            res += line.strip()
            res += ' '
    if ifchi:
        res = res.replace(" ","")
    print(res)
    with open(file,'w') as f:
        f.write(res)
    #call("cat tessres.txt".split())#cat tessres.txt| xclip
    call("xclip -i tessres.txt".split())
    #print()
#call("scrot 'scrot.png' -s".split())
while True:
    userin = input('(s)creenshot or (q)uit?\n s for eng, sc for chinese >>>')
    if userin == "s":
        call(["scrot", "scrot.png","-s"])
    #    call("gocr -i scrot.png -o gocres.txt".split())
    #    call("cat gocres.txt".split())
        call("tesseract scrot.png tessres".split())
        print("**************************************************")
        #call("cat tessres.txt".split())
        printfile('tessres.txt',0)
        print("**************************************************")
        call("cp scrot.png scrotbak.png".split())
        call("rm scrot.png".split())
    if userin == "sc":
        call(["scrot", "scrot.png","-s"])
        call("tesseract scrot.png tessres -l eng+chi_sim".split())
        print("**************************************************")
        #call("cat tessres.txt".split())
        printfile('tessres.txt',1)
        print("**************************************************")
        print("**************************************************")
        call("cp scrot.png scrotbak.png".split())
        call("rm scrot.png".split())
    if userin == "q":
        print("*******************baibai************************")
        break
