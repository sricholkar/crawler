from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'C:\Webdriver\geckodriver.exe')
driver.get("https://www.startnext.com/sirplus/pinnwand/")
def mehr():
    i=0
    while i < 20:
        try:
            clicked1 = driver.find_elements_by_link_text('[mehr]')[i]
            driver.execute_script('arguments[0].click();', clicked1)
        except:
            i-=1
            try:
                clicked1 = (driver.find_elements_by_link_text('[weniger]')[i])
                driver.execute_script('arguments[0].scrollIntoView(true);', clicked1)
                mehr();
            except:
                break
            break
def toggle():
    i=0
    while i < 20:
        try:
            clicked1 = driver.find_elements_by_class_name('toggle-text')[i]
            driver.execute_script('arguments[0].click();', clicked1)
            mehr();
        except:
            break
    
mehr()
toggle()
output = (driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/section[3]/div/div/div").text.encode('utf-8'))
print (output.decode('utf-8'))
driver.close()
