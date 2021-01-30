import sys
from torrequest import TorRequest


# http headers for request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/53.0.2785.143 "
                  "Safari/537.36 "
}


# Default Tor port configuration
# change this if ports are already been used
proxyPort = 9050
ctrlPort = 9051

# input for the code
site = "https://sppu.wheebox.com/WAC-3/allqusdownloadhtml.ils?testNo=1618&code=1052000&showTest=319&actForm=edit&set=1"


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
    # making the request
    count = 1
    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
        response = tr.get(site, headers=headers, verify=False)
        print(f"Fetching toc {count} file")

        open('./toc_' + str(count) + '.txt', 'wb').write(response.content)
        count += 1
