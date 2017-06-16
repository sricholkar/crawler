# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import pandas as pd


class StartNextSpider(scrapy.Spider):
    name="CrowdfundingComp"

    def start_requests(self):
        urls = []
        
        for i in range(30):
            urls.append("https://www.startnext.com/project/list/projects.php?lang=en&count=12"
                                 "&q=fundings%2Fcrowdindex-d%2F10%2F4120&pageNr="+str(i)+"&topic=tyNavigationTopicID_4301&areas=content&page=")
##        req =  scrapy.Request(url = "https://www.startnext.com/Projekte?"
##                             +"utm_source=website&utm_medium=header#!fundings/crowdindex-d/10/4120",
##                             method="GET",
##                             headers= {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"},
##                             encoding = "UTF-8", callback=self.parse)
        for url in urls:
            req =  scrapy.Request(url = url,
                             method="GET",
                             headers= {'Referer':"https://www.startnext.com/projects?utm_source=website&utm_medium=header"},
                             encoding = "UTF-8", callback=self.parse)
##        req.meta['item'] = data
            yield req
        
    def parse(self, response):
        s = Selector(response)
        data = pd.DataFrame(columns = ['Category', "Description", "Founder", "City", "FundingThreshold", "FundingGoal", "Keywords", "AboutProject", "ProjectGoal", "Team"])
        links = s.xpath("//header[@class='headline']/a/@href").extract()
##        data = response.meta['item']  
        for request in links:
            req = scrapy.Request(request, method="GET", encoding="utf-8", callback=self.parse_1)
            req.meta['item'] = data
            yield req
            
    def parse_1(self, response):
##        sel = Selector(response)
        data = response.meta['item']
        fetchCommentsRequest = scrapy.Request(url= response.url+r'/pinnwand/#pnav', method="GET",
                             encoding = "UTF-8", callback=self.fetchComments)
        yield fetchCommentsRequest
##        compDesc1 = sel.xpath("//section[@class='vcard']/div[@class='row']/div/text()")[1].extract()
##        compDesc = compDesc1.strip()
##        
####        print(compDesc.strip())
##        compCategory1 = sel.xpath("//section[@class='vcard']/div[@class='vcard__breadcrumb']/text()")[1].extract()
##        compCategory = compCategory1.replace(r"/", "")
##        compCategory = compCategory.strip()
##       
####        print(compCategory.strip())
##        compFounder1 =  sel.xpath("//div[@class='row'][2]/div[@class='col-md-3 col-md-offset-1 col-sm-4 col-xs-12']/div")[2]
##        compFounder2 = compFounder1.xpath(".//a/text()").extract_first()
##        compFounder = compFounder2.strip()
####        print(compFounder.strip())
##        compCity1 = sel.xpath("//section[@class='vcard']/div[@class='row'][3]/div[@class='col-sm-8']/div[@class='vcard__tags clearfix']/span/text()")[0].extract()
##        compCity = compCity1.strip()
####        print(compCity.strip())
##        compFundThreshold = sel.xpath("//div[@class='fact article-funding-threshlod'][1]/span[@class='value']/text()").extract_first()
####        print(compFundThreshold)
##        compFundingGoal = sel.xpath("//div[@class='fact article-funding-threshlod'][2]/span[@class='value']/text()").extract_first()
####        print(compFundingGoal)
##        compKeywords = sel.xpath("//div[@class='fact article-keywords']/span[@class='value']/text()").extract_first()
####        print(compKeywords)
##        comp_aboutProject = sel.xpath("//section[@class='sub-section']/div[1]/div[2]/div/p/text()").extract_first()
####        print(comp_aboutProject)
##        comp_projectGoal = sel.xpath("//section[@class='sub-section']/div[2]/div[2]/div/p/text()").extract_first()
####        print(comp_projectGoal)
##        comp_team_tot = []
##        comp_team = sel.xpath("//div[@class='team']/div")
##        comp_team_extracted = sel.xpath("//div[@class='team']/div").extract()
##        TotInTeam = len(comp_team_extracted)
##        for i in range(TotInTeam):
##            comp_team_tot.append(comp_team.xpath(".//div/span[@class='headline']/a/text()")[i].extract().strip())
##        comp_team_tot = " ".join(comp_team_tot)
####        print(comp_team_tot)
####        data = pd.DataFrame({"Category":compCategory,"Description":compDesc, "Founder": compFounder, "City": compCity, "FundingThreshold" : compFundThreshold, "FundingGoal" : compFundingGoal, "Keywords" : compKeywords,
####                             "AboutProject": comp_aboutProject, "ProjectGoal" : comp_projectGoal, "Team" : comp_team_tot })
##        comp_team_tot = [compCategory, compDesc, compFounder, compCity, compFundThreshold, compFundingGoal, compKeywords, comp_aboutProject, comp_projectGoal, comp_team_tot]
##        lol = pd.DataFrame(comp_team_tot).T
##        lol.to_csv("data.csv", mode='a', header=False)

        
    def fetchComments(self, response):
        sel = Selector(response)
        print (sel.xpath("//section[@class='main-section pin-board-section']/div/div[@id='eqWall']"))
