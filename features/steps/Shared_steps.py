from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.Actions.PCS.Shared_page import SharedPage
from pages.Locators.PCS.Locators import Locators
from utils.browser_setup import BrowserSetup
from utils.excel_reader import excel
from utils.excel_reader import read_excel_with_filter  # ✅ correct
# from utils.excel_reader import read_excel_data as read_excel_with_filter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from datetime import datetime
# from pages.Actions.PCS.dashboard_page import SharedPage
from behave import use_step_matcher
import json
import time
import allure
today_date = datetime.today().strftime('%d/%m/%Y')  # adjust format if needed


# ====================================================================================================

use_step_matcher("re")

# ====================================================================================================
# LOGIN (START)
# ====================================================================================================

@given("user launches the PCS application")
def step_impl(context):
    context.driver.get("https://app-pcs-next-ui-dev-centralindia-01-hkcbeggugrauggcc.centralindia-01.azurewebsites.net/")
    allure.attach(context.driver.current_url, name="Launch URL", attachment_type=allure.attachment_type.TEXT)

@when("user logs in with valid credentials")
def step_impl(context):
    # Sample wait - replace with actual login if needed
    time.sleep(2)
    allure.attach("Login simulated", name="Login Step", attachment_type=allure.attachment_type.TEXT)


@given("I launch the browser")
def step_impl(context):
    context.driver = BrowserSetup().get_driver()
    context.page = SharedPage(context.driver)


@when("I click the login button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_ICP_login()

# ICP (START)
@when("I click the ICP SignIn button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_ICP_login() 

@when("I click on Avatar button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_avatar_button()   

@when("I click on ICP Sign Out button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_ICP_Sign_Out_button()        

# LCCT (START)
@when("I click the LCCT SignIn button")
def step_impl(context):
    context.page.click_LCCT_login()   


@when("I click the 1Y button")
def step_impl(context):
    context.page.click_1Y() 
# --------------------------------------------------------------------------
# @when('I search for Shipments in the sidebar')
# def step_impl(context):
#     search_text = "Shipments"
#     context.page.enter_text_in_LCCT_sidebar_search(search_text)  


@when("I click on Exports Shipment")
def step_impl(context):
    context.page.exports_shipment()
# --------------------------------------------------------------------------
# @when('I search for Export Checklist in the sidebar')
# def step_impl(context):
#     search_text = "Export Checklist Approval"
#     context.page.enter_text_in_LCCT_sidebar_search(search_text)

@when("I click on Exports Checklist Approval")
def step_impl(context):
    context.page.exports_checklist_approval() 
# --------------------------------------------------------------------------
# @when("I search for Export Report in the sidebar")
# def step_impl(context):
#     search_text = "Export"
#     context.page.enter_text_in_LCCT_sidebar_search(search_text)

@when("I click on Export Report")
def step_impl(context):
    context.page.export_Report() 
# --------------------------------------------------------------------------
# @when("I search for Export Declaration in the sidebar")
# def step_impl(context):
#     search_text = "Export Declaration"
#     context.page.enter_text_in_LCCT_sidebar_search(search_text) 

@when("I click on Export Declaration")
def step_impl(context):
    context.page.export_declaration()
# --------------------------------------------------------------------------
# @when("I search for User Registration Tariff in the sidebar")
# def step_impl(context):
#     search_text = "User Registration Tariff"
#     context.page.enter_text_in_LCCT_sidebar_search(search_text) 

# --------------------------------------------------------------------------
# @when("I search for Logout in the sidebar")
# def step_impl(context):
#     search_text = "Logout"
#     context.page.enter_text_in_LCCT_sidebar_search(search_text) 

@then("I click on LCCT Logout button")
def step_impl(context):
    context.page.LCCT_Logout()             
# --------------------------------------------------------------------------
@when("I should see the LCCT Export Reports page")
def step_impl(context):
    assert context.page.check_LCCT_Export_Reports_Label()

@when("I should see the Export Shipment Listing HOME page")
def step_impl(context):
    assert context.page.check_Export_Shipment_Listing_Label()

@when("I should see the Export Checklist Approval page")
def step_impl(context):
    assert context.page.check_Export_Checklist_Approval_Label()

@when("I should see the Export Declaration page")
def step_impl(context):
    assert context.page.check_Export_Declarations_List_Label()        
# --------------------------------------------------------------------------
    
# LCCT (END)


@given('I load test data for "{data_name}"')
def step_load_test_data(context, data_name):
    print(f"Loading data for: Shipping_Agent_login")
    file_path = r"D:\Harshad\PCS\UI Automation\PCS_Selenium\test_data.xlsx"
    sheet_name = "Sheet1"
    context.test_data = excel.get_test_data(file_path, sheet_name, data_name)

@when("I open the login page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.open()




# -----------------------------------------  LCCT -----------------------------------------
@when("I enter valid LCCT Admin's username and password")
def step_impl(context):
    context.page.LCCT_enter_credentials("kalelcct@yopmail.com", "kale@123")  
# -----------------------------------------  LCCT -----------------------------------------
      

#  ----------------------------------------- OMAN START -----------------------------------------
@when("I enter valid OMAN Admin username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("mctoman@yopmail.com", "Kale@123")  

@when("I enter valid OMAN Freight Forwarder username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("novelmuscut", "Kale@123")

@when("I enter valid OMAN Airline username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("salamairline", "Kale@123")  

@when("I enter valid OMAN GHA username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("omansats", "Kale@123")  

@when("I enter valid OMAN TPS username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("tpsmct", "Kale@123")  

@when("I enter valid OMAN Airport username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("mctairport", "Kale@123")  

@when("I enter valid OMAN Airline 2 username and password")
def step_impl(context):
    context.page.OMAN_enter_credentials("AIRLINETURKOMAN", "Kale@123")  



#  ----------------------------------------- OMAN END -----------------------------------------


#  ----------------------------------------- ICP START -----------------------------------------

@when("I enter valid Shipping Agent's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("usersp", "admin")

@when("I enter NEW Shipping Agent's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("UserSP", "admin")

@when("I enter valid Community Admin's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("admin", "pass")  

@when("I enter valid Marine Department's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("usermarine", "admin")  

@when("I enter valid Ministry's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("userministry", "admin")        

@when("I enter valid Private Jetty's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("userpj", "admin")

@when("I enter valid Terminal Operator's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("userto", "admin")     

@when("I enter valid Immigration's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("userimig", "admin")   

@when("I enter valid Custom's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("usercus", "admin") 

@when("I enter valid Port Operator's username and password")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("userto", "admin")   

@when("I enter valid Branch user credentials")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_ICP_credentials("usersp", "admin")      
   
#  ----------------------------------------- ICP END -----------------------------------------

@when('I enter username "{username}"')
# def step_impl(context, username):
#     username_field = context.driver.find_element(By.ID, "username")  # Adjust locator
#     username_field.clear()
#     username_field.send_keys(username)
def step_impl(context, username):
        page = SharedPage(context.driver)
        page.enter_username(username)

@when('I enter password "{password}"')
# def step_impl(context, password):
#     password_field = context.driver.find_element(By.ID, "password")  # Adjust locator
#     password_field.clear()
#     password_field.send_keys(password)
def step_impl(context, password):
        page = SharedPage(context.driver)
        page.enter_password(password)  

# ====================================================================================================
# LOGIN (END)
# ====================================================================================================

# ====================================================================================================
# DASHBOARD (START)
# ====================================================================================================

@then('Expand menu bar should be collapsed')
def step_verify_menu_collapsed(context):
    shared_page = SharedPage(context.driver)
    is_collapsed = shared_page.is_menu_collapsed()
    assert is_collapsed, "❌ Menu Dashboard is visible (menu should be collapsed)."
    print("✅ Menu is collapsed as expected.")

@when("I should see the dashboard page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.is_dashboard_displayed()

@when("I should see the Ship Call Number page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.Verify_SCN_Header()

# LCCT (START)

@when("I should see the LCCT HOME page")
def step_impl(context):
    assert context.page.is_LCCT_dashboard_displayed()   

@when('I hover over the sidebar to expand it')
def step_impl(context):
    # context.page.LCCT_expand_sidebar()      
    landing_page = SharedPage(context.driver)
    landing_page.LCCT_expand_sidebar()       

# LCCT (END)



# OMAN (START)

@when("I should see the OMAN HOME page")
def step_impl(context):
    assert context.page.is_OMAN_dashboard_displayed()   

@when('I hover over the OMAN sidebar to expand it')
def step_impl(context):
    # context.page.LCCT_expand_sidebar()      
    landing_page = SharedPage(context.driver)
    landing_page.LCCT_expand_sidebar()       

# OMAN (END)


@then('I should see the user role label as "{expected_label}"')
def step_check_user_role(context, expected_label):
    actual_label = context.page.get_user_role_label()
    assert actual_label == expected_label, f"Expected '{expected_label}', but got '{actual_label}'"

@then("user should see the dashboard title")
def step_impl(context):
    dashboard = SharedPage(context.driver)
    actual_title = dashboard.get_title_text()
    expected_title = "Dashboard"
    allure.attach(actual_title, name="Actual Title", attachment_type=allure.attachment_type.TEXT)
    assert actual_title == expected_title

@then("user should see the Welcome message")
def step_impl(context):
    WelcomeMessage = SharedPage(context.driver)
    actual_welcome = WelcomeMessage.get_welcome_text()
    expected_welcome = "Welcome, "
    allure.attach(actual_welcome, name="Actual Title", attachment_type=allure.attachment_type.TEXT)
    print(f"[DEBUG] Expected: '{expected_welcome}'")
    print(f"[DEBUG] Actual: '{actual_welcome}'")
    assert expected_welcome.lower() in actual_welcome.lower().strip(), \
       f"Expected '{expected_welcome}' in '{actual_welcome}'"
    
@then("user should see the Username message")
def step_impl(context):
    Username = SharedPage(context.driver)
    actual_username = Username.get_logged_in_username()
    expected_username = "admin admin"
    allure.attach(actual_username, name="Actual Title", attachment_type=allure.attachment_type.TEXT)
    print(f"[DEBUG] Expected: '{expected_username}'")
    print(f"[DEBUG] Actual: '{actual_username}'")
    assert expected_username.lower() in actual_username.lower().strip(), \
       f"Expected '{expected_username}' in '{actual_username}'"    

@then("user should see the Date format displayed")
def step_impl(context):
    Dashboard_Date = SharedPage(context.driver)
    result = Dashboard_Date.verify_date_field()
    assert result is True, "❌ Date field verification failed."   

@then("user should see the Font size button")
def step_impl(context):
    dashboard_page = SharedPage(context.driver)
    dashboard_page.click_text_resize_icon()
    time.sleep(1)

@then("user should see the Toggle theme button")
def step_impl(context):
    theme_toggle = SharedPage(context.driver)
    theme_toggle.click_theme_toggle_icon()

@then("user should see the language selection button")
def step_impl(context):
    language_icon = SharedPage(context.driver)
    language_icon.click_language_toggle_icon()    
# ====================================================================================================
# DASHBOARD (END)
# ====================================================================================================


# =====================================================================================
# Excel Sheet  (START)
# =====================================================================================
@when('I enter username and password from Excel data')
def step_enter_credentials(context):
    username = context.test_data["Username"]
    password = context.test_data["Password"]
    context.page.enter_credentials(username, password)  

    # Login with all credentials in Excel data  

@when('I test login using valid credentials from Excel')
def step_impl(context):
    file_path = r"D:\Harshad\PCS\UI Automation\ICP\TestData\PCS\test_data.xlsx"
    sheet_name = "Sheet1"

    # Only run test rows where isValid == FALSE
    all_data = read_excel_with_filter(file_path, sheet_name, filter_by={"isValid": "TRUE"})

    for data in all_data:
        username = data['Username']
        password = data['Password']
        testcase = data['TestCase']
        print(f"Testing {testcase} with username: {username}")

        # Open login page
        context.page.open()

        # Enter credentials
        context.page.enter_credentials(username, password)

        # Click login
        context.page.click_login()

        # Check dashboard (this part is for valid users — do you really want this for isValid == FALSE?)
        assert context.page.is_dashboard_displayed(), f"Login failed for {testcase}"

        # Expand Sidebar
        context.page.click_sidebar_toggle_button()

        # Logout after success (if your app has logout)
        logout_button = context.page.is_logout_visible()
        logout_button.click()

    # Login with ONLY invalid credentials from Excel

@when('I test login using invalid credentials from Excel')
def step_impl(context):
    file_path = r"D:\Harshad\PCS\UI Automation\ICP\TestData\PCS\test_data.xlsx"
    sheet_name = "Sheet1"
    context.invalid_credentials = read_excel_with_filter(file_path, sheet_name, filter_by={"isValid": "FALSE"})
    context.failed_logins = []

    for row in context.invalid_credentials:
        context.page.enter_username(row["Username"])
        context.page.enter_password(row["Password"])
        context.page.click_login()
        if context.page.is_login_failed():
            context.failed_logins.append((row["Username"], row["Password"]))            

@then('each login attempt should show a login error')
def step_impl(context):
    assert len(context.failed_logins) == len(context.invalid_credentials), "Some invalid logins unexpectedly succeeded"


@then("I test login with all valid & invalid data from Excel")
def step_test_login_all(context):
    for data in context.login_data:
        username = str(data.get('Username', '')) or ''
        password = str(data.get('Password', '')) or ''
        testcase = data.get('TestCaseName', 'Unknown')
        expected_result = data.get('ExpectedResult', '').strip()
        
        print(f"Testing {testcase} with username: {username}")

        # Open login page
        context.page.open()

        # Enter credentials
        context.page.enter_username(username)
        context.page.enter_password(password)
        context.page.click_login()

        # Assert based on expected result
        if expected_result == 'dashboard':
            assert context.page.is_dashboard_displayed(), f"Dashboard NOT found for {testcase}"
            # Logout if login was successful
            if context.page.is_logout_visible():
                context.page.logout()
        elif expected_result == 'error_invalid_password':
            assert context.page.is_error_invalid_password_displayed(), f"Invalid password error not shown for {testcase}"
        elif expected_result == 'error_invalid_username':
            assert context.page.is_error_invalid_username_displayed(), f"Invalid username error not shown for {testcase}"
        elif expected_result == 'error_invalid_credentials':
            assert context.page.is_error_invalid_credentials_displayed(), f"Invalid credentials error not shown for {testcase}"
        elif expected_result == 'error_username_required':
            assert context.page.is_error_username_required_displayed(), f"Username required error not shown for {testcase}"
        elif expected_result == 'error_password_required':
            assert context.page.is_error_password_required_displayed(), f"Password required error not shown for {testcase}"
        elif expected_result == 'error_both_required':
            assert context.page.is_error_both_required_displayed(), f"Both fields required error not shown for {testcase}"
        else:
            raise Exception(f"Unknown expected result '{expected_result}' for {testcase}")        
        
# =====================================================================================
# Excel Sheet  (END)
# =====================================================================================



# ========================================================================================================
# SEARCH (START) 
# ========================================================================================================
@when("I click to expand sidebar")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_sidebar_toggle_button()

@when(u'I enter "{search_text}" in the sidebar search field')
def step_enter_sidebar_search(context, search_text):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(Locators.ICP_search_input))
    search_box.clear()
    search_box.send_keys(search_text)
     

@when("I search for Registration Template in the sidebar")
def step_impl(context):
    search_text = "Registration Template"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)

@when("I search for Transaction Template in the sidebar")
def step_impl(context):
    search_text = "Transaction Template"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)    

@when("I search for Registration Requests in the sidebar")
def step_impl(context):
    search_text = "Registration Requests"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)  

@when("I search for Registration Approval Workflow in the sidebar")
def step_impl(context):
    search_text = "Registration Approval Workflow"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)  

@when("I search for Transaction Approval Workflow in the sidebar")
def step_impl(context):
    search_text = "Transaction Approval Workflow"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)     

@when("I search for Vessel Profile in the sidebar")
def step_impl(context):
    search_text = "Vessel Profile"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)     

@when("I search for Vessel Registration in the sidebar")
def step_impl(context):
    search_text = "Vessel Registration"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)   

@when("I search for Ship Call Number  in the sidebar")
def step_impl(context):
    search_text = "Ship Call Number"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)     

@when("I search for Pre-Arrival Notification  in the sidebar")
def step_impl(context):
    search_text = "Pre-Arrival Notification"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)    

@when("I search for Arrival Clearance  in the sidebar")
def step_impl(context):
    search_text = "Arrival Clearance"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)     

@when("I search for Departure Clearance  in the sidebar")
def step_impl(context):
    search_text = "Departure Clearance"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text) 

@when("I search for Stakeholder Management  in the sidebar")
def step_impl(context):
    search_text = "Stakeholder Management"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)   

@when("I search for Terminal Configuration  in the sidebar")
def step_impl(context):
    search_text = "Terminal Configuration"
    context.page = SharedPage(context.driver)
    context.page.enter_text_in_sidebar_search(search_text)        

@then("I scroll to the bottom of the page")
def step_scroll_bottom(context):
    context.page.scroll_to_bottom()   
# ========================================================================================================
# SEARCH (END) 
# ========================================================================================================


# ========================================================================================================
# Community Admin  (START) 
# ========================================================================================================
@when("I should see the Welcome message")
def step_impl(context):
    assert context.page.is_Welcome_displayed()

@when("I should see the Login message")
def step_impl(context):
    assert context.page.is_Login_displayed()


 
@when("I click to expand Template Management")
def step_impl(context):
    context.page.click_template_mgmt_toggle()
    time.sleep(1) 

@when("I navigate to Registration Template page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Registration_Template = context.page.check_Registration_Template()
    Registration_Template.click()
    time.sleep(2) 

@when("I navigate to Transaction Template page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Transaction_Template = context.page.check_Transaction_Template()
    Transaction_Template.click()  
    time.sleep(1) 

@when("I navigate to Registration Requests page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Registration_Requests = context.page.check_Registration_Requests()
    Registration_Requests.click()      
    time.sleep(1) 

@when("I click to expand Workflow Configuration")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_Workflow_Conf_toggle()
    time.sleep(1) 

@when("I navigate to Registration Approval Workflow page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Registration_Approval = context.page.check_Registration_Approval_Workflow()
    Registration_Approval.click()        
    time.sleep(1) 

@when("I navigate to Transaction Approval Workflow page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Transaction_Approval = context.page.check_Transaction_Approval_Workflow()
    Transaction_Approval.click()       
    time.sleep(1) 
    
@when("I click to expand Vessel Management")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vessel_mgmt_toggle()
    time.sleep(1)

@when("I navigate to Vessel Profile page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.navigate_to_vessel_profile()  
    time.sleep(1)

@when("I navigate to Vessel Registration page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.navigate_to_vessel_registration()
    time.sleep(1)    

# ===============================================
@when("I navigate to Ship Call Number")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.navigate_to_ship_call_number()
    time.sleep(1)   

@when("I navigate to Pre-Arrival Notification")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.navigate_to_pre_arrival_notification()
    time.sleep(1)   

@when("I navigate to Arrival Clearance")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.navigate_to_arrival_clearance()
    time.sleep(1)   

@when("I navigate to Departure Clearance")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.navigate_to_departure_clearance()
    time.sleep(1)               

# ===============================================

@when("I navigate to Stakeholder Management page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.check_Stakeholder_Management()
    time.sleep(1)      

@when('I navigate to ePAN page')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.check_Pre_Arrival_Notification()
    time.sleep(1) 

@when("I navigate to Terminal Configuration page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.check_Terminal_Configuration()
    time.sleep(1)

# ========================================================================================================
# Community Admin  (END) 
# ========================================================================================================




# ========================================================================================================
# Registration Template  (START) 
# ========================================================================================================
@when("I should see the Registration Template header")
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.validate_Registration_Template_Header()

@when("I click on Create New Registration Template button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Create_New_Registration_Template = context.page.Create_New_Registration_Template()
    Create_New_Registration_Template.click()
    # time.sleep(5)      

@when("I choose a stakeholder type as Shipping Agent")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Choose_Shipping_Agent = context.page.Choose_Shipping_Agent()
    Choose_Shipping_Agent.click()
    time.sleep(2)   

@when("I click on Next to choose registration type")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Click_Next = context.page.Click_Next()
    time.sleep(2)  

@when("I select Registration type as User")
def step_impl(context):
    context.page = SharedPage(context.driver)
    User_Registration_Type = context.page.User_Registration_Type()
    User_Registration_Type.click()
    time.sleep(2)   

@when("I click on Next to open form page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    Registration_Next = context.page.Registration_Next()
    Registration_Next.click()
    time.sleep(5)                 

@when("I should see the Create New Template header")
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.Label_Create_New_Template()

@when("I enter a random Template Name")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_random_template_name(context)

@when("I enter the Template Description")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_template_description(context)

@when("I click SAVE button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_save_button() 

@when("I click PREVIEW button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_Preview_button()

@when("I click on GO BACK TO EDIT button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_go_back_to_edit()

@when("I click Cancel button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_Cancel_button()

@when("I confirm Cancel")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.confirm_Cancel()    

@when("Do not Cancel")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.dont_Cancel()   

@when("I search the Template")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Template_Name_Filter(context.template_name)

@when("I edit newly added template")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Edit_Post_Search()  

# ========================================================================================================
# Registration Template  (END) 
# ========================================================================================================



# ========================================================================================================
# Transaction Template  (START) 
# ========================================================================================================
@when("I should see the Transaction Template header")
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.validate_Transaction_Template_Header()

@when("I click on Transaction GO BACK TO EDIT button")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.transaction_click_go_back_to_edit()
# ========================================================================================================
# Transaction Template  (END) 
# ========================================================================================================

# HARSHAD

# ========================================================================================================
# Registration REQUESTS (START) 
# ========================================================================================================
@when('I should see the Registration Requests header')
def step_impl(context):
    page = SharedPage(context.driver)
    assert page.verify_stakeholder_registration_request_list_heading(), \
        "Stakeholder Registration Request List heading not found."

@when('I click on All filter in Stakeholder Registration Request List')
def step_click_all_filter(context):
    page = SharedPage(context.driver)
    page.click_all_filter_stakeholder_requests()

@when('I click on Pending filter in Stakeholder Registration Request List')
def step_click_pending_filter(context):
    page = SharedPage(context.driver)
    page.click_pending_filter_stakeholder_requests()

@when('I click on Approved filter in Stakeholder Registration Request List')
def step_click_approved_filter(context):
    page = SharedPage(context.driver)
    page.click_approved_filter_stakeholder_requests()

@when('I click on Rejected filter in Stakeholder Registration Request List')
def step_click_rejected_filter(context):
    page = SharedPage(context.driver)
    page.click_rejected_filter_stakeholder_requests()          

@when("I scroll the horizontal bar to the extreme right")
def step_scroll_horizontal_bar_right(context):
    context.page = SharedPage(context.driver)
    context.page.scroll_to_extreme_right()
    time.sleep(2) 

@when("I scroll the horizontal bar to the extreme left")
def step_scroll_horizontal_bar_left(context):
    context.page = SharedPage(context.driver)
    context.page.scroll_to_extreme_right()
    time.sleep(2)     

@when('I verify approval status column for all filter tiles')
def step_verify_approval_status_column(context):
    reg_page = SharedPage(context.driver)
    reg_page.verify_all_tiles()
# ========================================================================================================
# Registration REQUESTS (END) 
# ========================================================================================================



# ========================================================================================================
# ORGANIZATION SETUP (START) 
# ========================================================================================================

@when('I expand Organization Setup')
def step_expand_org_setup(context):
    sidebar = SharedPage(context.driver)
    sidebar.expand_organization_setup()


# ========================================================================================================
# ORGANIZATION SETUP (END) 
# ========================================================================================================

# ========================================================================================================
# BRANCH (START) 
# ========================================================================================================
@when('I click on Branch')
def step_select_org_info(context):
    org_page = SharedPage(context.driver)
    org_page.open_branch()
    time.sleep(4)

@when('I should see Branch Management Header')
def step_verify_brnh_mgmt_page_header(context):
    branch_page = SharedPage(context.driver)
    assert branch_page.verify_branch_heading_present(), "Branch Management heading not found!"

@when('I click on Create New Branch button')
def step_click_add_branch(context):
    branch_page = SharedPage(context.driver)
    branch_page.create_branch_user()
    time.sleep(2)

@when('I enter Branch Name')
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_branch_name(context)

@when('I enter Branch Email ID')
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_branch_email_id(context)

@when('I enter Branch Phone No.')
def step_impl(context):
    phone_no = "7777799999"
    page = SharedPage(context.driver)
    page.enter_branch_phone_no(phone_no)

@when('I enter Branch Address Line 1')
def step_impl(context):
    Address_Line_1 = "Address Line 1"
    page = SharedPage(context.driver)
    page.enter_branch_admin_Address_Line_1(Address_Line_1)

@when('I enter Branch Address Line 2')
def step_impl(context):
    Address_Line_2 = "Address Line 2"
    page = SharedPage(context.driver)
    page.enter_branch_admin_Address_Line_2(Address_Line_2)

@when('I enter Branch Address Line 3')
def step_impl(context):
    Address_Line_3 = "Address Line 3"
    page = SharedPage(context.driver)
    page.enter_branch_admin_Address_Line_3(Address_Line_3)

@when('I enter Branch City')
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_branch_city_dropdown()
    # time.sleep(4)  

@when('I enter Branch Postcode')
def step_impl(context):
    Postcode = "123456"
    page = SharedPage(context.driver)
    page.enter_branch_admin_Postcode(Postcode)

@when('I enter Branch State')
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_branch_state_dropdown()
    # time.sleep(2)  

@when('I enter Branch Country')
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_branch_country_dropdown()
    # time.sleep(2)  

@when('I enter Branch Admin First Name')
def step_impl(context):
    first_name = "John"
    page = SharedPage(context.driver)
    page.enter_branch_admin_first_name(first_name)

@when('I enter Branch Admin Middle Name')
def step_impl(context):
    middle_name = "M"
    page = SharedPage(context.driver)
    page.enter_branch_admin_middle_name(middle_name)

@when('I enter Branch Admin Last Name')
def step_impl(context):
    last_name = "Doe"
    page = SharedPage(context.driver)
    page.enter_branch_admin_last_name(last_name)

@when('I enter Branch Admin Designation')
def step_impl(context):
    designation = "Manager"
    page = SharedPage(context.driver)
    page.enter_branch_admin_designation(designation)

@when('I enter Branch Admin Email ID')
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_branch_admin_email_id(context)

@when('I enter Branch Admin Phone No.')
def step_impl(context):
    phone_no = "9876543210"
    page = SharedPage(context.driver)
    page.enter_branch_admin_phone_no(phone_no)

@when('I enter Branch Admin Username')
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_branch_admin_username(context)

@when('I click on Branch SAVE button')
def step_click_save_branch(context):
    branch_page = SharedPage(context.driver)
    branch_page.save_new_branch()
    time.sleep(3)  

@when('I click on Branch CANCEL button')
def step_click_cancel_branch(context):
    branch_page = SharedPage(context.driver)
    branch_page.cancel_new_branch()
    time.sleep(2)

@when('I click on Branch Name filter')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Branch_Name_Filter(context.branch_name)
    
@when('I click on Branch View button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.View_Branch_Post_Search()

@when('I click on Branch Edit button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Edit_Branch_Post_Search()

@when('I should see View Branch Header')
def step_verify_brnh_mgmt_page_header(context):
    branch_page = SharedPage(context.driver)
    assert branch_page.view_branch_heading_present(), "Branch Management heading not found!"

@when('I should see the Branch Username')
def step_impl(context):
    expected_username = "User9199"
    context.page = SharedPage(context.driver)
    actual_username = context.page.get_branch_username()
    assert actual_username == expected_username, \
        f"❌ Expected Branch Username: {expected_username}, but got: {actual_username}"
    print(f"✅ Branch Username verified successfully: {actual_username}")
    

# ========================================================================================================
# BRANCH (END) 
# ========================================================================================================


# ========================================================================================================
# USER (START) 
# ========================================================================================================

@when('I click on User')
def step_select_org_info(context):
    org_page = SharedPage(context.driver)
    org_page.open_user()

@when('I should see the User Management header')
def step_verify_user_mgmt_page(context):
    user_page = SharedPage(context.driver)
    assert user_page.verify_heading_present(), "User Management heading not found!"

@when('I click on Create User button')
def step_click_add_user(context):
    user_page = SharedPage(context.driver)
    user_page.create_new_user()
    time.sleep(2)  

@when("I click on User Type dropdown")
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_user_type_dropdown()
    time.sleep(2)    

@when("I click on Branch dropdown")
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_branch_dropdown()
    time.sleep(2)       

@when('I enter FirstName in First Name field')
def step_impl(context):
    first_name = "John"
    page = SharedPage(context.driver)
    page.enter_first_name(first_name)

@when('I enter MiddleName in Middle Name field')
def step_impl(context):
    middle_name = "M"
    page = SharedPage(context.driver)
    page.enter_middle_name(middle_name)

@when('I enter LastName in Last Name field')
def step_impl(context):
    last_name = "Doe"
    page = SharedPage(context.driver)
    page.enter_last_name(last_name)

@when('I enter Manager in Designation field')
def step_impl(context):
    designation = "Manager"
    page = SharedPage(context.driver)
    page.enter_designation(designation)

@when('I enter MobileNo in Phone No field')
def step_impl(context):
    phone_no = "9876543210"
    page = SharedPage(context.driver)
    page.enter_phone_no(phone_no)

@when("I enter a unique Username")
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_username(context)

@when("I enter emailId in Email ID field")
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_email_id(context)
    
@when('I click on User SAVE button')
def step_click_save_user(context):
    user_page = SharedPage(context.driver)
    user_page.save_new_user()
    time.sleep(10)  

@when('I click on User CANCEL button')
def step_click_cancel_user(context):
    user_page = SharedPage(context.driver)
    user_page.cancel_new_user()
    time.sleep(4)            
# ========================================================================================================
# USER (END) 
# ========================================================================================================


# ========================================================================================================
# Registration Approval Workflow (START) 
# ========================================================================================================
@when("I should see the Registration Approval Workflow Management header")
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.verify_workflow_page_title()

@when("I click on Create Registration Approval Workflow button")
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_add_button()

@when("I select Self from Initiator Type dropdown")
def step_select_self_from_initiator_type(context):
    context.page = SharedPage(context.driver)
    context.page.select_initiator_type_self()

@when("I enter a random Workflow Name")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_random_workflow_name(context)

@when("I enter Workflow Description")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_workflow_description(context)

@when("I drag Customs to Stage 1")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.drag_customs_to_stage_1()
    time.sleep(3)  # let UI finish rendering after drop

@when('I click on the ADD STAGE button')
def step_click_add_stage(context):
    page = SharedPage(context.driver)
    page.click_add_stage_button()

@when('I click on RAW SAVE button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_raw_SAVE_button() 

@when('I should see the RAW Save Popup')
def step_impl(context):
    context.page = SharedPage(context.driver)
    is_displayed = context.page.is_workflow_error_popup_displayed()
    assert is_displayed, "❌ Workflow error popup was not displayed"
    print("✅ Workflow error popup is displayed successfully")


# ========================================================================================================
# Registration Approval Workflow (END) 
# ========================================================================================================



# ========================================================================================================
# Transaction Approval Workflow (START) 
# ========================================================================================================
@when("I should see the Transaction Workflow header")
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.verify_transaction_workflow_header()
    time.sleep(3)

@when('I click on Create Workflow button')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_TAW_add_button()

@when('I choose a Module type for Transaction Approval Workflow')
def step_impl(context):
    context.page = SharedPage(context.driver)
    Choose_Module_Management = context.page.TAW_Vessel_Management()
    Choose_Module_Management.click()
    time.sleep(2)

# @when('I click on Next button for Transaction Approval Workflow')
# def step_impl(context):
#     Click_TAW_Next = context.page.Click_TAW_Next()
#     time.sleep(2) 
@when('I click on Next button for Transaction Approval Workflow')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Click_TAW_Next()     
    time.sleep(2) 

@when('I choose a Sub-Module type for Transaction Approval Workflow')
def step_impl(context):
    context.page = SharedPage(context.driver)
    Vessel_Registration_Type = context.page.Vessel_Registration_Type()
    Vessel_Registration_Type.click()
    time.sleep(2) 

# @when('I click on Next button for Transaction Approval Workflow')
# def step_impl(context):
#     sub_module_type = context.page.sub_module_type()
#     sub_module_type.click()
#     time.sleep(5)  

@when('I select an Initiator Type for Transaction Approval Workflow')
def step_select_self_from_initiator_type(context):
    context.page = SharedPage(context.driver)
    context.page.select_TAW_initiator_type_self()

@when('I choose unique Workflow Name for Transaction Approval Workflow')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_random_TAW_workflow_name(context)

@when('I give Workflow Description for Transaction Approval Workflow')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.enter_TAW_workflow_description(context)

@when('I add a Stakeholder for Transaction Approval Workflow')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.drag_TAW_customs_to_stage_1()
    time.sleep(3)  # let UI finish rendering after drop

@when('I click on TAW SAVE button') 
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_TAW_SAVE_button()

@when('I click on TAW CANCEL button') 
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_TAW_CANCEL_button()   

@when('I click on TAW Discard CANCEL button') 
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_TAW_discard_CANCEL_button()  

@when('I click on TAW Confirm CANCEL button') 
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_TAW_confirm_CANCEL_button()        

@when('I add a Stage for Transaction Approval Workflow')
def step_click_add_stage(context):
    page = SharedPage(context.driver)
    page.click_TAW_add_stage_button()

@when('I add another Stakeholder for Transaction Approval Workflow')

# ========================================================================================================
# Transaction Approval Workflow (END) 
# ========================================================================================================

# ========================================================================================================
# EPAN (START) 
# ========================================================================================================

@when('Validate ePAN page header')
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.validate_Pre_Arrival_Notification_Header()

@when('User clicks on Create ePAN button')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_Create_EPAN_button()

@when('Validate Create New ePAN page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Verify_Create_New_ePAN_Header()
    time.sleep(1)

@when('User enters SCN Number')
def step_impl(context):
    SCN_No = 'SCN5633411002'
    page = SharedPage(context.driver)
    page.enter_scn_number(SCN_No)
    time.sleep(1)  # small wait to let the page load

@when('User clicks on EPAN GO button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_EPAN_GO_button() 

@when('I click on ISSC Present radio button')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_ISSC_Present_button()

@when('I select Non Compliant Port as No')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_non_compliant_Np()

@when('I select Non Compliant Port as Yes')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_non_compliant_Yes()    

@when('I upload Crew List')
def upload_Crew_list(context):
    context.page = SharedPage(context.driver)
    context.register_page.upload_Crew_list("path/to/letter.pdf")

@when('I upload Passenger List')
def upload_Passenger_list(context):
    context.page = SharedPage(context.driver)
    context.register_page.upload_Passenger_list("path/to/letter.pdf")

@when('I upload DG Cargo Declaration')
def upload_Passenger_list(context):
    context.page = SharedPage(context.driver)
    context.register_page.upload_Cargo_Declaration("path/to/letter.pdf")

@when('I enter EPAN Port Code')
def step_impl(context):
    Port_Code = 'AUTO_PORT_CODE'
    page = SharedPage(context.driver)
    page.enter_port_code(Port_Code)
    time.sleep(1)  # small wait to let the page load

@when('I enter EPAN Port Name')
def step_impl(context):
    Port_Name = 'AUTO_PORT_NAME'
    page = SharedPage(context.driver)
    page.enter_port_name(Port_Name)
    time.sleep(1)  # small wait to let the page load

@when('I select EPAN Arrival date')
def step_impl(context):
    page = SharedPage(context.driver)
    page.EPAN_Arrival_date()

@when('I select EPAN Departure date')
def step_impl(context):
    page = SharedPage(context.driver)
    page.EPAN_Departure_date()

@when('I SUBMIT EPAN')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_EPAN_SUBMIT_button()

@when('I SAVE AS DRAFT EPAN')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_EPAN_SAVE_button()

@when('I CANCEL EPAN')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_EPAN_CANCEL_button()  

@when('I search newly created EPAN')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.SCN_No_Filter(context.SCN_No)

@when('I View searched EPAN')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.View_EPAN_Post_Search()

@when('I Amend newly created EPAN')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Amend_EPAN_Post_Search()

# ========================================================================================================
# EPAN (END) 
# ========================================================================================================


# ========================================================================================================
# SCN (START) 
# ========================================================================================================
@when('I navigate to SCN page')
def step_select_org_info(context):
    org_page = SharedPage(context.driver)
    org_page.open_scn_page()

@when('Validate SCN page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Verify_SCN_Header()
    time.sleep(3)

@when('User clicks on Create SCN button')
def step_click_add_user(context):
    user_page = SharedPage(context.driver)
    user_page.Create_new_SCN()
    time.sleep(1)  

@when('Validate Create New SCN page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Verify_Create_New_SCN_Header()
    time.sleep(1)

@when('User enters valid Vessel ID')
def step_impl(context):
    Vessel_ID = 'VESSEL24e971de4a6d464eb2cb8e8f0f9e7623'
    page = SharedPage(context.driver)
    page.enter_scn_Vessel_ID(Vessel_ID)
    time.sleep(1)  # small wait to let the page load

@when('User clicks on GO button')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_GO_button() 

@when('I select Port from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_port()
    time.sleep(1) 

@when('I select Terminals from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_terminal()
    time.sleep(1) 

@when('I define ETA from calendar')
def step_impl(context):
    page = SharedPage(context.driver)
    page.scn_eta_date()

@when('I define ETD from calendar')
def step_impl(context):
    page = SharedPage(context.driver)
    page.scn_etd_date()

@when('I select Purpose of Call from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.scn_purpose_of_call()
    time.sleep(1)

@when('I select Last port of call from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_last_port_of_call()
    time.sleep(1)

@when('I select Next port of call from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_next_port_of_call()
    time.sleep(4)

@when('I choose Outbound Handling as Yes')
def step_click_Out_bound_Yes(context):
    user_page = SharedPage(context.driver)
    user_page.click_Out_bound_Yes()
    time.sleep(1)

@when('I choose Outbound Handling as No')
def step_click_Out_bound_No(context):
    user_page = SharedPage(context.driver)
    user_page.click_Out_bound_No()
    time.sleep(1)

@when('I enter Inbound Voyage')
def step_impl(context):
    Inbound = 'Inbound'
    page = SharedPage(context.driver)
    page.enter_scn_Inbound(Inbound)
    time.sleep(1)  # small wait to let the page load

@when('I enter Outbound Voyage')
def step_impl(context):
    Outbound = 'Outbound'
    page = SharedPage(context.driver)
    page.enter_scn_Outbound(Outbound)
    time.sleep(2)  # small wait to let the page load

@when('I select Entry station from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_entry_custom_station()
    time.sleep(2)

@when('I select Exit station from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_exit_custom_station()
    time.sleep(2)

# @when('I validate GRT')
# @when('I validate NRT')

@when('I enter Remarks')
def step_impl(context):
    Remarks = 'AUTOMATION Remarks'
    page = SharedPage(context.driver)
    page.enter_scn_Remarks(Remarks)
    time.sleep(2)  # small wait to let the page load

@when('I click on SCN SUBMIT button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_scn_submit_button() 
    time.sleep(2)  # small wait to let the page load    

@when('I click on SCN CANCEL button')  
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_scn_cancel_button() 
    time.sleep(2)  # small wait to let the page load

@when('I click on No stay on page button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_scn_stay_on_page_button() 

@when('I click on Yes Cancel button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_scn_yes_cancel_button() 

@when('I click on View button')  

@when('I click on IMOnumber filter')

@when('I click on Approve button') 

@when('I click on Reject button') 

@when('I click on Confirm button') 

# ========================================================================================================
# SCN (END) 
# ========================================================================================================


# ========================================================================================================
# ARRIVAL CLEARANCE (START) 
# ========================================================================================================
@when('Validate Arrival Clearance page header')
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.validate_Arrival_Clearance_Header()

@when('User clicks on Create Arrival Clearance button')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_Create_Arrival_Clearance_button()

@when('Validate Create New Arrival Clearance page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Verify_Create_Arrival_Clearance_Header()
    time.sleep(1)

@when('User clicks on Arrival Clearance GO button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_Arrival_Clearance_GO_button()     

# ========================================================================================================
# ARRIVAL CLEARANCE (END) 
# ========================================================================================================

# ========================================================================================================
# DEPARTURE CLEARANCE (START) 
# ========================================================================================================
@when('Validate Departure Clearance page header')
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.validate_Departure_Clearance_Header()

@when('User clicks on Create Departure Clearance button')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.click_Create_Departure_Clearance_button()

@when('Validate Create New Departure Clearance page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Verify_Create_Departure_Clearance_Header()
    

# ========================================================================================================
# DEPARTURE CLEARANCE (END) 
# ========================================================================================================

# ========================================================================================================
# Vessel Profile (START) 
# ========================================================================================================
@when('I validate Vessel Profile page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Verify_Vessel_Profile_header()
    time.sleep(3)



@when('I validate Create New Vessel Profile page header')
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Create_Vessel_Profile_header()
    time.sleep(3)

@when('I expand Basic Vessel Information toggle')
def step_impl(context):
    context.page.basic_vessel_info_toggle()
    time.sleep(2)

@when('I enter Vessel Name')
def step_impl(context):
    vessel_name = 'Voyager'
    page = SharedPage(context.driver)
    page.enter_vessel_name(vessel_name)
    time.sleep(2)  # small wait to let the page load

@when('I enter duplicate Vessel Name')
def step_impl(context):
    vessel_name = 'Voyager'
    imo_no = 'IMO29'    
    page = SharedPage(context.driver)
    page.enter_dupicate_vessel_name(vessel_name, imo_no)
    time.sleep(2)  # small wait to let the page load

@when('I enter IMO number')
def step_impl(context):
    imo_no = 'IMO29'
    page = SharedPage(context.driver)
    page.enter_profile_imo_number(imo_no) 

@when('I enter Call Sign')
def step_impl(context):
    call_sign = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_call_sign(call_sign) 

@when('I expand Vessel Classification & Type toggle')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.vessel_classification_type_toggle()
    time.sleep(2)

@when('I click on General Type dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_General_type_dropdown()
    time.sleep(4) 

@when('I click on Vessel Type dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_Vessel_type_dropdown()
    time.sleep(4) 

@when('I expand Vessel Specifications toggle')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.vessel_specification_toggle()
    time.sleep(2)

@when('I enter LOA')
def step_impl(context):
    LOA = '1'
    page = SharedPage(context.driver)
    page.enter_LOA_number(LOA) 

@when('I enter LBP')
def step_impl(context):
    LBP = '1'
    page = SharedPage(context.driver)
    page.enter_LBP_number(LBP) 

@when('I enter Draft')
def step_impl(context):
    Draft = '1'
    page = SharedPage(context.driver)
    page.enter_Draft_number(Draft) 

@when('I enter Beam')
def step_impl(context):
    Beam = '1'
    page = SharedPage(context.driver)
    page.enter_Beam_number(Beam) 

@when('I collapse Vessel Specifications toggle')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.vessel_specification_collapse()
    time.sleep(2)    

@when('I click on SUBMIT button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vp_submit_button() 

@when('I click on SAVE button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vp_save_button() 

@when('I click on CANCEL button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vp_cancel_button() 

@when('I click on RESET button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vp_reset_button() 

@when('I search for Vessel in Column filter')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Vessel_Name_Filter(context.vessel_name)

@when('I click on Vessel Profile View button')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vp_view_button_post_search() 

# ========================================================================================================
# Vessel Profile (END) 
# ========================================================================================================



# ========================================================================================================
# Vessel Registration (START) 
# ========================================================================================================


@when('I enter Vessel in the sidebar search field')
def step_enter_sidebar_search(context):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(Locators.search_input))
    search_box.clear()
    search_box.send_keys("Vessel")
    time.sleep(1)  # small wait to let results load  

# ALL Tile
@when('The user clicks on the All button in Registration Requests')
def step_click_all_button(context):
    All_Vessels = SharedPage(context.driver)
    All_Vessels.click_all_button()

@when('The All tab should be active and show records')
def step_verify_all_tab_active(context):
    All_Requests = SharedPage(context.driver)  
    assert All_Requests.is_all_tab_active(), "All tab is not active"
    assert All_Requests.has_records(), "No records found in All tab"

@when('The user notes the number of records in All tab')
def step_count_all_tab_records(context):
    All_Requests = SharedPage(context.driver)
    count = All_Requests.get_row_count()
    print(f"Number of rows in All tab: {count}")
    assert count > 0, "No rows found in All tab"

# DRAFT Tile
@when('The user clicks on the Draft button in Registration Requests')
def step_click_Draft_button(context):
    Draft_Vessels = SharedPage(context.driver)
    Draft_Vessels.click_Draft_button()

@when('The Draft tab should be active and show records')
def step_verify_Draft_tab_active(context):
    Draft_Requests = SharedPage(context.driver)  
    assert Draft_Requests.is_Draft_tab_active(), "Draft tab is not active"
    assert Draft_Requests.has_records(), "No records found in Draft tab"

@when('The user notes the number of records in Draft tab')
def step_count_Draft_tab_records(context):
    Draft_Requests = SharedPage(context.driver)
    count = Draft_Requests.get_row_count()
    print(f"Number of rows in Draft tab: {count}")
    assert count > 0, "No rows found in Draft tab"

# SUBMITTED Tile
@when('The user clicks on the Submitted button in Registration Requests')
def step_click_Submitted_button(context):
    Submitted_Vessels = SharedPage(context.driver)
    Submitted_Vessels.click_Submitted_button()

@when('The Submitted tab should be active and show records')
def step_verify_Submitted_tab_active(context):
    Submitted_Requests = SharedPage(context.driver)  
    assert Submitted_Requests.is_Submitted_tab_active(), "Submitted tab is not active"
    assert Submitted_Requests.has_records(), "No records found in Submitted tab"

@when('The user notes the number of records in Submitted tab')
def step_count_Submitted_tab_records(context):
    Submitted_Requests = SharedPage(context.driver)
    count = Submitted_Requests.get_row_count()
    print(f"Number of rows in Submitted tab: {count}")
    assert count > 0, "No rows found in Submitted tab"

# APPROVED Tile
@when('The user clicks on the Approved button in Registration Requests')
def step_click_Approved_button(context):
    Approved_Vessels = SharedPage(context.driver)
    Approved_Vessels.click_Approved_button()

@when('The Approved tab should be active and show records')
def step_verify_Approved_tab_active(context):
    Approved_Requests = SharedPage(context.driver)  
    assert Approved_Requests.is_Approved_tab_active(), "Approved tab is not active"
    assert Approved_Requests.has_records(), "No records found in Approved tab"

@when('The user notes the number of records in Approved tab')
def step_count_Approved_tab_records(context):
    Approved_Requests = SharedPage(context.driver)
    count = Approved_Requests.get_row_count()
    print(f"Number of rows in Approved tab: {count}")
    assert count > 0, "No rows found in Approved tab"

# CANCELLED Tile
@when('The user clicks on the Cancelled button in Registration Requests')
def step_click_Cancelled_button(context):
    Cancelled_Vessels = SharedPage(context.driver)
    Cancelled_Vessels.click_Cancelled_button()

@when('The Cancelled tab should be active and show records')
def step_verify_Cancelled_tab_active(context):
    Cancelled_Requests = SharedPage(context.driver)  
    assert Cancelled_Requests.is_Cancelled_tab_active(), "Cancelled tab is not active"
    assert Cancelled_Requests.has_records(), "No records found in Cancelled tab"

@when('The user notes the number of records in Cancelled tab')
def step_count_Cancelled_tab_records(context):
    Cancelled_Requests = SharedPage(context.driver)
    count = Cancelled_Requests.get_row_count()
    print(f"Number of rows in Cancelled tab: {count}")
    assert count > 0, "No rows found in Cancelled tab"

@when('The user clicks on the Rejected button in Registration Requests')
def step_click_Rejected_button(context):
    Rejected_Vessels = SharedPage(context.driver)
    Rejected_Vessels.click_Rejected_button()

@when('The Rejected tab should be active and show records')
def step_verify_Rejected_tab_active(context):
    Rejected_Requests = SharedPage(context.driver)  
    assert Rejected_Requests.is_Rejected_tab_active(), "Rejected tab is not active"
    assert Rejected_Requests.has_records(), "No records found in Rejected tab"

@when('The user notes the number of records in Rejected tab')
def step_count_Rejected_tab_records(context):
    Rejected_Requests = SharedPage(context.driver)
    count = Rejected_Requests.get_row_count()
    print(f"Number of rows in Rejected tab: {count}")
    assert count > 0, "No rows found in Rejected tab"

@then('I should see "Vessel Registration" in the results')
def step_impl(context):
    context.page = SharedPage(context.driver)
    element = context.page.is_vessel_registration_visible()
    assert element is not None, "'Vessel Registration' was not found"
    assert element.is_displayed()

@when('I click on Vessel Registration from the search results')
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.click_vessel_registration()

@then("I should be navigated to the Vessel Registration page")
def step_impl(context):
    context.page = SharedPage(context.driver)
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/vessel-registration")
    )
    assert "/vessel-registration" in context.driver.current_url, "Not on Vessel Registration page"

@then('I should see the "Vessel Name" column header')
def step_impl(context):
    page = SharedPage(context.driver)
    assert page.is_vessel_name_column_visible(), '"Vessel Name" column header is not visible'

# @then('I click on the add vessel button')
# def step_impl(context):
#     page = SharedPage(context.driver)
#     page.click_add_vessel_button()
#     time.sleep(10)  # small wait to let the page load

@then('I click on the Submit vessel button')
def step_click_submit(context):
    context.page = SharedPage(context.driver)
    driver = context.driver

    # Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the Submit button to be present
    submit_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(Locators.Vessel_registration_Submit)
    )

    # Scroll element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    try:
        # Try normal click first
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_Submit)
        )
        submit_button.click()
        print("✅ Submit button clicked with normal click")
    except:
        # If intercepted, fallback to JS click
        driver.execute_script("arguments[0].click();", submit_button)
        print("⚡ Submit button clicked with JS click fallback")


@then('I click on the SaveAsDraft vessel button')
def step_click_submit(context):
    context.page = SharedPage(context.driver)
    driver = context.driver

    # Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the Submit button to be present
    SaveAsDraft_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(Locators.Vessel_registration_SaveAsDraft)
    )

    # Scroll element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", SaveAsDraft_button)

    try:
        # Try normal click first
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_SaveAsDraft)
        )
        SaveAsDraft_button.click()
        print("✅ Save As Draft button clicked with normal click")
    except:
        # If intercepted, fallback to JS click
        driver.execute_script("arguments[0].click();", SaveAsDraft_button)
        print("⚡ Save As Draft button clicked with JS click fallback")

@then('I click on the Cancel vessel button')
def step_click_submit(context):
    driver = context.driver

    # Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the Submit button to be present
    Cancel_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(Locators.Vessel_registration_Cancel)
    )

    # Scroll element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", Cancel_button)

    try:
        # Try normal click first
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.Vessel_registration_Cancel)
        )
        Cancel_button.click()
        print("✅ Cancel button clicked with normal click")
    except:
        # If intercepted, fallback to JS click
        driver.execute_script("arguments[0].click();", Cancel_button)
        print("⚡ Cancel button clicked with JS click fallback")        

@then('The user chooses to stay on Register New Vessel page')
def step_stay_on_page(context):
    dialog = SharedPage(context.driver)
    dialog.click_stay_on_page_vessel_Registration()

@then('The user confirms cancel on Register New Vessel page')
def step_click_yes_cancel(context):
    dialog = SharedPage(context.driver)
    dialog.click_yes_cancel_vessel_Registration()
    time.sleep(2)  # small wait to let the page load

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Basic Vessel Information
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

@then('I enter vessel name on Register New Vessel page')
def step_impl(context):
    vessel_name = 'Voyager'
    page = SharedPage(context.driver)
    page.enter_vessel_name(vessel_name)
    time.sleep(2)  # small wait to let the page load

@then('I enter IMO number on Register New Vessel page')
def step_impl(context):
    imo_no = 'IMO12'
    page = SharedPage(context.driver)
    page.enter_imo_number(imo_no)   

@then('I enter Call Sign on Register New Vessel page')
def step_impl(context):
    call_sign = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_call_sign(call_sign)   

@then('I enter Official Number on Register New Vessel page')
def step_impl(context):
    official_number = 'ON'
    page = SharedPage(context.driver)
    page.enter_Official_Number(official_number)     

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Registration and Compliance panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

@then("I click on the Registration and Compliance panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_registration_compliance_panel()

# -------------- -------------- -------------- -------------- -------------- -------------- --------------

@then('I enter Ship Registry Certificate No. on Register New Vessel page')
def step_impl(context):
    Ship_Registry_Certificate_No = '12345'
    page = SharedPage(context.driver)
    page.enter_Ship_Registry_Certificate_No(Ship_Registry_Certificate_No)  

@then(u'I enter Ship Registry Date on Register New Vessel page')
def step_impl(context):
    Ship_Registry_Date = "20-02-2000"
    page = SharedPage(context.driver)
    page.enter_Ship_Registry_Date(Ship_Registry_Date)

@then('I select Vessel Nationality Type on Register New Vessel page')
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_Vessel_Nationality()  

@then('I enter Vessel Flag')  
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_Vessel_Flag("India")
    time.sleep(1)  


@then('I enter Port of registry')  
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_port_of_registry("India")
    time.sleep(1)  

@then('I enter Area of operation')  
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_area_of_operation("International Waters")
    time.sleep(1) 

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Vessel Classification & Type panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

# And I click on the Vessel Classification & Type panel
# -----------------------------------------------------
@then("I click on the Vessel Classification & Type panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_Vessel_Classification_Type_panel()
    time.sleep(1)

@then("I enter General Type")
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_General_Type_station("Cargo")
    time.sleep(1)

@then("I enter Vessel Type")
def step_impl(context):
    page = SharedPage(context.driver)  
    page.select_Vessel_Type_station("Container Ship")
    time.sleep(2)

@then('I enter Sub Type')
def step_impl(context):
    Sub_Type = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Sub_Type(Sub_Type)

# @then('I enter Customs Agent Code')
# def step_impl(context):
#     call_sign = 'AUTO'
#     page = SharedPage(context.driver)
#     page.enter_call_sign(call_sign)

# And I enter Cargo Type
# @then('I enter Cargo Type')
# def step_impl(context):
#     call_sign = 'AUTO'
#     page = SharedPage(context.driver)
#     page.enter_call_sign(call_sign)

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Vessel Specifications panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

# And I click on the Vessel Specifications panel
# ----------------------------------------------
@then("I click on the Vessel Specifications panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_Vessel_Specifications_panel()

@then('I enter Year Built')
def step_impl(context):
    year_built = '2020'
    page = SharedPage(context.driver)
    page.enter_year_built(year_built)

@then('I enter Built Place')
def step_impl(context):
    Built_Place = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Built_Place(Built_Place)

@then('I enter Vessel With Gear')
def step_impl(context):
    vessel_gear = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Vessel_With_Gear(vessel_gear)

@when("I enter Type of Hull")
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_Type_of_Hull()
    time.sleep(2)

@when("I enter Position of Bridge")
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_Position_of_Bridge()
    time.sleep(2)

@then('I enter LOA (Length Overall)')
def step_impl(context):
    Length_Overall = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Length_Overall(Length_Overall)

@then('I enter Depth')
def step_impl(context):
    Depth = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Depth(Depth)

@then('I enter Draft')
def step_impl(context):
    Draft = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Draft(Draft)

@then('I enter Freeboard')
def step_impl(context):
    Freeboard = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Freeboard(Freeboard)

@then('I enter LBP (Length Between Perpendiculars)')
def step_impl(context):
    LBP = '10'
    page = SharedPage(context.driver)
    page.enter_LBP_number(LBP)

@then('I enter Beam')
def step_impl(context):
    Beam = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Beam(Beam)

@then('I enter Displacement, numeric only,')
def step_impl(context):
    Displacement = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Displacement(Displacement)

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Tonnage & Capacity panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

# And I click on the Tonnage & Capacity panel
# -------------------------------------------
@then("I click on the Tonnage & Capacity panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_Tonnage_Capacity_panel()

@then('I enter Gross Tonnage')
def step_impl(context):
    Gross_Tonnage = '1000'
    page = SharedPage(context.driver)
    page.enter_Gross_Tonnage(Gross_Tonnage)
 
@then('I enter Net Tonnage')
def step_impl(context):
    Net_Tonnage = '1000'
    page = SharedPage(context.driver)
    page.enter_Net_Tonnage(Net_Tonnage)

@then('I enter Deadweight Tonnage')
def step_impl(context):
    Deadweight_Tonnage = '1000'
    page = SharedPage(context.driver)
    page.enter_Deadweight_Tonnage(Deadweight_Tonnage)

@then('I enter Crew Capacity')
def step_impl(context):
    Crew_Capacity = '1000'
    page = SharedPage(context.driver)
    page.enter_Crew_Capacity(Crew_Capacity)

@then('I enter Passenger Capacity')
def step_impl(context):
    Passenger_Capacity = '1000'
    page = SharedPage(context.driver)
    page.enter_Passenger_Capacity(Passenger_Capacity)

@then('I enter TEU Capacity')
def step_impl(context):
    TEU_Capacity = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_TEU_Capacity(TEU_Capacity)

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Ownership & Management panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

# And I click on the Ownership & Management panel
# -----------------------------------------------
@then("I click on the Ownership & Management panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_Ownership_Management_panel()

@then('I enter Owner Name')
def step_impl(context):
    owner_name = 'SHIP OWNER '
    page = SharedPage(context.driver)
    page.enter_owner_name(owner_name)

@then('I enter Owner Email')
def step_impl(context):
    email = 'automation.script@hotmail.com'
    page = SharedPage(context.driver)
    page.enter_owner_email(email)

@then('I enter Owner Mobile No')
def step_impl(context):
    mobile_no = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_owner_mobile_no(mobile_no)

@then('I enter Owner Code')
def step_impl(context):
    owner_code = 'AUTO_OWNER'
    page = SharedPage(context.driver)
    page.enter_owner_code(owner_code)

@then('I enter Shipping Line Name')
def step_impl(context):
    Shipping_Line_Name = 'AUTO'
    page = SharedPage(context.driver)
    page.enter_Shipping_Line_Name(Shipping_Line_Name)

@then('I enter Owner Address Line 1')
def step_impl(context):
    Address_Line_1 = 'Address Line 1'
    page = SharedPage(context.driver)
    page.enter_owner_Address_Line_1s(Address_Line_1)

@then('I enter Owner Address Line 2')
def step_impl(context):
    Address_Line_2 = 'Address Line 2'
    page = SharedPage(context.driver)
    page.enter_owner_Address_Line_2(Address_Line_2)

@then('I enter Owner Address Line 3')
def step_impl(context):
    Address_Line_3 = 'Address Line 3'
    page = SharedPage(context.driver)
    page.enter_owner_Address_Line_3(Address_Line_3)

@when("I enter Owner City")
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_owner_City()
    time.sleep(2)

@when('I select Ownership & Management Entry station from dropdown')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_scn_entry_custom_station()
    time.sleep(2)

@then('I enter Owner Street')
def step_impl(context):
    Street = 'Automation Street'
    page = SharedPage(context.driver)
    page.enter_owner_Street(Street)

@when("I enter Owner State")
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_owner_State()
    time.sleep(2)

@when('I enter Owner Country')
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_owner_Country()
    time.sleep(2)

@then('I enter Owner Postcode')
def step_impl(context):
    PostCode = '400601'
    page = SharedPage(context.driver)
    page.enter_owner_post_code(PostCode)

# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Shipping & Operations panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

# And I click on the Shipping & Operations panel
# ----------------------------------------------
@then("I click on the Shipping & Operations panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_Shipping_Operators_panel()

@then('I enter Shipping Agent Code')
def step_impl(context):
    Shipping_Agent_Code = '007'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Code(Shipping_Agent_Code)

@then('I enter Shipping Agent Name')
def step_impl(context):
    Shipping_Agent_Name = 'James Bond'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Name(Shipping_Agent_Name)

@then('I enter Shipping Agent Email')
def step_impl(context):
    Email = 'automation.script@gmail.com'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Email(Email)

@then('I enter Mobile No')
def step_impl(context):
    Mobile_No = '7007007007'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Mobile_No(Mobile_No)

@then('I enter Charterer Details')
def step_impl(context):
    charter_details = 'CD123'
    page = SharedPage(context.driver)
    page.enter_Charterer_Details(charter_details)

@then('I enter Shipping Agent Address Line 1')
def step_impl(context):
    Address_Line_1 = 'Address Line 1'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Address_Line_1(Address_Line_1)

@then('I enter Shipping Agent Address Line 2')
def step_impl(context):
    Address_Line_2 = 'Address Line 2'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Address_Line_2(Address_Line_2)

@then('I enter Shipping Agent Address Line 3')
def step_impl(context):
    Address_Line_3 = 'Address Line 3'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Address_Line_3(Address_Line_3)

@when("I enter Shipping Agent City")
def step_impl(context):
    page = SharedPage(context.driver)
    page.select_Shipping_Agent_City()
    time.sleep(2)

@then('I enter Shipping Agent Street')
def step_impl(context):
    Street = 'Automation Street'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Street(Street)
    
@when("I enter Shipping Agent State")
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_State()
    time.sleep(2)

@when('I enter Shipping Agent Country')
def step_impl(context):
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Country()
    time.sleep(2)

@then('I enter Shipping Agent Postcode')
def step_impl(context):
    PostCode = '400601'
    page = SharedPage(context.driver)
    page.enter_Shipping_Agent_Postcode(PostCode)
    
# -------------- -------------- -------------- -------------- -------------- -------------- --------------
# Documents panel
# -------------- -------------- -------------- -------------- -------------- -------------- --------------

# And I click on the Documents panel
# ----------------------------------
@then("I click on the Documents panel")
def step_impl(context):
    page = SharedPage(context.driver)
    context.page.step_click_Documents_panel()

# And I enter Ship Registry Certificate
# And I enter Tonnage Certificate
# And I enter Load Line Certificate
# And I enter Class Certificate
# And I enter Owner/Charterer Authorization Letter

@when("NEW Shipping Agent clicks on Create New button in Vessel Registration")
def step_impl(context):
    context.page = SharedPage(context.driver)
    context.page.Register_new_vessel() 

@when("Register New Vessel page should be displayed")
def step_impl(context):
    context.page = SharedPage(context.driver)
    assert context.page.is_Register_New_Vessel_displayed()

# @when('I click on Register New Vessel button')
# def step_click_add_user(context):
#     user_page = SharedPage(context.driver)
#     user_page.Register_new_vessel()
#     time.sleep(10)      

# ========================================================================================================
# Vessel Registration (END) 
# ========================================================================================================

  
# ==========================================================================================================================

@then('I should see "{expected_result}"')
def step_verify_login(context, expected_result):
    wait = WebDriverWait(context.driver, 10)

    locator_map = {
        'dashboard': (By.XPATH, "//*[contains(text(),'Dashboard') and self::h1]"),
        'error_invalid_password': (By.XPATH, "//div[contains(text(),'Invalid Username or Password')]"),
        'error_invalid_username': (By.XPATH, "//div[contains(text(),'Invalid Username or Password')]"),
        'error_invalid_credentials': (By.XPATH, "//div[contains(text(),'Invalid Username or Password')]"),
        'error_username_required': (By.XPATH, "//div[contains(text(),'Username or Email is required')]"),
        'error_password_required': (By.XPATH, "//div[contains(text(),'Password is required')]"),
        'error_both_required': (By.XPATH, "//div[contains(text(),'Username and Password are required')]"),
    }

    if expected_result not in locator_map:
        raise ValueError(f"Unknown expected_result: {expected_result}")

    locator = locator_map[expected_result]

    try:
        element = wait.until(EC.visibility_of_element_located(locator))
        assert element.is_displayed(), f"{expected_result} not shown"
    except TimeoutException:
        context.driver.save_screenshot(f"screenshots/{expected_result}_fail.png")
        raise AssertionError(f"{expected_result} not shown within timeout — screenshot saved.")

# ========================================================================================================


#============================================================================================================================    
#       STAKEHOLDER MANAGEMENT (START)
#============================================================================================================================     
@when("I should see the Stakeholder Management header")
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.verify_stakeholder_management_header()

@when("I click on Create Stakeholder")
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.Create_new_Stakeholder()

@when("I should see the Create Stakeholder Management header")
def step_impl(context):
    shared_page = SharedPage(context.driver)
    shared_page.create_stakeholder_management_header()

@when("I choose Stakeholder Master Type")
def step_impl(context):
    page = SharedPage(context.driver)
    page.click_stakeholder_master_type()
    time.sleep(2) 


# @when("I choose unique Stakeholder Code")
# def step_impl(context):
#     Stakeholder_Code = 'AUTO'
#     page = SharedPage(context.driver)
#     page.unique_Stakeholder_Code(Stakeholder_Code) 

@when("I choose unique Stakeholder Code")
def step_impl(context):
    stakeholder_code = context.page.unique_Stakeholder_Code("AUTO")
    context.Stakeholder_Code = stakeholder_code   # ✅ save in Behave context

# @when("I enter unique Stakeholder Name")
# def step_impl(context):
#     stakeholder_name = context.page.enter_Stakeholder_Name("AUTO")
#     context.Stakeholder_Name = stakeholder_name   # ✅ save into behave context

@when("I enter unique Stakeholder Name")
def step_impl(context):
    stakeholder_name = context.page.enter_Stakeholder_Name("AUTO")
    context.Stakeholder_Name = stakeholder_name   # ✅ save in Behave context    

@when("I make Stakeholder Active")
def step_impl(context):
    context.page.click_stakeholder_active_button()   


@when('I click on Stakeholder SAVE button')
def step_impl(context):
    context.page.click_stakeholder_SAVE_button() 


@when('I click on Stakeholder CANCEL button')  
def step_impl(context):
    context.page.click_stakeholder_CANCEL_button()


@when("I click on Stakeholder Name View button inside table")
def step_impl(context):
    context.page.stakeholder_Name_Filter(context.Stakeholder_Name)

@when("I click on Edit Stakeholder button inside table")
def step_impl(context):
    context.page.stakeholder_Edit()

@when('I click on Update button')  
def step_impl(context):
    context.page.click_stakeholder_UPDATE_button()

# @when("I search Stakeholder by Code")
# def step_impl(context):
#     context.page.Search_Stakeholder_By_Code(context.Stakeholder_Code)


#============================================================================================================================    
#       STAKEHOLDER MANAGEMENT (END) 
#============================================================================================================================     




#============================================================================================================================    
#       REGISTER STAKEHOLDER (START)
#============================================================================================================================ 

# @when('I click on New Registration')
# def step_click_new_registration(context):
#     context.register_page = RegisterPage(context.driver)
#     context.register_page.click_new_registration()

# @when('I select Stakeholder Type')
# def step_select_stakeholder_type(context):
#     context.register_page.select_stakeholder_type()

# @when('I check Templates dropdown')
# def step_check_templates_dropdown(context):
#     context.register_page.verify_templates_dropdown()

# @when('I enter Organization Name')
# def step_enter_organization_name(context):
#     context.register_page.enter_organization_name("Test Org")

# @when('I enter Business Email ID')
# def step_enter_business_email(context):
#     context.register_page.enter_business_email("org@example.com")

# @when('I enter Phone No')
# def step_enter_phone(context):
#     context.register_page.enter_phone("9876543210")

# @when('I enter Terminal Code')
# def step_enter_terminal_code(context):
#     context.register_page.enter_terminal_code("TC1234")

# @when('I enter Address Line 1')
# def step_enter_address1(context):
#     context.register_page.enter_address1("Line 1")

# @when('I enter Address Line 2')
# def step_enter_address2(context):
#     context.register_page.enter_address2("Line 2")

# @when('I enter Address Line 3')
# def step_enter_address3(context):
#     context.register_page.enter_address3("Line 3")

# @when('I enter City')
# def step_enter_city(context):
#     context.register_page.enter_city("Mumbai")

# @when('I enter Postcode')
# def step_enter_postcode(context):
#     context.register_page.enter_postcode("400001")

# @when('I enter State')
# def step_enter_state(context):
#     context.register_page.enter_state("Maharashtra")

# @when('I enter Country')
# def step_enter_country(context):
#     context.register_page.enter_country("India")

# @when('I enter First Name')
# def step_enter_first_name(context):
#     context.register_page.enter_first_name("John")

# @when('I enter Last Name')
# def step_enter_last_name(context):
#     context.register_page.enter_last_name("Doe")

# @when('I enter Designation')
# def step_enter_designation(context):
#     context.register_page.enter_designation("Manager")

# @when('I enter Username')
# def step_enter_username(context):
#     context.register_page.enter_username("john.doe")

# @when('I enter Email')
# def step_enter_email(context):
#     context.register_page.enter_email("john.doe@example.com")

# @when('I upload Letter of Authorization')
# def step_upload_authorization_letter(context):
#     context.register_page.upload_authorization_letter("path/to/letter.pdf")

# @when('I upload ID Card')
# def step_upload_id_card(context):
#     context.register_page.upload_id_card("path/to/idcard.jpg")

# @when('I upload Passport')
# def step_upload_passport(context):
#     context.register_page.upload_passport("path/to/passport.jpg")

# @when('I click on Preview button')
# def step_click_preview(context):
#     context.register_page.click_preview()

# @when('I check Terms and Conditions checkbox')
# def step_check_terms(context):
#     context.register_page.check_terms_and_conditions()

# @when('I click on Submit button')
# def step_click_submit(context):
#     context.register_page.click_submit()

# @when('I click on Back to Login')
# def step_back_to_login(context):
#     context.register_page.click_back_to_login()


# @when('I click on Registration Requests')
# def step_click_registration_requests(context):
#     context.dashboard_page.click_registration_requests()

# @when('I click on Pending tile')
# def step_click_pending_tile(context):
#     context.dashboard_page.click_pending_tile()

# @when('I click on 1st entry view button')
# def step_click_first_entry(context):
#     context.dashboard_page.click_first_view_button()

# @when('I verify Username Details')
# def step_verify_user_details(context):
#     context.dashboard_page.verify_username_details()

# @when('I click on Approve button')
# def step_click_approve(context):
#     context.dashboard_page.click_approve_button()

# @when('I enter Remarks')
# def step_enter_remarks(context):
#     context.dashboard_page.enter_remarks("Approved.")

# @when('I click on Confirm button')
# def step_click_confirm(context):
#     context.dashboard_page.click_confirm_button()

# @when('I check for request approved message')
# def step_check_approval_message(context):
#     assert context.dashboard_page.is_approval_message_displayed()

# # @then('I click on Logout button')
# # def step_click_logout(context):
# #     context.dashboard_page.click_logout()

# @when('I enter Username credentials')
# def step_enter_registered_user_credentials(context):
#     context.login_page.enter_credentials("john.doe", "password123")


# # =====================================================================================
# # Excel Sheet  (START)
# # =====================================================================================



# @when('I load registration data from Excel')
# def step_load_data(context):
#     context.test_data = read_excel_data("TestData/RegisterUser.xlsx", "UserData")[0]
#     # for row in read_excel_data("TestData/RegisterUser.xlsx", "UserData"):
#     # Pass to Behave context and call test flow



@when('I load registration data from Excel')
def step_impl(context):
    file_path = r"D:\Harshad\PCS\UI Automation\ICP\TestData\PCS\RegisterUser.xlsx"
    sheet_name = "Sheet1"

    all_data = excel.get_all_login_data(file_path, sheet_name) 

@when('I enter Organization Name from excel')
def step_org_name(context):
    context.register_page.enter_organization_name(context.current_data['org_name'])

@when('I enter Business Email ID from excel')
def step_email(context):
    context.register_page.enter_business_email(context.current_data['business_email'])

@when('I enter Phone No from excel')
def step_phone(context):
    context.register_page.enter_phone(context.current_data['phone'])

@when('I enter Terminal Code from excel')
def step_terminal(context):
    context.register_page.enter_terminal_code(context.current_data['terminal_code'])

@when('I enter Address Line 1 from excel')
def step_address(context):
    context.register_page.enter_address1(context.current_data['address1'])

@when('I enter Username from excel')
def step_username(context):
    context.register_page.enter_username(context.current_data['username'])

@when('I enter Email from excel')
def step_user_email(context):
    context.register_page.enter_email(context.current_data['email'])


# =====================================================================================
# Excel Sheet  (END)
# =====================================================================================


#============================================================================================================================    
#       REGISTER STAKEHOLDER (END)
#============================================================================================================================ 


# ========================================================================================================
# LOGOUT (START) 
# ========================================================================================================
@then("I should see the Logout option")
def step_impl(context):
    logout_button = context.page.is_logout_visible()
    time.sleep(2)
    logout_button.click()

@then("I click on Logout button")
def step_impl(context):
    logout = context.page.is_logout_visible()
    assert logout is not None, "Logout button was not found on the page."
    time.sleep(2)
    logout.click()

@when("I click to Logout from application")
def step_impl(context):
    logout = context.page.is_logout_visible()
    assert logout is not None, "Logout button was not found on the page."
    logout.click()    

@then("I should see the SIGNIN option")
def step_impl(context):
    signin_button = context.page.is_signIn_visible()
    assert signin_button is not None, "SIGNIN button was not visible after logout"
    assert signin_button.is_displayed()
# ========================================================================================================
# LOGOUT (END) 
# ========================================================================================================
