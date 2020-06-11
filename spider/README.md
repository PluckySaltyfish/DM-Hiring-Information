### 项目简介
分布式爬虫，爬取智联招聘的信息，双向爬取。
### 环境及依赖

- scrapy
- python 2.7
- scrapy-redis
- mysqldb
- redis

### 运行方式
#### slaver 端
`zhilian/zhilian/spiders`下运行：

```python
scrapy run zl.py

```

#### master 端
运行redis,运行mysql,在mysql中运行`crawler.sql`
	
`zhilian`下运行

	python process_item_for_mysql.py


### 其它说明
#### 类别筛选
该项目爬取的是大数据相关职业，如果要爬取全部职业，可将`process_item_for_mysql.py`中的`url_arg1 = "&kw=大数据&sm=1&p=1"`改为`url_arg1 =&sm=1&p=1`，即删去此筛选。
同理也可以对其它的职位做相应筛选。

#### 分布式实现
用多台服务器（或PC）爬取的时候，需要将slaver端传输数据的IP地址修改成master主机的IP地址，即修改`zhilian/zhilian/settings.py`中的`REMOTE_HOST`。
	 