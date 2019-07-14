import csv,os,time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path=r'C:\Users\SRI\Downloads\chromedriver_win32\chromedriver.exe')
i=11
while( i<61):
	driver.get('https://www.tkrcetautonomous.org')

	driver.find_element_by_id('lnkLogins').click()
	driver.find_element_by_xpath('//*[@id="lnkStudent"]').click()
	driver.find_element_by_id('txtUserId').send_keys('17K91A05'+('0'+str(i))if i<10 else '17K91A05'+str(i))
	driver.find_element_by_id('txtPwd').send_keys('17K91A05'+('0'+str(i))if i<10 else '17K91A05'+str(i))
	driver.find_element_by_id('btnLogin').click()

	try:
	
		table_path = '/html/body/form/div[3]/table[4]/tbody/tr/td/table/tbody/tr/td[2]/div/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/table[2]'
		driver.find_element_by_id('lnkStuInfo').click()
	except :
		with open('data.csv','a+',newline='') as g:
			writer = csv.writer(g)
			writer.writerow('some thong wrong')
		i +=1
		continue
	res = driver.execute_script("return document.documentElement.outerHTML")
	soup = BeautifulSoup(res,'lxml')

	table = soup.find('div',{'id':'cpStudCorner_PanelStuInfo'})
	#print(table)

	table_rows = table.find_all('tr')
	data = []
	temp = []

	y = table.find_all('input')
	for x in y:
		temp.append(str(x.get('value')))
	
	for tr in table_rows:
	    td = tr.find_all('td')
	    #print(td)
	    #print('\n\n\n')
	    row = [ele.text.replace('\n','') for ele in td]
	    #print(row)
	    data.append([ele for ele in row if ele]) # Get rid of empty values
	data.pop(0)
	data.pop(0)
	data.pop(0)

	flat_list = []
	for sublist in data:
	    for item in sublist:
	        flat_list.append(item)
	
	#print(temp)
	with open('data.csv','a+',newline='') as g:
		writer = csv.writer(g)
		if i==1:
		 	writer.writerow(flat_list)
		writer.writerow(temp)
	
	print (i)
	i +=1


