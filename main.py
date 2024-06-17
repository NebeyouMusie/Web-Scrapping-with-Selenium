from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

with open('Web-Scrapping-with-Selenium/data.json', 'w') as f:
    json.dump([], f)
    
    
def write_json(new_data, filename='Web-Scrapping-with-Selenium/data.json'):
  with open(filename, 'r+') as file:
    # load the existing data into a dictionary
    file_data = json.load(file)
    # join new_data e=with file_data
    file_data.append(new_data)
    # set file's current position at offset
    file.seek(0)
    # convert back to json
    json.dump(file_data, file, indent = 4)
    

driver = webdriver.Chrome()
driver.get('https://hdtoday.to/home')

try:
  element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main-wrapper"]/div/section[1]/div[2]')))
  
  elem_list = driver.find_element(By.ID, 'trending-movies')
  
  items = elem_list.find_elements(By.CLASS_NAME, 'flw-item')
  
  
  for item in items:
    title = item.find_element(By.TAG_NAME, 'h3').text
    year = item.find_element(By.CLASS_NAME, 'fdi-item').text
    duration = item.find_element(By.CLASS_NAME, 'fdi-duration').text
    type = item.find_element(By.CLASS_NAME, 'fdi-type').text
     
   
    print(f'Title: {title}')
    print(f'Year: {year}')
    print(f'Duration: {duration}')
    print(f'Type: {type}')
    
    
    # write to the json file
    write_json({
      'title': title,
      'year': year,
      'duration': duration,
      'type': type
    })
   
    

  time.sleep(10)

except Exception as e:
  print(e, 'Main Error')
