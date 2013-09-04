#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' DiscuzRobot - Discuz!论坛的机器人程序，实现了登录，签到，发贴及回帖等功能
by Conanca
'''

import urllib2, urllib, cookielib, re, time
import time
import datetime

class DiscuzRobot:

    def __init__(self, forumUrl, userName, password, proxy = None):
        ''' 初始化论坛url、用户名、密码和代理服务器 '''
        self.forumUrl = forumUrl
        self.userName = userName
        self.password = password
        self.formhash = ''
        self.isLogon = False
        self.isSign = False
        self.xq = ''
        self.jar = cookielib.CookieJar()
        if not proxy:
            openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.jar))
        else:
            openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.jar), urllib2.ProxyHandler({'http' : proxy}))
        urllib2.install_opener(openner)

    def login(self):
        ''' 登录论坛 '''
        url = self.forumUrl + "/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&inajax=1";
        postData = urllib.urlencode({'username': self.userName.encode("gbk"), 'password': self.password, 'answer': '', 'cookietime': '2592000', 'handlekey': 'ls', 'questionid': '0', 'quickforward': 'yes',  'fastloginfield': 'username'})
        req = urllib2.Request(url,postData)
        content = urllib2.urlopen(req).read()
#        print content.decode("gbk").encode('utf-8')
        if self.userName.encode("gbk") in content:
            self.isLogon = True
            print 'logon success!'
            self.initFormhashXq()
        else:
            print 'logon faild!'

    def initFormhashXq(self):
        ''' 获取formhash和心情 '''
        content = urllib2.urlopen(self.forumUrl + '/plugin.php?id=dsu_paulsign:sign').read().decode('gbk')
        rows = re.findall(r'<input type=\"hidden\" name=\"formhash\" value=\"(.*?)\" />', content)
        if len(rows)!=0:
            self.formhash = rows[0]
            print 'formhash is: ' + self.formhash
        else:
            print 'none formhash!'
        rows = re.findall(r'<input id=.* type=\"radio\" name=\"qdxq\" value=\"(.*?)\" style=\"display:none\">', content)
        if len(rows)!=0:
            self.xq = rows[0]
            print 'xq is: ' + self.xq
        elif u'已经签到' in content:
            self.isSign = True
            print 'signed before!'
        else:
  #          print 'none xq!'
            pass
    def reply(self, tid, subject = u'',msg = u'不错哦 顶一下'):
        ''' 回帖 '''
        self.initFormhashXq()
        url = self.forumUrl + '/forum.php?mod=post&action=reply&fid=41&tid={}&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'.format(tid)
        postData = urllib.urlencode({'formhash': self.formhash, 'message': msg.encode('gbk'), 'subject': subject.encode('gbk'), 'posttime':int(time.time()) })
        req = urllib2.Request(url,postData)
        content = urllib2.urlopen(req).read().decode('gbk')
        #print content
        if u'发布成功' in content:
            print 'reply success!'
            print tid
        else:
            print 'reply faild!'

    def publish(self, fid, typeid, subject = u'发个帖子测试一下下，嘻嘻~~~',msg = u'发个帖子测试一下下，嘻嘻~~~'):
        ''' 发帖 '''
        url = self.forumUrl + '/forum.php?mod=post&action=newthread&fid={}&extra=&topicsubmit=yes'.format(fid)
        postData = urllib.urlencode({'formhash': self.formhash, 'message': msg.encode('gbk'), 'subject': subject.encode('gbk'), 'posttime':int(time.time()), 'addfeed':'1', 'allownoticeauthor':'1', 'checkbox':'0', 'newalbum':'', 'readperm':'', 'rewardfloor':'', 'rushreplyfrom':'', 'rushreplyto':'', 'save':'', 'stopfloor':'', 'typeid':typeid, 'uploadalbum':'', 'usesig':'1', 'wysiwyg':'0' })
        req = urllib2.Request(url,postData)
        content = urllib2.urlopen(req).read().decode('gbk')
        #print content
        if subject in content:
            print 'publish success!'
        else:
            print 'publish faild!'

    def sign(self,msg = u'哈哈，我来签到了！'):
        ''' 签到 '''
        if self.isSign:
            return
        if self.isLogon and self.xq:
            url = self.forumUrl + '/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
            postData = urllib.urlencode({'fastreply': '1', 'formhash': self.formhash, 'qdmode': '1', 'qdxq': self.xq, 'todaysay':msg.encode('gbk') })
            req = urllib2.Request(url,postData)
            content = urllib2.urlopen(req).read().decode('gbk')
            #print content
            if u'签到成功' in content:
                self.isSign = True
                print 'sign success!'
                return
        print 'sign faild!'

    def speak(self,msg = u'hah,哈哈，测试一下！'):
        ''' 发表心情 '''
        url = self.forumUrl + '/home.php?mod=spacecp&ac=doing&handlekey=doing&inajax=1'
        postData = urllib.urlencode({'addsubmit': '1', 'formhash': self.formhash, 'referer': 'home.php', 'spacenote': 'true', 'message':msg.encode('gbk') })
        req = urllib2.Request(url,postData)
        content = urllib2.urlopen(req).read().decode('gbk')
        #print content
        if u'操作成功' in content:
            print 'speak success!'
        else:
            print 'speak faild!'

if __name__ == '__main__':
    robot = DiscuzRobot('http://www.264006.com',u'汉字服', 'h456')
    robot.login()
#    robot.sign()
#    robot.speak()
#    robot.publish(41,36)
    now = datetime.datetime.now()
    print (now.strftime('%Y-%m-%d %H:%M:%S'))

    tid = [615002,613701,610906,609551,604363,611054,600147]
   
    for i in tid:

        robot.reply(i)
        time.sleep(20)
