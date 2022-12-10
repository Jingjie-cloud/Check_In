from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def sockboom():
  try:
    driver = get_web_driver()
    driver.maximize_window()
    driver.get("https://sockboom.bar/auth/login")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//*[@id='email' and @type='email']").click()
    driver.find_element_by_xpath("//*[@id='email' and @type='email']").send_keys('username')
    driver.find_element_by_xpath("//*[@id='passwd' and @type='password']").click()
    driver.find_element_by_xpath("//*[@id='passwd' and @type='password']").send_keys('password')
    driver.find_element_by_xpath("//*[@class='btn btn-rose btn-simple btn-wd btn-lg']").click()
    driver.implicitly_wait(3)
    #driver.find_element_by_xpath("//*[@style='display: inline-block; background-color: rgb(140, 212, 245); box-shadow: rgba(140, 212, 245, 0.8) 0px 0px 2px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset;']").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[7]/div/button").click()
    driver.implicitly_wait(3)
    try:
      #driver.find_element_by_xpath("//*[@class='i-button button-check']").click()
      driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/section/div/section[2]/div/div[2]/div[2]/div/div[2]/div/p/button").click()
    except:
      #driver.find_element_by_xpath("//*[@style='display: inline-block; background-color: rgb(77, 155, 255); box-shadow: rgba(77, 155, 255, 0.8) 0px 0px 2px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset;']").click()
      driver.find_element_by_xpath("/html/body/div[3]/div[7]/div/button").click()
      chick_in = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/section/div/section[2]/div/div[2]/div[2]/div/div[2]/div/p/button")
      ActionChains(driver,2).move_to_element(chick_in).chick().perform()
  except:
    raise
  finally:
    driver.quit()
if __name__ == '__main__':
  sockboom()
