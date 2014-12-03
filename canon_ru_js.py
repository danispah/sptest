# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CanonRuBank(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://canon-winter-2014-ru.sales-promotions.com/customer-apply-for-promotion/?country_promotion=18&lng=ru"
        #~ self.base_url = "http://sales-promotions/_webdevs/matanasov/customer-apply-for-promotion?link=canon-winter-2014-ru.sales-promotions.com&country_promotion=18&lng=ru"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_canon_ru_bank(self):
	    driver = self.driver
	    #~ unittest.main()
	    driver.get(self.base_url)
	    # type | id=first_name | IJIJOI
	    driver.find_element_by_id("first_name").clear()
	    driver.find_element_by_id("first_name").send_keys(u"Иван")
	    #~ driver.find_element_by_id("first_name").send_keys("123456ala153026002877"*100)
	    # type | id=mid_name | ;;'
	    driver.find_element_by_id("mid_name").clear()
	    driver.find_element_by_id("mid_name").send_keys(u"Иванов")
	    #~ driver.find_element_by_id("mid_name").send_keys("123456ala153026002877"*100)
	    # type | id=last_name | OI
	    driver.find_element_by_id("last_name").clear()
	    driver.find_element_by_id("last_name").send_keys(u"Иванов")
	    # type | id=city | KL
	    driver.find_element_by_id("city").clear()
	    driver.find_element_by_id("city").send_keys("KL")
	    # type | id=phone_mobile | +7901123456789
	    driver.find_element_by_id("phone_mobile").clear()
	    driver.find_element_by_id("phone_mobile").send_keys("+79721234567")
	    # type | id=email_confirm | qq@qq.qq
	    driver.find_element_by_id("email_confirm").clear()
	    driver.find_element_by_id("email").send_keys("qq@qq.qq")
	    driver.find_element_by_id("email_confirm").send_keys("qq@qq.qq")
	    # click | id=reg_promotion_client_anchor_date_birth | 
	    driver.find_element_by_id("reg_promotion_client_anchor_date_birth").click()
	    # click | id=reg_promotion_client_anchor_date_birth | 
	    #~ driver.find_element_by_id("reg_promotion_client_anchor_date_birth").click()
	    # click | css=a.cpCurrentDate | 
	    driver.find_element_by_css_selector("a.cpCurrentDate").click()
	    # click | css=a.cpCurrentDate | 
	    #~ driver.find_element_by_css_selector("a.cpCurrentDate").click()
	    # type | id=date_birth | 26/11/2014
	    driver.find_element_by_id("date_birth").clear()
	    driver.find_element_by_id("date_birth").send_keys("26/11/2014")
	    # select | id=answer_8043 | label=Из рассылки по электронной почте
	    Select(driver.find_element_by_id("answer_8043")).select_by_visible_text(u"Из рассылки по электронной почте")
	    # click | id=terms_conditions | 
	    driver.find_element_by_id("terms_conditions").click()
	    # click | css=input.next_step | 
	    driver.find_element_by_css_selector("input.next_step").click()
	    # select | id=series_promotions | label=Объективы
	    Select(driver.find_element_by_id("series_promotions")).select_by_visible_text(u"Объективы")
	    # select | id=products_promotion | label=EF-S60 F2.8 Macro USM
	    Select(driver.find_element_by_id("products_promotion")).select_by_visible_text("EF-S60 F2.8 Macro USM")
	    # type | id=serial_number | 123456
	    driver.find_element_by_id("serial_number").clear()
	    #~ driver.find_element_by_id("serial_number").send_keys("123456")
	    driver.find_element_by_id("serial_number").send_keys("153026002877")
	    #~ driver.find_element_by_id("serial_number").send_keys("123456ala")
	    #~ driver.find_element_by_id("serial_number").send_keys("123456ala153026002877"*100)
	    #~ print "123456ala153026002877"*100
	    dsc = 0
	    # select | id=series_promotions | label=Вспышки
	    #~ Select(driver.find_element_by_id("series_promotions")).select_by_visible_text(u"Вспышки")
	    #~ Select(driver.find_element_by_id("series_promotions")).select_by_visible_text(u"Компактные камеры") #dsc
	    #~ dsc = 1
	    #~ Select(driver.find_element_by_id("series_promotions")).select_by_visible_text(u"Видеокамеры") 
	    #~ dsc = 1
	    Select(driver.find_element_by_id("series_promotions")).select_by_visible_text(u"Зеркальные камеры")
	    # select | id=products_promotion | label=Speedlite 430 EX II
	    #~ Select(driver.find_element_by_id("products_promotion")).select_by_visible_text("Speedlite 430 EX II") #Вспышки
	    #~ Select(driver.find_element_by_id("products_promotion")).select_by_visible_text("SX510")  #Компактные камеры")
	    Select(driver.find_element_by_id("products_promotion")).select_by_visible_text("70D")  #Zеркальные камеры
	    #~ Select(driver.find_element_by_id("products_promotion")).select_by_visible_text("R506") #Видеокамеры
	    # click | css=input.next_step.showit | 
	    #~ driver.find_element_by_css_selector("input.next_step.showit").click()
	    xxx = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div/div[3]/div[2]/div[1]/div[2]/span")
	    xxx.click()
    	    driver.find_element_by_css_selector("input.next_step.showit").click()
	    #~ print  93, "Компактные камеры", u"UnexpectedAlertPresentException: Alert Text: \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0432\u0441\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u043b\u044f, \u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0435 \xab*\xbb.".encode('utf-8')
	    time.sleep(15)
	    # type | id=store_name | gdfg
	    #~ driver.find_element_by_id("store_name").clear()
	    driver.find_element_by_id("store_name").send_keys(u"Иванов")
	    # click | id=reg_promotion_client_anchor_date_purchase | 
	    driver.find_element_by_id("reg_promotion_client_anchor_date_purchase").click()
	    # click | link=26 | 
	    driver.find_element_by_link_text("Сегодня").click()
	    # type | id=date_purchase | 26/11/2014
	    driver.find_element_by_id("date_purchase").clear()
	    driver.find_element_by_id("date_purchase").send_keys("01/12/2014")
	    # select | id=answer_7941 | label=Да
	    Select(driver.find_element_by_id("answer_7941")).select_by_visible_text(u"Да")   #BUG if not selected!!!!!!!!!!!!!!!!!!!!!!!!!
	    # type | id=bank_name | gfd
	    if not dsc:
		    driver.find_element_by_id("bank_name").clear()
		    driver.find_element_by_id("bank_name").send_keys(u"Иванов")
		    # type | id=bank_account | 30101810600000000000
		    driver.find_element_by_id("bank_account").clear()
		    driver.find_element_by_id("bank_account").send_keys("30101810600000000000")
		    # type | id=bank_code_other | 30101810600000000000
		    driver.find_element_by_id("bank_code_other").clear()
		    driver.find_element_by_id("bank_code_other").send_keys("301018106000000000001")
		    # type | id=bank_branch_code | 30101810600000000000
		    driver.find_element_by_id("bank_branch_code").clear()
		    driver.find_element_by_id("bank_branch_code").send_keys("30101810600000000000")
		    # type | id=bank_account_type | 123456789
		    driver.find_element_by_id("bank_account_type").clear()
		    driver.find_element_by_id("bank_account_type").send_keys("123456789")
		    # type | id=bank_benficiary | ЕИОЕАГЖХЖГ
		    driver.find_element_by_id("bank_benficiary").clear()
		    driver.find_element_by_id("bank_benficiary").send_keys(u"ЕИОЕАГЖХЖГ")
	    # click | id=button_subscribe | 
	    driver.find_element_by_id("button_subscribe").click()
	    #~ if driver.find_element_by_id("bank_account") > 31
	    #~ self.assertIn(u"Введен неверный Номер счета, просьба введите правильный", self.close_alert_and_get_its_text())
	    # assertTitle | Canon Winter 2014 Russia |
	    #~ print u"Alert Text: \u041a\u043e\u0440\u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0441\u043a\u0438\u0439 \u0441\u0447\u0435\u0442:\u0412\u0432\u0435\u0434\u0435\u043d \u043d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u041d\u043e\u043c\u0435\u0440 \u043a\u043e\u0440\u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0441\u043a\u043e\u0433\u043e \u0441\u0447\u0435\u0442\u0430, \u043f\u0440\u043e\u0441\u044c\u0431\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439".encode('utf-8')
	    #~ print u"Alert Text: \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0432\u0441\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u043b\u044f, \u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0435 \xab*\xbb.".encode('utf-8')
	    self.assertEqual("Canon Winter 2014 Russia", driver.title)
	    driver.find_element_by_tag_name("h1")
	    driver.save_screenshot('canon_ru_mozilla_ty.png')
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        #~ self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()   
