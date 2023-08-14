#import boto3
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time 

browser_options = ChromeOptions()
browser_options.headless = True

driver = Chrome(options = browser_options)
driver.get("http://www.mtslash.me/forum.php")
time.sleep(1)

element = driver.find_element(By.CLASS_NAME,"xs1")
count = element.find_element(By.TAG_NAME,"strong")
print(count.text)

driver.quit()








#import requests
#import time 
#import datetime

#def lambda_handler(event: any, context: any):
    #create a dynamodb client
    # dynamodb = boto3.resource("dynamodb")
    # table = dynamodb.Table('QingHuaTable')


#count_div = soup.find('div', id = 'wp')
# count_text = count_div.find('strong').text
# now = datetime.datetime.now()
# nowdate = now.date()
# nowtime = now.strftime("%H:%M")
# timezone = datetime.datetime.now().astimezone().tzinfo

    # response = table.put_item(
    #     Item={
    #         'date': str(nowdate),
    #         'time': str(nowtime),
    #         'timezone':str(timezone),
    #         'count' : str(count_text)
    #     }
    # )
    # return(response)

