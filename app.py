from flask import Flask,render_template
import pymysql

us = input('请输入数据库授权的用户名：')
uk = input('请输入数据库用户名密码：')
base=input('请输入使用的数据库：')
conn = pymysql.connect(host='192.168.8.88', user=us, password=uk, port=3306, charset='utf8',db=base)
cur = conn.cursor()
app = Flask(__name__) #实例化Flask类，并将当前的项目提交给他
#
#
@app.route('/')                        #定义路由，定义一个页面url信息，运行该项目后可以通过定义的url地址得到页面信息，默认情况下’/‘,就是表示本机的回环ip127.0.0.1：5000
def hello_world():
     global conn,cur
     sqo='select * from 66ys1'
     cur.execute(sqo)
     re=cur.fetchall()
     sqi='select * from indexto'
     cur.execute(sqi)
     rc=cur.fetchall()
     #视图函数，该函数和路由的定义匹配，一个路由匹配一个视图函数，在视图函数中，来定义页面显示的内容
     return render_template('5.html',ry=re,eg=re[0][1],sy=re[0][2],s2=re[1][1],s2d=re[1][2],s3=re[2][1]\
                            ,s3d=re[2][2],s4=re[3][1],s4d=re[3][2],s5=re[4][1],s5d=re[4][2],s6=re[5][1],s6d=re[5][2]\
                            ,s7=re[6][1],s7d=re[6][2],s8=re[7][1],s8d=re[7][2],s9=re[8][1],s9d=re[8][2],s10=re[9][1]\
                            ,s10d=re[9][2],s11=re[10][1],s11d=re[10][2],s12=re[11][1],s12d=re[11][2]\
                            ,egim=rc[0][2],s2im=rc[1][2],s3im=rc[2][2],s4im=rc[3][2]\
                            ,s5im=rc[4][2],s6im=rc[5][2],s7im=rc[6][2],s8im=rc[7][2]\
                            ,s9im=rc[8][2],s10im=rc[9][2],s11im=rc[10][2],s12im=rc[11][2])  #视图函数中的return可以直接被显示到页面上，可以返回普通字符串，也可以返回会html代码，还可以返回整个页面的页面模板文件

@app.route('/<string:res>')
def gettemp(res):
     #from 爬虫 import imagepath
     global conn, cur
     sqo = 'select * from ima;'
     cur.execute(sqo)
     re = cur.fetchall()
     sqoi = 'select * from happy;'
     cur.execute(sqoi)
     rh = cur.fetchall()
     if res=='xijupian':
          d=5
          return render_template('q.html',a=d,ry=re,eg=re[0][1],sy=re[0][2],s2=re[1][1],s2d=re[1][2],s3=re[2][1]\
                            ,s3d=re[2][2],s4=re[3][1],s4d=re[3][2],s5=re[4][1],s5d=re[4][2],s6=re[5][1],s6d=re[5][2]\
                            ,s7=re[6][1],s7d=re[6][2],s8=re[7][1],s8d=re[7][2],s9=re[8][1],s9d=re[8][2],s10=re[9][1]\
                            ,s10d=re[9][2],s11="static/20210803/5",s11d=re[10][2],s12=re[11][1],s12d=re[11][2]\
                                 ,t1=rh[0][2], t2=rh[1][2], t3=rh[2][2], t4=rh[3][2] \
                                 , t5=rh[4][2], t6=rh[5][2], t7=rh[6][2], t8=rh[7][2] \
                                 , t9=rh[8][2], t10=rh[9][2], t11=rh[10][2], t12=rh[11][2])
     elif res=='dongzuopian':
          return render_template('1.html')
     elif res=='aiqingpian':
          return render_template('1.html')
     elif res=='kehuanpian':
          return render_template('1.html')
     elif res=='kongbupian':
          return render_template('1.html')
     elif res == 'zhanzhengpian':
          return render_template('1.html')
     elif res == 'jilupian':
          return render_template('1.html')
     elif res == 'juqingpian':
          return render_template('1.html')
     elif res == '3Ddianying':
          return render_template('1.html')
     elif res == 'guochan':
          return render_template('1.html')
     elif res == 'gangtai':
          return render_template('1.html')
     elif res == 'rihan':
          return render_template('1.html')
     elif res == 'oumei':
          return render_template('1.html')
     elif res == 'guopei':
          return render_template('1.html')
     elif res == 'zongyi':
          return render_template('1.html')
          #return也可以返回html格式的标签
@app.route('/<string:res>,<string:hq>')
def j(res,hq):
     # conn = pymysql.connect(host='192.168.89.129', user='root', password='123.com', port='3306', charset='utf8')
     # cur = conn.cursor()
     # sql='select * from 66ys;'
     a=5
     if res=='xijupian' and hq=='xijupian':
          return render_template('q.html',c=a)

if __name__ == '__main__':             #程序与运行控制部分，当将项目文件的位置信息等于__main__，就运行是实例化的Flask函数
     app.run()                         #run方法中可以设定debug=True，host='ip',port='port'id' 等等
#
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/login/<string:uname>,<int:ii>',methods=['GET','POST']) #不止可以设定url地址，还可以设定形参变量,还可以在其中加入methods变量的设定，他决定了页面中的数据传输方式
# #GET和POST两个可以同时使用
# def helll(uname,ii):
#     return '用户名:'+uname+' '+' 密码:'+str(ii)
# if __name__=='__main__':
#     app.run()
# from flask import Flask,render_template
# #在flask项目中有两个默认的创建的目录，一个叫static，templates，首先static目录是用来存放音频、视频、图片等
# #temlates用来存放html模板的如.css文件.js文件等，html文件
# app = Flask(__name__)
# @app.route('/',methods=['GET'])
# def hello_world():
#     return render_template("index.html") #此返回的为template的模板
#
# if __name__=='__main__':
#     app.run()
#将处理好的信息传输到页面上
# from flask import Flask,render_template
# import random
# app=Flask(__name__)
# @app.route('/')
# def memage():
#     luck=random.randrange(0,11) #将这个数字传递到页面中显示,列表和字典使用同样的方法进行传递参数
#     dic={1:"哈哈"}
#     lie=['hah','hehe']
# #在render_template的第一个参数后面写一个接参变量
#     return render_template("index.html",ln=luck,f=dic,men=lie)
# if __name__ =='__main__':
#     app.run()
#from flask import Flask,render_template
# import random
# app=Flask(__name__)
# @app.route('/')
# def cq():
#     return render_template("1.html",c='电脑',p1='玩家',w='vs ')
# @app.route("/<string:res>")
# def gaming(res):
#     pc=random.choice(['🖐','✊','✌'])
#     if res=="🖐":
#         if res=='🖐' and pc not in('🖐','✌'):
#             w1='赢'
#         elif res=='🖐' and pc =='✌':
#             w1='输'
#         else:
#             w1='平局'
#         return render_template("1.html",p1='🖐',c=pc,w=w1)
#     elif res=='✊':
#         if res == '✊' and pc not in ('🖐', '✌'):
#             w1 = '平局'
#         elif res == '✊' and pc == '✌':
#             w1 = '赢'
#         else:
#             w1 = '输'
#         return render_template("1.html",p1='✊',c=pc,w=w1)
#     elif res=="✌":
#         if res == '✌' and pc == '🖐':
#             w1 = '赢'
#         elif res == '✌' and pc == '✌':
#             w1 = '平局'
#         else:
#             w1 = '输'
#         return render_template("1.html",p1='✌',c=pc,w=w1)
# if __name__ =='__main__':
#     app.run()
# from flask import Flask,render_template
# import random
# app=Flask(__name__)
#
# @app.route("/")
# def mypage():
#     return render_template("✊.html",p1="玩家",c1="电脑",wol="VS")
#
# @app.route("/<string:res>")
# def gaming(res):
#     com=random.choice(["🖐🏻","✊🏻","✌🏻"])
#     if res=="🖐🏻":
#         return render_template("✊.html",p1="🖐🏻",c1=com)
#     elif res=="✊🏻":
#         return render_template("✊.html",p1="✊🏻",c1=com)
#     elif res=="✌🏻":
#         return render_template("✊.html",p1="✌🏻",c1=com)
#
# if __name__=="__main__":
#     app.run()