



# 🎄来自同济圣诞老人的圣诞礼物

Christmas Card for TJer <u>(Designed &amp; Powered by Six-past-TwentyTwo)</u>

-----

<div align="left" display="inline-block">
㊗️TJer：<br/>
&nbsp;&nbsp;&nbsp;&nbsp;圣诞快乐 万事胜意 喜乐长安<br/>
&nbsp;&nbsp;&nbsp;&nbsp;今夜星空闪烁<br/>
&nbsp;&nbsp;&nbsp;&nbsp;我陪你等<br/>
&nbsp;&nbsp;&nbsp;&nbsp;初雪❄️ 圣诞树🎄 新年烟火🎆 和更好的我们<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;—— 软件学院二十二点零六团队
</div>
<br/>

<div align="center">
  <img src="christmas-card/Christmas-Card-for-TJUer-green.PNG" alt="Christmas-Card-for-TJUer-green" width="30%;" />
  <img src="christmas-card/Christmas-Card-for-TJUer-public.PNG" alt="Christmas-Card-for-TJUer-red" width="30%;" />
  <img src="christmas-card/Christmas-Card-for-TJUer-glod.PNG" alt="Christmas-Card-for-TJUer-glod" width="30%;" />
</div>
<br/>

<details>
	<summary>For Developers⬇️</summary>

## 写在前面

这个小礼物本想作为我的个人小程序[二十二点零六](https://github.com/doubleZ0108/Six-past-TwentyTwo)在2020年圣诞节送给同济的特殊礼物，在原本的计划中通过小程序数据库中已验证邮箱的用户的学号，结合有姓名和头像的定制贺卡通过系列爬虫和邮箱服务群发邮件，但由于个人开发者的种种限制加上系列问题，导致用代码群发过多邮件之后被锁死，美好的幻想和很长时间的准备都觉得很不甘心

还记得2020.12.24那天晚上，原本在图书馆复习辅修的期末考核，突然想对团队的小一个月有个交代，兴头上做了一张通用的祝福贺卡放在手机上，从南北楼到图书馆一楼到顶楼，每个地方都通过Airdrop尽可能多的送给更多TJer美好的圣诞祝福，当然还有很多有趣的小插曲就不在这里说了...

项目的核心代码都是软院19级学妹完成的，她也是二十二点零六的忠实粉丝，在我发布招募令之后不顾个人得失毅然相信我并加入我，也希望以此仓库作为她大学生活中一段难忘的回忆🎄🎅🏻🎁

<br/>

## 主要功能

- [x] 输入头像和昵称，生成圣诞专属贺卡
- [x] 使用selenium 通过浏览器自动化登陆163邮箱获取已注册用户的学号信息
- [x] 发送圣诞贺卡至已用户邮箱

<br/>

## 如何使用

1. 生成圣诞贺卡

   ```shell
   > cd src
   # gen_card.py中ln70 ava_path和ln73 text修改为头像路径和昵称
   
   > python gen_card.py
   ```

2. 登陆163邮箱

   ```shell
   > cd src
   # login_163.py中ln17输入邮箱密码
   
   > python login_163.py
   ```

3. 发送邮件

   ```shell
   > cd src
   # post_email.py中ln57输入邮箱授权码;ln64输入待发送贺卡路径;ln65输入收件人邮箱
   
   > python post_email.py
   ```


<br/>

### TODOs

- [ ] 解决使用163邮箱自动批量发送邮件失败
- [ ] 使用`requests`库和`cookie`登陆163邮箱而非浏览器自动化

<br/>

## 目录结构
```
.
├── README.md
├── christmas-card
│   ├── Christmas-Card-for-TJUer-glod.PNG
│   ├── Christmas-Card-for-TJUer-green.PNG
│   ├── Christmas-Card-for-TJUer-public.PNG
│   └── Christmas-Card-for-TJUer-red.PNG
├── resource
│   ├── ava.jpg
│   ├── card.png
│   ├── lvse.png
│   └── 仓耳小丸子.ttf
└── src
    ├── gen_card.py
    ├── login_163.py
    └── post_email.py
```

</details>

<br/>

## 关于我们

|  姓名  |        学院         |      分工      |                           联系方式                           |                    头像                     |
| :----: | :-----------------: | :------------: | :----------------------------------------------------------: | :-----------------------------------------: |
|  张喆  |    软件学院 17级    | 项目发起人、PM | [doublez@alumni.tongji.edu.cn](mailto:doublez@alumni.tongji.edu.cn) |  ![zz-avatar](README.assets/zz-avatar.JPG)  |
| 陈开昕 |    软件学院 17级    |      美术      |  [sternstarry18@gmail.com](mailto:sternstarry18@gmail.com)   | ![ckx-avatar](README.assets/ckx-avatar.JPG) |
| 陈中悦 |    软件学院 19级    |    代码实现    |        [1418621447@qq.com](mailto:1418621447@qq.com)         | ![czy-avatar](README.assets/czy-avatar.JPG) |
| 傅薏帆 | 新生院济勤学堂 20级 |      文案      |                              /                               | ![fyf-avatar](README.assets/fyf-avatar.JPG) |

<br/>

<div align="center">
Copyright© Tongji Univ. SSE<br/>
Six past Twenty Two<br/>
All Right Reserved.<br/>
</div>
