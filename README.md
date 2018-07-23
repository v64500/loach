### loach

- loach是一个移动端爬虫，针对现下很火的短视频app—抖音

  1. 支持多个android设备并行自动化
  2. 支持任意android设备的服务端部署到任意机器
  3. 支持使用http方法控制任务

- 示意图

  ![](https://github.com/daxingshen/imgines/raw/master/loach_示意图修正.png)

  1. appium 提供了一组restful[接口用来控制设备](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol#session-1)
  2. scheduler会将从http接收到的command在存在可用设备的时候丢给设备去执行
     1. 对于CRAWLING类型的任务，是长期有效的，即任务没有终结点，设备会被永久占用
     2. 对于FINDING类型的任务，重试三次
  3. 确保android sdk正确配置并adb devices能看到设备

- QAQ

  1. 整个系统有哪些组成？

     loach进程、appium实例若干、android设备若干（数量等于appium实例数量）

  2. 一句话概括loach的逻辑？

     http api控制loach（shceduler），loach控制appium实例，appium实例控制android设备

  3. 部署对网络的要求

     loach进程、appium实例、android设备必须相互知道其它所在的位置。即在同一LAN

  4. loach、appium、android只能在一台机器上运行么？

     不必，正如Q3，互通是唯一网络要求

  5. 补充

     目前我使用i5+8Gwindows部署六台设备很流畅，如果需要大量部署的话。估计两位数就上限了。

     提供两种思路：

     1. 分布式部署，一个loach带十个设备还是很轻松的，若干个loach进程选择一个作为master进程并对外提供http服务(开发中)
     2. 若干个loach并行，并各自对外提供http服务

- 白话部署

     1. 环境

        appium： 1.8.1 实例六个 端口4723-4728

        设备：华为畅享7 SLA-TL10 六台 ip分别是 192.168.1.201-206 端口 5555-5560

        loach：1.2

     2. 启动

        1. adb连接设备

           > adb connect 192.168.1.201:5555
           >
           > adb connect 192.168.1.202:5556
           >
           > adb connect 192.168.1.203:5557
           >
           > adb connect 192.168.1.204:5558
           >
           > adb connect 192.168.1.205:5559
           >
           > adb connect 192.168.1.206:5560

        2. 启动appium

           > appium -p 4723 -U 192.168.1.201
           >
           > appium -p 4724 -U 192.168.1.202
           >
           > appium -p 4725 -U 192.168.1.203
           >
           > appium -p 4726 -U 192.168.1.204
           >
           > appium -p 4727 -U 192.168.1.205
           >
           > appium -p 4728 -U 192.168.1.206

        3. 启动loach

           > cd loach/loach/instances
           >
           > python app.py

        4. 添加任务

           >  POST 127.0.0.1:8080/douyin/task/devices/

           参数

           ```
           {
             "1": {
                 "ip": "192.168.1.201",
                 "port": 5555,
                 "sip": "192.168.1.106",
                 "sport":4723
               },
             "2": {
                 "ip": "192.168.1.202",
                 "port": 5556,
                 "sip": "192.168.1.106",
                 "sport":4724
               },
             "3": {
                 "ip": "192.168.1.203",
                 "port": 5557,
                 "sip": "192.168.1.106",
                 "sport":4725
               },
             "4": {
                 "ip": "192.168.1.204",
                 "port": 5558,
                 "sip": "192.168.1.106",
                 "sport":4726
               },
             "5": {
                 "ip": "192.168.1.205",
                 "port": 5559,
                 "sip": "192.168.1.106",
                 "sport":4727
               },
             "6": {
                 "ip": "192.168.1.206",
                 "port": 5560,
                 "sip": "192.168.1.106",
                 "sport":4728
               }
           }
           ```

           > POST 127.0.0.1:8080/douyin/task/crawling/

           ```
           {
             "attrs":["following", "work", "like"]
           }
           ```

           


     

        

   
     



