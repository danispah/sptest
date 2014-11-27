# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome import service


class DeCanon(unittest.TestCase):
    def setUp(self):
        fp = webdriver.FirefoxProfile()
	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("javascript.enabled", False)
	self.driver = webdriver.Firefox(firefox_profile=fp)
	self.driver.implicitly_wait(30)
        self.base_url = "http://sales-promotions/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_de_canon(self):
	driver = self.driver
	#~ driver.start_session(desired_capabilities={'javascriptEnabled': False})
	# open | /?link=canon-winter-2014-nordics-baltics.sales-promotions.com&country_promotion=9&lng=da | 
	driver.get(self.base_url + "/?link=canon-winter-2014-nordics-baltics.sales-promotions.com&country_promotion=9&lng=da")
	# assertTitle | Canons julekampagne | 
	self.assertEqual("Canons julekampagne", driver.title)
	# click | link=Udvalgte produkter | 
	driver.find_element_by_link_text("Udvalgte produkter").click()
	# click | link=Forhandlere | 
	driver.find_element_by_link_text("Forhandlere").click()
	# click | link=Indløs din gave | 
	driver.find_element_by_link_text(u"Indløs din gave").click()
	# click | css=input.next_step | 
	#~ driver.find_element_by_css_selector("input.next_step").click()
	# assertAlert | Titel:*
	# Ups! Nogle felter er obligatoriske. Udfyld venligst alle! | 
	# select | id=title | label=Hr.
	Select(driver.find_element_by_id("title")).select_by_visible_text("Hr.")
	# type | id=first_name | dsf
	driver.find_element_by_id("first_name").clear()
	driver.find_element_by_id("first_name").send_keys("dsf")
	# type | id=last_name | fsd
	driver.find_element_by_id("last_name").clear()
	driver.find_element_by_id("last_name").send_keys("fsd")
	# type | id=address_1 | fsd
	driver.find_element_by_id("address_1").clear()
	driver.find_element_by_id("address_1").send_keys("fsd")
	# type | id=city | dfs
	driver.find_element_by_id("city").clear()
	driver.find_element_by_id("city").send_keys("dfs")
	# type | id=postal_code | dfs
	driver.find_element_by_id("postal_code").clear()
	driver.find_element_by_id("postal_code").send_keys("dfs")
	# type | id=phone | dfs
	driver.find_element_by_id("phone").clear()
	driver.find_element_by_id("phone").send_keys("dfs")
	# type | id=email | dfs
	driver.find_element_by_id("email").clear()
	driver.find_element_by_id("email").send_keys("dfs")
	# type | id=email_confirm | dfs
	driver.find_element_by_id("email_confirm").clear()
	driver.find_element_by_id("email_confirm").send_keys("dfs")
	# click | css=input.next_step | 
	#~ driver.find_element_by_css_selector("input.next_step").click()
	# assertAlert | E-mail adresse:*
	# Angiv en gyldig e-mail-adresse | 
	#~ self.assertRegexpMatches(self.close_alert_and_get_its_text(), "^E-mail adresse:[\\s\\S]*\nAngiv en gyldig e-mail-adresse$")
	# type | id=phone | q
	driver.find_element_by_id("phone").clear()
	driver.find_element_by_id("phone").send_keys("q")
	# type | id=email | dfs@dfs.dd
	driver.find_element_by_id("email").clear()
	driver.find_element_by_id("email").send_keys("dfs@dfs.dd")
	# type | id=email_confirm | dfs@dfs.dd
	driver.find_element_by_id("email_confirm").clear()
	driver.find_element_by_id("email_confirm").send_keys("dfs@dfs.dd")
	# click | css=input.next_step | 
	#~ driver.find_element_by_css_selector("input.next_step").click()
	# select | id=answer_7893 | label=Latvia
	Select(driver.find_element_by_id("answer_7893")).select_by_visible_text("Latvia")
	# select | id=products_promotion1 | label=EOS100D
	#~ Select(driver.find_element_by_id("products_promotion1")).select_by_visible_text("EOS100D")
	# type | id=serial_number1 | dvcxv
	driver.find_element_by_id("serial_number1").clear()
	driver.find_element_by_id("serial_number1").send_keys("dvcxv")
	# click | id=reg_promotion_client_anchor_date_purchase1 | 
	driver.find_element_by_id("reg_promotion_client_anchor_date_purchase1").click()
	# click | link=19 | 
	#~ driver.find_element_by_link_text("19").click()
	# type | id=date_purchase1 | 19/11/2014
	#~ driver.find_element_by_id("date_purchase1").clear()
	driver.find_element_by_id("date_purchase1").send_keys("19/11/2014")
	# type | id=store_name1 | dv
	driver.find_element_by_id("store_name1").clear()
	driver.find_element_by_id("store_name1").send_keys("dv")
	# type | id=purchase_upload_file1 | C:\Users\YBSpahieva\Pictures\banner-en20141027183627.png
	#~ driver.find_element_by_id("purchase_upload_file1").clear()
	driver.find_element_by_id("purchase_upload_file1").send_keys("C:\\Users\\YBSpahieva\\Pictures\\banner-en20141027183627.png")
	# select | id=products_promotion2 | label=EF 50mm f/1.8 II
	#~ Select(driver.find_element_by_id("products_promotion2")).select_by_visible_text("EF 50mm f/1.8 II")
	# type | id=serial_number2 | dv
	driver.find_element_by_id("serial_number2").clear()
	driver.find_element_by_id("serial_number2").send_keys("dv")
	# click | css=#label-under-serial_number2 > div.table-cell.colspan2 > em > a | 
	driver.find_element_by_css_selector("#label-under-serial_number2 > div.table-cell.colspan2 > em > a").click()
	# click | id=reg_promotion_client_anchor_date_purchase2 | 
	driver.find_element_by_id("reg_promotion_client_anchor_date_purchase2").click()
	# click | link=15 | 
	#~ driver.find_element_by_link_text("15").click()
	# type | id=date_purchase2 | 15/11/2014
	#~ driver.find_element_by_id("date_purchase2").clear()
	driver.find_element_by_id("date_purchase2").send_keys("15/11/2014")
	# type | id=store_name2 | dsv
	driver.find_element_by_id("store_name2").clear()
	driver.find_element_by_id("store_name2").send_keys("dsv")
	# type | id=purchase_upload_file2 | C:\Users\YBSpahieva\Pictures\banner-1.png
	#~ driver.find_element_by_id("purchase_upload_file2").clear()
	driver.find_element_by_id("purchase_upload_file2").send_keys("C:\\Users\\YBSpahieva\\Pictures\\banner-1.png")
	# click | css=input.next_step | 
	#~ driver.find_element_by_css_selector("input.next_step").click()
	# click | id=terms | 
	driver.find_element_by_id("terms").click()
	# click | link=Kontakt os | 
	driver.find_element_by_link_text("Kontakt os").click()
	# click | link=Oplysninger om cookies | 
	driver.find_element_by_link_text("Oplysninger om cookies").click()
	# type | id=bank_name | dvs
	driver.find_element_by_id("bank_name").clear()
	driver.find_element_by_id("bank_name").send_keys("dvs")
	# type | id=bank_account | DV
	driver.find_element_by_id("bank_account").clear()
	driver.find_element_by_id("bank_account").send_keys("DV")
	# type | id=bank_code | DVS
	driver.find_element_by_id("bank_code").clear()
	driver.find_element_by_id("bank_code").send_keys("DVS")
	# type | id=bank_benficiary | vd
	driver.find_element_by_id("bank_benficiary").clear()
	driver.find_element_by_id("bank_benficiary").send_keys("vd")
	# click | id=button_subscribe | 
	driver.find_element_by_id("button_subscribe").click()
	# assertAlert | IBAN:*
	# Dine opplysninger er urette eller manglende. | 
	#~ self.assertRegexpMatches(self.close_alert_and_get_its_text(), "^IBAN:[\\s\\S]*\nDine opplysninger er urette eller manglende\\.$")
	# type | id=bank_account | DK5000400440116243
	driver.find_element_by_id("bank_account").clear()
	driver.find_element_by_id("bank_account").send_keys("DK5000400440116243")
	# click | id=button_subscribe | 
	driver.find_element_by_id("button_subscribe").click()
	# assertAlert | Swift-kode:*
	# Dine opplysninger er urette eller manglende. | 
	#~ self.assertRegexpMatches(self.close_alert_and_get_its_text(), "^Swift-kode:[\\s\\S]*\nDine opplysninger er urette eller manglende\\.$")
	# type | id=bank_code | DABADKKKAAR
	driver.find_element_by_id("bank_code").clear()
	driver.find_element_by_id("bank_code").send_keys("DABADKKKAAR")
	# click | id=button_subscribe | 
	driver.find_element_by_id("button_subscribe").click()
	# assertAlert | Ups! Nogle felter er obligatoriske. Udfyld venligst alle! | 
	#~ self.assertIn("Ups! Nogle felter er obligatoriske. Udfyld venligst alle!", self.close_alert_and_get_its_text())
	# click | id=terms_conditions | 
	driver.find_element_by_id("terms_conditions").click()
	# click | id=subscribe | 
	driver.find_element_by_id("subscribe").click()
	# click | id=button_subscribe | 
	driver.find_element_by_id("button_subscribe").click()
	# assertTitle | Canons julekampagne | 
	self.assertEqual("Canons julekampagne", driver.title)
	driver.save_screenshot('de_canon_ie_ty.png')
    
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
