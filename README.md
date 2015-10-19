宝宝的作业
================================

[![Build Status](https://travis-ci.org/walkerning/Baobao_Homework.svg?branch=master)](https://travis-ci.org/walkerning/Baobao_Homework)

每个练习为practices包下的一个模块/包，模块/包顶层必须有可调用的
solution对象(函数/其class实现了`__call__`特殊方法的对象)，传入参数检查返回结果

宝宝自己可以跑测试
--------------------------------

如果宝宝需要自己先跑测试, 有两种选择

### 通过setup.py

在项目根目录下运行`python setup.py test`即可

### 直接使用py.test

1. 先下载virutalenv: `pip install virtualenv`

2. 在项目根目录下创建virtualenv目录: `virtualenv VENV`

3. `source VENV/bin/activate`

4. 下载py.test: `pip install pytest`

5. 可以执行`py.test tests/ <一系列option>`，关于可以使用的option，使用`py.test --help`查看
   也可以执行`make test`



--------------------------------

- [x] 练习1. 10/10/2015布置
