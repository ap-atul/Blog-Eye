import sys
from torrequest import TorRequest

"""
Usage: 
Default without changing the port
$ python3 blogeye.py 

For new port config
$ python3 blogeye.py proxyPort controlPort

"""

# http headers for request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/53.0.2785.143 "
                  "Safari/537.36 "
}

print("""\033[1m\033[37m
 _______   ___        ______    _______        _______  ___  ___  _______  
|   _  "\ |"  |      /    " \  /" _   "|      /"     "||"  \/"  |/"     "| 
(. |_)  :)||  |     // ____  \(: ( \___)     (: ______) \   \  /(: ______) 
|:     \/ |:  |    /  /    ) :)\/ \           \/    |    \\  \/  \/    |   
(|  _  \\  \  |___(: (____/ // //  \ ____     // ___)_   /   /   // ___)_  
|: |_)  :)( \_|:  \\        / (:   _(  __|  (:      "| /   /   (:      "| 
(_______/  \_______)\"_____/   \_______)      \_______)|___/     \_______) 

                                                    \033[41m  AP-Atul ;)  \033[0m""")

# Default Tor port configuration
# change this if ports are already been used
proxyPort = 9050
ctrlPort = 9051

# input for the code
site = input("Enter your Blog Address : ")
blog = int(input("Enter The number of Viewers : "))


def run(count):
    """
    making the request and display the count completed
    :param count: int, the count of views
    :return: None
    """
    response = tr.get(site, headers=headers, verify=False)
    print(f"{count + 1} Blog view added .......")
    tr.reset_identity()


if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] and sys.argv[2]:
            proxyPort = sys.argv[1]
            ctrlPort = sys.argv[2]

    # making the request
    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
        for i in range(blog):
            run(i)
