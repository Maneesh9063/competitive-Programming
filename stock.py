from bs4 import BeautifulSoup
from selenium import webdriver
import csv,os,datetime,time,json
# from hello import d
#with Display() :#as display:

a = os.getcwd()+'\\'+str(datetime.date.today())
try:
	os.mkdir(a)
except:
	pass
'''profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", a)#os.getcwd())#+str(a))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk",'image/png')# "file/png")
'''
driver = webdriver.Chrome(executable_path=r'C:\Users\SRI\Downloads\chromedriver_win32\chromedriver.exe')



#driver.get('https://chartink.com/login')

#driver.find_element_by_id('email').send_keys('soumith852@gmail.com')
#driver.find_element_by_id('password').send_keys('soumithchartink')
#driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[4]/div/button').click()

driver.get('https://chartink.com/screener/top-losers-11')

# with open('C:\\Users\\SRI\\Desktop\\test1.json') as handle:
# 	s=handle.read()
# for i in d:
# 	driver.add_cookie(i)
# 	print(d)

# while True:
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res,'lxml')

table = soup.find('table',{'id':'DataTables_Table_0'})
table_rows = table.find_all('tr')
data = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [ele.text for ele in td]
    data.append([ele for ele in row if ele]) # Get rid of empty values

data.pop(0)
count = int(data[-1][0])
# print(data[-1][0])
for i in data:
	with open(r'C:\Users\SRI\Desktop\cs.csv','a+',newline='') as f:
		writer = csv.writer(f)
		writer.writerow(i)
if count != 0:
    try:
      driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[8]/div[1]/div/div[5]/ul/li[3]/a').click()
    except:
      print("cant load or only 25 entries")
# elif count == 0:
# 	break


with open('cs.csv') as csvfile:
	readIt = csv.reader(csvfile,delimiter=',')
	for row in readIt:
		if row[2] != '2':
			driver.get('https://chartink.com/stocks/'+row[2]+'.html')
			# driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/form/div[1]/div[2]/select/option[1]').click()
			# driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/form/div[4]/div/div[2]/select/optgroup/option[1]').click()
			driver.find_element_by_xpath('//*[@id="innerb"]').click()
			# time.sleep(5)
			driver.switch_to.frame(driver.find_element_by_id('ChartImage'))
			driver.find_element_by_css_selector('div#saverbutton').click()

driver.quit()