# AutoLogin
学校的自动登陆脚本
# 运行环境
python2.7的环境下开发
需要导入的包：  
1. requests       安装：`pip install requests`
2. ConfigParser   安装：`pip install ConfigParser`
3. argparse       安装：`pip install argparse`
注：  
在python3环境下，`ConfigParser` 已经更名为 `configparser`，请使用`pip install configparser`进行安装。并将`login.py`文件中的 `from ConfigParser import ConfigParser`更改为`from configparser import ConfigParser`
# 使用方法
方法一： 使用配置文件。在配置文件login.conf中写入用户名密码，然后运行`python login.py`
方法二： 命令行中使用参数。`python login.py -u username -p password`
