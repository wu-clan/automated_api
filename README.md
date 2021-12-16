# python接口自动化测试框架

## 🧠设计思路
- python3 + unittest + ddt + requests

## 👀目录结构介绍
- common/: 公共类
- core/: 配置
- data/: 测试数据
- db/: 数据库相关
- log/: 日志文件
- packages/: 存放第三方库包，如HTMLTestRunner
- report/: 测试报告存放
- testcase/: 放置接口自动化测试项目和用例
- utils/: 工具包
- run_*.py: 执行接口测试用例主程序

## 👨‍💻👩‍💻使用
```shell
# 下载
git clone https://gitee.com/wu_cl/automated_api.git
# 安装依赖包
pip install -r requirements.txt
```

### 1: 指定用例所在目录
```
testcase 目录下的文件夹可视为单个项目目录

在 config.ini 配置中修改 project = 名称 为对应的项目目录名即可
```
### 2: 如何运行测试
```
run_all.py 文件, 直接运行即可, 会运行所有的用例

run_class.py 文件, 指定需要测试的类名, 并导入该类到文件,
运行即可, 会运行指定类下的所有用例
```
### 3: 如何查看报告
```
运行完之后到 report文件夹下 查看
```
## ❓问题相关
### 1: 为什么日志没有内容
```
日志内容需要手动写入, 详细示例demo中几乎都有体现, 请自行查看
```
### 2: 为什么没有测试报告
```
html 测试报告需要 run_all 或打开 run_class的写入注释 自动生成
excel 测试报告要手动写入, 详情查看测试用例: testAPI.py
yaml 测试报告要手动写入, 详情查看测试用例: testAPI.py
```
### 2: excel 测试报告有问题
```
1: excel 测试数据要严格按照 DemoAPITestCase.xlsx 模板格式编写, 
名字可以变, 存放位置不要变, 调用时指定文件名
2: excel 测试报告的文件名称是固定的
```
### 3: yaml 测试报告有问题
```
1: yaml 测试数据要严格按照 DemoAPITestCase.yaml 模板格式编写,
名字可以变, 存放位置不要变, 调用时指定文件名 
2: yaml 测试报告名称可自定义或默认, 
```