from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from pages.Locators.PCS.Locators import Locators
# from pages.Locators.LCCT.LCCT_Locators import Locators
# from pages.Locators.OMAN.OMAN_Locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random
import string
import os

# Format today's date as DD-MM-YYYY
today_date = datetime.now().strftime("%d-%m-%Y")

class SharedPage:

    # ✅ Define at class level so it's always available
    random_suffix = None  

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) 
        self.url = "https://app-pcs-next-ui-dev-centralindia-01-hkcbeggugrauggcc.centralindia-01.azurewebsites.net/"
        # self.url = "https://uatlcct.kalelogistics.com/login"
        # self.url = "https://cesuat.kalelogistics.com/login"
        # self.url = "https://acsuat.omanports.om/login"     

    def open(self):
        self.driver.get(self.url)

# ====================================================================================================
# LOGIN (START)
# ====================================================================================================
# For multiple login --------------------
    # def enter_credentials(self, username, password):
    #     self.driver.find_element(*Locators.username_input).send_keys(username)
    #     self.driver.find_element(*Locators.password_input).send_keys(password)

    def enter_ICP_credentials(self, username, password):
        wait = WebDriverWait(self.driver, 20)  # Increased timeout
    
        try:
            username_input = wait.until(EC.visibility_of_element_located(Locators.ICP_username_input))
            username_input.send_keys(username)
        except TimeoutException:
            print("❌ Username field not visible. Current URL:", self.driver.current_url)
            print(self.driver.page_source)
            raise

        try:
            password_input = wait.until(EC.visibility_of_element_located(Locators.ICP_password_input))
            password_input.send_keys(password)
        except TimeoutException:
            print("❌ Password field not visible. Current URL:", self.driver.current_url)
            print(self.driver.page_source)
            raise 
# -------------------------------------- LCCT START -----------

    def LCCT_enter_credentials(self, username, password):
        wait = WebDriverWait(self.driver, 20)  # Increased timeout
    
        try:
            LCCT_username_input = (By.XPATH, "//input[@id='txtEmailId']") 
            username_input = wait.until(EC.visibility_of_element_located(LCCT_username_input))
            username_input.send_keys(username)
        except TimeoutException:
            print("❌ Username field not visible. Current URL:", self.driver.current_url)
            print(self.driver.page_source)
            raise

        try:
            LCCT_password_input = (By.XPATH, "//input[@id='txtPasswordId']") 
            password_input = wait.until(EC.visibility_of_element_located(LCCT_password_input))
            password_input.send_keys(password)
        except TimeoutException:
            print("❌ Password field not visible. Current URL:", self.driver.current_url)
            print(self.driver.page_source)
            raise 


    def enter_text_in_LCCT_sidebar_search(self, search_text):
        try:
            LCCT_Menu_Search = (By.XPATH, "//input[@placeholder='Search']")
            print(f"🔍 Trying to enter 'search_text' in the LCCT sidebar search...")
            search_input = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(LCCT_Menu_Search)
            )
            search_input.clear()
            search_input.send_keys(search_text)
            print(f"✅ Entered 'search_text' in sidebar search.")
        except TimeoutException:
            print("❌ Sidebar search input not found or not visible.")
            self.driver.save_screenshot("sidebar_search_not_found.png")
            raise


# -------------------------------------- LCCT END -----------


# -------------------------------------- OMAN START -----------

    def OMAN_enter_credentials(self, username, password):
        wait = WebDriverWait(self.driver, 200)  # Increased timeout
    
        try:
            username_input = wait.until(EC.visibility_of_element_located(Locators.OMAN_username_input))
            username_input.send_keys(username)
        except TimeoutException:
            print("❌ Username field not visible. Current URL:", self.driver.current_url)
            print(self.driver.page_source)
            raise

        try:
            password_input = wait.until(EC.visibility_of_element_located(Locators.OMAN_password_input))
            password_input.send_keys(password)
        except TimeoutException:
            print("❌ Password field not visible. Current URL:", self.driver.current_url)
            print(self.driver.page_source)
            raise 

# -------------------------------------- OMAN END -----------


    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, "username")
        username_field.clear()
        # username_field.send_keys(username)
        username_field.send_keys(username.strip() if username else "")

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")  # Adjust locator
        password_field.clear()
        # password_field.send_keys(password)
        password_field.send_keys(password.strip() if password else "")    

    def click_ICP_login(self):
        self.driver.find_element(*Locators.submit).click()
        time.sleep(5)

    def click_avatar_button(self):
        self.driver.find_element(*Locators.avatar_button).click()
        time.sleep(2)   

    def click_ICP_Sign_Out_button(self):
        self.driver.find_element(*Locators.ICP_Sign_Out).click()
        time.sleep(2)              

    def click_LCCT_login(self):
        LCCT_SignIn = (By.XPATH, "//button[@id='btnLoginId']")
        self.driver.find_element(*LCCT_SignIn).click()
        time.sleep(5)    

    def click_OMAN_login(self):
        self.driver.find_element(*Locators.OMAN_SignIn).click()
        time.sleep(5)  

# ====================================================================================================
# LOGIN (END)
# ====================================================================================================


# ====================================================================================================
# DASHBOARD (START)
# ====================================================================================================

    def is_menu_collapsed(self):
        """
        Checks if the sidebar menu is collapsed.
        Returns True if collapsed, False if expanded.
        """
        sidebar_locator = (Locators.dashboard_expand_bar)
        sidebar_element = self.driver.find_element(*sidebar_locator)
        sidebar_class = sidebar_element.get_attribute("class")

        # Collapsed means 'sidebar-pinned' is NOT in the class
        return 'sidebar-pinned' not in sidebar_class

    def is_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.dashboard_header)
            )
            time.sleep(1)
            return self.driver.find_element(*Locators.dashboard_header).is_displayed()
        except Exception as e:
            print(f"Dashboard NOT found: {e}")
        return False
       

    def is_Register_New_Vessel_displayed(self):
        try:
            WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.Register_New_Vessel_Header)
            )
            time.sleep(1)
            return self.driver.find_element(*Locators.Register_New_Vessel_Header).is_displayed()
        except Exception as e:
            print(f"Dashboard NOT found: {e}")
        return False
# ------------------------------------ OMAN START-------------------------------------------

    def is_OMAN_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located(Locators.OMAN_dashboard_header)
            )
            time.sleep(1)
            print(f"INSIDE DASHBOARD PAGE") 
            return self.driver.find_element(*Locators.OMAN_dashboard_header).is_displayed()
        except Exception as e:
            print(f"Dashboard NOT found: {e}")
        return False

# Side Bar Export Start

    def exports_job_maintenance(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Export_Job_Maintenance))
            oneY_btn.click()
            time.sleep(2)
        except Exception as e:
            print(f"❌ Failed to click Exports shipment button: {e}") 


    def check_Export_Job_List_Label(self):
        try:
            WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located(Locators.Export_Job_List_Label)
            )
            time.sleep(1)
            print(f"INSIDE Shipment Listing PAGE") 
            return self.driver.find_element(*Locators.Export_Job_List_Label).is_displayed()
        except Exception as e:
            print(f"Export Shipment Listing NOT found: {e}")
        return False

# Side Bar Export End

# Side Bar Import Start

    def imports_job_maintenance(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Import_Job_Maintenance))
            oneY_btn.click()
            time.sleep(2)
        except Exception as e:
            print(f"❌ Failed to click Exports shipment button: {e}") 


    def check_Imports_Job_List_Label(self):
        try:
            WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located(Locators.Import_Job_List_Label)
            )
            time.sleep(1)
            print(f"INSIDE Shipment Listing PAGE") 
            return self.driver.find_element(*Locators.Import_Job_List_Label).is_displayed()
        except Exception as e:
            print(f"Export Shipment Listing NOT found: {e}")
        return False

# Side Bar Import End

    def click_oman_new_job_button(self):
        self.driver.find_element(*Locators.OMAN_create_new_job).click()
        time.sleep(5)      

    def click_oman_quick_awb(self):
        self.driver.find_element(*Locators.OMAN_quick_awb_link).click()
        time.sleep(5)  

    def check_Export_Create_Quick_AWB(self):
        try:
            WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located(Locators.OMAN_create_new_awb_header)
            )
            time.sleep(1)
            print(f"INSIDE Create Quick AWB") 
            return self.driver.find_element(*Locators.OMAN_create_new_awb_header).is_displayed()
        except Exception as e:
            print(f"Create Quick AWB NOT found: {e}")
        return False



# FROM BOGOTA FILE (START)   ==================================

        
    def click_shipment_type_and_select_direct(self):
        print("Waiting for Shipment Type dropdown to be clickable...")
        dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.shipment_type_dropdown)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()

        print("Waiting for 'DIRECT' option to appear...")
        direct = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.direct_option)
        )
        direct.click()
       
    def enter_prefix(self, prefix_value):
        print("Waiting for Prefix input field...")
        prefix_input = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.prefix_input)  # Update locator if needed
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", prefix_input)
        prefix_input.clear()
        prefix_input.send_keys(prefix_value)  
        time.sleep(3) 
        prefix_input.send_keys(Keys.TAB)
        print("Entered prefix and tabbed out.")  
        
               

    def enter_mawb_number(self):
        def generate_awb_number():
            serial_number = random.randint(1000000, 9999999)
            check_digit = serial_number % 7
            return f"{serial_number}{check_digit}"

        awb_number = generate_awb_number()
        print(f"Generated Air Way Bill Number: {awb_number}")

        mawb_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.mawb_no_field)
        )
        mawb_field.send_keys(awb_number)
        


    def select_destination(self):
        try:
            print("Clicking Destination (Dest) field...")
            dest_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((self.destination))
            )
            # dest_input.click()
            dest_input.clear()
            dest_input.send_keys("DWB")
            time.sleep(3) 
            print("Selected DWB in Destination field.")
        except Exception as e:
            self.driver.save_screenshot("dest_error.png")
            print("Failed to select Destination. Screenshot saved.")
            raise e        
        
    def enter_number_of_pieces(self, number):
        nop_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.nop)
        )
        nop_input.clear()
        nop_input.send_keys(number)        


    def enter_weight(self, number):
        weight_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.grwt)
        )
        weight_input.send_keys(number) 
        weight_input.send_keys(Keys.TAB)       

    def enter_flt_code(self, code):
        flt_code_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.fltCode)
        )
        flt_code_field.clear()
        flt_code_field.send_keys(code)
        print(f"Entered Flight Code: {code}")        

    def enter_fltNo(self, fltNo):
        wait = WebDriverWait(self.driver, 20)
        print("Waiting for Flight Number input field...")
        fltNo_input = wait.until(EC.element_to_be_clickable(self.fltNo))
        # fltNo_input.clear()
        fltNo_input.send_keys(fltNo)
        print("Entered Flight Number.")             
   
    def enter_flt_date(self):
        # Format today's date as DD/MM/YYYY
        dt = datetime.today()
        today = f"{dt.strftime('%d')}/0{dt.strftime('%m')}/{dt.strftime('%Y')}"
        print(today)
        # Wait for the date input field to be visible
        date_input = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.FLT_DATE_INPUT)
        )

        # date_input.clear()
        date_input.click()
        date_input.send_keys(today)
        date_input.send_keys(Keys.TAB)
           
    def enter_nature_of_goods(self, text):
        wait = WebDriverWait(self.driver, 20)
        print(f"Entering '{text}' in Nature of Goods field...")
        input_field = wait.until(EC.element_to_be_clickable(self.nature_of_goods_field))
        input_field.send_keys(text)   

    def enter_commodity(self, commodity_text):
        wait = WebDriverWait(self.driver, 20)
        input_field = wait.until(EC.element_to_be_clickable(self.commodity_field))
        input_field.send_keys(commodity_text) 
        time.sleep(3)
        # input_field.send_keys(Keys.TAB)    
    

    def select_shc_option(self):
        wait = WebDriverWait(self.driver, 10)
        
        # Click on the SHC dropdown
        wait.until(EC.element_to_be_clickable(self.SHC_DROPDOWN)).click()

        # Wait for the dropdown option and click
        wait.until(EC.element_to_be_clickable(self.SHC_OPTION_ACT)).click() 
        time.sleep(10)        


    def select_handling_location(self):
        # Step 1: Click input
        input_elem = WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(self.handling_location_input)
        )
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_elem)

        # Optional: small pause to stabilize after scroll
        time.sleep(0.5)

        # Step 2: Send keys to filter list
        input_elem.send_keys("MCT - MCT")
        time.sleep(2)
        input_elem.send_keys(Keys.TAB)


    def enter_gha(self, gha_value):
        print(f"Entering GHA: {gha_value}")

        # Step 1: Wait for field to be clickable
        gha_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.gha_input)
        )
        # Step 2: Send GHA value
        gha_field.send_keys(gha_value)
        time.sleep(5)
        gha_field.send_keys(Keys.TAB)
        time.sleep(5)  # Small buffer if dropdown appears

    def click_add_dimension(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_dimension_button)
        ).click()        

    def wait_for_cargo_info_popup(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.cargo_info_popup)
        )        
        time.sleep(2)

    def enter_pieces(self, pieces_value):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pieces_input)
        ).send_keys(pieces_value)    
        time.sleep(2)

    def enter_length(self, length_value):
        Length = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.length_input)
        )
        Length.clear()
        Length.send_keys(length_value)
        time.sleep(2)
        

    def enter_width(self, width_value):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.width_input)
        ).send_keys(width_value)     
        time.sleep(2)           

    def enter_height(self, height_value):
        Height = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.height_input)
        )
        Height.send_keys(height_value)
        Height.send_keys(Keys.TAB)  
        time.sleep(2)   

    def select_uom_cm(self):
        UOM = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.UOM_CM_OPTION)
            )
        UOM.click()    
                   

    def get_total_volumetric_wt(self):
        by, value = self.Tot_Volumetric_WT
        # Wait until value is non-empty
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(by, value).get_attribute("value").strip() != ""
        )
        wt_input = self.driver.find_element(by, value)
        time.sleep(5)
        return wt_input.get_attribute("value").strip()
                    

    def click_popup_save(self):
        by, value = self.Popup_Save_Button
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the button to be clickable
        save_button = wait.until(EC.element_to_be_clickable((by, value)))
        
        # Optionally scroll into view if necessary
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        
        # Now click
        save_button.click()
        print("Clicked Popup-SAVE button")

    def wait_for_create_quick_awb(self):
        self.wait.until(EC.visibility_of_element_located(self.CREATE_QUICK_AWB_TEXT))

# Click on AWB Save button & wait for Popup message 

    # Action method
    def click_save_and_wait_for_success(self):
        # Click SAVE
        time.sleep(5)
        save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()
        print("Clicked SAVE button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_button)

        time.sleep(5)
        # Wait for green success popup
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUCCESS_POPUP))
        print("Green success popup appeared")                    # self.driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        # time.sleep(1)  # Small delay to allow any animation to settle
        time.sleep(5)

# FROM BOGOTA FILE (END)     ==================================



    def oman_quick_AWB_save(self):
        self.driver.find_element(*Locators.Create_Quick_AWB_Save).click()
        time.sleep(5)  

# ------------------------------------ OMAN END-------------------------------------------


    # ------------------------------------ LCCT -------------------------------------------

    # def is_LCCT_dashboard_displayed(self):
    #     try:
    #         WebDriverWait(self.driver, 50).until(
    #         EC.visibility_of_element_located(Locators.LCCT_dashboard_header)
    #         )
    #         time.sleep(1)
    #         print(f"INSIDE DASHBOARD PAGE") 
    #         return self.driver.find_element(*Locators.LCCT_dashboard_header).is_displayed()
    #     except Exception as e:
    #         print(f"Dashboard NOT found: {e}")
    #     return False

    def click_1Y(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.LCCT_1Y))
            oneY_btn.click()
            time.sleep(3)
        except Exception as e:
            print(f"❌ Failed to click 1Y button: {e}")

    # def exports_menu(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 50)
    #         oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Exports_Dropdown))
    #         oneY_btn.click()
    #     except Exception as e:
    #         print(f"❌ Failed to click Exports menu button: {e}")

    def export_Report(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Export_Report))
            oneY_btn.click()
            time.sleep(20)
        except Exception as e:
            print(f"❌ Failed to click Exports shipment button: {e}")           

    def exports_shipment(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Export_Shipments))
            oneY_btn.click()
            time.sleep(20)
        except Exception as e:
            print(f"❌ Failed to click Exports shipment button: {e}")     

    def exports_checklist_approval(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Export_Checklist_Approval))
            oneY_btn.click()
            time.sleep(20)
        except Exception as e:
            print(f"❌ Failed to click Exports Checklist Approval button: {e}")       

    def export_declaration(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            oneY_btn = wait.until(EC.element_to_be_clickable(Locators.Export_Declaration))
            oneY_btn.click()
            time.sleep(20)
        except Exception as e:
            print(f"❌ Failed to click Exports Declaration button: {e}") 
# -------------------------------------------------------------------------------------------------
    def check_LCCT_Export_Reports_Label(self):
        try:
            WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(Locators.Export_LCCT_Reports_Label)
            )
            time.sleep(1)
            print(f"INSIDE Export Report PAGE") 
            return self.driver.find_element(*Locators.Export_LCCT_Reports_Label).is_displayed()
        except Exception as e:
            print(f"Export Report NOT found: {e}")
        return False              

    def check_Export_Shipment_Listing_Label(self):
        try:
            WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(Locators.Export_Shipment_Listing_Label)
            )
            time.sleep(1)
            print(f"INSIDE Shipment Listing PAGE") 
            return self.driver.find_element(*Locators.Export_Shipment_Listing_Label).is_displayed()
        except Exception as e:
            print(f"Export Shipment Listing NOT found: {e}")
        return False

    def check_Export_Checklist_Approval_Label(self):
        try:
            WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(Locators.Export_Checklist_Approval_Label)
            )
            time.sleep(1)
            print(f"INSIDE Export Report PAGE") 
            return self.driver.find_element(*Locators.Export_Checklist_Approval_Label).is_displayed()
        except Exception as e:
            print(f"Export Report NOT found: {e}")
        return False

    def check_Export_Declarations_List_Label(self):
        try:
            WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(Locators.Export_Declarations_List_Label)
            )
            time.sleep(1)
            print(f"INSIDE Export Report PAGE") 
            return self.driver.find_element(*Locators.Export_Declarations_List_Label).is_displayed()
        except Exception as e:
            print(f"Export Report NOT found: {e}")
        return False

# -------------------------------------------------------------------------------------------------
    def LCCT_Company_Setup_Branch(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            CompanySetupBranch_btn = wait.until(EC.element_to_be_clickable(Locators.LCCT_CompanySetupBranch))
            CompanySetupBranch_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f"❌ Failed to click Company Setup Branch button: {e}") 
# -------------------------------------------------------------------------------------------------

    def click_LCCT_add_new_company_branch_button(self):
        """Click the LCCT Company Setup Branch Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.LCCT_Add_CompanySetupBranch)
        ).click() 
# -------------------------------------------------------------------------------------------------

    def is_lcct_branch_save_visible(self):
        """Check the LCCT Company Setup Branch SAVE button"""
        try:
            WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(Locators.LCCT_SAVE)
            )
            time.sleep(1)
            print(f"LCCT Branch SAVE") 
            return self.driver.find_element(*Locators.LCCT_SAVE).is_displayed()
        except Exception as e:
            print(f"LCCT Branch SAVE NOT found: {e}")
        return False
# -------------------------------------------------------------------------------------------------
    def LCCT_Logout(self):
        try:
            LCCT_Logout = (By.XPATH, "//span[normalize-space()='Logout']")
            wait = WebDriverWait(self.driver, 50)
            logout_btn = wait.until(EC.element_to_be_clickable(*LCCT_Logout))
            logout_btn.click()
            time.sleep(8)
        except Exception as e:
            print(f"❌ Failed to click Logout button: {e}")                                     

    def LCCT_expand_sidebar(self):
        try:
            wait = WebDriverWait(self.driver, 50)
            toggle_btn = wait.until(EC.element_to_be_clickable(Locators.LCCT_sidebar_toggle))
            toggle_btn.click()
            print("✅ Sidebar toggle button clicked successfully.")
        except Exception as e:
            print(f"❌ Failed to click sidebar toggle: {e}")
        # try:
        #     # time.sleep(20)
        #     print(f"INSIDE TRY BLOCK") 
        #     sidebar_toggle = WebDriverWait(self.driver, 50).until(
        #         EC.visibility_of_element_located(Locators.LCCT_sidebar_toggle)
        #     )
        #     actions = ActionChains(self.driver)
        #     actions.move_to_element(sidebar_toggle).pause(1).perform()
        # except Exception as e:
        #     print(f"Error while expanding sidebar: {e}")  
    # ------------------------------------ LCCT -------------------------------------------

    def get_title_text(self):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.dashboard_header)
        )
        return title_element.text        

    def get_welcome_text(self):
        welcome_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.welcome_message)
        )
        return welcome_element.text  

    def get_logged_in_username(self):
        user_name_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.user_name)
        )
        return user_name_element.text       

#  ----- Dashboard Date Start-------

    def verify_date_field(self):
        """
        Verifies the date field value shown in the top-right corner of the dashboard.
    
        Parameters:
            driver (webdriver.Chrome): An active Selenium WebDriver instance.
            expected_value (str): Default expected placeholder or date value.
            timeout (int): Time to wait for the element.

        Returns:
            bool: True if expected or actual date is found, False otherwise.
        """

        try:
            # Wait for the span inside the date button
            # wait = WebDriverWait(driver, timeout)
            date_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.dashboard_date))
            date_text = date_element.text.strip()
            print(f"Found date field with text: '{date_text}'")
            expected_value="DD/MM/YYYY"
            # Check against expected placeholder or a valid date format
            if date_text == expected_value:
                print("✅ Placeholder date is correctly displayed.")
                return True
            elif len(date_text) == 10 and "/" in date_text:
                print(f"✅ Actual date is displayed: {date_text}")
                return True
            else:
                print(f"❌ Unexpected date value: {date_text}")
                return False
        except Exception as e:
            print(f"❌ Exception while verifying date field: {e}")
            return False
#  ----- Dashboard Date End --------  


#  ----- Text Size Start -------
    def click_text_resize_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.text_size)
        ).click()

#  ----- Text Size End -------


#  ----- Select Theme Start -------
    def click_theme_toggle_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.select_theme)).click()
#  ----- Select Theme End -------


#  ----- Select Theme Start -------
    def click_language_toggle_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.language_selector)
        ).click()
#  ----- Select Theme End -------

    def is_login_failed(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located(Locators.invalid_Username_Password))
            return "invalid" in error.text.lower()
        except:
            return False    

    def click_sidebar_toggle_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(Locators.sidebar_button)
        ).click()
        time.sleep(3)

    def get_user_role_label(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(
            (Locators.CommunityAdminLabel)
        ))
        return element.text
# ====================================================================================================
# DASHBOARD (END)
# ====================================================================================================


# ========================================================================================================
# SEARCH (START) 
# ========================================================================================================   
    def enter_search_text(self, text):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.search_input)
        )
        search_box.clear()
        search_box.send_keys(Locators.text)

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page until the Submit button is visible."""
        submit_locator = (By.XPATH, "//button[contains(.,'Submit')]")

        # Scroll until the Submit button is in view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", 
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(submit_locator)
            )
        )
        print("✅ Scrolled to the bottom of the page.")    
# ========================================================================================================
# SEARCH (END) 
# ========================================================================================================


# ========================================================================================================
# Community Admin  (START) 
# ========================================================================================================
    def is_Login_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Login_message)
            )
            time.sleep(1)
            return True
        except:
            print("Login message NOT displayed")
            return False
        
    def is_Welcome_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.welcome_message)
            )
            time.sleep(1)
            return True
        except:
            print("Welcome message NOT displayed")
            return False        
        
    def enter_text_in_sidebar_search(self, search_text):
        try:
            print(f"🔍 Trying to enter Search Text in the sidebar search...")
            search_input = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(Locators.ICP_search_input)
            )
            search_input.clear()
            search_input.send_keys(search_text)
            time.sleep(3)  # small wait to let results load 
            print(f"✅ Entered Sesrch Text in sidebar search.")
        except TimeoutException:
            print("❌ Sidebar search input not found or not visible.")
            self.driver.save_screenshot("sidebar_search_not_found.png")
            raise
   
    
    def click_template_mgmt_toggle(self):
        # self.driver.find_element(*Locators.Template_Management_toggle).click()
        print("✅ Template Toggle button is clicked.")
        toggle = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.Template_Management_toggle)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)
        time.sleep(1)
        toggle.click()

    def check_Registration_Template(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Registration_Template)
        )
    
    def check_Transaction_Template(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Transaction_Template)
        )

    def check_Registration_Requests(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Registration_Requests)
        )

    def click_Workflow_Conf_toggle(self):
        self.driver.find_element(*Locators.Workflow_Configuration_toggle).click()
        time.sleep(1)

    def check_Registration_Approval_Workflow(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Registration_Approval_Workflow)
        )

    def check_Transaction_Approval_Workflow(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Transaction_Approval_Workflow)
        )

    def click_vessel_mgmt_toggle(self):
        print("✅ Vessel Toggle button is clicked.")
        toggle = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.Vessel_Management_toggle)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)
        toggle.click()
        time.sleep(3)

    def navigate_to_vessel_profile(self):
        try:
            Vessel_Profile = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.Vessel_Profile)
            )
            print("✅ Vessel Profile element is clickable.")
            Vessel_Profile.click()
        except Exception as e:
            print(f"❌ Failed to find or click Vessel Profile: {e}")
            self.driver.save_screenshot("vessel_profile_not_found.png")
            raise
                     

    def navigate_to_vessel_registration(self):
        try:
            vessel_registration = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Vessel_Registration)
            )
            # Scroll into view first
            self.driver.execute_script("arguments[0].scrollIntoView(true);", vessel_registration)
            time.sleep(1)  # let UI settle

            # Click with ActionChains to avoid overlap
            ActionChains(self.driver).move_to_element(vessel_registration).click().perform()
            print("✅ Vessel Registration clicked successfully.")
        except Exception as e:
            print(f"❌ Failed to find or click Vessel Registration: {e}")
            self.driver.save_screenshot("vessel_registration_not_found.png")
            raise

# ===============================================

    def navigate_to_ship_call_number(self):
        try:
            ship_call_number = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.ship_call_number)
            )
            # Scroll into view first
            self.driver.execute_script("arguments[0].scrollIntoView(true);", ship_call_number)
            time.sleep(1)  # let UI settle

            # Click with ActionChains to avoid overlap
            ActionChains(self.driver).move_to_element(ship_call_number).click().perform()
            print("✅ Ship Call Number clicked successfully.")
        except Exception as e:
            print(f"❌ Failed to find or click Ship Call Number: {e}")
            self.driver.save_screenshot("ship_call_number_not_found.png")
            raise

    def navigate_to_pre_arrival_notification(self):
        try:
            pre_arrival_notification = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.pre_arrival_notification)
            )
            # Scroll into view first
            self.driver.execute_script("arguments[0].scrollIntoView(true);", pre_arrival_notification)
            time.sleep(1)  # let UI settle

            # Click with ActionChains to avoid overlap
            ActionChains(self.driver).move_to_element(pre_arrival_notification).click().perform()
            print("✅ Pre-Arrival Notification clicked successfully.")
        except Exception as e:
            print(f"❌ Failed to find or click Pre-Arrival Notification: {e}")
            self.driver.save_screenshot("pre_arrival_notification_not_found.png")
            raise

    def navigate_to_arrival_clearance(self):
        try:
            arrival_clearance = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.arrival_clearance)
            )
            # Scroll into view first
            self.driver.execute_script("arguments[0].scrollIntoView(true);", arrival_clearance)
            time.sleep(1)  # let UI settle

            # Click with ActionChains to avoid overlap
            ActionChains(self.driver).move_to_element(arrival_clearance).click().perform()
            print("✅ Arrival Clearance clicked successfully.")
        except Exception as e:
            print(f"❌ Failed to find or click Arrival Clearance: {e}")
            self.driver.save_screenshot("arrival_clearance_not_found.png")
            raise

    def navigate_to_departure_clearance(self):
        try:
            departure_clearance = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.departure_clearance)
            )
            # Scroll into view first
            self.driver.execute_script("arguments[0].scrollIntoView(true);", departure_clearance)
            time.sleep(1)  # let UI settle

            # Click with ActionChains to avoid overlap
            ActionChains(self.driver).move_to_element(departure_clearance).click().perform()
            print("✅ Departure Clearance clicked successfully.")
        except Exception as e:
            print(f"❌ Failed to find or click Departure Clearance: {e}")
            self.driver.save_screenshot("departure_clearance_not_found.png")
            raise

# ===============================================
        

    def check_Stakeholder_Management(self):
        try:
            # Wait for the element to be visible
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Stakeholder_Management)
            )
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Wait for it to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.Stakeholder_Management)
            )

            # Click
            element.click()
            print("✅ Stakeholder Management clicked.")

        except Exception as e:
            print(f"❌ Failed to click Stakeholder Management: {e}")
            raise

    def check_Terminal_Configuration(self):
        try:
            # Wait for the element to be visible
            Terminal_Configuration = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Terminal_Configuration)
            )
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", Terminal_Configuration)

            # Wait for it to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.Terminal_Configuration)
            )

            # Click
            Terminal_Configuration.click()
            print("✅ Terminal Configuration clicked.")

        except Exception as e:
            print(f"❌ Failed to click Terminal Configuration: {e}")
            raise        
# ========================================================================================================
# Community Admin  (END) 
# ========================================================================================================

# ========================================================================================================
# Registration Template  (START) 
# ========================================================================================================
    def validate_Registration_Template_Header(self):
        try:
            # ✅ Wait until loader disappears (max 60 seconds)
            WebDriverWait(self.driver, 60).until(
                EC.invisibility_of_element_located(Locators.Loading_Spinner)
            )

            # ✅ Wait until the header is visible (max 60 seconds)
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(Locators.Registration_Template_Header)
            )

            header = self.driver.find_element(*Locators.Registration_Template_Header)
            if header.is_displayed():
                print("✅ Registration Template header is displayed.")
                return True
            else:
                print("❌ Registration Template header is not visible.")
                return False

        except NoSuchElementException:
            print("❌ Registration Template header not found.")
            return False

        except Exception as e:
            print(f"❌ Exception while validating Registration Template header: {e}")
            return False


    def Create_New_Registration_Template(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Create_New_Registration_Template)
        ) 

    def Choose_Shipping_Agent(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(Locators.Choose_Shipping_Agent)
        ) 
    
    def Click_Next(self):
        try:
            # Wait for the button to be present in the DOM
            next_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(Locators.Click_Next)
            )

            # Scroll into view (to avoid "not clickable" issues)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", next_button)
            time.sleep(1)  # Optional small delay

            # Wait until button is clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.Click_Next)
            )

            next_button.click()
            print("✅ Clicked on NEXT button.")
            return True
        except TimeoutException:
            print("❌ NEXT button not found within timeout.")
            return False
        except Exception as e:
            print(f"❌ Exception while clicking NEXT button: {e}")
            return False
        
    def User_Registration_Type(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.User_Registration_Type)
        )    

    def Registration_Next(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Registration_Next)
        )            
 
    def Label_Create_New_Template(self):
        label = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Label_Create_New_Template)
        )
        assert label.text.strip() == "Create New Template"
        return True
    
    def enter_random_template_name(self, context):
        random_number = random.randint(000, 999)
        template_name = f"ShippingAgents{random_number}"
        self.template_name = template_name  # optional: store it for later use

        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.Template_Name_Input)
        ).send_keys(template_name)
        context.template_name = template_name  # store in context

    def enter_template_description(self, context):
        # description = f"Shipping Agent Description"
        description = f"{context.template_name}_Description"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Template_Description_Input)
        ).send_keys(description)
        time.sleep(2)        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_save_button(self):
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.SAVE_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)   

    def click_save_button(self):
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SAVE_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
        time.sleep(5)
        save_btn.click()
        time.sleep(3)

    def click_Preview_button(self):
        preview_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.PREVIEW_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", preview_btn)
        time.sleep(5)
        preview_btn.click()  

    def click_go_back_to_edit(self):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(Locators.GO_BACK_TO_EDIT)
            )
            element.click()
            print("✅ GO BACK TO EDIT button clicked.")
        except Exception as e:
            print(f"⚠️ Standard click failed: {e}. Trying with JavaScript.")
            try:
                js_element = self.driver.find_element(*Locators.GO_BACK_TO_EDIT)
                self.driver.execute_script("arguments[0].click();", js_element)
                print("✅ Clicked GO BACK TO EDIT using JavaScript.")
            except Exception as e:
                print(f"❌ JS click also failed: {e}")
                self.driver.save_screenshot("go_back_to_edit_failure.png")
                raise       

    def click_Cancel_button(self):
        cancel_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CANCEL_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cancel_btn)
        time.sleep(5)
        cancel_btn.click()   

    def dont_Cancel(self):
        dont_Cancel_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.NO_DONT_CANCEL)
        )
        dont_Cancel_btn.click()
        time.sleep(2)           

    def confirm_Cancel(self):
        confirm_cancel_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.YES_CANCEL_BUTTON)
        )
        confirm_cancel_btn.click()
        time.sleep(5)     

    def Template_Name_Filter(self, template_name):
        try:
            print("🔍 Locating Template Name filter chip...")
            chip = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(Locators.Template_Name_Column_Filter)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", chip)

            clickable_chip = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Template_Name_Column_Filter)
            )
            clickable_chip.click()
            print("✅ Clicked on Template Name filter chip.")

            # Now locate the input field
            filter_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Add_filter_value)
            )
            filter_input.clear()
            filter_input.send_keys(template_name)
            print(f"✅ Entered template name: {template_name}")
            time.sleep(2)

        except Exception as e:
            self.driver.save_screenshot("Template_Name_Filter_Failed.png")
            print("❌ Filter chip not found or not clickable. Screenshot saved.")
            raise e

    def Edit_Post_Search(self):
        Edit_Post_Search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Edit_Post_Search)
        )
        Edit_Post_Search.click()
        time.sleep(5)                                
# ========================================================================================================
# Registration Template  (END) 
# ========================================================================================================


# ========================================================================================================
# Transaction Template  (START) 
# ========================================================================================================
    def validate_Transaction_Template_Header(self):
        try:
            # ✅ Wait until loader disappears (max 60 seconds)
            WebDriverWait(self.driver, 60).until(
                EC.invisibility_of_element_located(Locators.Loading_Spinner)
            )

            # ✅ Wait until the header is visible (max 60 seconds)
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(Locators.Transaction_Template_Header)
            )

            header = self.driver.find_element(*Locators.Transaction_Template_Header)
            if header.is_displayed():
                print("✅ Transaction Template header is displayed.")
                return True
            else:
                print("❌ Transaction Template header is not visible.")
                return False

        except NoSuchElementException:
            print("❌ Transaction Template header not found.")
            return False

        except Exception as e:
            print(f"❌ Exception while validating Transaction Template header: {e}")
            return False    

    def transaction_click_go_back_to_edit(self):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(Locators.Transaction_Back_to_Edit)
            )
            element.click()
            print("✅ GO BACK TO EDIT button clicked.")
        except Exception as e:
            print(f"⚠️ Standard click failed: {e}. Trying with JavaScript.")
            try:
                js_element = self.driver.find_element(*Locators.GO_BACK_TO_EDIT)
                self.driver.execute_script("arguments[0].click();", js_element)
                print("✅ Clicked GO BACK TO EDIT using JavaScript.")
            except Exception as e:
                print(f"❌ JS click also failed: {e}")
                self.driver.save_screenshot("transact_go_back_to_edit_failure.png")
                raise
# ========================================================================================================
# Transaction Template  (END) 
# ========================================================================================================



# ========================================================================================================
# Registration REQUESTS (START) 
# ========================================================================================================
    def verify_stakeholder_registration_request_list_heading(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Registration_Request_Header)
            )
            return True
        except TimeoutException:
            return False
        
    def click_all_filter_stakeholder_requests(self):
        """Click the 'All' filter in Stakeholder Registration Request List."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Registration_Request_All)
        ).click()

    def click_pending_filter_stakeholder_requests(self):
        """Click the 'Pending' filter in Stakeholder Registration Request List."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Registration_Request_Pending)
        ).click()

    def click_approved_filter_stakeholder_requests(self):
        """Click the 'Approved' filter in Stakeholder Registration Request List."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Registration_Request_Approved)
        ).click()      

    def click_rejected_filter_stakeholder_requests(self):
        """Click the 'Rejected' filter in Stakeholder Registration Request List."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Registration_Request_Rejected)
        ).click()   


    def scroll_to_extreme_right(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.Registration_Request_horizontal_bar)
        )
        self.driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", element)
        time.sleep(1)

    def scroll_to_extreme_left(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.Registration_Request_horizontal_bar)
        )
        self.driver.execute_script("arguments[0].scrollLeft = 0", element)
        time.sleep(1)

    def click_tile_and_verify_status(self, tile_locator, expected_status=None):
        # Click on the tile
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tile_locator)).click()
        
        # Wait for table to refresh
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*Locators.Registration_Request_Approval_Status_Cells)) > 0
        )
        
        # Get all statuses from the last column
        statuses = [cell.text.strip() for cell in self.driver.find_elements(*Locators.Registration_Request_Approval_Status_Cells)]
        
        if expected_status:  # For Pending / Approved / Rejected
            assert all(status == expected_status for status in statuses), \
                f"❌ Expected all '{expected_status}', but got {statuses}"
        else:  # For 'All' tile
            assert any(status != "" for status in statuses), \
                "❌ No statuses found for 'All' tile"
        
        print(f"✅ Verification passed for tile '{expected_status or 'All'}' - statuses: {statuses}")

    def verify_all_tiles(self):
        self.click_tile_and_verify_status(Locators.Registration_Request_All)
        self.click_tile_and_verify_status(Locators.Registration_Request_Pending, expected_status="Pending")
        self.click_tile_and_verify_status(Locators.Registration_Request_Approved, expected_status="Approved")
        self.click_tile_and_verify_status(Locators.Registration_Request_Rejected, expected_status="Rejected")        
# ========================================================================================================
# Registration REQUESTS (END) 
# ========================================================================================================



# ========================================================================================================
# ORGANIZATION SETUP (START) 
# ========================================================================================================

    def expand_organization_setup(self):
        """Clicks the arrow button to expand/collapse Organization Setup submenu"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Organization_Setup_Header)
        ).click()


# ========================================================================================================
# ORGANIZATION SETUP (END) 
# ========================================================================================================

# ========================================================================================================
# BRANCH (START) 
# ========================================================================================================
    def verify_branch_heading_present(self):
        """Verify Branch Management heading is displayed"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Branch_Management_Header)
        ).is_displayed()  
    
    def create_branch_user(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_Branch_Button)
        ).click()
    
    def enter_branch_name(self, context):
        random_suffix = random.randint(1000, 9999)
        branchname = f"Branch{random_suffix}"

        field = self.driver.find_element(*Locators.Branch_Name)
        field.clear()
        field.send_keys(branchname)

        # ✅ Save into behave context
        context.generated_branchname = branchname  

        print(f"✅ Unique Branchname entered: {branchname}")
        return branchname    
    
    def enter_branch_email_id(self, context):
        if not hasattr(context, "generated_branchname"):
            raise Exception("Branchname not generated yet. Call enter_branchname() first.")

        email_id = f"{context.generated_branchname}@example.com"
        field = self.driver.find_element(*Locators.Branch_Email_ID)
        field.clear()
        field.send_keys(email_id)
        print(f"✅ Email ID entered: {email_id}")

    def enter_branch_phone_no(self, phone_no):
        field = self.driver.find_element(*Locators.Branch_Phone_No)
        field.clear()
        field.send_keys(phone_no)
        print(f"✅ Phone No entered: {phone_no}") 

    # def enter_branch_admin_Address_Line_1(self, Address_Line_1):
    #     field = self.wait.until(EC.element_to_be_clickable(Locators.Address_Line_1))
    #     field.clear()
    #     field.send_keys(Address_Line_1)
    #     print(f"✅ First Name entered: {Address_Line_1}")

    def enter_branch_admin_Address_Line_1(self, Address_Line_1):
        try:
            field = self.wait.until(
                EC.presence_of_element_located(Locators.Branch_Address_Line_1)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.Branch_Address_Line_1))
            field.clear()
            field.send_keys(Address_Line_1)
            print(f"✅ Address Line 1 entered: {Address_Line_1}")
        except Exception as e:
            raise Exception(f"Unable to enter Branch Address Line 1: {e}")
    

    def enter_branch_admin_Address_Line_2(self, Address_Line_2):
        field = self.wait.until(EC.element_to_be_clickable(Locators.Branch_Address_Line_2))
        field.clear()
        field.send_keys(Address_Line_2)
        print(f"✅ First Name entered: {Address_Line_2}")

    def enter_branch_admin_Address_Line_3(self, Address_Line_3):
        field = self.wait.until(EC.element_to_be_clickable(Locators.Branch_Address_Line_3))
        field.clear()
        field.send_keys(Address_Line_3)
        print(f"✅ First Name entered: {Address_Line_3}")    

    def click_branch_city_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_City)
            )
            dropdown.click()
            print("✅ Clicked on City dropdown")
            time.sleep(2)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_City_select)
            )
            select_branch.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected City in City dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select in City dropdown: {e}")
        
    def enter_branch_admin_Postcode(self, Postcode):
        field = self.wait.until(EC.element_to_be_clickable(Locators.Branch_Postcode))
        field.clear()
        field.send_keys(Postcode)
        print(f"✅ First Name entered: {Postcode}")

    def click_branch_state_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_State)
            )
            dropdown.click()
            print("✅ Clicked on State dropdown")
            time.sleep(2)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_State_select)
            )
            select_branch.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected State in State dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select in State dropdown: {e}")
                
    def click_branch_country_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_Country)
            )
            dropdown.click()
            print("✅ Clicked on Country dropdown")
            time.sleep(2)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_Country_select)
            )
            select_branch.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected State in Country dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select in Country dropdown: {e}")

    def enter_branch_admin_first_name(self, first_name):
        field = self.wait.until(EC.element_to_be_clickable(Locators.Branch_Admin_First_Name))
        field.clear()
        field.send_keys(first_name)
        print(f"✅ First Name entered: {first_name}")
    
    def enter_branch_admin_middle_name(self, middle_name):
        field = self.driver.find_element(*Locators.Branch_Admin_Middle_Name)
        field.clear()
        field.send_keys(middle_name)
        print(f"✅ Middle Name entered: {middle_name}")
    
    def enter_branch_admin_last_name(self, last_name):
        field = self.driver.find_element(*Locators.Branch_Admin_Last_Name)
        field.clear()
        field.send_keys(last_name)
        print(f"✅ Last Name entered: {last_name}")
    
    def enter_branch_admin_designation(self, designation):
        field = self.driver.find_element(*Locators.Branch_Admin_Designation)
        field.clear()
        field.send_keys(designation)
        print(f"✅ Designation entered: {designation}")
    
    def enter_branch_admin_email_id(self, context):
        if not hasattr(context, "generated_username"):
            raise Exception("Username not generated yet. Call enter_username() first.")

        email_id = f"{context.generated_username}@example.com"
        field = self.driver.find_element(*Locators.Branch_Admin_Email_ID)
        field.clear()
        field.send_keys(email_id)
        print(f"✅ Email ID entered: {email_id}")

    def enter_branch_admin_phone_no(self, phone_no):
        field = self.driver.find_element(*Locators.Branch_Admin_Phone_No)
        field.clear()
        field.send_keys(phone_no)
        print(f"✅ Phone No entered: {phone_no}")        

    def enter_branch_admin_username(self, context):
        random_suffix = random.randint(1000, 9999)
        username = f"User{random_suffix}"

        field = self.driver.find_element(*Locators.Branch_Admin_Username)
        field.clear()
        field.send_keys(username)

        # ✅ Save into behave context
        context.generated_username = username  

        print(f"✅ Unique Username entered: {username}")
        return username    
        
    def save_new_branch(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Branch_SAVE)
        ).click()

    def cancel_new_branch(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Branch_CANCEL)
        ).click()

    def Branch_Name_Filter(self, branch_name):
        try:
            print("🔍 Locating Template Name filter chip...")
            chip = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(Locators.Branch_Name_Column_Filter)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", chip)

            clickable_chip = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Branch_Name_Column_Filter)
            )
            clickable_chip.click()
            print("✅ Clicked on Template Name filter chip.")

            # Now locate the input field
            filter_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Add_filter_value)
            )
            filter_input.clear()
            filter_input.send_keys(branch_name)
            print(f"✅ Entered template name: {branch_name}")
            time.sleep(2)   

        except Exception as e:
            self.driver.save_screenshot("Template_Name_Filter_Failed.png")
            print("❌ Filter chip not found or not clickable. Screenshot saved.")
            raise e
                         
    def View_Branch_Post_Search(self):
        Edit_Post_Search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Branch_Name_View)
        )
        Edit_Post_Search.click()
        time.sleep(5) 

    def Edit_Branch_Post_Search(self):
        Edit_Post_Search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Branch_Name_Edit)
        )
        Edit_Post_Search.click()
        time.sleep(5)         

    def view_branch_heading_present(self):
        """Verify View Branch heading is displayed"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.View_Branch_Header)
        ).is_displayed()  

    def get_branch_username(self):
        try:
            field = self.wait.until(
                EC.visibility_of_element_located(Locators.View_Branch_Username)
            )
            return field.text.strip()
        except Exception as e:
            raise Exception(f"Unable to fetch Branch Username: {e}")

# ========================================================================================================
# BRANCH (END) 
# ========================================================================================================
    def open_branch(self):
        """Clicks Organization Information submenu option"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Branch)
        ).click()

# ========================================================================================================
# USER (START) 
# ========================================================================================================
    def open_user(self):
        """Clicks Organization Information submenu option"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.User)
        ).click()

    def verify_heading_present(self):
        """Verify User Management heading is displayed"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.User_management_page_heading)
        ).is_displayed()      

    def create_new_user(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.create_new_user)
        ).click()


    def click_user_type_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.User_Type_Dropdown)
            )
            dropdown.click()
            print("✅ Clicked on User Type dropdown")
            time.sleep(1)  # small delay so options load
            select_user = self.wait.until(
                EC.element_to_be_clickable(Locators.User_select)
            )
            select_user.click()
            time.sleep(1)  # small delay so options load
            print("✅ Selected 'User' in User Type dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select in User Type dropdown: {e}")

    def click_branch_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.User_Branch_Dropdown)
            )
            dropdown.click()
            print("✅ Clicked on Branch dropdown")
            time.sleep(2)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.Branch_select)
            )
            select_branch.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected 'User' in Branch dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select in Branch dropdown: {e}")

    def enter_first_name(self, first_name):
        field = self.wait.until(EC.element_to_be_clickable(Locators.User_First_Name))
        field.clear()
        field.send_keys(first_name)
        print(f"✅ First Name entered: {first_name}")

    def enter_middle_name(self, middle_name):
        field = self.driver.find_element(*Locators.User_Middle_Name)
        field.clear()
        field.send_keys(middle_name)
        print(f"✅ Middle Name entered: {middle_name}")

    def enter_last_name(self, last_name):
        field = self.driver.find_element(*Locators.User_Last_Name)
        field.clear()
        field.send_keys(last_name)
        print(f"✅ Last Name entered: {last_name}")

    def enter_designation(self, designation):
        field = self.driver.find_element(*Locators.User_Designation)
        field.clear()
        field.send_keys(designation)
        print(f"✅ Designation entered: {designation}")

    def enter_phone_no(self, phone_no):
        field = self.driver.find_element(*Locators.User_Phone_No)
        field.clear()
        field.send_keys(phone_no)
        print(f"✅ Phone No entered: {phone_no}")

    def enter_email_id(self, context):
        if not hasattr(context, "generated_username"):
            raise Exception("Username not generated yet. Call enter_username() first.")

        email_id = f"{context.generated_username}@example.com"
        field = self.driver.find_element(*Locators.User_Email)
        field.clear()
        field.send_keys(email_id)
        print(f"✅ Email ID entered: {email_id}")

    def enter_username(self, context):
        random_suffix = random.randint(1000, 9999)
        username = f"User{random_suffix}"

        field = self.driver.find_element(*Locators.User_UserName)
        field.clear()
        field.send_keys(username)

        # ✅ Save into behave context
        context.generated_username = username  

        print(f"✅ Unique Username entered: {username}")
        return username

    def save_new_user(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.User_SAVE_button)
        ).click()

    def cancel_new_user(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.User_CANCEL_button)
        ).click()        

# ========================================================================================================
# USER (END) 
# ========================================================================================================


# ========================================================================================================
# REGISTRATION APPROVAL WORKFLOW (START) 
# ========================================================================================================
    def verify_workflow_page_title(self):
        expected_title = "Registration Approval Workflow Management"
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Registration_Approval_Workflow_Management_header)
        )
        assert element.text.strip() == expected_title, f"Expected '{expected_title}', but got '{element.text}'"

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_Registration_Approval_Workflow)).click()  

    def select_initiator_type_self(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.initiatorType))
        Select(dropdown).select_by_visible_text("Self")


    def enter_random_workflow_name(self, context):
        random_number = random.randint(1000, 9999)
        workflow_name = f"Shipping_Agent_Workflow_{random_number}"
        context.workflow_name = workflow_name  # store for later use

        workflow_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Workflow_Name))
        workflow_field.clear()
        workflow_field.send_keys(workflow_name)

    def enter_workflow_description(self, context):
        workflow_description = f"{context.workflow_name}_Description"
        description_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Workflow_Description))
        description_field.clear()
        description_field.send_keys(workflow_description)

    def drag_customs_to_stage_1(self):
        wait = WebDriverWait(self.driver, 20)
        source = wait.until(
            EC.presence_of_element_located(
                Locators.Customs_tile
            )
        )
        target = wait.until(
            EC.presence_of_element_located(
                Locators.Drag
            )
        )
        # Step 1: Pointer-based drag to get Angular's listeners active
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).pause(0.5).release().perform()
        # Step 2: Fire JS-based HTML5 drop to complete data transfer
        drag_and_drop_js = """
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function (key, value) {
                        this.data[key] = value;
                    },
                    getData: function (key) {
                        return this.data[key];
                    }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent("on" + event.type, event);
                }
            }
            var source = arguments[0];
            var target = arguments[1];
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(source, dragStartEvent);
            var dragEnterEvent = createEvent('dragenter');
            dispatchEvent(target, dragEnterEvent, dragStartEvent.dataTransfer);
            var dragOverEvent = createEvent('dragover');
            dispatchEvent(target, dragOverEvent, dragStartEvent.dataTransfer);
            var dropEvent = createEvent('drop');
            dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(source, dragEndEvent, dragStartEvent.dataTransfer);
        """
        self.driver.execute_script(drag_and_drop_js, source, target)
        # Step 3: Verify drop
        try:
            wait.until(EC.presence_of_element_located(Locators.STAGE_1))
            print("✅ Dragged 'Customs' to Stage 1 successfully.")
        except TimeoutException:
            raise AssertionError("❌ Customs was not found inside Stage 1 after drop.")      

    def click_add_stage_button(self):
        # Wait for presence
        add_stage_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.ADD_STAGE_BUTTON)
        )

        # Wait for it to become clickable and enabled
        WebDriverWait(self.driver, 15).until(
            lambda driver: add_stage_btn.is_enabled() and add_stage_btn.is_displayed()
        )

        add_stage_btn.click()
        print("✅ Clicked on ADD STAGE button successfully.") 

    def click_raw_SAVE_button(self):
        """Scroll to bottom and click the SAVE button"""
        try:
            save_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.RAW_SAVE)
            )
            # Scroll SAVE button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
            # Small pause in case of sticky headers/footers
            time.sleep(1)
            save_btn.click()
            print("✅ Clicked on SAVE button after scrolling")
        except Exception as e:
            raise Exception(f"Unable to click on SAVE button: {e}")
        
    def is_workflow_error_popup_displayed(self):
        """Check whether the workflow error popup is displayed"""
        try:
            popup = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(Locators.RAW_SAVE_Error)
            )
            return popup.is_displayed()
        except:
            return False    


# ========================================================================================================
# Registration Approval Workflow (END) 
# ========================================================================================================



# ========================================================================================================
# Transaction Approval Workflow (START) 
# ========================================================================================================
    def verify_transaction_workflow_header(self):
        expected_title = "Transaction Workflow"
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Transaction_Workflow_Header)
        )
        assert element.text.strip() == expected_title, f"Expected '{expected_title}', but got '{element.text}'"


    def click_TAW_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_Transaction_Approval_Workflow)).click()  

    def TAW_Vessel_Management(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(Locators.Choose_Vessel_Management)
        ) 

    def Click_TAW_Next(self):
        try:
            # Wait for the button to be present in the DOM
            next_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(Locators.Module_Type_Next)
            )

            # Scroll into view (to avoid "not clickable" issues)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", next_button)
            time.sleep(1)  # Optional small delay

            # Wait until button is clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.Module_Type_Next)
            )

            next_button.click()
            print("✅ Clicked on NEXT button.")
            return True
        except TimeoutException:
            print("❌ NEXT button not found within timeout.")
            return False
        except Exception as e:
            print(f"❌ Exception while clicking NEXT button: {e}")
            return False

    def Vessel_Registration_Type(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Choose_Vessel_Registration)
        )    
    time.sleep(2) 
      

    def sub_module_Next(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.sub_module_Next)
        )         

    # def select_TAW_initiator_type_self(self):
    #     dropdown = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(Locators.TAW_initiatorType))
    #     Select(dropdown).select_by_visible_text("SHIPPING_AGENT")

    def select_TAW_initiator_type_self(self):
        try:
            # Step 1: Open the dropdown
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.TAW_initiatorType)
            )
            dropdown.click()
            time.sleep(1)  # give animation time

            # Step 2: Click the SHIPPING_AGENT option
            option = self.wait.until(
                EC.element_to_be_clickable(Locators.TAW_initiatorType_value)
            )
            option.click()
            print("✅ SHIPPING_AGENT selected in Initiator Type")

        except Exception as e:
            raise Exception(f"❌ Unable to select Initiator Type (SHIPPING_AGENT): {e}")
    
    def enter_random_TAW_workflow_name(self, context):
        random_number = random.randint(1000, 9999)
        workflow_name = f"Vessel_Agent_Workflow_{random_number}"
        context.workflow_name = workflow_name  # store for later use

        workflow_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TAW_Workflow_Name))
        workflow_field.clear()
        workflow_field.send_keys(workflow_name)

    def enter_TAW_workflow_description(self, context):
        workflow_description = f"{context.workflow_name}_Description"
        description_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.TAW_Workflow_Description))
        description_field.clear()
        description_field.send_keys(workflow_description)

    def drag_TAW_customs_to_stage_1(self):
        wait = WebDriverWait(self.driver, 20)
        source = wait.until(
            EC.presence_of_element_located(
                Locators.TAW_Customs_tile
            )
        )
        target = wait.until(
            EC.presence_of_element_located(
                Locators.TAW_Drag
            )
        )
        # Step 1: Pointer-based drag to get Angular's listeners active
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).pause(0.5).release().perform()
        # Step 2: Fire JS-based HTML5 drop to complete data transfer
        drag_and_drop_js = """
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function (key, value) {
                        this.data[key] = value;
                    },
                    getData: function (key) {
                        return this.data[key];
                    }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent("on" + event.type, event);
                }
            }
            var source = arguments[0];
            var target = arguments[1];
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(source, dragStartEvent);
            var dragEnterEvent = createEvent('dragenter');
            dispatchEvent(target, dragEnterEvent, dragStartEvent.dataTransfer);
            var dragOverEvent = createEvent('dragover');
            dispatchEvent(target, dragOverEvent, dragStartEvent.dataTransfer);
            var dropEvent = createEvent('drop');
            dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(source, dragEndEvent, dragStartEvent.dataTransfer);
        """
        self.driver.execute_script(drag_and_drop_js, source, target)
        # Step 3: Verify drop
        try:
            wait.until(EC.presence_of_element_located(Locators.TAW_STAGE_1))
            print("✅ Dragged 'Customs' to Stage 1 successfully.")
        except TimeoutException:
            raise AssertionError("❌ Customs was not found inside Stage 1 after drop.")      

    def click_TAW_SAVE_button(self):
        """Scroll to bottom and click the SAVE button"""
        try:
            save_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.TAW_SAVE)
            )
            # Scroll SAVE button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
            # Small pause in case of sticky headers/footers
            time.sleep(1)
            save_btn.click()
            print("✅ Clicked on SAVE button after scrolling")
        except Exception as e:
            raise Exception(f"Unable to click on SAVE button: {e}")
        
    def click_TAW_CANCEL_button(self):
        """Scroll to bottom and click the SAVE button"""
        try:
            cancel_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.TAW_CANCEL)
            )
            # Scroll SAVE button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cancel_btn)
            # Small pause in case of sticky headers/footers
            time.sleep(1)
            cancel_btn.click()
            print("✅ Clicked on SAVE button after scrolling")
        except Exception as e:
            raise Exception(f"Unable to click on SAVE button: {e}")   

    def click_TAW_discard_CANCEL_button(self):
        """Scroll to bottom and click the discard Cancel button"""
        try:
            discard_cancel_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.TAW_DISCARD_CANCEL)
            )
            time.sleep(1)
            discard_cancel_btn.click()
            print("✅ Clicked on Discard SAVE button")
        except Exception as e:
            raise Exception(f"Unable to click on Discaed SAVE button: {e}")   

    def click_TAW_confirm_CANCEL_button(self):
        """Scroll to bottom and click the confirm Cancel button"""
        try:
            confirm_cancel_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.TAW_CONFIRM_CANCEL)
            )
            time.sleep(1)
            confirm_cancel_btn.click()
            print("✅ Clicked on Confirm SAVE button")
        except Exception as e:
            raise Exception(f"Unable to click on Confirm SAVE button: {e}")                     

    def click_TAW_add_stage_button(self):
        # Wait for presence
        add_stage_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.TAW_ADD_STAGE_BUTTON)
        )

        # Wait for it to become clickable and enabled
        WebDriverWait(self.driver, 15).until(
            lambda driver: add_stage_btn.is_enabled() and add_stage_btn.is_displayed()
        )

        add_stage_btn.click()
        print("✅ Clicked on ADD STAGE button successfully.") 

# ========================================================================================================
# Transaction Approval Workflow (END) 
# ========================================================================================================


# ========================================================================================================
# SCN (START) 
# ========================================================================================================
    def open_scn_page(self):
        """Clicks Vessel Management submenu option"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SCN)
        ).click()

    def Verify_SCN_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.SCN_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False    
            
    def Create_new_SCN(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_SCN)
        ).click()

    def Verify_Create_New_SCN_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Create_SCN_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False         

    def enter_scn_Vessel_ID(self, Vessel_ID):
        field = self.wait.until(EC.element_to_be_clickable(Locators.SCN_Vessel_ID))
        field.clear()
        field.send_keys(Vessel_ID)
        print(f"✅ SCN Vessel_ID entered: {Vessel_ID}")

    def click_GO_button(self):
        """Click the GO button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SCN_GO)
        ).click()
        time.sleep(2)

    def select_scn_port(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.SCN_Port)
            )
            dropdown.click()
            print("✅ Clicked on Port dropdown")
            search_port = self.wait.until(EC.element_to_be_clickable(Locators.SCN_Port_Search))
            search_port.clear()
            search_port.send_keys("INNSA")
            print(f"✅ SCN search port entered: INNSA")            
            time.sleep(2)  # small delay so options load
            select_port = self.wait.until(
                EC.element_to_be_clickable(Locators.SCN_Port_select)
            )
            select_port.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Port dropdown")
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Port dropdown: {e}")
        
    def select_scn_terminal(self):
        try:
            terminal_dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.SCN_Terminals)
            )
            terminal_dropdown.click()
            print("✅ Clicked on Terminal dropdown")           
            time.sleep(2)  # small delay so options load
            select_terminal = self.wait.until(
                EC.element_to_be_clickable(Locators.SCN_Terminal_Name)
            )
            select_terminal.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Terminal Name dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Terminal dropdown: {e}")  
              
    # def scn_eta_date(self):
    #     try:
    #         # Step 1: Click ETA calendar field
    #         eta_calendar = self.wait.until(
    #             EC.element_to_be_clickable(Locators.ETA))
    #         try:
    #             eta_calendar.click()
    #         except:
    #         # fallback JS click
    #             self.driver.execute_script("arguments[0].click();", eta_calendar)
    #         print("✅ Clicked on ETA Calendar")           
    #         time.sleep(1)  # small delay so options load
    #         # Step 2: Calculate next date
    #         next_day = datetime.now() + timedelta(days=1)
    #         day_str = str(next_day.day)  # e.g., '25'
    #         # Step 3: Locator for calendar day span
    #         # Assuming each day is a <span> with text equal to the day number
    #         calendar_day_locator = f"(//span[normalize-space()='{day_str}'])[1]"
    #         # Step 4: Action - click the next day's span
    #         select_date = self.wait.until(
    #         EC.element_to_be_clickable((By.XPATH, calendar_day_locator)))
    #         select_date.click()
    #         time.sleep(2)
    #     except Exception as e:
    #         raise Exception(f"❌ Unable to click and select ETA Date: {e}")   


    def scn_eta_date(self):
        try:
            # Step 1: Click ETA calendar field
            eta_calendar = self.wait.until(
                EC.element_to_be_clickable(Locators.ETA))
            try:
                eta_calendar.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", eta_calendar)
            print("✅ Clicked on ETA Calendar")           
            time.sleep(1)  # small delay so options load

            # Step 2: Navigate to next month
            eta_next_month = self.wait.until(
                EC.element_to_be_clickable(Locators.ETA_Next_Month))
            try:
                eta_next_month.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", eta_next_month)
            print("✅ Clicked on ETA next month")           
            time.sleep(1)  # small delay so options load

            # Step 3: Click on 1st of Next month
            eta_next_month_first = self.wait.until(
                EC.element_to_be_clickable(Locators.ETA_Next_Month_First))
            try:
                eta_next_month_first.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", eta_next_month_first)
            print("✅ Clicked on ETA next month 1st")           
            time.sleep(1)  # small delay so options load
        except Exception as e:
            raise Exception(f"❌ Unable to click and select ETA Date: {e}")               


    def scn_etd_date(self):
        try:
            # Step 1: Click ETA calendar field
            etd_calendar = self.wait.until(
                EC.element_to_be_clickable(Locators.ETD))
            try:
                etd_calendar.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", etd_calendar)
            print("✅ Clicked on ETD Calendar")           
            time.sleep(1)  # small delay so options load

            # Step 2: Navigate to next month
            # etd_next_month = self.wait.until(
            #     EC.element_to_be_clickable(Locators.ETD_Next_Month))
            # try:
            #     etd_next_month.click()
            # except:
            # # fallback JS click
            #     self.driver.execute_script("arguments[0].click();", etd_next_month)
            # print("✅ Clicked on ETD next month")           
            # time.sleep(1)  # small delay so options load

            # Step 3: Click on 1st of Next month
            etd_next_month_second = self.wait.until(
                EC.element_to_be_clickable(Locators.ETD_Next_Month_Second))
            try:
                etd_next_month_second.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", etd_next_month_second)
            print("✅ Clicked on ETD next month 2nd")           
            time.sleep(1)  # small delay so options load
        except Exception as e:
            raise Exception(f"❌ Unable to click and select ETA Date: {e}")  


    def scn_purpose_of_call(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Purpose_of_Call)
            )
            dropdown.click()
            print("✅ Clicked on Purpose of call dropdown")
            time.sleep(2)  # small delay so options load
            select_Purpose_of_call = self.wait.until(
                EC.element_to_be_clickable(Locators.Purpose_of_Call_select)
            )
            select_Purpose_of_call.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Purpose of call dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Purpose of call dropdown: {e}")

    def select_scn_last_port_of_call(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Last_port_of_call)
            )
            dropdown.click()
            print("✅ Clicked on Last port of call dropdown")
            time.sleep(2)  # small delay so options load
            select_Last_port_of_call = self.wait.until(
                EC.element_to_be_clickable(Locators.Last_port_of_call_select)
            )
            select_Last_port_of_call.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Last port of call dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Last port of call dropdown: {e}")
        
    def select_scn_next_port_of_call(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Next_port_of_call)
            )
            dropdown.click()
            print("✅ Clicked on Next port of call dropdown")
            time.sleep(2)  # small delay so options load
            select_Next_port_of_call = self.wait.until(
                EC.element_to_be_clickable(Locators.Next_port_of_call_select)
            )
            select_Next_port_of_call.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Next port of call dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Next port of call dropdown: {e}")

    # def click_Out_bound_Yes(self):
    #     """Click the Outbound Handling Yes button"""
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Locators.Outbound_Handling_Yes)
    #     ).click() 

    def click_Out_bound_Yes(self):
        """Scroll to bottom and click the Outbound Handling Yes button"""
        try:
            # Step 1: Scroll to bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("✅ Scrolled to bottom of page")

            # Step 2: Wait until button is clickable
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.Outbound_Handling_Yes)
            )

            # Step 3: Scroll element into view (extra safety)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)  # small pause for UI stability

            # Step 4: Click the button
            # button.click()
            # print("✅ Clicked Outbound Handling Yes button")
            try:
                button.click()
                print("✅ Clicked Outbound Handling Yes button (normal click)")
            except ElementClickInterceptedException:
            # Step 5: Fallback - JavaScript click
                self.driver.execute_script("arguments[0].click();", button)
                print("⚠️ Normal click intercepted, used JS click instead")

        except Exception as e:
            raise Exception(f"❌ Unable to click Outbound Handling Yes button: {e}")


    # def click_Out_bound_No(self):
    #     """Click the Outbound Handling No button"""
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Locators.Outbound_Handling_No)
    #     ).click() 

    def enter_scn_Inbound(self, Inbound):
        field = self.wait.until(EC.element_to_be_clickable(Locators.Inbound_Voyage))
        field.clear()
        field.send_keys(Inbound)
        print(f"✅ SCN Remarks entered: {Inbound}")

    def enter_scn_Outbound(self, Outbound):
        field = self.wait.until(EC.element_to_be_clickable(Locators.Outbound_Voyage))
        field.clear()
        field.send_keys(Outbound)
        print(f"✅ SCN Remarks entered: {Outbound}")

    def select_scn_entry_custom_station(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Entry_Custom_station)
            )
            dropdown.click()
            print("✅ Clicked on Entry Custom station dropdown")
            time.sleep(2)  # small delay so options load
            select_Entry_Custom_station = self.wait.until(
                EC.element_to_be_clickable(Locators.Entry_Custom_station_select)
            )
            select_Entry_Custom_station.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Entry Custom station dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Entry Custom station dropdown: {e}")
        
    def select_scn_exit_custom_station(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Exit_Custom_station)
            )
            dropdown.click()
            print("✅ Clicked on Exit Custom station dropdown")
            time.sleep(2)  # small delay so options load
            select_Exit_Custom_station = self.wait.until(
                EC.element_to_be_clickable(Locators.Exit_Custom_station_select)
            )
            select_Exit_Custom_station.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in Exit Custom station dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Exit Custom station dropdown: {e}")

    def enter_scn_Remarks(self, Remarks):
        field = self.wait.until(EC.element_to_be_clickable(Locators.SCN_Remarks))
        field.clear()
        field.send_keys(Remarks)
        print(f"✅ SCN Remarks entered: {Remarks}")

    def click_scn_submit_button(self):
        """Click the SUBMIT button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SCN_SUBMIT)
        ).click()

    def click_scn_cancel_button(self):
        """Click the CANCEL button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SCN_CANCEL)
        ).click() 

    def click_scn_stay_on_page_button(self):
        """Clicks on 'No, Stay on Page' button in the confirmation dialog."""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Locators.SCN_Stay_On_Page)
        ).click()

    def click_scn_yes_cancel_button(self):
        """Clicks on 'Yes, Cancel' button in the confirmation dialog."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SCN_Confirm_Cancel)
        ).click()
# ========================================================================================================
# SCN (END) 
# ========================================================================================================


# ========================================================================================================
# EPAN (START) 
# ========================================================================================================
    def check_Pre_Arrival_Notification(self):
        """Click the GO button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN)
        ).click()

    def validate_Pre_Arrival_Notification_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.EPAN_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False  

    def click_Create_EPAN_button(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_EPAN)
        ).click()

    def Verify_Create_New_ePAN_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Create_ePAN_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False   
        
    def enter_scn_number(self, SCN_No): 
        field = self.wait.until(EC.element_to_be_clickable(Locators.EPAN_SCN_Number))
        field.clear()
        field.send_keys(SCN_No)
        print(f"✅ SCN_No entered: {SCN_No}")

    def click_EPAN_GO_button(self):
        """Click the GO button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_GO)
        ).click()
        time.sleep(2)

    def click_ISSC_Present_button(self):
        """Click the ISSC Present button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_ISSC_Present)
        ).click()

    def click_non_compliant_No(self):
        """Click the non compliant button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_Non_Compliant_Port_No)
        ).click()

    def click_non_compliant_Yes(self):
        """Click the non compliant button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_Non_Compliant_Port_Yes)
        ).click()

    def upload_Crew_list(self, filepath):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_Crew_List)
        )
        assert field.is_displayed(), "Crew List not visible"
        field.send_keys(os.path.abspath(filepath))

    def upload_Passenger_list(self, filepath):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_Passenger_List)
        )
        assert field.is_displayed(), "Passenger List not visible"
        field.send_keys(os.path.abspath(filepath))

    def upload_Cargo_Declaration(self, filepath):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_DG_Cargo_Declaration)
        )
        assert field.is_displayed(), "Cargo Declaration not visible"
        field.send_keys(os.path.abspath(filepath))

    def enter_port_code(self, Port_Code):
        # Step 1: Scroll to bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("✅ Scrolled to bottom of page")

        field = self.wait.until(EC.element_to_be_clickable(Locators.EPAN_Port_Code))
        # Step 3: Scroll element into view (extra safety)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)

        field.clear()
        field.send_keys(Port_Code)
        print(f"✅ SCN_No entered: {Port_Code}")        

    def enter_port_name(self, Port_Name):
        field = self.wait.until(EC.element_to_be_clickable(Locators.EPAN_Port_Name))
        field.clear()
        field.send_keys(Port_Name)
        print(f"✅ SCN_No entered: {Port_Name}") 

    def EPAN_Arrival_date(self):
        try:
            # Step 1: Click EPAN Arrival Calendar field
            epan_arrival_calendar = self.wait.until(
                EC.element_to_be_clickable(Locators.EPAN_Arrival))
            try:
                epan_arrival_calendar.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", epan_arrival_calendar)
            print("✅ Clicked on EPAN Arrival Calendar")           
            time.sleep(1)  # small delay so options load


            # Step 2: Calculate next date
            next_day = datetime.now() + timedelta(days=1)
            day_str = str(next_day.day)  # e.g., '25'

            # Step 3: Locator for calendar day span
            # Assuming each day is a <span> with text equal to the day number
            calendar_day_locator = f"(//span[normalize-space()='{day_str}'])[1]"

            # Step 4: Action - click the next day's span
            select_date = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, calendar_day_locator)))
            select_date.click()
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select EPAN Arrival Date: {e}")     

    def EPAN_Departure_date(self):
        try:
            # Step 1: Click ETA calendar field
            epan_departure_calendar = self.wait.until(
                EC.element_to_be_clickable(Locators.EPAN_Departure))
            try:
                epan_departure_calendar.click()
            except:
            # fallback JS click
                self.driver.execute_script("arguments[0].click();", epan_departure_calendar)
            print("✅ Clicked on EPAN Arrival Calendar")           
            time.sleep(1)  # small delay so options load
            # Step 2: Calculate next date
            next_day = datetime.now() + timedelta(days=1)
            day_str = str(next_day.day)  # e.g., '25'
            # Step 3: Locator for calendar day span
            # Assuming each day is a <span> with text equal to the day number
            calendar_day_locator = f"(//span[normalize-space()='{day_str}'])[2]"
            # Step 4: Action - click the next day's span
            select_date = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, calendar_day_locator)))
            select_date.click()
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select EPAN Arrival Date: {e}")   

    def click_EPAN_SUBMIT_button(self):
        """Scroll to bottom and click the SUBMIT button"""
        try:
            submit_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.EPAN_SUBMIT)
            )
            # Scroll SAVE button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            # Small pause in case of sticky headers/footers
            time.sleep(1)
            submit_btn.click()
            print("✅ Clicked on SUBMIT button after scrolling")
        except Exception as e:
            raise Exception(f"Unable to click on SUBMIT button: {e}")         

    def click_EPAN_SAVE_button(self):
        """Scroll to bottom and click the SAVE button"""
        try:
            save_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.EPAN_SAVE_AS_DRAFT)
            )
            # Scroll SAVE button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
            # Small pause in case of sticky headers/footers
            time.sleep(1)
            save_btn.click()
            print("✅ Clicked on SAVE button after scrolling")
        except Exception as e:
            raise Exception(f"Unable to click on SAVE button: {e}")        

    def click_EPAN_CANCEL_button(self):
        """Click the CANCEL button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EPAN_CANCEL)
        ).click()         

    def SCN_No_Filter(self, SCN_No):
        try:
            print("🔍 Locating SCN_No filter chip...")
            chip = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(Locators.EPAN_SCN_No_Filter)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", chip)

            clickable_chip = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.EPAN_SCN_No_Filter)
            )
            clickable_chip.click()
            print("✅ Clicked on SCN_No filter chip.")

            # Now locate the input field
            filter_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.EPAN_SCN_No_Search)
            )
            filter_input.clear()
            filter_input.send_keys(SCN_No)
            print(f"✅ Entered SCN_No: {SCN_No}")
            time.sleep(2)

        except Exception as e:
            self.driver.save_screenshot("Vessel_Name_Filter_Failed.png")
            print("❌ Filter chip not found or not clickable. Screenshot saved.")
            raise e

    def View_EPAN_Post_Search(self):
        View_EPAN_Post_Search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.EPAN_View_Details)
        )
        View_EPAN_Post_Search.click()
        time.sleep(2)        

    def Amend_EPAN_Post_Search(self):
        Amend_EPAN_Post_Search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.EPAN_Amend_Details)
        )
        Amend_EPAN_Post_Search.click()
        time.sleep(2)  

# ========================================================================================================
# EPAN (END) 
# ========================================================================================================


        
# ========================================================================================================
# ARRIVAL CLEARANCE (START) 
# ========================================================================================================

    def validate_Arrival_Clearance_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Arrival_Clearance_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False  

    def click_Create_Arrival_Clearance_button(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_Arrival_Clearance)
        ).click()
        time.sleep(3)

    def Verify_Create_Arrival_Clearance_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Create__Arrival_Clearance_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False   
        
    def click_Arrival_Clearance_GO_button(self):
        """Click the GO button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Arrival_Clearance_GO)
        ).click()
        time.sleep(2)
# ========================================================================================================
# ARRIVAL CLEARANCE (END) 
# ========================================================================================================


# ========================================================================================================
# DEPARTURE CLEARANCE (START) 
# ========================================================================================================
    def validate_Departure_Clearance_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Departure_Clearance_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False  

    def click_Create_Departure_Clearance_button(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_Departure_Clearance)
        ).click()
        time.sleep(3)

    def Verify_Create_Departure_Clearance_Header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Create__Departure_Clearance_Header),
            f"Heading is not visible"
            )
            time.sleep(1)
            return True
        except TimeoutException:
            return False   

# ========================================================================================================
# DEPARTURE CLEARANCE (END) 
# ========================================================================================================

# ========================================================================================================
# VESSEL PROFILE (START) 
# ========================================================================================================
    def Verify_Vessel_Profile_header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Vessel_Profile_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False
        
    def Register_new_vessel(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Register_New_Vessel_Profile)
        ).click()

    def Create_Vessel_Profile_header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Create_Vessel_Profile_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False
        
    def basic_vessel_info_toggle(self):
        print("✅ Basic Vessel Info Toggle button is clicked.")
        toggle = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.VP_Basic_Vessel_Information_toggle)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)
        time.sleep(1)
        toggle.click()

    def enter_profile_imo_number(self, imo_no):
        try:
            if SharedPage.random_suffix is None:
                raise Exception("Random suffix not generated yet. Call enter_vessel_name first!")

            unique_imo_no = f"{imo_no}{SharedPage.random_suffix}"

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_IMO_Number)
            )
            field.clear()
            field.send_keys(unique_imo_no)
            print(f"✅ IMO Number entered: {unique_imo_no}")
        except Exception as e:
            raise Exception(f"Unable to enter IMO No: {e}")
        
    def vessel_classification_type_toggle(self):
        print("✅ Vessel Classification Type Toggle button is clicked.")
        toggle = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.VP_Vessel_Classification_Type_toggle)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)
        time.sleep(1)
        toggle.click()

    def click_General_type_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.VP_General_Type)
            )
            dropdown.click()
            print("✅ Clicked on General Type dropdown")
            time.sleep(2)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.VP_General_Type_select)
            )
            select_branch.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected in General Type dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select General in type dropdown: {e}")
        
    def click_Vessel_type_dropdown(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.VP_Vessel_Type)
            )
            dropdown.click()
            print("✅ Clicked on Vessel Type dropdown")
            time.sleep(2)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.VP_Vessel_Type_select)
            )
            select_branch.click()
            time.sleep(2)  # small delay so options load
            print("✅ Selected Vessel in Type dropdown")
            time.sleep(2)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select vessel in type dropdown: {e}")

    def vessel_specification_toggle(self):
        print("✅ Vessel Specification Toggle button is clicked.")
        toggle = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.VP_Vessel_Specification_toggle)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)
        time.sleep(1)
        toggle.click() 

    def vessel_specification_collapse(self):
        print("✅ Vessel Specification Collapse button is clicked.")
        toggle = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.VP_Vessel_Specification_collapse)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)
        time.sleep(1)
        toggle.click()         

    def enter_LOA_number(self, LOA):
        field = self.wait.until(EC.element_to_be_clickable(Locators.VP_LOA))
        field.clear()
        field.send_keys(LOA)
        print(f"✅ LOA entered: {LOA}")

    def enter_LBP_number(self, LBP):
        field = self.wait.until(EC.element_to_be_clickable(Locators.VP_LBP))
        field.clear()
        field.send_keys(LBP)
        print(f"✅ LBP entered: {LBP}")

    def enter_Draft_number(self, Draft):
        field = self.wait.until(EC.element_to_be_clickable(Locators.VP_Draft))
        field.clear()
        field.send_keys(Draft)
        print(f"✅ Draft entered: {Draft}")

    def enter_Beam_number(self, Beam):
        field = self.wait.until(EC.element_to_be_clickable(Locators.VP_Beam))
        field.clear()
        field.send_keys(Beam)
        print(f"✅ Beam entered: {Beam}")

    def click_vp_submit_button(self):
        """Click the SUBMIT button"""
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_SUBMIT)
            )
            # Ensure button is visible in viewport
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)  # Small pause for any animation
            try:
                button.click()
            except:
                # Fallback if intercepted
                self.driver.execute_script("arguments[0].click();", button)

            print("✅ Submit button clicked successfully")
        except Exception as e:
            raise Exception(f"❌ Unable to click Submit button: {e}")

    def click_vp_save_button(self):
        """Click the SAVE button"""
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_SAVE)
            )
            # Ensure button is visible in viewport
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)  # Small pause for any animation
            try:
                button.click()
            except:
                # Fallback if intercepted
                self.driver.execute_script("arguments[0].click();", button)

            print("✅ Save button clicked successfully")
        except Exception as e:
            raise Exception(f"❌ Unable to click Save button: {e}")

    def click_vp_cancel_button(self):
        """Click the CANCEL button"""
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_CANCEL)
            )
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)  # allow animation/scroll finish
            try:
                button.click()
                print("✅ Cancel button clicked successfully")
            except:
                # Fallback to JS click
                self.driver.execute_script("arguments[0].click();", button)

            print("✅ Cancel button clicked with JavaScript")
        except Exception as e:
            raise Exception(f"❌ Unable to click Cancel button: {e}")

    def click_vp_reset_button(self):
        """Click the RESET button"""
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_RESET)
            )
            # Ensure button is visible in viewport
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)  # Small pause for any animation
            try:
                button.click()
            except:
                # Fallback if intercepted
                self.driver.execute_script("arguments[0].click();", button)

            print("✅ Reset button clicked successfully")
        except Exception as e:
            raise Exception(f"❌ Unable to click Reset button: {e}")


    def Vessel_Name_Filter(self, vessel_name):
        try:
            print("🔍 Locating Vessel Name filter chip...")
            chip = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(Locators.VP_Vessel_Name_Column_Filter)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", chip)

            clickable_chip = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_Vessel_Name_Column_Filter)
            )
            clickable_chip.click()
            print("✅ Clicked on Vessel Name filter chip.")

            # Now locate the input field
            filter_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Add_filter_value)
            )
            filter_input.clear()
            filter_input.send_keys(vessel_name)
            print(f"✅ Entered template name: {vessel_name}")
            time.sleep(2)

        except Exception as e:
            self.driver.save_screenshot("Vessel_Name_Filter_Failed.png")
            print("❌ Filter chip not found or not clickable. Screenshot saved.")
            raise e

    def click_vp_view_button_post_search(self):
        View_Post_Search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.VP_View)
        )
        View_Post_Search.click()
        time.sleep(5) 

    def enter_dupicate_vessel_name(self, vessel_name, imo_no):
        try:
            # Generate suffix once per scenario
            if SharedPage.random_suffix is None:
                SharedPage.random_suffix = str(random.randint(10000, 99999))

            unique_vessel_name = f"{vessel_name}{SharedPage.random_suffix}"

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.FormVesselName)
            )
            time.sleep(2)
            field.clear()
            field.send_keys(unique_vessel_name)

            unique_imo_no = f"{imo_no}{SharedPage.random_suffix}"
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.VP_IMO_Number)
            )
            field.clear()
            field.send_keys(unique_imo_no)
            print(f"✅ IMO Number entered: {unique_imo_no}")            

            print(f"✅ Vessel Name entered: {unique_vessel_name}")
        except Exception as e:
            raise Exception(f"Unable to enter Vessel Name: {e}")
        
# ========================================================================================================
# VESSEL PROFILE (END) 
# ========================================================================================================

# ========================================================================================================
# VESSEL REGISTRATION (START) 
# ========================================================================================================


# ALL Tile
    def click_all_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_Registration_Requests_All)
        )
        element.click()

    def is_all_tab_active(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(Locators.Vessel_Registration_Requests_All)
            )
            return True
        except:
            return False

# DRAFT Tile
    def click_Draft_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_Registration_Requests_Draft)
        )
        element.click()

    def is_Draft_tab_active(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(Locators.Vessel_Registration_Requests_Draft)
            )
            return True
        except:
            return False

# SUBMITTED Tile
    def click_Submitted_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_Registration_Requests_Submitted)
        )
        element.click()

    def is_Submitted_tab_active(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(Locators.Vessel_Registration_Requests_Submitted)
            )
            return True
        except:
            return False

# APPROVED Tile
    def click_Approved_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_Registration_Requests_Approved)
        )
        element.click()

    def is_Approved_tab_active(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(Locators.Vessel_Registration_Requests_Approved)
            )
            return True
        except:
            return False

# CANCELLED Tile
    def click_Cancelled_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_Registration_Requests_Cancelled)
        )
        element.click()

    def is_Cancelled_tab_active(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(Locators.Vessel_Registration_Requests_Cancelled)
            )
            return True
        except:
            return False


# REJECTED Tile
    def click_Rejected_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_Registration_Requests_Rejected)
        )
        element.click()

    def is_Rejected_tab_active(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(Locators.Vessel_Registration_Requests_Rejected)
            )
            return True
        except:
            return False

# ==============

    def has_records(self):
        rows = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(Locators.record_rows)
        )
        print(f"Total No of rows: len(rows)")
        return len(rows) > 0
    
    def get_row_count(self):
        """Returns the number of visible rows in the AG Grid table."""
        try:
            rows = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(Locators.record_rows)
            )
            return len(rows)
        except:
            return 0


    def click_add_vessel_button(self):
        """NEW Shipping Agent clicks on Create New button in Vessel Registration."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_button)
        ).click()

    def click_submit_vessel_button(self):
        """Click on the floating '+' button in the bottom-right corner."""
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_Submit)
        ).click()        

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            BASIC VESSEL INFORMATION                                                                       
# -------------- -------------- -------------- -------------- -------------- -------------- --------------          
        
    def enter_vessel_name(self, vessel_name):
        try:
            # Always generate unique vessel name
            SharedPage.random_suffix = str(random.randint(10000, 99999))
            unique_vessel_name = f"{vessel_name}{SharedPage.random_suffix}"

            wait = WebDriverWait(self.driver, 30)

            # 1️⃣ Wait till visible
            field = wait.until(
                EC.visibility_of_element_located(Locators.FormVesselName)
            )

            # 2️⃣ Scroll & focus (Formio inputs NEED this)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", field
            )
            self.driver.execute_script("arguments[0].focus();", field)

            # 3️⃣ Wait till clickable
            wait.until(
                EC.element_to_be_clickable(Locators.FormVesselName)
            )

            # 4️⃣ Clear + Type
            field.clear()
            field.send_keys(unique_vessel_name)

            time.sleep(0.5)

            print(f"✅ Vessel Name entered: {unique_vessel_name}")

        except Exception as e:
            # traceback.print_exc()
            raise Exception("Unable to enter Vessel Name") from e

    def enter_imo_number(self, imo_no):
        try:
            if SharedPage.random_suffix is None:
                raise Exception("Random suffix not generated yet. Call enter_vessel_name first!")

            unique_imo_no = f"{imo_no}{SharedPage.random_suffix}"

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.FormIMO_NO_INPUT)
            )
            field.clear()
            field.send_keys(unique_imo_no)
            time.sleep(1)
            print(f"✅ IMO Number entered: {unique_imo_no}")
        except Exception as e:
            raise Exception(f"Unable to enter IMO No: {e}")

    def enter_call_sign(self, call_sign):
        try:
            if SharedPage.random_suffix is None:
                raise Exception("Random suffix not generated yet. Call enter_vessel_name first!")

            unique_call_sign = f"{call_sign}{SharedPage.random_suffix}"

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.FormCALL_SIGN_INPUT)
            )
            field.clear()
            field.send_keys(unique_call_sign)
            time.sleep(1)
            print(f"✅ Call Sign entered: {unique_call_sign}")
        except Exception as e:
            raise Exception(f"Unable to enter Call Sign: {e}")

    def enter_Official_Number(self, official_no):
        try:
            if SharedPage.random_suffix is None:
                raise Exception("Random suffix not generated yet. Call enter_vessel_name first!")

            unique_official_no = f"{official_no}{SharedPage.random_suffix}"

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.FormOFFICIAL_NUMBER_INPUT)
            )
            field.clear()
            field.send_keys(unique_official_no)
            time.sleep(1)
            print(f"✅ Official Number entered: {unique_official_no}")
        except Exception as e:
            raise Exception(f"Unable to enter Official Number: {e}")

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            REGISTRATION & COMPLIANCE                                                                       
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

    # def enter_registry_certificate_no(self, registry_no):
    #     try:
    #         if SharedPage.random_suffix is None:
    #             raise Exception("Random suffix not generated yet. Call enter_vessel_name first!")

    #         unique_registry_no = f"{registry_no}{SharedPage.random_suffix}"

    #         field = WebDriverWait(self.driver, 20).until(
    #             EC.element_to_be_clickable(Locators.FormRegistryCertificateNo)
    #         )
    #         field.clear()
    #         field.send_keys(unique_registry_no)

    #         print(f"✅ Registry Certificate No. entered: {unique_registry_no}")
    #     except Exception as e:
    #         raise Exception(f"Unable to enter Registry Certificate No: {e}")  
        


    def step_click_registration_compliance_panel(self):
        """Click the Registration & Compliance panel"""
        locator = (By.XPATH, "//div[@role='button' and normalize-space()='Registration & Compliance']")
        try:
            panel = self.wait.until(EC.presence_of_element_located(locator))
        
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", panel)
            time.sleep(1)

            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
                print("✅ Clicked Registration & Compliance panel (normal click)")
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", panel)
                print("⚠️ Used JavaScript click as fallback")
        except TimeoutException:
            raise Exception("❌ Registration & Compliance panel not found on page")
         
    
    # def enter_ship_registry_certificate_number(self, certificate_number):
    #     input_field = self.wait.until(
    #         EC.visibility_of_element_located(self.SHIP_REGISTRY_CERTIFICATE_INPUT)
    #     )
    #     input_field.clear()
    #     input_field.send_keys(certificate_number)    

    # ✅ Method to enter certificate number
    def enter_Ship_Registry_Certificate_No(self, Ship_Registry_Certificate_No):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Ship_Registry_Certificate_No)
            )
            field.clear()
            field.send_keys(Ship_Registry_Certificate_No)
            print(f"✅ Register Certificate entered: {Ship_Registry_Certificate_No}")
        except Exception as e:
            raise Exception(f"Unable to enter Ship Registry Certificate No: {e}") 
        # Register_Certificate = self.wait.until(EC.element_to_be_clickable(Locators.Ship_Registry_Certificate_No))
        # Register_Certificate.clear()
        # Register_Certificate.send_keys(Ship_Registry_Certificate_No)
        # print(f"✅ Register Certificate entered: {Ship_Registry_Certificate_No}")         

    def enter_Ship_Registry_Date(self, Ship_Registry_Date):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Ship_Registry_Date)
            )
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
            time.sleep(1)

            # Clear and send date
            field.clear()
            field.send_keys(Ship_Registry_Date)
            time.sleep(2)
            field.send_keys(Keys.TAB)  # Close calendar popup

            print(f"✅ Ship Registry Date entered: {Ship_Registry_Date}")
        except Exception as e:
            raise Exception(f"❌ Unable to enter Ship Registry Date: {e}")

                    
    def enter_Vessel_Nationality(self):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Vessel_Nationality)
            )
            field.click()
            print(f"✅ Vessel Nationality Type is Foreign")
            time.sleep(2)  # Pauses the execution for 1 second
        except Exception as e:
            raise Exception(f"Unable to select Vessel Nationality: {e}") 

    def select_Vessel_Flag(self, Vessel_Flag):  
        # Scroll to the top of the page before interacting
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)  # allow page to stabilize after scroll
        # Wait for and click the dropdown        
        try:
            VesselFlag = self.wait.until(
                EC.element_to_be_clickable(Locators.Vessel_Flag)
            )
            VesselFlag.click()
            VesselFlag.send_keys(Vessel_Flag)
            VesselFlag.send_keys(Keys.ENTER)
            time.sleep(2)  # small delay so options load
            print("✅ Clicked on Vessel Flag dropdown")
            Vessel_Flag = self.wait.until(
                EC.element_to_be_clickable(Locators.Vessel_Flag_Select)
            )
            Vessel_Flag.click()
            print("✅ Selected in Vessel Flag dropdown")
            time.sleep(2)  # Pauses the execution for 1 second
            VesselFlag.send_keys(Keys.TAB)
        except Exception as e:
            raise Exception(f"Unable to select Vessel Flag: {e}")
        
    def select_port_of_registry(self, Port_of_Registry):  
        try:
            RegistryPort = self.wait.until(
                EC.element_to_be_clickable(Locators.Port_of_Registry)
            )
            RegistryPort.click()
            RegistryPort.send_keys(Port_of_Registry)
            RegistryPort.send_keys(Keys.ENTER)
            time.sleep(2)  # small delay so options load
            print("✅ Clicked on Port of Registry dropdown")
            Port_of_Registry_Select = self.wait.until(
                EC.element_to_be_clickable(Locators.Port_of_Registry_select)
            )
            Port_of_Registry_Select.click()
            print("✅ Selected in Port of Registry dropdown")
            time.sleep(2)  # Pauses the execution for 1 second
            RegistryPort.send_keys(Keys.TAB)
            time.sleep(2)  # Pauses the execution for 1 second            
        except Exception as e:
            raise Exception(f"Unable to select Port of Registry: {e}")

    def select_area_of_operation(self, Area_of_operation):  
        try:
            OperationArea = self.wait.until(
                EC.element_to_be_clickable(Locators.Area_of_operation)
            )
            OperationArea.click()
            OperationArea.send_keys(Area_of_operation)
            OperationArea.send_keys(Keys.ENTER)
            time.sleep(2)  # small delay so options load
            print("✅ Clicked on Port of Registry dropdown")
            Area_of_operation_Select = self.wait.until(
                EC.element_to_be_clickable(Locators.Area_of_operation_Select)
            )
            Area_of_operation_Select.click()
            print("✅ Selected in Port of Registry dropdown")
            time.sleep(2)  # Pauses the execution for 1 second
            OperationArea.send_keys(Keys.TAB)
            time.sleep(2)  # Pauses the execution for 1 second            
        except Exception as e:
            raise Exception(f"Unable to select Port of Registry: {e}") 
        
# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            VESSEL CLASSIFICATION & TYPE                                                                       
# -------------- -------------- -------------- -------------- -------------- -------------- --------------        

    def step_click_Vessel_Classification_Type_panel(self):
        """Click the Vessel Classification panel"""
        try:
            panel = self.wait.until(EC.presence_of_element_located(Locators.VESSEL_CLASSIFICATION_TYPE_PANEL))
        
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", panel)
            time.sleep(1)
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(panel)).click()
                print("✅ Clicked Vessel Classification panel (normal click)")
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", panel)
                print("⚠️ Used JavaScript click as fallback")
        except TimeoutException:
            raise Exception("❌ Vessel Classification panel not found on page")    


    def select_General_Type_station(self, General_Type):  
        try:
            GeneralType = self.wait.until(
                EC.element_to_be_clickable(Locators.General_Type)
            )
            GeneralType.click()
            GeneralType.send_keys(General_Type)
            GeneralType.send_keys(Keys.ENTER)
            time.sleep(2)  # small delay so options load
            print("✅ Clicked on Port of Registry dropdown")
            General_Type_Select = self.wait.until(
                EC.element_to_be_clickable(Locators.General_Type_select)
            )
            General_Type_Select.click()
            print("✅ Selected in Port of Registry dropdown")
            time.sleep(2)  # Pauses the execution for 1 second
            GeneralType.send_keys(Keys.TAB)
        except Exception as e:
            raise Exception(f"Unable to select Port of Registry: {e}")
        
    def select_Vessel_Type_station(self, Vessel_Type):  
        try:
            VesselType = self.wait.until(
                EC.element_to_be_clickable(Locators.Vessel_Type)
            )
            VesselType.click()
            VesselType.send_keys(Vessel_Type)
            VesselType.send_keys(Keys.ENTER)
            time.sleep(2)  # small delay so options load
            print("✅ Clicked on Vessel Type dropdown")
            General_Type_Select = self.wait.until(
                EC.element_to_be_clickable(Locators.Vessel_Type_select)
            )
            General_Type_Select.click()
            print("✅ Selected in Vessel Type dropdown")
            time.sleep(2)  # Pauses the execution for 1 second
            VesselType.send_keys(Keys.TAB)
        except Exception as e:
            raise Exception(f"Unable to select Vessel Type: {e}")

    # ✅ Method to enter Sub Type
    def enter_Sub_Type(self, Sub_Type):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Sub_Type)
            )
            field.clear()
            field.send_keys(Sub_Type)
            print(f"✅ Sub Type entered: {Sub_Type}")
        except Exception as e:
            raise Exception(f"Unable to enter Sub Type: {e}")
        
    def enter_Customs_Agent_Code(self, Customs_Agent_Code):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Customs_Agent_Code)
            )
            field.clear()
            field.send_keys(Customs_Agent_Code)
        except Exception as e:
            raise Exception(f"Unable to enter Customs Agent Code: {e}")       

    def enter_Cargo_Type(self, Cargo_Type):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Cargo_Type)
            )
            field.clear()
            field.send_keys(Cargo_Type)
        except Exception as e:
            raise Exception(f"Unable to enter Cargo Type: {e}")                          
        
# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            VESSEL SPECIFICATIONS                                                                       
# -------------- -------------- -------------- -------------- -------------- -------------- --------------           
    def step_click_Vessel_Specifications_panel(self):
        panel_icon = self.wait.until(
            EC.element_to_be_clickable(Locators.VESSEL_SPECIFICATION_PANEL)
        )
        ActionChains(self.driver).move_to_element(panel_icon).click().perform()  
        time.sleep(5)  # Pauses the execution for 5 seconds   

    def enter_Year_Built(self, Year_Built):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Year_Built)
            )
            field.clear()
            field.send_keys(Year_Built)
        except Exception as e:
            raise Exception(f"Unable to enter Year Built: {e}") 
        
    def enter_Built_Place(self, Built_Place):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Built_Place)
            )
            field.clear()
            field.send_keys(Built_Place)
        except Exception as e:
            raise Exception(f"Unable to enter Built Place: {e}")

    def enter_Vessel_With_Gear(self, Vessel_With_Gear):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Vessel_With_Gear)
            )
            field.clear()
            field.send_keys(Vessel_With_Gear)
        except Exception as e:
            raise Exception(f"Unable to enter Vessel With Gear: {e}") 

    def select_Type_of_Hull(self, Type_of_Hull):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Type_of_Hull)
            )
            field.clear()
            field.send_keys(Type_of_Hull)
        except Exception as e:
            raise Exception(f"Unable to enter Type of Hull: {e}")

    def select_Position_of_Bridge(self, Position_of_Bridge):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Position_of_Bridge)
            )
            field.clear()
            field.send_keys(Position_of_Bridge)
        except Exception as e:
            raise Exception(f"Unable to enter Position of Bridge: {e}")    

    def enter_Length_Overall(self, Length_Overall):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Length_Overall)
            )
            field.clear()
            field.send_keys(Length_Overall)
        except Exception as e:
            raise Exception(f"Unable to enter Length_Overall: {e}") 

    def enter_Depth(self, Depth):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Depth)
            )
            field.clear()
            field.send_keys(Depth)
        except Exception as e:
            raise Exception(f"Unable to enter Depth: {e}") 

    def enter_Draft(self, Draft):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Draft)
            )
            field.clear()
            field.send_keys(Draft)
        except Exception as e:
            raise Exception(f"Unable to enter Draft: {e}") 

    def enter_Freeboard(self, Freeboard):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Freeboard)
            )
            field.clear()
            field.send_keys(Freeboard)
        except Exception as e:
            raise Exception(f"Unable to enter Freeboard: {e}") 

    def enter_Length_Between_Perpendiculars(self, Length_Between_Perpendiculars):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Length_Between_Perpendiculars)
            )
            field.clear()
            field.send_keys(Length_Between_Perpendiculars)
        except Exception as e:
            raise Exception(f"Unable to enter Length_Between_Perpendiculars: {e}") 

    def enter_Beam(self, Beam):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Beam)
            )
            field.clear()
            field.send_keys(Beam)
        except Exception as e:
            raise Exception(f"Unable to enter Beam: {e}") 

    def enter_Displacement(self, Displacement):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Displacement)
            )
            field.clear()
            field.send_keys(Displacement)
        except Exception as e:
            raise Exception(f"Unable to enter Displacement: {e}")                                                                                     

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            TONNAGE & CAPACITY                                                                       
# -------------- -------------- -------------- -------------- -------------- -------------- -------------- 

    def step_click_Tonnage_Capacity_panel(self):
        panel_icon = self.wait.until(
            EC.element_to_be_clickable(Locators.Tonnage_Capacity_PANEL)
        )
        ActionChains(self.driver).move_to_element(panel_icon).click().perform()  
        time.sleep(5)  # Pauses the execution for 5 seconds   

    def enter_Gross_Tonnage(self, Gross_Tonnage):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Gross_Tonnage)
            )
            field.clear()
            field.send_keys(Gross_Tonnage)
        except Exception as e:
            raise Exception(f"Unable to enter Gross_Tonnage: {e}") 
        
    def enter_Net_Tonnage(self, Net_Tonnage):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Net_Tonnage)
            )
            field.clear()
            field.send_keys(Net_Tonnage)
        except Exception as e:
            raise Exception(f"Unable to enter Net_Tonnage: {e}") 

    def enter_Deadweight_Tonnage(self, Deadweight_Tonnage):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Deadweight_Tonnage)
            )
            field.clear()
            field.send_keys(Deadweight_Tonnage)
        except Exception as e:
            raise Exception(f"Unable to enter Deadweight_Tonnage: {e}") 

    def enter_Crew_Capacity(self, Crew_Capacity):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Crew_Capacity)
            )
            field.clear()
            field.send_keys(Crew_Capacity)
        except Exception as e:
            raise Exception(f"Unable to enter Crew_Capacity: {e}") 
        
    def enter_Passenger_Capacity(self, Passenger_Capacity):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Passenger_Capacity)
            )
            field.clear()
            field.send_keys(Passenger_Capacity)
        except Exception as e:
            raise Exception(f"Unable to enter Passenger_Capacity: {e}") 

    def enter_TEU_Capacity(self, TEU_Capacity):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.TEU_Capacity)
            )
            field.clear()
            field.send_keys(TEU_Capacity)
        except Exception as e:
            raise Exception(f"Unable to enter TEU_Capacity: {e}")                 


# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            OWNERSHIP & MANAGEMENT                                                                      
# -------------- -------------- -------------- -------------- -------------- -------------- -------------- 

    def step_click_Ownership_Management_panel(self):
        panel_icon = self.wait.until(
            EC.element_to_be_clickable(Locators.Ownership_Management_PANEL)
        )
        ActionChains(self.driver).move_to_element(panel_icon).click().perform()  
        time.sleep(5)  # Pauses the execution for 5 seconds 

    def enter_owner_name(self, Owner_Name):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Owner_Name)
            )
            field.clear()
            field.send_keys(Owner_Name)
        except Exception as e:
            raise Exception(f"Unable to enter Owner_Name: {e}") 

    def enter_owner_email(self, Email):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Email)
            )
            field.clear()
            field.send_keys(Email)
        except Exception as e:
            raise Exception(f"Unable to enter Email: {e}") 

    def enter_owner_mobile_no(self, Mobile_No):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Mobile_No)
            )
            field.clear()
            field.send_keys(Mobile_No)
        except Exception as e:
            raise Exception(f"Unable to enter Mobile_No: {e}") 
        
    def enter_Owner_Code(self, Owner_Code):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Owner_Code)
            )
            field.clear()
            field.send_keys(Owner_Code)
        except Exception as e:
            raise Exception(f"Unable to enter Owner_Code: {e}") 
        
    def enter_Shipping_Line_Name(self, Shipping_Line_Name):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Line_Name)
            )
            field.clear()
            field.send_keys(Shipping_Line_Name)
        except Exception as e:
            raise Exception(f"Unable to enter Shipping_Line_Name: {e}") 
        
    def enter_owner_Address_Line_1(self, Address_Line_1):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Address_Line_1)
            )
            field.clear()
            field.send_keys(Address_Line_1)
        except Exception as e:
            raise Exception(f"Unable to enter Address_Line_1: {e}") 
        
    def enter_owner_Address_Line_2(self, Address_Line_2):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Address_Line_2)
            )
            field.clear()
            field.send_keys(Address_Line_2)
        except Exception as e:
            raise Exception(f"Unable to enter Address_Line_2: {e}")        

    def enter_owner_Address_Line_3(self, Address_Line_3):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Address_Line_3)
            )
            field.clear()
            field.send_keys(Address_Line_3)
        except Exception as e:
            raise Exception(f"Unable to enter Address_Line_3: {e}")    

    def select_owner_City(self, City):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.City)
            )
            field.clear()
            field.send_keys(City)
        except Exception as e:
            raise Exception(f"Unable to enter City: {e}") 

    def enter_owner_Street(self, Street):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Street)
            )
            field.clear()
            field.send_keys(Street)
        except Exception as e:
            raise Exception(f"Unable to enter Street: {e}") 

    def select_owner_State(self, State):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.State)
            )
            field.clear()
            field.send_keys(State)
        except Exception as e:
            raise Exception(f"Unable to enter State: {e}") 

    def select_owner_Country(self, Country):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Country)
            )
            field.clear()
            field.send_keys(Country)
        except Exception as e:
            raise Exception(f"Unable to enter Country: {e}") 

    def enter_owner_post_code(self, Postcode):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Postcode)
            )
            field.clear()
            field.send_keys(Postcode)
        except Exception as e:
            raise Exception(f"Unable to enter Postcode: {e}") 


# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            SHIPPING & OPERATIONS                                                                      
# -------------- -------------- -------------- -------------- -------------- -------------- -------------- 

    def step_click_Shipping_Operators_panel(self):
        panel_icon = self.wait.until(
            EC.element_to_be_clickable(Locators.Shipping_Operations_PANEL)
        )
        ActionChains(self.driver).move_to_element(panel_icon).click().perform()  
        time.sleep(5)  # Pauses the execution for 5 seconds 

    def enter_Shipping_Agent_Code(self, Shipping_Agent_Code):  
        try:
            field = WebDriverWait(Locators.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Code)
            )
            field.clear()
            field.send_keys(Shipping_Agent_Code)
        except Exception as e:
            raise Exception(f"Unable to enter Shipping_Agent_Code: {e}") 
        
    def enter_Shipping_Agent_Name(self, Shipping_Agent_Name):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Name)
            )
            field.clear()
            field.send_keys(Shipping_Agent_Name)
        except Exception as e:
            raise Exception(f"Unable to enter Shipping_Agent_Name: {e}") 

    def enter_Shipping_Agent_Email(self, Email):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Email)
            )
            field.clear()
            field.send_keys(Email)
        except Exception as e:
            raise Exception(f"Unable to enter Shipping_Agent_Email: {e}") 

    def enter_Shipping_Agent_Mobile_No(self, Mobile_No):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Mobile_No)
            )
            field.clear()
            field.send_keys(Mobile_No)
        except Exception as e:
            raise Exception(f"Unable to enter Mobile_No: {e}") 

    def enter_Charterer_Details(self, Charterer_Details):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Charterer_Details)
            )
            field.clear()
            field.send_keys(Charterer_Details)
        except Exception as e:
            raise Exception(f"Unable to enter Charterer_Details: {e}") 

    def enter_Shipping_Agent_Address_Line_1(self, Address_Line_1):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Address_Line_1)
            )
            field.clear()
            field.send_keys(Address_Line_1)
        except Exception as e:
            raise Exception(f"Unable to enter Address_Line_1: {e}") 

    def enter_Shipping_Agent_Address_Line_2(self, Address_Line_2):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Address_Line_2)
            )
            field.clear()
            field.send_keys(Address_Line_2)
        except Exception as e:
            raise Exception(f"Unable to enter Address_Line_2: {e}")                                                 

    def enter_Shipping_Agent_Address_Line_3(self, Address_Line_3):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Address_Line_3)
            )
            field.clear()
            field.send_keys(Address_Line_3)
        except Exception as e:
            raise Exception(f"Unable to enter Address_Line_3: {e}") 

    def select_Shipping_Agent_City(self, City):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_City)
            )
            field.clear()
            field.send_keys(City)
        except Exception as e:
            raise Exception(f"Unable to enter City: {e}") 
        
    def enter_Shipping_Agent_Street(self, Street):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Street)
            )
            field.clear()
            field.send_keys(Street)
        except Exception as e:
            raise Exception(f"Unable to enter Street: {e}") 

    def enter_Shipping_Agent_State(self, State):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_State)
            )
            field.clear()
            field.send_keys(State)
        except Exception as e:
            raise Exception(f"Unable to enter State: {e}") 

    def enter_Shipping_Agent_Country(self, Country):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Country)
            )
            field.clear()
            field.send_keys(Country)
        except Exception as e:
            raise Exception(f"Unable to enter Country: {e}")

    def enter_Shipping_Agent_Postcode(self, Postcode):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Shipping_Agent_Postcode)
            )
            field.clear()
            field.send_keys(Postcode)
        except Exception as e:
            raise Exception(f"Unable to enter Postcode: {e}") 

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
#                            DOCUMENTS                                                                      
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

    def step_click_Documents_panel(self):
        panel_icon = self.wait.until(
            EC.element_to_be_clickable(Locators.Documents_PANEL)
        )
        ActionChains(self.driver).move_to_element(panel_icon).click().perform()  
        time.sleep(5)  # Pauses the execution for 5 seconds 

    def enter_Ship_Registry_Certificate(self, Ship_Registry_Certificate):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Ship_Registry_Certificate)
            )
            field.clear()
            field.send_keys(Ship_Registry_Certificate)
        except Exception as e:
            raise Exception(f"Unable to enter Ship_Registry_Certificate: {e}") 

    def enter_Tonnage_Certificate(self, Tonnage_Certificate):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Tonnage_Certificate)
            )
            field.clear()
            field.send_keys(Tonnage_Certificate)
        except Exception as e:
            raise Exception(f"Unable to enter Tonnage_Certificate: {e}") 
        
    def enter_Load_Line_Certificate(self, Load_Line_Certificate):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Load_Line_Certificate)
            )
            field.clear()
            field.send_keys(Load_Line_Certificate)
        except Exception as e:
            raise Exception(f"Unable to enter Load_Line_Certificate: {e}") 

    def enter_Class_Cerificate(self, Class_Cerificate):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Class_Cerificate)
            )
            field.clear()
            field.send_keys(Class_Cerificate)
        except Exception as e:
            raise Exception(f"Unable to enter Class_Cerificate: {e}") 

    def enter_Owner_Charterer_Authorization_Letter(self, Owner_Charterer_Authorization_Letter):  
        try:
            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Owner_Charterer_Authorization_Letter)
            )
            field.clear()
            field.send_keys(Owner_Charterer_Authorization_Letter)
        except Exception as e:
            raise Exception(f"Unable to enter Owner_Charterer_Authorization_Letter: {e}")

    def click_stay_on_page_vessel_Registration(self):
        """Clicks on 'No, Stay on Page' button in the confirmation dialog."""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_stay_on_page)
        ).click()

    def click_yes_cancel_vessel_Registration(self):
        """Clicks on 'Yes, Cancel' button in the confirmation dialog."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_YES_Cancel)
        ).click()
# ========================================================================================================
# VESSEL REGISTRATION (END) 
# ========================================================================================================


#============================================================================================================================    
#       STAKEHOLDER MANAGEMENT (START)
#============================================================================================================================     
    def verify_stakeholder_management_header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Stakeholder_Management_Header),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False
        
    def Create_new_Stakeholder(self):
        """Click the floating Add (+) button"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Create_Stakeholder)
        ).click()  

    def create_stakeholder_management_header(self):
        """
        Verifies that a given page heading (h1) is visible.
        :param heading_text: The exact text of the heading to verify.
        """        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Create_Stakeholder_Management),
            f"Heading is not visible"
            )
            return True
        except TimeoutException:
            return False
        
    def click_stakeholder_master_type(self):
        try:
            dropdown = self.wait.until(
                EC.element_to_be_clickable(Locators.Stakeholder_Master_Type)
            )
            dropdown.click()
            print("✅ Clicked on Stakeholder Master Type dropdown")
            time.sleep(1)  # small delay so options load
            select_branch = self.wait.until(
                EC.element_to_be_clickable(Locators.Select_Stakeholder_Type)
            )
            select_branch.click()
            time.sleep(1)  # small delay so options load
            print("✅ Selected Stakeholder in Type dropdown")
            time.sleep(1)
        except Exception as e:
            raise Exception(f"❌ Unable to click and select Stakeholder in type dropdown: {e}")

    def unique_Stakeholder_Code(self, Stakeholder_Code):
        try:
            # Always reset and generate a fresh suffix (5 random uppercase letters)
            suffix = ''.join(random.choices(string.ascii_uppercase, k=5))  # random letters
            SC = f"{Stakeholder_Code}{suffix}"

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Stakeholder_Code)
            )
            field.clear()
            field.send_keys(SC)

            print(f"✅ Stakeholder Code entered: {SC}")
            return SC   # ✅ return value
        except Exception as e:
            raise Exception(f"Unable to enter Stakeholder Code: {e}")       

    def enter_Stakeholder_Name(self, Stakeholder_Name):
        try:
            # Always reset and generate a fresh suffix
            suffix = ''.join(random.choices(string.digits, k=5))  # random digits
            SN = f"{Stakeholder_Name}{suffix}"
            # # ✅ Save to context for later steps
            # self.context.Stakeholder_Name = SN  

            field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Stakeholder_Name)
            )
            field.clear()
            field.send_keys(SN)

            print(f"✅ Stakeholder Name entered: {SN}")
            return SN   # ✅ return value so step can save in context
        except Exception as e:
            raise Exception(f"Unable to enter Stakeholder Name: {e}")  
                         
    def click_stakeholder_active_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Stakeholder_Status)
        )
        element.click()
        time.sleep(1)

    def click_stakeholder_SAVE_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Stakeholder_SAVE)
        )
        element.click()
        time.sleep(2)

    def click_stakeholder_CANCEL_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Stakeholder_CANCEL)
        )
        element.click()
        time.sleep(2)

    def stakeholder_Name_Filter(self, SN):
        try:
            print("🔍 Locating Stakeholder Name filter chip...")
            chip = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(Locators.Stakeholder_Name_Column_Filter)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", chip)

            clickable_chip = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Locators.Stakeholder_Name_Column_Filter)
            )
            clickable_chip.click()
            print("✅ Clicked on Stakeholder Name filter chip.")

            # Now locate the input field
            filter_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.Search_Stakeholder_value)
            )
            filter_input.clear()
            filter_input.send_keys(SN)
            print(f"✅ Entered Stakeholder name: {SN}")
            time.sleep(2)

        except Exception as e:
            self.driver.save_screenshot("Stakeholder_Name_Filter_Failed.png")
            print("❌ Filter chip not found or not clickable. Screenshot saved.")
            raise e       

    def stakeholder_Edit(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Edit_Stakeholder)
        )
        element.click()
        time.sleep(2)

    def click_stakeholder_UPDATE_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.Update_Stakeholder)
        )
        element.click()
        time.sleep(2)
#============================================================================================================================    
#       STAKEHOLDER MANAGEMENT (END) 
#============================================================================================================================     


# ========================================================================================================
# LOGOUT (START) 
# ========================================================================================================

# For multiple login --------------------                        

    def is_error_invalid_password_displayed(self):
        return "Invalid password" in Locators.invalid_Username_Password

    def is_error_invalid_username_displayed(self):
        return "Invalid username" in Locators.invalid_Username_Password

    def is_error_invalid_credentials_displayed(self):
        return "Invalid credentials" in Locators.invalid_Username_Password

    def is_error_username_required_displayed(self):
        return "Username is required" in Locators.username_required

    def is_error_password_required_displayed(self):
        return "Password is required" in Locators.password_required

    # def is_error_both_required_displayed(self):
    #     return "Username and password are required" in self.error_message().text
    
# --------------------------------------    

    def is_logout_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Logout)
        )
    
    def click_logout(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.Logout)
        ).click()    
    
    def is_signIn_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.submit)
        )    

# ========================================================================================================
# LOGOUT (END) 
# ======================================================================================================== 
