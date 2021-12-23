import urllib.request    #网页获取工具,请求访问指定的网页
#urllib.error这个包含了所有的urllib.request导致的异常
import urllib
#urllib.parse用于解析urls
#urllib.robotparser用于解析robots.txt文件
import re
#用于解释正则表达式
import time
import os
import pymysql
us = input('请输入数据库授权的用户名：')
uk = input('请输入数据库用户名密码：')
base=input('请输入使用的数据库：')
conn=pymysql.connect(host='192.168.8.88',port=3306,user=us,password=uk,charset='utf8')
cur=conn.cursor()
bases='create database ' + base + ';'
try:
    cur.execute(bases)
except:
    print(bases, '库已存在')
else:
    print(base, '库创建成功')
sqi = 'use ' + base
try:
    cur.execute(sqi)
except:
    pass
else:
    print('当前所在库为', base)
def get_html(url):
    page=urllib.request.urlopen(url)
    #print(page)
    html=page.read()
    html=html.decode('gbk')
    return html
def getjpg(url):
    url = get_html(url)
    # res = r'src="(https.+?\.jpg)" onerror="src=(.*？)" alt="(.*?)"'
    res =r'src="(https.+?\.jpg)" onerror="(.*?)" alt="(.*?)"'
    rq=re.compile(res)
    ryc=rq.findall(url)
    return ryc
def getlocal(rl):
    di=time.strftime('%Y%m%d%M%S')
    savepath="static/"+di
    try:
         os.mkdir(savepath)
    except FileExistsError:
         print(di+'文件已经存在,不在创建')
    for i in rl:
         imagepath=savepath+'/'+i[2]+'.jpg'
         #調用對應方法下的圖片
         urllib.request.urlretrieve(i[0],imagepath)
         print('图片'+i[2]+'抓取完毕')
def getiamgepath(ui):
    for i in ui:
        sqlf='insert into ima(url,name) values('+"'"+i[0]+"','"+i[2]+"');"
        cur.execute(sqlf)
        conn.commit()
def getlink(ur):
    gh=1
    dis=0
    while True:
        gh+=1
        ait = input('请输入喜剧第'+str(gh)+'页存放磁力链接的表名：')
        aiqt = 'create table ' + ait + '(id int(5) primary key auto_increment,name varchar(20),link varchar(1000));'
        try:
            cur.execute(aiqt)
        except:
            print('已存在')
            for i in ur:
                # print(i)
                c3 = i[0]
                # print(c3)
                rye = get_html(c3)
                # print(rye)
                c3_1 = r'<a href="(.+?)">(.*?)</td>'
                rtc = re.compile(c3_1)
                down = rtc.findall(rye)
                if down == []:
                    c3_1 = r'<a rel="nofollow" target="_blank" href="(.+?)">(.*?)</td>'
                    rtc = re.compile(c3_1)
                    down = rtc.findall(rye)
                # print(down)
                dis+=1
                dqp = 'update ' + ait + " set name='" + i[1] + "',link='" + down[0][0] + "' where id="+str(dis)+";"
                try:
                    cur.execute(dqp)
                    conn.commit()
                except:
                    print('添加失败，请重新添加')
                else:
                    print('下载链接' + i[1] + '保存完成')
                    break
        else:
            print('下载链接文件创建成功')
        for i in ur:
            #print(i)
            c3 = i[0]
            #print(c3)
            rye = get_html(c3)
            # print(rye)
            c3_1 = r'<a href="(.+?)">(.*?)</td>'
            rtc = re.compile(c3_1)
            down = rtc.findall(rye)
            if down==[]:
                c3_1 = r'<a rel="nofollow" target="_blank" href="(.+?)">(.*?)</td>'
                rtc = re.compile(c3_1)
                down = rtc.findall(rye)
            #print(down)
            dqp = 'insert into ' + ait + "(name,link) values('" + i[1] + "','" + down[0][0] + "');"
            try:
                cur.execute(dqp)
                conn.commit()
            except:
                print('添加失败，请重新添加')
                continue
            else:
                print('下载链接' + i[1] + '保存完成')
        break
def getfilm(url):
    get=get_html(url)
    c2 = r'<a href="(https.+?\.html)" title="(.*?)"'
    rellow = re.compile(c2)
    pkq = rellow.findall(get)
    return pkq
def getindexjpg(url):
    url = get_html(url)
    #print(url)
    # res = r'src="(https.+?\.jpg)" onerror="src=(.*？)" alt="(.*?)"'
    res =r'<img src="(https.+?.jpg)" title="(.*?)"/><span>'
    rq=re.compile(res)
    ryc=rq.findall(url)
    return ryc
rl=getindexjpg('http://www.66ys.co')
#print(rl)
indexc='create table indexto(id int(3) primary key auto_increment,name varchar(20),addr varchar(50));'
try:
    cur.execute(indexc)
except:
    print('已存在')
    for i in rl:
        #print(i)
        insq = 'insert into indexto(addr,name) values(' + "'" + i[0] + "','" + i[1] + "');"
        cur.execute(insq)
        conn.commit()
        print('保存完毕')
else:
    for i in rl:
        #print(i)
        insq = 'insert into indexto(addr,name) values(' + "'" + i[0] + "','" + i[1] + "');"
        cur.execute(insq)
        conn.commit()
        print('保存完毕')


di=time.strftime('%Y%m%d%M%S')
savepath="static/"+di
try:
     os.mkdir(savepath)
except FileExistsError:
     print(di+'文件已经存在,不在创建')
# for i in rl:
#      imagepath=savepath+'/'+i[1]+'.jpg'
#          #調用對應方法下的圖片
#      urllib.request.urlretrieve(i[0],imagepath)
#      print('图片'+i[1]+'抓取完毕')
a=get_html('http://www.66ys.co/')
#print(a)
at=r'<a href="(https.+?)" target="_blank"><img src="https.+?\.jpg" title="(.*?)"'
at=re.compile(at)
at=at.findall(a)
#print(at)
print('创建一个用于存储首页电影下载链接的表')
aiqt = 'create table 66ys1(id int(5) primary key auto_increment,name varchar(20),link varchar(100));'
try:
    cur.execute(aiqt)
except:
    print('已存在')
    dty=0
    for i in at:
        # print(i)
        c3 = i[0]
        # print(c3)
        rye = get_html(c3)
        # print(rye)
        c3_1 = r'<a href="(.+?)">(.*?)</td>'
        rtc = re.compile(c3_1)
        down = rtc.findall(rye)
        if down == []:
            c3_1 = r'<a rel="nofollow" target="_blank" href="(.+?)">(.*?)</td>'
            rtc = re.compile(c3_1)
            down = rtc.findall(rye)
        # print(down)
        dty+=1
        dqp = "update 66ys1 set name='" + i[1] + "',link='" + down[0][0] + "' where id=" + str(dty) + ";"
        #print(dqp)
        try:
            cur.execute(dqp)
            conn.commit()
        except:
            print('添加失败，请重新添加')
        else:
            print('下载链接' + i[1] + '保存完成')
else:
    print('下载链接文件创建成功')
    for i in at:
        # print(i)
        c3 = i[0]
        # print(c3)
        rye = get_html(c3)
        # print(rye)
        c3_1 = r'<a href="(.+?)">(.*?)</td>'
        rtc = re.compile(c3_1)
        down = rtc.findall(rye)
        if down == []:
            c3_1 = r'<a rel="nofollow" target="_blank" href="(.+?)">(.*?)</td>'
            rtc = re.compile(c3_1)
            down = rtc.findall(rye)
        # print(down)
        dqp = "insert into 66ys1(name,link) values('" + i[1] + "','" + down[0][0] + "');"
        try:
            cur.execute(dqp)
            conn.commit()
        except:
            print('添加失败，请重新添加')
            continue
        else:
            print('下载链接' + i[1] + '保存完成')

ret=r'<a href="(https.+?)"\[!--sel--\]>(.*?)</a>'
ry=re.compile(ret)
rli=ry.findall(a)
#print(rli)
c1=rli[0][0]
#print(c1)
get=get_html(c1)
#print(get)
c2=r'<a href="(https.+?\.html)" title="(.*?)"'
rellow=re.compile(c2)
pointc2=rellow.findall(get)
#print(pointc2)

while True:
    print('此为喜剧的首页电影下载链接')
    aiqt = 'create table happy (id int(10) primary key auto_increment,name varchar(20),link varchar(100));'
    try:
        cur.execute(aiqt)
    except:
        print('此表已存在')
        disgit=0
        for i in pointc2:
            # print(i)
            c3 = i[0]
            # print(c3)
            rye = get_html(c3)
            # print(rye)
            c3_1 = r'<a href="(magnet.+?)">(.*?)</a>'
            rtc = re.compile(c3_1)
            down = rtc.findall(rye)
            disgit+=1
            sty='update happy set name='+"'"+i[1]+"' ,link='"+down[0][0]+"'  where id="+str(disgit)+';'
            try:
                cur.execute(sty)
                conn.commit()
            except:
                print('添加失败，请重新添加')
                continue
            else:
                print('下载链接' + i[1] + '保存完成')
    else:
        print('下载链接文件创建成功')
    for i in pointc2:
        #print(i)
        c3 = i[0]
        #print(c3)
        rye = get_html(c3)
        # print(rye)
        c3_1 = r'<a href="(magnet.+?)">(.*?)</a>'
        rtc = re.compile(c3_1)
        down = rtc.findall(rye)
        #print(down)
        dqp = "insert into happy(name,link) values('" + i[1] + "','" + down[0][0] + "');"
        try:
            cur.execute(dqp)
            conn.commit()
        except:
            print('添加失败，请重新添加')
            continue
        else:
            print('下载链接'+i[1]+'保存完成')
    break
while True:
    print('存储图片url')
    sql='create table ima (id int(2) primary key auto_increment,url varchar(40),name varchar(10));'
    try:
        cur.execute(sql)
    except:
        print('创建失败，名称已被使用,请重新输入一个文件名')
        continue
    else:
        print('文件已创建')
        break
p2=r'&nbsp;<a href="(https.+?\.html)">'
p2r=re.compile(p2)
p2a=p2r.findall(get)

#print(p2a)                 # c=getjpg(c1)
jpglist=getjpg(c1)
#print(jpglist)
getlocal(jpglist)
getiamgepath(jpglist)
numl=0
for i in p2a:
    if numl==4:
        break
    numl += 1
    j1=getjpg(i)
    getlocal(j1)
    getiamgepath(j1)
    #ef=getfilm(i)
    #getlink(ef)




































# res=r'src="(https.+?\.jpg)" title="(.*?)"' #r表示强制转移
# r=re.compile(res)
# rl=r.findall(a)
#
# dirname=time.strftime('%Y%m%d%H%M%S')
# print(dirname)
# savepath="C:/Users/flaskProject/static/"+dirname
# try:
#     os.mkdir(savepath)
# except FileExistsError:
#     print(dirname+'文件已經存在,不在創建')
# for i in rl:
#     imagepath=savepath+'/'+i[1]+'.jpg'
#     #調用對應方法下的圖片
#     urllib.request.urlretrieve(i[0],imagepath)
#     print('图片'+i[1]+'抓取完毕')




