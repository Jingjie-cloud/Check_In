from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def sockboom():
  try:
    driver = get_web_driver()
    driver.get("https://sockboom.bar/auth/login")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='email'] and @type='email'").click()
    driver.find_element_by_xpath("//*[@id='email']").send_keys('username')
    driver.find_element_by_xpath("//*[@id='passwd'] and @type='passwd'").click()
    driver.find_element_by_xpath("//*[@id='passwd']").send_keys('password')
    driver.find_element_by_xpath("//*[@id='login']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@style='display: inline-block; background-color: rgb(140, 212, 245); box-shadow: rgba(140, 212, 245, 0.8) 0px 0px 2px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset;']").click()
    time.sleep(2)
    try:
      driver.find_element_by_xpath("//*[@class='i-button button-check']").click()
    except:
      driver.find_element_by_xpath("//*[@style='display: inline-block; background-color: rgb(77, 155, 255); box-shadow: rgba(77, 155, 255, 0.8) 0px 0px 2px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset;']").click()
    time.sleep(3)
    chick_in = driver.find_element_by_xpath("//*[@class='i-button button-check']")
    ActionChains(driver).move_to_element(chick_in).perform()
    chick_in.click()
  except:
    raise
  finally:
    driver.quit()
if __name__ == '__main__':
  sockboom()
