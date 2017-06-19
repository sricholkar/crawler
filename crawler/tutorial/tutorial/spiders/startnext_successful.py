import scrapy
import pandas as pd
from scrapy.selector import Selector

class startNextSpider(scrapy.Spider):
    name="startNextSuccessfulProjects"

    def start_requests(self):
        urls = []
        for i in range(500):
            urls.append("https://www.startnext.com/project/list/projects.php?"+
                        "lang=de&count=12&q=erfolgreich%2Fcrowdindex-d%2F10%2F4120&pageNr="+str(i)+"&topic=tyNavigationTopicID_4301&areas=content&page=")

                   
        for url in urls:
            request = scrapy.Request(url= url, method ="GET", headers = {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"},
                                     encoding="UTF-8", callback = self.parse)
            yield request

    def parse(self, response):
        s = Selector(response)
        links = s.xpath("//header[@class='headline']/a/@href").extract()
        for link in links:
            company = link.split("/")[-1]
            request = scrapy.Request(url=link, method ="GET", headers = {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"},
                                     encoding="UTF-8", callback = self.parseCompanyInfo)
            request.meta['item'] = company
            yield request

            
    def parseCompanyInfo(self, response):
        sel = Selector(response)
        company = response.meta['item']

        compCategory = sel.xpath("//section[@class='vcard']/div[@class='vcard__breadcrumb']/text()")[1].extract().split("/")[-1].strip()

        compFounder1 =  sel.xpath("//div[@class='row'][2]/div[@class='col-md-3 col-md-offset-1 col-sm-4 col-xs-12']/div")[2]
        compFounder2 = compFounder1.xpath(".//a/text()").extract_first()
        compFounder = compFounder2.strip()

        compCity1 = sel.xpath("//section[@class='vcard']/div[@class='row'][3]/div[@class='col-sm-8']/div[@class='vcard__tags clearfix']/span/text()")[0].extract()
        compCity = compCity1.strip()

        compDesc1 = sel.xpath("//section[@class='vcard']/div[@class='row']/div/text()")[1].extract()
        compDesc = compDesc1.strip()

        compFundingGoal = sel.xpath("//div[@class='fact article-funding-threshlod'][2]/span[@class='value']/text()").extract_first()

        compKeywords = sel.xpath("//div[@class='fact article-keywords']/span[@class='value']/text()").extract_first()

        comp_aboutProject = sel.xpath("//section[@class='sub-section']/div[1]/div[2]/div/p/text()").extract_first()

        comp_team_tot = []
        comp_team = sel.xpath("//div[@class='team']/div")
        comp_team_extracted = sel.xpath("//div[@class='team']/div").extract()
        TotInTeam = len(comp_team_extracted)
        for i in range(TotInTeam):
            comp_team_tot.append(comp_team.xpath(".//div/span[@class='headline']/a/text()")[i].extract().strip())
        comp_team_tot = " ".join(comp_team_tot)

        status = sel.xpath("//div[@class='fact fact-end success']/div[2]/span[@class='caption']/text()").extract_first()

        comp = [company, compCategory, compFounder, compCity, compDesc, compFundingGoal, compKeywords, comp_aboutProject, comp_team_tot, status]
        data = pd.DataFrame(comp).T
        data.to_csv("datasucc.csv", mode='a', header=False)



        

        

        

        
        
        
        
        
         
