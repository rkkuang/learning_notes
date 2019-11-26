#https://api.wanmen.org/4.0/recommend/course/5d8dd249cdc3c553fb677baa?limit=15

from urllib import request
from urllib.request import urlopen
import json
import os
import sys
import time
from subprocess import call
abspath = os.path.abspath('./')
savedir = "./wm"


headers ={
"Accept": "vnd.wanmen.v8+json",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjViZmI3NDBjNmY1NWRmMGQ0Y2Q3MDE5MiIsImlhdCI6MTU3NDY5MTM2NywiZXhwIjoxNTc3MjgzMzY3LCJpc3MiOiJ1cm46YXBpIn0.LfbKzNEKSmhp5GaKQWXEoxivFfw0eFa7WINs_eNj5FQ",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
"X-App": "uni",
"X-Time": "5ddd1a01",
"X-Token": "e420d7c8dc24da0c2b6ed3f9219aa2bd",
"Sec-Fetch-Mode": "cors",
"Origin": "https://www.wanmen.org",
}
# "X-App": "uni",
# "X-Time": "5ddceecc",
# "X-Token": "475f43c845b052c01ca3cd443d489776"

# 遍历获取接口
course_url = "https://api.wanmen.org/4.0/content/lectures?courseId=5d8dd249cdc3c553fb677baa"
# lecbase_url = "https://www.wanmen.org/courses/5d8dd249cdc3c553fb677baa/lectures/58c942032f8052899cb6e65d"
# lecbase_url = "https://www.wanmen.org/courses/5d8dd249cdc3c553fb677baa/lectures/"
lecbase_url = " https://api.wanmen.org/4.0/content/lectures/"

# https://api.wanmen.org/4.0/content/lectures/58c942032f8052899cb6e65d

def get_url(course_url, headers):
    req = request.Request(url=course_url, headers = headers)#, method='POST'
    response = request.urlopen(req)
    content = response.read().decode('utf-8')
    jcontent = json.loads(content)
    return jcontent

jcontent = get_url(course_url, headers)
# print(jcontent)
# A huge list
# len(jcontent) = 147!!!

# fromchap = int(sys.argv[1])
# tochap = int(sys.argv[2])

for chapindx in range(1, 147+1):
    chapcont = jcontent[chapindx-1]
    chapname = chapcont["name"]
    print("{}:{}".format(chapindx,chapname), end="\t")

# fromchap = int(input("from which chapter:>>>"))
# tochap = int(input("to which chapter:>>>"))

chpsindxs = input("please input all chpters, e.g. 1 2 4 :>>>")
chpsindxs = chpsindxs.split(" ")
chpsindxs = [int(i) for i in chpsindxs]


# for chapindx in range(fromchap, tochap+1):
for chapindx in chpsindxs:
    chapcont = jcontent[chapindx-1]
    chapname = chapcont["name"]
    chapsavedir = savedir+"/{}".format(chapname)
    # chapsavedir = savedir+"/{}{}".format(chapindx, chapname)
    if os.path.exists(chapsavedir) is False:
        os.mkdir(chapsavedir)
    for chd in chapcont["children"]:
        chdname=chd["name"]
        filename=chapsavedir+"/{}.mp4".format(chdname)
        if os.path.exists(filename) is False:
        #     os.mkdir(filename)
            # lecid = chd["source"]["lecId"] #wrong!!!
            lecid=chd["_id"]
            lecurl = lecbase_url+lecid
            print(lecurl)
            lecjcontent = get_url(lecurl, headers)
            mp4url = None
            try:
                # mp4url = lecjcontent["hls"]["pcMid"]
                # print(lecjcontent)
                # print(lecjcontent["video"])
                mp4url = lecjcontent["video"]["hls"]["pcMid"]
            except:
                print("No hls in {}".format(chdname))
            if mp4url:
                try:
                    # print(lecjcontent)
                    cmd="ffmpeg -threads 4 -i {} -c copy -y -bsf:a aac_adtstoasc {}".format(mp4url,filename)
                    # print("*******cmd: ",cmd)
                    call(cmd.split())
                except():
                    print("No hls in {}".format(chdname))
            time.sleep(5)
    # print("sleeping")
    # time.sleep(60*6*len(chapcont["children"])) # each video 6 minute



        #{'_id': '58c942032f8052899cb6e65d', 'courseId': '587d737d92b8724efcb67078', 'name': '级数求和1——泰勒展开和傅里叶展开', 'parentId': '58bb67da8d3ac6dc9b13cedf', 'createdAt': '2017-03-15T13:30:43.750Z', 'order': 1, 'hide': False, 'hls': {'mobileLow': 'https://media.wanmen.org/e5ca739d66a6e0384f63e1e7f9e10dc2_mobile_low.m3u8?sign=2132fc2ed46ca27ec2e95549c3734af8&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'mobileMid': 'https://media.wanmen.org/e5ca739d66a6e0384f63e1e7f9e10dc2_mobile_mid.m3u8?sign=0869e0e2f2582157ef9681cee809356b&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'pcLow': 'https://media.wanmen.org/e5ca739d66a6e0384f63e1e7f9e10dc2_pc_low.m3u8?sign=328d5b81e9e8039e30ff970c8a96ef9d&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'pcMid': 'https://media.wanmen.org/e5ca739d66a6e0384f63e1e7f9e10dc2_pc_mid.m3u8?sign=8f20a86b9f5ae29a94a00ded75dddedf&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'pcHigh': 'https://media.wanmen.org/e5ca739d66a6e0384f63e1e7f9e10dc2_pc_high.m3u8?sign=f99e76b6ded2e60c4077cbadfb7d4852&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2'}, 'updatedAt': '2019-10-31T09:40:56.901Z', 'video': {'_id': '5c357342a9a18334258f6bdc', 'hls': {'mobileLow': 'https://media.wanmen.org/4e3c46a7-e4ae-4cca-93d1-dd9a5c07d809_mobile_low.m3u8?sign=aacce040709f38c963562e7b7fed4d6a&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'pcLow': 'https://media.wanmen.org/4e3c46a7-e4ae-4cca-93d1-dd9a5c07d809_pc_low.m3u8?sign=e86b4add3d3856344825380f511c1964&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'pcHigh': 'https://media.wanmen.org/4e3c46a7-e4ae-4cca-93d1-dd9a5c07d809_pc_high.m3u8?sign=d85f3facb6359a99560881c15fa74ec7&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'pcMid': 'https://media.wanmen.org/4e3c46a7-e4ae-4cca-93d1-dd9a5c07d809_pc_mid.m3u8?sign=fba88ced4ff194ad152763b9dcb17c17&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2', 'mobileMid': 'https://media.wanmen.org/4e3c46a7-e4ae-4cca-93d1-dd9a5c07d809_mobile_mid.m3u8?sign=9e25dbedf896a495ba930edd1e2ab4fa&t=5ddcbd79&r=554c9c616df7e1e1dc27fc083316b1d2'}}, 'from': 'playback', 'actions': {'watch': True, 'download': True}, 'isPreset': True, 'videoDuration': 992.44, 'videoSize': {'mobileLow': 85504, 'pcHigh': 149192, 'pcLow': 182920, 'pcMid': 85504, 'mobileMid': 149192}, 'isGeneratingAudio': False, 'audio': {'_id': '5db857bcd50d6b5f42c73e80', 'name': '级数求和1——泰勒展开和傅里叶展开', 'url': 'https://audio.wanmen.org/1552e51f93643ec6363be6bea7d06257.mp3', 'createdAt': '2019-10-29T15:16:12.830Z', 'updatedAt': '2019-10-29T15:16:12.830Z'}, 'audioDuration': 992.626939, 'audioSize': 15882.493, 'opDuration': 8, 'edDuration': 10}