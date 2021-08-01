



# 一封来自同济圣诞老人的贺卡

🎄Christmas Card for TJer (Designed &amp; Powered by Six-past-TwentyTwo)

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

> 这里是项目的背景和一些引入intro



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

> 还没有做的尽善尽美的东西
>
> 还可以做的更好的

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
