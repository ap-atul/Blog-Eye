import sys
from torrequest import TorRequest

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/53.0.2785.143 "
                  "Safari/537.36 "
}


print("""\033[93m
  _     _                                
 | |   | |                               
 | |__ | | ___   __ _    ___ _   _  ___  
 | '_ \| |/ _ \ / _` |  / _ \ | | |/ _ \ 
 | |_) | | (_) | (_| | |  __/ |_| |  __/ 
 |_.__/|_|\___/ \__, |  \___|\__, |\___| 
                 __/ |        __/ |      
                |___/        |___/       

                   \033[37;41m  AP-Atul ;)  \033[0m""")

# Default Tor port configuration
proxyPort = 9050
ctrlPort = 9051

# site = input("Enter your Blog Address : ")
# blog = int(input("Enter The number of Viewers : "))

urlCodeBooks = ["https://syntaxarticles.blogspot.com/2020/09/using-ffmpeg-to-trim-your-videos.html",
        "https://syntaxarticles.blogspot.com/2020/08/audio-de-noising-using-python-wavelets.html",
        "https://syntaxarticles.blogspot.com/2020/06/jwt-token-auth-json-web-tokens-in-nodejs.html",
        "https://syntaxarticles.blogspot.com/2020/05/should-i-read-book-or-take-course.html",
        "https://syntaxarticles.blogspot.com/2020/01/adding-firebase-functionality-in-your_31.html",
        "https://syntaxarticles.blogspot.com/2020/01/adding-firebase-functionality-in-your.html",
        "https://syntaxarticles.blogspot.com/2020/01/vibrate-device-when-user-goes-in-wrong.html",
        "https://syntaxarticles.blogspot.com/2018/12/monetise-your-android-app-admob.html",
        "https://syntaxarticles.blogspot.com/2018/11/converting-html5-game-for-android-2.html"]

urlPingBright = ["https://pingbrightside.blogspot.com/2018/12/books-what-to-take-and-what-not.html",
		"https://pingbrightside.blogspot.com/2018/12/the-more-troubles-more-fun-to-win.html",
		"https://pingbrightside.blogspot.com/2018/12/8-tips-to-make-your-day-productive.html",
		"https://pingbrightside.blogspot.com/2018/12/top-5-practices-to-increase-mental.html",
		"https://pingbrightside.blogspot.com/2018/09/do-what-you-have-to-do-until-you-can-do.html",
		"https://pingbrightside.blogspot.com/2018/04/want-to-have-day-off.html"]


def run(opt):
    if opt == 1:
        links = urlCodeBooks
    else:
        links = urlPingBright

    for link in links:
        response = tr.get(link, headers=headers, verify=True)
        #     time.sleep(10)
        #     print(response.text)
        print(f"Blog view added .......")
        tr.reset_identity()


if __name__ == '__main__':
    blog = int(sys.argv[1])
    option = int(sys.argv[2])
    # if len(sys.argv) > 3:
    #     if sys.argv[1] and sys.argv[2]:
    #         proxyPort = sys.argv[1]
    #         ctrlPort = sys.argv[2]

    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
        for i in range(blog):
            run(option)




