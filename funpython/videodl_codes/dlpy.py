from subprocess import call
import sys
# import shlex, subprocess

#python3 dlpy.py https://www.bilibili.com/video/av58129929/?p= 3 58 ./PrinciplesofComputerOrganization

# >>> import shlex, subprocess
# >>> command_line = input()
# /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
# >>> args = shlex.split(command_line)
# >>> print(args)
# ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
# >>> p = subprocess.Popen(args) # Success!

url = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
path = sys.argv[4]


#url = input('download_url, eg: https://www.bilibili.com/video/av51992761/?p= :\n>>>')
#start = int(input('start number,eg: 1 :>>>'))
#end = int(input('end number,eg: 10 :>>>'))
#path = (input('save path :>>>'))
#call("cd {}".format(path).split())
#call(["cd",path])
for index in range(start,end+1):
    tempurl = url+str(index)

    # command_line = "you-get {} -o {}".format(tempurl, path)
    # args = shlex.split(command_line)
    # subprocess.Popen(args)

    call(["you-get",tempurl,"-o",path])


    # print(tempurl)
    # input('<<<<<<<<<<<<<')
    # call(["screencapture","-i", "./GUI/screenshot.png"])
    #try:
    #call(["you-get",tempurl])
    # call("you-get {} -o {}".format(tempurl, path))
    #except:
    #       print("download failed")
