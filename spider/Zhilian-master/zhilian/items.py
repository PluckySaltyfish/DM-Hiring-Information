# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # 第一层

    # 职位名称
    positionName = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 公司性质
    companyNature = scrapy.Field()
    # 公司规模
    companyScale = scrapy.Field()
    # 详细链接
    subUrl = scrapy.Field()

    # 第二层

    # 职位描述
    positionDescription = scrapy.Field()
    # 工作地点
    location = scrapy.Field()
    # 职位领域
    positionField = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()
    # 最低学历
    degree = scrapy.Field()
    # 最大工资
    maxSalary = scrapy.Field()
    # 最小工资
    minSalary = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    # 招聘人数
    vacancies = scrapy.Field()
    # 员工福利
    welfare = scrapy.Field()

