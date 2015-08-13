# 前言
坑爹的「什么值得买」，只要你留有相关联系方式，就会删掉你的评论。
很难跟其他人讨论。

解决方法，升到 Lv3，将联系方式写在个人简介

而每天签到都会有积分，所以写了这个自动签到的脚本。

# 使用方法


1、请确保你已经安装 python2.7

2、
```python
git clone git@github.com:linjunzhu/smzdm_checkin_daily.git
cd smzdm_checking_daily
```

3、修改`account.ini`
```python
# 可以写多个，同时签到
[user1]
username=iamusername@gmail.com
password=iampassword
[user2]
username=iamusername@gmail.com
password=iampassword
```
4、
```python
python smzdm.py
```

此时登录「什么值得买」，你会看到已经签到成功了。

#每天自动执行
1、 确保你使用 Linux or Mac OSX 系统

2、打开`smzdm_execute.sh`
```shell
#! /bin/bash

. /etc/profile

# 修改这里的路径为实际项目路径！！！
app_path="/home/deployer/smzdm_checkin_daily"

cd $app_path

case "$1" in
  start)
      /usr/bin/python $app_path/smzdm.py start &
     ;;
  *)
        echo $"Usage: $0 {start}"
        exit 1
esac

exit 1

```
3、
```shell
# 开始编辑自动执行脚本
crontab -e
```
```shell
# 在文件末尾添加（路径根据实际情况修改)
# 每天早上7点将进行签到
0 7 * * * /bin/sh /home/deployer/smzdm_checkin_daily/smzdm_execute.sh start
```
```shell
# 查看自动执行脚本
cdeployer@Xshare:~$ crontab -l
0 7 * * * /bin/sh /home/deployer/smzdm_checkin_daily/smzdm_execute.sh start
```


# 吐槽
「什么值得买」居然是用`GET`方式来进行登录的，直接把账号密码通通暴露在路径上，也就是说我们的明文账号密码都会一一记录在日志上。
```python
http://www.smzdm.com/user/login/jsonp_check?callback=jQuery111004638147682417184_1439357637485&user_login=%s&user_pass=%s&rememberme=%s&is_pop=%s&captcha=&_=1439357637487" % (user_login, user_pass, rememberme, is_pop)
```