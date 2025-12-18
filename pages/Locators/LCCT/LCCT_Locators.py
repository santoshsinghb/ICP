from selenium.webdriver.common.by import By

class Locators:

        # ========================================================================================================
        # Login page  (START) 
        # ========================================================================================================        
        username_input = (By.XPATH, "//input[@id='username']")        
        password_input = (By.XPATH, "//input[@id='password']")
        LCCT_username_input = (By.XPATH, "//input[@id='txtEmailId']")        
        LCCT_password_input = (By.XPATH, "//input[@id='txtPasswordId']")        
        invalid_Username_Password = (By.XPATH, "//div[contains(text(),'Invalid Username or Password')]")
        username_required = (By.XPATH, "//div[contains(text(),'Username or Email is required')]")
        password_required = (By.XPATH, "//div[contains(text(),'Password is required')]")
        submit = (By.CSS_SELECTOR, "button[type='submit']")
        LCCT_SignIn = (By.XPATH, "//button[@id='btnLoginId']")
        # ========================================================================================================
        # Login page  (END) 
        # ======================================================================================================== 



        # ========================================================================================================
        # Dashboard page  (START) 
        # ========================================================================================================
        # dashboard_expand_bar = (By.XPATH, "//aside[contains(@class, 'app-sidebar')]")
        # dashboard_header = (By.XPATH, "//*[contains(text(),'Dashboard') and self::h1]")
        LCCT_dashboard_header = (By.XPATH, "//h2[@class='text pb-2']")
        # welcome_message = (By.XPATH, "//h3[contains(normalize-space(.),'Welcome')]")
        # user_name = (By.XPATH, "//h3[contains(normalize-space(.),'Welcome')]/span")
        # Login_message = (By.XPATH, "//span[@class='text-capitalize']")
        # dashboard_date = (By.XPATH, "//button[contains(@class, 'klui-feature-icon')]//span[contains(text(), 'DD/MM/YYYY')]")
        # text_size = (By.XPATH, "//button[contains(@class, 'klui-feature-icon')]//i[contains(@class, 'fa-text-size')]")
        # select_theme = (By.XPATH, "//button[contains(@class, 'test-debug') and contains(@title, 'toggle the theme')]")
        # language_selector = (By.XPATH, "//button[.//i[contains(@class, 'fa-globe-asia')]]")
        # sidebar_button = (By.XPATH, "//button[@aria-label='Toggle Sidebar' and contains(@class, 'sidebar-pinner')]")
        # CommunityAdminLabel = (By.XPATH, "//div[@class='sidebar-user-data']//small[contains(translate(text(), ' ', ''), 'CommunityAdmin')]")
        # search_input = (By.XPATH, "//input[@placeholder='Search' and contains(@class, 'form-control sidebar-search')]")  # ← Search locator
        LCCT_sidebar_toggle = (By.XPATH, "//div[contains(@class,'sidebar-toggler-box')]")
        LCCT_1Y = (By.XPATH, "//label[@for='period_Type_id3']")
        # ========================================================================================================
        # Dashboard page  (END) 
        # ========================================================================================================
        


       

        
        # ========================================================================================================
        # LCCT ARISE  (START) 
        # ========================================================================================================
        LCCT_Menu_Search = (By.XPATH, "//input[@placeholder='Search']")
        Exports_Dropdown = (By.XPATH, "//span[normalize-space()='Exports']")
        Export_Report = (By.XPATH, "//li[@class='ng-star-inserted current']//li[@title='Export']//span[contains(text(),'Export')]")
        Export_Shipments = (By.XPATH, "//ul[@class='search-sidebar-menu']//li[@title='Exports']//ul//div[@class='ng-star-inserted']//span[contains(text(),'Shipments')]")
        Export_Checklist_Approval = (By.XPATH, "//li[@class='ng-star-inserted current']//span[contains(text(),'Export Checklist Approval')]")
        Export_Declaration = (By.XPATH, "//li[@class='ng-star-inserted current']//span[contains(text(),'Export Declarations')]")
        LCCT_User_Registration_Tariff = (By.XPATH, "//li[@class='ng-star-inserted current']//span[contains(text(),'User Registration Tariff')]")
        

        Export_LCCT_Reports_Label = (By.XPATH, "//strong[normalize-space()='Export LCCT Reports']")
        Export_Shipment_Listing_Label = (By.XPATH, "//span[@class='ml-0']")
        Export_Checklist_Approval_Label = (By.XPATH, "//span[@class='ml-0']")
        Export_Declarations_List_Label = (By.XPATH, "//span[@class='ml-0']")

        # Company Setup 
        LCCT_CompanySetupBranch = (By.XPATH, "//li[@class='ng-star-inserted current']//span[contains(text(),'Branch')]")
        LCCT_Add_CompanySetupBranch = (By.XPATH, "//button[@class='floating-btn floating-btn-circle']")
        LCCT_SAVE = (By.XPATH, "//button[contains(text(),'Save')]")
        LCCT_Branch_Code = (By.XPATH, "//input[@id='txtBranchCodeId']")
        LCCT_Branch_Name = (By.XPATH, "//input[@id='txtBranchNameId']")
        LCCT_Branch_Reporting_Officer = (By.XPATH, "//input[@class='ng-untouched igx-input-group__input ng-star-inserted ng-valid ng-pristine']")
        LCCT_Branch_RO = (By.XPATH, "//span[@title='123 - TEST']")
        LCCT_Branch_Address_1 = (By.XPATH, "//input[@id='txtAddress1Id']")
        LCCT_Branch_Country_Name = (By.XPATH, "//input[@class='igx-input-group__input ng-star-inserted ng-dirty ng-valid ng-touched']")
        LCCT_Branch_Country = (By.XPATH, "//igx-drop-down-item[@id='igx-drop-down-item-706']//span[@class='igx-drop-down__inner']")
        LCCT_Branch_City_Name = (By.XPATH, "//input[@class='igx-input-group__input ng-star-inserted ng-invalid ng-touched ng-dirty']")
        LCCT_Branch_ZipCode = (By.XPATH, "//input[@id='txtPostCodeId']")


        MenuBar =	(By.XPATH, "//div[@class='uplift-sidebar sidebar-closed']")
        Export_Tab =	(By.XPATH, "(//a[@id='Exports']/span[contains(text(),'Exports')])[2]")
        Exports_EnquiryListing_SubTab =	(By.XPATH, "(//a[@id='Enquiries']/span[contains(text(),'Enquiries')])[2]")
        EnquiryListing_Screen =	(By.XPATH, "//div[@class='listview__left']/ex-enquiry-list/div")
        CreateEnquiry_Screen =	(By.XPATH, "//div[@class='slide-from-right-master p-3 opened']/ex-enquiry-form/div")
        Movement_DD =	(By.XPATH, "(//input[@name='autoComplete'])[1]")
        Movement_HyperlinkList =	(By.XPATH, "//div[@class='igx-overlay']/div/div/div/div/igx-drop-down-item/span/span/span")
        RFQ_Currency_DD =	(By.XPATH, "(//input[@name='autoComplete'])[2]")
        RFQ_Deadline_CalendarIcon =	(By.XPATH, "(//igx-icon[@title='Choose Date'])[3]")

        # RFQ Details
        Customer_Tb =	(By.XPATH, "(//input[@name='autoComplete'])[3]")
        Customer_HyperlinkList =	(By.XPATH, "//div[@class='igx-overlay']/div/div/div/div/igx-drop-down-item/span/span/span[1]")
        Origin_Tb =	(By.XPATH, "(//input[@name='autoComplete'])[4]")
        Origin_HyperlinkList =	(By.XPATH, "//div[@class='igx-overlay']/div/div/div/div/igx-drop-down-item/span/span/span[1]")
        Destination_Tb =	(By.XPATH, "(//input[@name='autoComplete'])[5]")
        Destination_HyperlinkList =	(By.XPATH, "//div[@class='igx-overlay']/div/div/div/div/igx-drop-down-item/span/span/span[1]")
        Incoterms_DD =	(By.XPATH, "(//input[@name='autoComplete'])[6]")
        TargetFreightRate_Tb =	(By.XPATH, "//input[@id='TargetFreightRate']")
        ExpectedCargoReadiness_CalendarIcon =	(By.XPATH, "(//igx-icon[@title='Choose Date'])[3]")


        LCCT_Logout = (By.XPATH, "//span[normalize-space()='Logout']")
        # ========================================================================================================
        # LCCT ARISE  (END) 
        # ========================================================================================================


        # ========================================================================================================
        # Logout
        # ========================================================================================================                
        Logout = (By.CSS_SELECTOR, "button[aria-label='Logout']")



        # file_path = r"D:\Harshad\PCS\UI Automation\PCS_Selenium\test_data.xlsx"