# xjtu健康每日报自动填报脚本（仅适用于本科生）
## xjtu健康每日报python脚本，仅用于学习研究。使用本脚本产生的其他后果，均由使用者自行承担，与作者无关。
### 强烈建议不太清楚具体操作和原理的同学使用jkrb.exe可执行文件！！！
本脚本使用了Seleium自动化测试库，可以实现健康日报的自动填报，结合bat文件和任务计划可实现开机自动填报。
jkrb.py需配置好python环境和seleium库及浏览器驱动后才可正常使用，浏览器驱动和id.txt文件需放置在jkrb.py同目录下。


jkrb.exe为打包好的程序，支持Edge，Chrome和Firefox，需将对应的浏览器驱动和id.txt文件与程序放在同一目录下，即可使用。
各浏览器驱动详见：http://www.testclass.net/selenium_python/selenium3-browser-driver
需下载对应版本才可正常使用哦！
暂时使用id.txt文本文件存储用户名（学号）和密码,首行为用户名，第二行为密码。  
填写格式如下：  
```  
1234567890  
abcdefg
```
很简单的脚本,大家看个乐子就好，觉得可以的记得给个star！
