import scrapy
import pandas as pd
from scrapy.selector import Selector

##class StartNext(scrapy.Item):
##    category = scrapy.Field()
##    headline = scrapy.Field()
##    description = scrapy.Field()
##    funding = scrapy.Field()
##    remDays = scrapy.Field()

class StartNextSpider(scrapy.Spider):
    name = "CrowdfundingCompanies"
    data = pd.DataFrame()
    def start_requests(self):
        urls = []

        data = pd.DataFrame()
        for i in range(30):
            urls.append("https://www.startnext.com/project/list/projects.php?lang=en&count=12"
                                 "&q=fundings%2Fcrowdindex-d%2F10%2F4120&pageNr="+str(i)+"&topic=tyNavigationTopicID_4301&areas=content&page=")

        for url in urls:
            request = scrapy.Request(url=url, method="GET", headers={'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"},encoding="utf-8", callback=self.parse)
            request.meta['item'] = data
            yield  request
    def parse(self, response):
        # item = StartNext()
        s = Selector(response)

        # links = (s.xpath("//div[@class='image']/a/@href").extract())
        # filename = "links.txt"
        # with open(filename, "r") as f:
        #     if f.readline() == "":
        #         f.close()
        #         with open(filename, "w") as f:
        #             for link in links:
        #                 print(link)
        #                 f.write(link+"\n")
        #     else:
        #         f.close()
        #         with open(filename, "a") as f:
        #             for link in links:
        #                 print(link)
        #                 f.write(link+"\n")
        #         f.close()
        #
        # print("saved file %s" % links)
        category = s.xpath("//div[@class='image']/div[@class='category']/span[@class='text']/a/text()").extract()
        if len(category) < 12:
            category.append('X')
        else:
            pass
        headline = s.xpath("//header[@class='headline']/a/text()").extract()
        description = s.xpath("//div[@class='description']/div[@class='contains']/div[@class='teaser']/text()").extract()
        fundings = s.xpath("//div[@class='facts']/div[@class='facts-row']/span[@class='fact fundings']/span[@class='value']/text()").extract()
        remainingDays = s.xpath("//div[@class='facts']/div[@class='facts-row']/span[@class='fact remain']/span[@class='value']/span[@class='value']/text()").extract()
        period = s.xpath("//div[@class='facts']/div[@class='facts-row']/span[@class='fact remain']/span[@class='value']/span[@class='desc']/text()").extract()
        remDays = []
        desc = []
        print(description)
        for i in description:
            desc.append(i.strip())
        print(desc)    
        for i, j in zip(remainingDays, period):
            remDays.append(i +" "+ j)
        # item['category'] = category
        # item['headline'] = headline
        # item['description'] = desc
        # item['funding'] = fundings
        # item['remDays'] = remDays
        # yield item
        print(len(category), len(headline), len(desc), len(fundings), len(remDays))
        print(category)

        #Constructing dataframe and saving it to csv file
        data = pd.DataFrame({"category":category, "headline":headline, "description":desc, "funding":fundings, "Remaining Days":remDays})
        data.append(data)
        data = data[['category', 'headline', 'description', 'funding', 'Remaining Days']]
        data.to_csv("startnext.csv", mode='a')

        print("Finished writing to file")






