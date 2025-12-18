from selenium.webdriver.common.by import By

class Locators:

        # ========================================================================================================
        # OMAN Login page  (START) 
        # ========================================================================================================        
        OMAN_username_input = (By.XPATH, "//input[@id='txtEmailId']")        
        OMAN_password_input = (By.XPATH, "//input[@id='txtPasswordId']")        
        OMAN_SignIn = (By.XPATH, "//button[@id='btnLoginId']")
        # ========================================================================================================
        # OMAN Login page  (END) 
        # ======================================================================================================== 



        # ========================================================================================================
        # Dashboard page  (START) 
        # ========================================================================================================
        OMAN_dashboard_header = (By.XPATH, "//h2[@class='text pb-2']")
        # search_input = (By.XPATH, "//input[@placeholder='Search' and contains(@class, 'form-control sidebar-search')]")  # ← Search locator
        LCCT_sidebar_toggle = (By.XPATH, "//div[contains(@class,'sidebar-toggler-box')]")
        LCCT_1Y = (By.XPATH, "//label[@for='period_Type_id3']")
        LCCT_Menu_Search = (By.XPATH, "//input[@placeholder='Search']")        
        # ========================================================================================================
        # Dashboard page  (END) 
        # ========================================================================================================
        

        # ========================================================================================================
        # OMAN (START) 
        # ========================================================================================================

        Export_Job_Maintenance = (By.XPATH, "//ul[@class='search-sidebar-menu']//li[@title='Export']//ul//div[@class='ng-star-inserted']//span[contains(text(),'Job Maintenance')]")
        Export_Job_List_Label = (By.XPATH, "//span[@class='new-btn-reset-capitalcase']")

        Import_Job_Maintenance = (By.XPATH, "//ul[@class='search-sidebar-menu']//li[@title='Import']//ul//div[@class='ng-star-inserted']//span[contains(text(),'Job Maintenance')]")
        Import_Job_List_Label = (By.XPATH, "//span[@class='mt-1']")

        OMAN_create_new_job = (By.XPATH, "//button[normalize-space()='+']")
        OMAN_quick_awb_link = (By.XPATH, "//button[normalize-space()='Quick AWB']")
        OMAN_create_new_awb_header = (By.XPATH, "//span[@title='DG Report']")

        OMAN_Quick_AWB_Prefix = (By.XPATH, "//label[normalize-space(text())='Prefix *']/following::input[1]")
        OMAN_Quick_AWB_MAWB = (By.XPATH, "//label[normalize-space(text())='MAWB No. *']/following::input[1]")
        OMAN_Quick_AWB_Destination = (By.XPATH, "//igx-input-group[@class='autocomplete igx-input-group igx-input-group--invalid igx-input-group--focused']//input[@name='autoComplete']")
        OMAN_Quick_AWB_NoP = (By.XPATH, "//igx-input-group[@class='igx-input-group igx-input-group--required igx-input-group--invalid igx-input-group--focused']//input[@id='TotNoOfPieces']")
        OMAN_Quick_AWB_Gross_Weight = (By.XPATH, "//input[@id='GrossWeightMAWB']")
        OMAN_Quick_AWB_Flight_No = (By.XPATH, "//igx-input-group[@class='igx-input-group igx-input-group--required igx-input-group--focused']//input[@id='AirlineCarrierCode']")
        OMAN_Quick_AWB_Flight_Date = (By.XPATH, "//form[@class='form ng-invalid ng-untouched ng-pristine']//igx-icon[@title='Choose Date'][normalize-space()='calendar_today']")
        OMAN_Quick_AWB_Nature_Of_Goods = (By.XPATH, "//igx-input-group[@class='igx-input-group igx-input-group--required igx-input-group--focused']//input[@id='AirlineCarrierCode']")
        OMAN_Quick_AWB_Commodity = (By.XPATH, "//input[@aria-expanded='true']")
        OMAN_Quick_AWB_SHC = (By.XPATH, "//input[@aria-expanded='true']")

        Create_Quick_AWB_Save = (By.XPATH, "//div[@class='col-md-12']//button[@class='new-btn-primary mr-2'][normalize-space()='Save']")
        # ========================================================================================================
        # OMAN (END) 
        # ========================================================================================================



        # ========================================================================================================
        # Logout
        # ========================================================================================================                
        Logout = (By.CSS_SELECTOR, "button[aria-label='Logout']")



        # file_path = r"D:\Harshad\PCS\UI Automation\PCS_Selenium\test_data.xlsx"