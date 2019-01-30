#作业
#1、计算时间差距
import time
import sys
def dateinput():
    date = input("请您输入一个时间（格式例如：1995-07-02): ")
    return date
def datetrans(tdate):
    spdate = tdate.replace("/","-")
    try:
        datesec = time.strptime(spdate,'%Y-%m-%d')
    except ValueError:
        print ("%s is not a rightful date!!" % tdate)
        sys.exit(1)
    return time.mktime(datesec)
def daysdiff(d1,d2):
    daysec = 24 * 60 * 60
    return int(( d1 - d2 )/daysec)
date1 = dateinput()
date2 = dateinput()
date1sec = datetrans(date1)
date2sec = datetrans(date2)
print(date1sec,date2sec)
a=abs(date1sec-date2sec)/(60)
b=a/60
c=abs(date1sec-date2sec)
print("这两个时间之间相差: ",abs(daysdiff(date1sec,date2sec)),"天","\n相差",a,"分钟，","\n相差",b,"小时","\n相差",c,"秒")
#结果
"""
请您输入一个时间（格式例如：1995-07-02): 1995-12-7
请您输入一个时间（格式例如：1995-07-02): 2019-1-30
818265600.0 1548777600.0
这两个时间之间相差:  8455 天 
相差 12175200.0 分钟， 
相差 202920.0 小时 
相差 730512000.0 秒

"""
#2、判断邮箱
import re
email=input("请输入你的邮箱：")
if len(email) > 7:
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        print("你的邮箱符合要求")
    else:
         print("你输入的邮箱不正确！")
            # return 1
    # return 0
else:
    print("你输入的邮箱不正确！")
"""
请输入你的邮箱：111111
你输入的邮箱不正确！
请输入你的邮箱：1376311810@qq.com
你的邮箱符合要求
"""


#网站爬图片
import requests
from bs4 import BeautifulSoup
import os
url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%99%BE%E5%BA%A6%E5%9B%BE%E6%A0%87&step_word=&hs=0&pn=1&spn=0&di=165990&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3572347546%2C3948256807&os=3550551904%2C2707901661&simid=4223870408%2C791719851&adpicid=0&lpn=0&ln=1501&fr=&fmq=1548828324930_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.lgstatic.com%2Fi%2Fimage%2FM00%2FA2%2F0C%2FCgp3O1ipEhKAM_lwAAAs_vlUoqM183.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bsw257_z%26e3Bv54AzdH3F25g2ftAzdH3Fq80dm00_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.content, 'lxml')
def Saving(url,name):
    root = r'C:\pictures\\'
    path = root + name + '.jpg'
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            print(url)
            r = requests.get(url)
            print(r)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬去失败")
def GetPicture():
    PictureList = soup.select('div.summary-pic > a > img')
    Picture =PictureList[0].get('src')
    NameList = soup.select('dd.lemmaWgt-lemmaTitle-title > h1')
    Name = NameList[0].text
    LinkList = soup.select('a.link-inner')
    Saving(Picture, Name)
GetPicture()




"""
re模块 正则表达式
这里写反斜杠也是转义的意思，python在re模块中使用都需要加反斜杠
\d 是匹配一个数字
\+ 大于等于1
\w 匹配数字字母下划线和中横杠
\* 匹配0个或多个
\t 指标符
. 除了回车意外的的所有
* 大于等于0
+ 大于等于1
0或1
{m}，{m,n} 出现m次，出现m到n次，包括mn re匹字符串 re.match()
re.match(pattern, string, flags)
默认有3个参数，是最后一个我们不是很关注他，就默认。
通过你前面写的pattern(正则表达式的意思)，匹配后面的string(字符串),他只能在你给的字符串的起始位置查找，注意和search的区别。
还有根据实践的结果，如果匹配失败返回none re.search()
他和match有相同的作用，但是有区别。他会在整个字符串内容中匹配,直到找到第一个相匹配的字符串。
re.findall()
他和match和search差不多，但是他是找出字符串中所有的
import re
result1 = re.match('\d+','dshfjasdsf23432dhfhsjdjfhjsd')
if result1:
print result1.group()
result2 = re.search('\d+','dshfjasdsf23432dhfhsjdjfhjsd')
print result2
print result2.group()
result3 = re.findall('\d+','dshfjasdsf23432dhfhsjdjfhjsd34')
print  result3
#输出结果：
<_sre.SRE_Match object at 0x0000000002BFA510>
23432
['23432', '34']
编译正则表达式 re.compile
他和编译生成的.pyc文件差不多，.pyc是为了再次使用时快速调用。正则表达式也可以经过编译，编译之后匹配其他的也会加快匹配速度
com = re.compile('\d+')
print type(com)
输出结果：
<type '_sre.SRE_Pattern'>
他返回了一个对象
使用方法：
也就是直接调用返回对象findall函数
com = re.compile('\d+')
print com.findall('dshfjasdsf23432dhfhsjdjfhjsd34')
练习
匹配一个文件中的所有字符串
import re
f = open('love.txt','r')
feitian = f.read()
f.close()
print re.findall('a',feitian)
##也可以一行一行的匹配
f = open("love.txt", "r")
while True:
    line = f.readline()
    if line:
        line=line.strip()
        p=line.rfind('.')
        filename=line[0:p]
        print  line
    else:
        break
f.close()
输出：
['a', 'a', 'a']
正则表达式中的分组
result2 = re.search('(\d+)\w*(\d+)','dshfjasdsf23432dhfhs23423jdjfhjsd')
print result2.group()
print result2.groups()
#输出结果：
23432dhfhs23423
('23432', '3')
#注意： 他不重复拿，这里解释一下为什么第二个输出为3，因为中间都被\w*接收了，这里我们在给一个例子
result2 = re.search('(\d+)dhfhs(\d+)','dshfjasdsf23432dhfhs23423jdjfhjsd')
print result2.group()
print result2.groups()
输出结果：
23432dhfhs23423
('23432', '23423')
练习
匹配一个字符串中的ip
import re
ip = 'sdhflsdhfj1723.234.234234.df.34.1234.df.324.xc.3+dsf172.25.254.1 sdfjk2130sdkjf.sdjfs'
result1 = re.findall('(?:\d{1,3}\.){3}\d{1,3}',ip)
result2 = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
print result1
print result2
#输出结果：
['172.25.254.1']
['172.25.254.1']
时间的表示方式
import time
print time.time()
1510923748.06
#计算从1970年1月1日到现在有多少秒
print time.gmtime()
time.struct_time(tm_year=2017, tm_mon=11, tm_mday=17, tm_hour=13, tm_min=2, tm_sec=28, tm_wday=4, tm_yday=321, tm_isdst=0)
格式化成一个对象，他是当前的时间
print time.strftime('%Y%m%d')
20171117
输出格式化之后的时间，他的格式化和linux一样

os模块
os.sep可以取代操作系统特定的路径分隔符。windows下为 “\”
os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
os.getenv()获取一个环境变量，如果没有返回none
os.putenv(key, value)设置一个环境变量值
os.listdir(path)返回指定目录下的所有文件和目录名。
os.remove(path)函数用来删除一个文件。
os.system(command)函数用来运行shell命令。
os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
os.path.split(p)函数返回一个路径的目录名和文件名。
os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
os.path.existe()函数用来检验给出的路径是否真地存在
os.curdir:返回当前目录（'.')
os.chdir(dirname):改变工作目录到dirname
os.path.getsize(name):获得文件大小，如果name是目录返回0L
os.path.abspath(name):获得绝对路径
os.path.normpath(path):规范path字符串形式
os.path.splitext():分离文件名与扩展名
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径
os.stat() 相当于 Linux 下 stat 命令
os.listdir() 列出给定目录的内容
os.mkdir(path) 创建目录
os.mkdirs(path) 创建目录树,相当于mkdir -p 操作 sys模块
sys.argv 获取传递给脚本的参数,参数解析类似于 bash 的方式,第
一个参数代表脚本本身
sys.exit(n) 退出程序，正常退出时exit(0)
sys.version 获取Python解释程序的版本信息
sys.maxint 最大的Int值
sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform 返回操作系统平台名称
"""
