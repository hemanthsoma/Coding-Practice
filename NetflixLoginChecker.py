from selenium import webdriver
try:
    gmailId='Your Mail Id'
    passWord = 'Your Password'
    driver =webdriver.Firefox()
    driver.get('https://netflix.com')
    driver.implicitly_wait(15) 
    signIn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/a')
    signIn.click()
    loginBox = driver.find_element_by_xpath('//*[@id="id_userLoginId"]') 
    loginBox.send_keys(gmailId)
    passWordBox = driver.find_element_by_xpath('//*[@id="id_password"]')
    passWordBox.send_keys(passWord)
    login = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button')
    login.click()
    print('Login Successful...!!') 
except: 
    print('Login Failed')
    
'''
Input your login detail
'''
