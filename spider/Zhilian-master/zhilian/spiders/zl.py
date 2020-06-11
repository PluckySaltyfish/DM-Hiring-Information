# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from zhilian.items import ZhilianItem
import scrapy
import math

class ZlSpider(RedisSpider):
    name = 'zl'

    allowed_domains = ['sou.zhaopin.com', 'jobs.zhaopin.com']

    # start_urls = []
    # start_urls.append(baseUrl+city[0]+baseUrl2+str(offset))
    redis_key = 'zlspider:start_urls'

    def parse(self, response):
        # 取职位数
        number = response.xpath('//div[3]/div[3]/div[2]/span[1]/em/text()').extract()
        if not len(number):
            return
        offset = 1
        page = int(math.ceil(int(number[0]) / 60.0))
        yield scrapy.Request(url=response.url, meta={'meta_0': page,"meta_2":offset}, callback=self.page_parse)


    def page_parse(self,response):
        # 从初始页获取部分信息
        page = response.meta['meta_0']
        offset = response.meta['meta_2']
        items = []
        for j in range(0, len(response.xpath("//div[@class='newlist_detail newlist']").extract())):
            item = ZhilianItem()

            # 公司名称
            item['companyName'] = response.xpath('//form//ul/li[2]/a[1]/text()').extract()[j].replace('\'', '\"')

            # 公司性质
            item['companyNature'] = response.xpath('//form//ul/li[3]/span[2]/text()').extract()[j][5:].replace('\'',
                                                                                                               '\"')
            # 公司规模
            item['companyScale'] = response.xpath("//li[@class='newlist_deatil_two']/span[3]/text()").extract()[j][
                                   5:].replace('\'', '\"')

            # 详细链接
            item['subUrl'] = response.xpath('//form//ul/li[1]/div//@href').extract()[j]

            items.append(item)

        for item in items:
            # 发送详情页请求，传递item，并用detail_parse()处理所得响应
            print "request: " + item['subUrl']
            yield scrapy.Request(url=item['subUrl'], meta={'meta_1': item}, callback=self.detail_parse)

        offset += 1
        if offset <= page:
            pos = response.url.rfind('=')
            yield scrapy.Request(url=response.url[0:pos+1] + str(offset), meta={'meta_0':page,'meta_2':offset },callback=self.page_parse)


    def detail_parse(self,response):
        # 处理详情页信息
        item = response.meta['meta_1']
        # 职位名称
        item['positionName'] = response.xpath('//h1/text()').extract()[0].replace('\'', '\"')
        # 职位描述
        item['positionDescription'] = self.getDescription(response)
        # 工作地点
        item['location'] = self.getLocation(response).replace('\'','\"')
        # 职位领域
        item['positionField'] = self.getPositionField(response).replace('\'','\"')
        # 工作经验
        item['experience'] = self.getExperience(response)
        # 最低学历
        item['degree'] = self.getDegree(response)

        salary = self.getSalary(response)
        # 最小工资
        item['minSalary'] = salary[0]
        # 最大工资
        item['maxSalary'] = salary[1]
        # 发布时间
        item['publishTime'] = self.getPublishTime(response)
        # 招聘人数
        item['vacancies'] = self.getVacancies(response)
        # 员工福利

        item['welfare'] = self.getWelfare(response)
        # 将完整的item返回至redis
        yield item

    def getDescription(self, response):
        content = ""
        content = content.join(response.xpath("//div[6]/div[1]/div[1]/div/div[1]/descendant::text()").extract())
        content=''.join(content.split())
        content = content.replace('\r','')
        content = content.replace('\n','')
        content = content.replace('\t','')
        content = content.replace('\'','\"')
        return content

    def getLocation(self,response):
        location = response.xpath('//div[6]/div[1]/ul/li[2]/strong/a/text()').extract()
        if len(location):
            return location[0]
        else :
            return response.xpath('//div[6]/div[1]/ul/li[2]/strong/text()').extract()[0]

    def getPositionField(self, response):
        return response.xpath('//div[6]/div[1]/ul/li[8]/strong/a/text()').extract()[0]

    def getExperience(self, response):
        return response.xpath('//div[6]/div[1]/ul/li[5]/strong/text()').extract()[0]

    def getDegree(self, response):
        return response.xpath('//div[6]/div[1]/ul/li[6]/strong/text()').extract()[0]

    def getSalary(self,response):
        salary = response.xpath('//div[6]/div[1]/ul/li[1]/strong/text()').extract()[0].split('-')
        list = []

        if len(salary) == 2:
            # 最小工资
            list.append(int(salary[0]) / 1000)
            # 最大工资
            list.append(int(salary[1].split('/')[0][0:-1]) / 1000)
        else:
            list.append(salary[0])
            list.append(salary[0])
        return list

    def getPublishTime(self, response):
        return response.xpath("//span[@id='span4freshdate']/text()").extract()[0]

    def getVacancies(self, response):
        content =response.xpath("//div[6]/div[1]/ul/li[7]/strong/text()").extract_first()
        content=content.replace(u'人','')
        content=content.replace(' ','')
        return content

    def getWelfare(self,response):
        welfare = response.xpath("//div[@class='welfare-tab-box']/span/text()").extract()
        content = ""
        for each_item in welfare:
            content = content + each_item + ','
        return content[0:-1]