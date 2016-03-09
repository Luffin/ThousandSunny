#ThousandSunny

在阅读了R菊苣的[pyprint](https://github.com/RicterZ/pyprint)和MartianZ的[MartianZ-BLOG](https://github.com/MartianZ/MartianZ-BLOG)的代码后，自己尝试写的一个渣博客。

博客使用tornado+jinja2+sqlalchemy完成博客搭建，采用sqlite作为数据库存储文章友链等数据，博客的主题修改自[jekyll-minimal-theme](https://github.com/henrythemes/jekyll-minimal-theme)。后台使用bootstrap框架搭建，可以添加、删除和编辑文章及友链。

博客里的一些命名来自《One Piece》

###Installation

克隆项目到本地并进入文件夹

	git clone https://github.com/Luffin/ThousandSunny.git
	cd ThousandSunny
安装所需第三方Python库	
	
	tornado
	jinja2
	sqlalchemy
也可以通过`pip install -r requirement.txt`来安装这些库

__注意(写在运行前):__

`GoingMerry`文件夹中的`settings.py`文件夹中可以修改

* 博客名字
* 数据库名字
* 数据库路径
* 首页显示文章数
* 文章索引页面的文章显示数量

__其中的COOKIE_SECRET要自己修改并妥善保管__

可以使用`python GoingMerry/cookie_secret.py`来生成自己的cookie签名密钥

运行程序

	python GoingMerry/creat_db.py
	python main.py
	

###TODO

响应式布局

添加代码块的高亮、行标、复制显示原文的插件

滚动加载图片而不是一次性全部载出
