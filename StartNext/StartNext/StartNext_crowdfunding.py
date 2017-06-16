import scrapy
from scrapy.Selector import Selector

class StartNextSpider(scrapy.Spider):
    name="CrowdfundingComp"

    def start_requests(self):
        urls = []

##        for i in range(30):
##            urls.append("https://www.startnext.com/project/list/projects.php?lang=en&count=12"
##                                 "&q=fundings%2Fcrowdindex-d%2F10%2F4120&pageNr="+str(i)+"&topic=tyNavigationTopicID_4301&areas=content&page=")

##        for url in urls:
##            request = scrapy.Request(url=url, method="GET", headers= {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"}, encoding = "UTF-8")
##            yield request
        yield scrapy.Request(url="https://www.startnext.com/Projekte?utm_source=website&utm_medium=header#!fundings/crowdindex-d/10/4120",  method="GET", headers= {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"}, encoding = "UTF-8"
                             , callback=self.parse)

        def parse(self, response):
            s = Selector(response)
            links = s.xpath("//header[@class='headline']/a/@href.text()").extract()
            print(links)
##            for request in links:
##                data = scrapy.Request(request, method="GET", headers= {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"}, encoding = "UTF-8" )
##                yield data
##            def parse(self, response):
##                sel = Selector(response)
##                compDesc = sel.xpath("//section[@class='vcard']/div[@class='row'][2]/div/text()")[1].extract()
##                print(compDesc.strip())
