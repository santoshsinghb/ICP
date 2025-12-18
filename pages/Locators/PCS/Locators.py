from selenium.webdriver.common.by import By

class Locators:

        # ========================================================================================================
        # Login page  (START) 
        # ========================================================================================================        
        ICP_username_input = (By.XPATH, "//input[@id='username']")        
        ICP_password_input = (By.XPATH, "//input[@id='password']")
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
        avatar_button = (By.XPATH, "//img[@aria-label='Avatar']")
        dashboard_expand_bar = (By.XPATH, "//aside[contains(@class, 'app-sidebar')]")
        dashboard_header = (By.XPATH, "//*[contains(text(),'Dashboard') and self::h1]")
        LCCT_dashboard_header = (By.XPATH, "//h2[@class='text pb-2']")
        welcome_message = (By.XPATH, "//h3[contains(normalize-space(.),'Welcome')]")
        user_name = (By.XPATH, "//h3[contains(normalize-space(.),'Welcome')]/span")
        Login_message = (By.XPATH, "//span[@class='text-capitalize']")
        dashboard_date = (By.XPATH, "//button[contains(@class, 'klui-feature-icon')]//span[contains(text(), 'DD/MM/YYYY')]")
        text_size = (By.XPATH, "//button[contains(@class, 'klui-feature-icon')]//i[contains(@class, 'fa-text-size')]")
        select_theme = (By.XPATH, "//button[contains(@class, 'test-debug') and contains(@title, 'toggle the theme')]")
        language_selector = (By.XPATH, "//button[.//i[contains(@class, 'fa-globe-asia')]]")
        sidebar_button = (By.XPATH, "//button[@aria-label='Toggle Sidebar' and contains(@class, 'sidebar-pinner')]")
        CommunityAdminLabel = (By.XPATH, "//div[@class='sidebar-user-data']//small[contains(translate(text(), ' ', ''), 'CommunityAdmin')]")
        ICP_search_input = (By.XPATH, "//input[@id='sidebar-search']")  # ← Search locator
        LCCT_sidebar_toggle = (By.XPATH, "//div[contains(@class,'sidebar-toggler-box')]")
        LCCT_1Y = (By.XPATH, "//label[@for='period_Type_id3']")
        # ========================================================================================================
        # Dashboard page  (END) 
        # ========================================================================================================
        







        # ========================================================================================================
        # Community Admin  (START) 
        # ========================================================================================================
        # Template_Management_toggle = (By.XPATH, "//input[@placeholder='Search...' and contains(@class, 'klui-adv-sidebar-search-input')]")
        Template_Management_toggle = (By.XPATH, "//span[text()='Template Management']/ancestor::button//i[contains(@class, 'fa-chevron-down')]")
        Workflow_Configuration_toggle = (By.XPATH, "//button[contains(@class,'sidebar-submenu-btn') and .//span[text()='Workflow Configuration']]")
        Organization_Setup_Header = (By.XPATH, "//button[@type='button' and @aria-label='Toggle submenu for Organization Setup']")
        Vessel_Management_toggle = (By.XPATH, "//button[.//span[text()='Vessel Management']]")

        Dashboard = (By.XPATH, "//button[@type='button' and @aria-label='Go to Dashboard']")
        Registration_Template = (By.XPATH, "//span[normalize-space()='Registration Template']")
        # Transaction_Template = (By.CSS_SELECTOR, "button[aria-label='Go to menu.lbl_transaction_template'] span")
        Transaction_Template = (By.XPATH, "//span[normalize-space()='Transaction Template']")
        Registration_Requests = (By.CSS_SELECTOR, "button[aria-label='Go to Registration Requests'] span")
        Organization_Information = (By.XPATH, "//button[@type='button' and @aria-label='Go to Organization Information']")
        Branch = (By.XPATH, "//button[@type='button' and @aria-label='Go to Branch']")
        User = (By.XPATH, "//button[@type='button' and @aria-label='Go to User']")
        Registration_Approval_Workflow = (By.XPATH, "//button[@aria-label='Go to Registration Approval Workflow']//span[normalize-space()='Registration Approval Workflow']")
        Transaction_Approval_Workflow = (By.XPATH, "//button[.//span[text()='Transaction Approval Workflow']]")
        EPAN = (By.XPATH, "//span[normalize-space()='Pre-Arrival Notification']")
        SCN = (By.XPATH, "//button[.//span[text()='Ship Call Number']]") 
        Vessel_Profile = (By.XPATH, "//button[@type='button' and @aria-label='Go to Vessel Profile']")
        # Vessel_Registration = (By.XPATH, "//button[@type='button' and @aria-label='Go to Vessel Registration']")
        Vessel_Registration = (By.XPATH, "//button[@class='sidebar-btn' and @aria-label='Go to Vessel Registration']//span[normalize-space(text())='Vessel Registration']")
        ship_call_number = (By.XPATH, "//span[normalize-space()='Ship Call Number']")
        pre_arrival_notification = (By.XPATH, "//span[normalize-space()='Pre-Arrival Notification']")
        arrival_clearance = (By.XPATH, "//span[normalize-space()='Arrival Clearance']")
        departure_clearance = (By.XPATH, "//span[normalize-space()='Departure Clearance']")
        Stakeholder_Management = (By.CSS_SELECTOR, "button[aria-label='Go to Stakeholder Management'] span")
        Terminal_Configuration = (By.XPATH, "//span[normalize-space()='Terminal Configuration']")
        # ========================================================================================================
        # Community Admin  (END) 
        # ========================================================================================================




        # ========================================================================================================
        # REGISTRATION TEMPLATE (START) 
        # ========================================================================================================
        Registration_Template_Header = (By.XPATH, "//h1[normalize-space()='Registration Template']")
        Loading_Spinner = (By.XPATH, "//div[@class='loading-spinner']")
        Create_New_Registration_Template = (By.XPATH, "//button[contains(@class,'btn klui-btn-circle-plus primary float-bottom-right')]")
        Choose_Shipping_Agent = (By.XPATH, "//button[contains(@class, 'template-builder-step-btn')]//span[text()='Shipping Agent']")
        Click_Next = (By.XPATH, "//button[contains(text(), 'Next')]")
        User_Registration_Type = (By.XPATH, "//button[contains(@class, 'template-builder-step-btn')]//span[normalize-space(text())='User']")
        Registration_Next = (By.XPATH, "//button[normalize-space(text())='Next']")
        Label_Create_New_Template = (By.XPATH, "//div[contains(@class, 'page-title')]//h1[normalize-space()='Create New Template']")
        Template_Name_Input = (By.XPATH, "//input[@placeholder='Enter Template Name']")
        Template_Description_Input = (By.XPATH, "//input[@placeholder='Enter Template Description']")
        SAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'btn') and normalize-space()='Save']")
        PREVIEW_BUTTON = (By.XPATH, "//button[normalize-space()='Preview Template']")
        GO_BACK_TO_EDIT = (By.XPATH, "(//button[.//i[contains(@class, 'fa-edit')]])[1]")
        CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
        YES_CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Yes, Cancel']")
        NO_DONT_CANCEL = (By.XPATH, "//button[normalize-space()=\"No, Don't Cancel\"]")
        Template_Name_Column_Filter = (By.XPATH, "//div[@col-id='name']//span[@class='ag-icon ag-icon-filter']")
        Add_filter_value = (By.XPATH, "//input[@placeholder='Filter...' and contains(@class, 'ag-text-field-input')]")
        Edit_Post_Search = (By.XPATH,"(//i[contains(@class, 'fa-edit')]/ancestor::button)[1]")
        # ========================================================================================================
        # REGISTRATION TEMPLATE (END) 
        # ========================================================================================================



        # ========================================================================================================
        # TRANSACTION TEMPLATE (START) 
        # ========================================================================================================
        Transaction_Template_Header = (By.XPATH, "//h1[normalize-space()='Transaction Template']")
        Create_New_Transaction_Template = (By.XPATH, "//button[@class='btn klui-btn-circle-plus primary float-bottom-right']")
        Select_Vessel_Management = (By.XPATH, "//button[@class='template-builder-step-btn']//span[contains(text(),'Vessel Management')]")
        Next_Registration_Type = (By.XPATH, "//button[normalize-space()='Next']")
        select_registration_type = (By.XPATH,"//button[@class='template-builder-step-btn']//span[contains(text(),'Vessel Registration')]")
        Transaction_Back_to_Edit = (By.XPATH, "(//button[.//i[contains(@class, 'fa-edit')] ])[1]")
        # ========================================================================================================
        # TRANSACTION TEMPLATE (END) 
        # ========================================================================================================  


        # ========================================================================================================
        # REGISTRATION REQUESTS (START) 
        # ========================================================================================================
        Registration_Request_Header = (By.XPATH, "//h1[normalize-space()='Stakeholder Registration Request List']")
        Registration_Request_All = (By.XPATH, "//button[.//small[normalize-space()='All']]")
        Registration_Request_Pending = (By.XPATH, "//button[.//small[normalize-space()='Pending']]")
        Registration_Request_Approved = (By.XPATH, "//button[.//small[normalize-space()='Approved']]")
        Registration_Request_Rejected = (By.XPATH, "//button[.//small[normalize-space()='Rejected']]")
        Registration_Request_horizontal_bar = (By.XPATH, "//div[contains(@class,'ag-body-horizontal-scroll-viewport')]")
        Registration_Request_Approval_Status_Cells = (By.XPATH, "//div[@col-id='approvalStatus']")
        # ========================================================================================================
        # REGISTRATION REQUESTS (END) 
        # ========================================================================================================        


        # ========================================================================================================
        # ORGANIZATION INFORMATION (START) 
        # ========================================================================================================
        View_Organization_Information = (By.XPATH, "//h1[normalize-space()='View Organization Information']")
        Stakeholder_Type = (By.XPATH, "//strong[normalize-space()='Stakeholder Type']")
        Organisation_Details = (By.XPATH, "//strong[normalize-space()='Organisation Details']")
        Address_Details = (By.XPATH, "//strong[normalize-space()='Address Details']")
        Contact_Details = (By.XPATH, "//strong[normalize-space()='Contact Details']")
        Username_Details = (By.XPATH, "//strong[@class='fs-16 fw-400']")        

        # ========================================================================================================
        # ORGANIZATION INFORMATION (END) 
        # ========================================================================================================



        # ========================================================================================================
        # BRANCH (START) 
        # ========================================================================================================
        Branch_Management_Header = (By.XPATH, "//h1[normalize-space()='Branch Management']")
        Branch_Name_Column_Filter = (By.XPATH, "//div[@col-id='name']//span[@class='ag-icon ag-icon-filter']")
        Branch_Name_filter_value = (By.XPATH, "//input[@placeholder='Filter...' and contains(@class, 'ag-text-field-input')]")
        Branch_Name_View = (By.XPATH,"(//button[@aria-label='View Details'])[1]")
        Branch_Name_Edit = (By.XPATH,"(//i[contains(@class, 'fa-edit')]/ancestor::button)[1]")
        View_Branch_Header = (By.XPATH, "//h1[normalize-space()='View Branch']")
        View_Branch_Username = (By.XPATH, "//strong[normalize-space()='User9199']") 
        Create_Branch_Button = (By.XPATH, "//button[@class='btn klui-btn-circle-plus primary float-bottom-right']") 

        # Notification Details
        # ---------------------
        Branch_Name = (By.XPATH, "//input[@name='data[branch][name]']") 
        Branch_Email_ID = (By.XPATH, "//input[@name='data[branch][email]']") 
        Branch_Phone_No = (By.XPATH, "//input[@name='data[branch][phoneNumber]']") 

        # Address Details
        # ----------------
        Branch_Address_Line_1 = (By.XPATH, "//input[@name='data[branch][addressLine1]']") 
        Branch_Address_Line_2 = (By.XPATH, "//input[@name='data[branch][addressLine2]']") 
        Branch_Address_Line_3 = (By.XPATH, "//input[@name='data[branch][addressLine3]']") 
        Branch_City = (By.XPATH, "//label[contains(normalize-space(),'City')]/following::div[contains(@class,'form-control ui fluid selection dropdown')][1]") 
        Branch_City_select = (By.XPATH, "(//span[contains (text(),'Mumbai')])")
        Branch_Postcode = (By.XPATH, "//input[@name='data[branch][postcode]']") 
        Branch_State = (By.XPATH, "//label[contains(normalize-space(),'City')]/following::div[contains(@class,'form-control ui fluid selection dropdown')][2]") 
        Branch_State_select = (By.XPATH, "(//span[contains (text(),'Maharashtra')])")
        Branch_Country = (By.XPATH, "//label[contains(normalize-space(),'City')]/following::div[contains(@class,'form-control ui fluid selection dropdown')][3]") 
        Branch_Country_select = (By.XPATH, "(//span[contains (text(),'India')])")

        # Branch Admin
        # ------------
        Branch_Admin_First_Name = (By.XPATH, "//input[@name='data[admin][firstName]']") 
        Branch_Admin_Middle_Name = (By.XPATH, "//input[@name='data[admin][middleName]']") 
        Branch_Admin_Last_Name = (By.XPATH, "//input[@name='data[admin][lastName]']") 
        Branch_Admin_Designation = (By.XPATH, "//input[@name='data[admin][designation]']") 
        Branch_Admin_Email_ID = (By.XPATH, "//input[@name='data[admin][email]']") 
        Branch_Admin_Phone_No = (By.XPATH, "//input[@name='data[admin][phoneNumber]']") 
        Branch_Admin_Username = (By.XPATH, "//input[@name='data[admin][userName]']") 

        Branch_SAVE = (By.XPATH, "//button[normalize-space()='Save']")  
        Branch_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']") 


        # ========================================================================================================
        # BRANCH (END) 
        # ========================================================================================================



        # ========================================================================================================
        # USER (START) 
        # ========================================================================================================
        User_management_page_heading = (By.XPATH, "//h1[normalize-space(text())='User Management']")
        create_new_user = (By.XPATH, "//button[contains(@class,'klui-btn-circle-plus')]")
        User_Type_Dropdown = (By.XPATH, "//label[contains(normalize-space(),'User Type')]/following::div[contains(@class,'dropdown')][1]")
        User_select = (By.XPATH, "(//span[contains (text(),'User')])[2]")
        User_Branch_Dropdown = (By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/section[1]/div[1]/div[1]/app-create[1]/div[1]/div[2]/div[1]/lib-formio[1]/formio[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]")
        Branch_select = (By.XPATH, "(//div[contains(@class, 'choices__list') and contains(@class, 'dropdown')])[2]//div[contains(@class, 'choices__item')][1]")
        User_First_Name = (By.XPATH, "//input[@name='data[firstName]']")
        User_Middle_Name = (By.XPATH, "//input[@name='data[middleName]']")
        User_Last_Name = (By.XPATH, "//input[@name='data[lastName]']")
        User_Designation = (By.XPATH, "//input[@name='data[designation]']")
        User_Phone_No = (By.XPATH, "//input[@name='data[phoneNumber]']")
        User_Email = (By.XPATH, "//input[@name='data[email]']")
        User_UserName = (By.XPATH, "//label[normalize-space(text())='Username']/following::input[1]")
        User_SAVE_button = (By.XPATH, "//button[normalize-space()='Save']")
        User_CANCEL_button = (By.XPATH, "//button[normalize-space()='Cancel']")
        

        # For the dropdown option (dynamic, param-based locator)
        def user_type_option(user_type):
                return (By.XPATH, f"//div[contains(@class,'choices__list')]//div[text()='{user_type}']")

        # ========================================================================================================
        # USER (END) 
        # ========================================================================================================








        # ========================================================================================================
        # REGISTRATION APPROVAL WORKFLOW (START) 
        # ========================================================================================================
        Registration_Approval_Workflow_Management_header = (By.XPATH, "//h1[normalize-space()='Registration Approval Workflow Management']")
        Create_Registration_Approval_Workflow = (By.XPATH, "//button[contains(@class, 'klui-btn-circle-plus') and contains(@class, 'float-bottom-right')]")
        initiatorType = (By.XPATH, "//select[@id='initiatorType' and @formcontrolname='initiatorType']")
        Workflow_Name = (By.XPATH, "//input[@id='name' and @placeholder='Workflow Name' and @formcontrolname='name']")
        Workflow_Description = (By.XPATH, "//input[@id='description' and @formcontrolname='description' and @placeholder='Workflow Description']")
        # Customs_tile = (By.XPATH, "//div[@id='stakeholders-list']//strong[normalize-space(text())='Customs']")
        Customs_tile = (By.XPATH, "//div[contains(@class,'cdk-drag drag-from-list')][1]")
        STAGE_1 = (By.XPATH, "//button[.//span[normalize-space(text())='Open Settings']]")
        Drag = (By.XPATH, "//div[contains(@class,'drop-area') and contains(@class,'graph-bg')]")
        ADD_STAGE_BUTTON = (By.XPATH, "//button[normalize-space()='Add Stage']")
        RAW_SAVE = (By.XPATH, "//button[@type='submit']")
        RAW_SAVE_Error = (By.XPATH, "//p[@class='px-2 flex-grow-1']")
        # ========================================================================================================
        # REGISTRATION APPROVAL WORKFLOW (END) 
        # ========================================================================================================


        # ========================================================================================================
        # TRANSACTION APPROVAL WORKFLOW (START) 
        # ========================================================================================================
        Transaction_Workflow_Header = (By.XPATH, "//h1[normalize-space()='Transaction Workflow']")
        Create_Transaction_Approval_Workflow = (By.XPATH, "//i[@class='fal fa-plus']")
        Choose_Vessel_Management = (By.XPATH, "//button[contains(@class, 'template-builder-step-btn')]//span[text()='Vessel Management']")
        Module_Type_Next = (By.XPATH, "//button[normalize-space()='Next']")
        Choose_Vessel_Registration = (By.XPATH, "//button[contains(@class, 'template-builder-step-btn')]//span[text()='Vessel Registration']")
        # Sub_Module_Next = (By.XPATH, "//button[normalize-space()='Next']")
        TAW_initiatorType = (By.XPATH, "//select[@id='stakeholderType']")
        TAW_initiatorType_value = (By.XPATH, "//select[@id='stakeholderType']/option[@value='SHIPPING_AGENT']")
        TAW_Workflow_Name = (By.XPATH, "//input[@id='name']")
        TAW_Workflow_Description = (By.XPATH, "//input[@id='description']")
        TAW_Customs_tile = (By.XPATH, "//strong[normalize-space()='Customs']")
        TAW_STAGE_1 = (By.XPATH, "//div[@class='card-item']//klui-toggle-switch")
        TAW_Drag = (By.XPATH, "//div[contains(@class,'drop-area') and contains(@class,'graph-bg')]")
        TAW_ADD_STAGE_BUTTON = (By.XPATH, "//button[normalize-space()='Add Stage']")
        TAW_SAVE = (By.XPATH, "//button[@type='submit']")
        TAW_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']")   
        TAW_CONFIRM_CANCEL = (By.XPATH, "//button[@class='klui-btn klui-btn-primary']") 
        TAW_DISCARD_CANCEL = (By.XPATH, "//button[@class='klui-btn klui-btn-secondary']")      
        # ========================================================================================================
        # TRANSACTION APPROVAL WORKFLOW (END) 
        # ========================================================================================================

       


        #=========================================================================================================    
        # STAKEHOLDER MANAGEMENT (START)
        #=========================================================================================================     
        Stakeholder_Management_Header = (By.XPATH, "//h1[normalize-space()='Stakeholder Management']")
        Create_Stakeholder_Management = (By.XPATH, "//h1[normalize-space()='Create Stakeholder Management']")
        Create_Stakeholder = (By.XPATH, "//i[@class='fal fa-plus']") 
        Stakeholder_Master_Type = (By.XPATH, "//select[@id='stakeholderType']")
        Select_Stakeholder_Type = (By.XPATH, "//select[@formcontrolname='stakeholderMasterTypeCode']/option[normalize-space()='Shipping Agent']")
        Stakeholder_Code = (By.XPATH, "//div[@class='page-body']//div[2]//app-custom-validator[1]//div[1]//input[1]")
        Stakeholder_Name = (By.XPATH, "//div[3]//app-custom-validator[1]//div[1]//input[1]")
        Stakeholder_Status = (By.XPATH, "//label[@for='isActive']")
        Stakeholder_SAVE = (By.XPATH, "//button[normalize-space()='Save']")
        Stakeholder_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']")
        Stakeholder_Name_Column_Filter = (By.XPATH, "//div[@col-id='name']//span[@class='ag-icon ag-icon-filter']")
        Search_Stakeholder_value = (By.XPATH, "//input[@placeholder='Filter...' and contains(@class, 'ag-text-field-input')]")
        Edit_Stakeholder = (By.XPATH, "//i[@class='fal fa-edit text-primary']")
        Update_Stakeholder = (By.XPATH, "//button[normalize-space()='Update']")
        #=========================================================================================================    
        # STAKEHOLDER MANAGEMENT (END)
        #=========================================================================================================      

        # ========================================================================================================
        # SCN (START) 
        # ========================================================================================================
        SCN_Header = (By.XPATH, "//h1[normalize-space()='Ship Call Number']") 
        Create_SCN = (By.XPATH, "//span[normalize-space()='Create New']") 
        Create_SCN_Header = (By.XPATH, "//h1[normalize-space()='Create New Ship Call Number']") 
        SCN_Vessel_ID = (By.XPATH, "//input[@placeholder='Enter Vessel ID']")
        SCN_GO = (By.XPATH, "//button[normalize-space()='GO']")
        SCN_Port = (By.XPATH, "//input[@placeholder='Select Port']")
        SCN_Port_Search = (By.XPATH, "//input[@placeholder='Search...']")
        SCN_Port_select = (By.XPATH, "//div[@aria-label='NHAVA SHEVA']")
        SCN_Terminals = (By.XPATH, "//input[@placeholder='Select Terminals']") 
        SCN_Terminal_Name = (By.XPATH, "//div[@aria-label='Bharat Mumbai Container Terminals (BMCT)']")
        ETA = (By.XPATH, "//div[3]//app-custom-validator[1]//input[2]")
        ETD = (By.XPATH, "//div[4]//app-custom-validator[1]//input[2]")
        ETA_Next_Month = (By.XPATH, "(//span[@class='flatpickr-next-month'][normalize-space()='>'])[1]")
        ETD_Next_Month = (By.XPATH, "(//span[@class='flatpickr-next-month'][normalize-space()='>'])[2]")
        ETA_Next_Month_First = (By.XPATH, "(//span[@class='flatpickr-day'][normalize-space()='1'])[1]")
        ETD_Next_Month_Second = (By.XPATH, "(//span[@class='flatpickr-day'][normalize-space()='2'])[2]")
        Purpose_of_Call = (By.XPATH, "//input[@placeholder='Purpose of Call']")
        Purpose_of_Call_select = (By.XPATH, "//div[@aria-label='Barter Trade']") 
        Last_port_of_call = (By.XPATH, "//input[@placeholder='Select Last port of call']")
        Last_port_of_call_select = (By.XPATH, "//div[@aria-label='AGARTALA']")
        Next_port_of_call = (By.XPATH, "//input[@placeholder='Select Next port of call']") 
        Next_port_of_call_select = (By.XPATH, "//div[@id='QA-klui-select-dropdown-item-23-1']")
        Outbound_Handling_Yes = (By.XPATH, "//span[normalize-space()='Yes']") 
        Outbound_Handling_No = (By.XPATH, "//span[normalize-space()='No']") 
        Inbound_Voyage = (By.XPATH, "//input[@formcontrolname='inboundVoyage']") 
        Outbound_Voyage = (By.XPATH, "//input[@formcontrolname='outboundVoyage']") 
        Entry_Custom_station = (By.XPATH, "//input[@placeholder='Select Entry station']")
        Exit_Custom_station = (By.XPATH, "//input[@placeholder='Select Exit station']")
        Entry_Custom_station_select = (By.XPATH, "//div[@aria-label='JNPT Parking Plaza']")         
        Exit_Custom_station_select = (By.XPATH, "//div[@aria-label='Nhava Sheva – APMT (GTI)']")
        GRT = (By.XPATH, "//select[@formcontrolname='grossRegisteredTonnage']") 
        NRT = (By.XPATH, "//select[@formcontrolname='netRegisteredTonnage']") 
        SCN_Remarks = (By.XPATH, "//textarea[@type='text']") 
        SCN_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
        SCN_IMO_Filter = () 
        SCN_View = ()
        SCN_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']") 
        SCN_Stay_On_Page = (By.XPATH, "//button[@class='btn btn-secondary']") 
        SCN_Confirm_Cancel = (By.XPATH, "//button[@class='btn btn-primary me-1']") 
        SCN_Approve = (By.XPATH, "")
        SCN_Reject = (By.XPATH, "")
        # ========================================================================================================
        # SCN (END) 
        # ========================================================================================================  


        # ========================================================================================================
        # EPAN (START) 
        # ========================================================================================================      
        Create_EPAN = (By.XPATH, "//span[normalize-space()='Create New']")
        EPAN_Header = (By.XPATH, "//h1[normalize-space()='Pre-Arrival Notification']")
        Create_ePAN_Header = (By.XPATH, "//h1[normalize-space()='Create New Pre-Arrival Notification']")
        EPAN_SCN_Number = (By.XPATH, "//input[@placeholder='Enter SCN Number']")
        EPAN_GO = (By.XPATH, "//button[normalize-space()='GO']")
        EPAN_ISSC_Present = (By.XPATH, "//input[@id='radio-opt-0']")
        EPAN_ISSC_Not_Present = (By.XPATH, "//input[@id='radio-opt-1']")
        EPAN_Non_Compliant_Port_Yes = (By.XPATH, "//span[normalize-space()='Yes']")
        EPAN_Non_Compliant_Port_No = (By.XPATH, "//span[normalize-space()='No']s")
        EPAN_Crew_List = (By.XPATH, "//klui-file-upload[@placeholder='Upload Crew List']//button[@type='button'][normalize-space()='Upload File']")
        EPAN_Passenger_List = (By.XPATH, "//klui-file-upload[@placeholder='Upload Passenger List']//button[@type='button'][normalize-space()='Upload File']")
        EPAN_DG_Cargo_Declaration = (By.XPATH, "//klui-file-upload[@placeholder='Upload DG Cargo Declaration']//button[@type='button'][normalize-space()='Upload File']")
        EPAN_Port_Code = (By.XPATH, "//input[@placeholder='Code']")
        EPAN_Port_Name = (By.XPATH, "//input[@placeholder='Name']")
        EPAN_Arrival = (By.XPATH, "//div[4]//input[2]")
        EPAN_Departure = (By.XPATH, "//div[5]//input[2]")
        EPAN_SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")
        EPAN_SAVE_AS_DRAFT = (By.XPATH, "//button[normalize-space()='Save as Draft']")
        EPAN_CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']")
        EPAN_View_Details = (By.XPATH, "//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-last-left-pinned ag-column-first ag-cell-focus']//i[@class='fal fa-eye text-primary']")
        EPAN_Amend_Details = (By.XPATH, "//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-last-left-pinned ag-column-first ag-cell-focus']//i[@class='fal fa-edit text-primary']")
        EPAN_ALL = (By.XPATH, "//small[normalize-space()='All']")
        EPAN_Draft = (By.XPATH, "//small[normalize-space()='Draft']")
        EPAN_Submitted = (By.XPATH, "//small[normalize-space()='Submitted']")
        EPAN_Approved = (By.XPATH, "//small[normalize-space()='Approved']")
        EPAN_Cancelled = (By.XPATH, "//small[normalize-space()='Cancelled']")
        EPAN_Rejected = (By.XPATH, "//small[normalize-space()='Rejected']")
        EPAN_SCN_No_Filter = (By.XPATH, "//div[@class='ag-header-cell ag-header-parent-hidden ag-header-cell-sortable ag-focus-managed ag-header-active']//span[@class='ag-header-icon ag-header-cell-filter-button']//span[@role='presentation']")
        EPAN_SCN_No_Search = (By.XPATH, "//input[@id='ag-890-input']")
        # ========================================================================================================
        # EPAN (END) 
        # ======================================================================================================== 

        # ========================================================================================================
        # ARRIVAL CLEARANCE (START) 
        # ========================================================================================================
        Arrival_Clearance_Header = (By.XPATH, "//h1[normalize-space()='Arrival Clearance']")
        Create_Arrival_Clearance = (By.XPATH, "//span[normalize-space()='Create New']")
        Create__Arrival_Clearance_Header = (By.XPATH, "//h1[@class='d-inline-flex align-items-center']")
        Arrival_Clearance_GO = (By.XPATH, "//button[normalize-space()='GO']")
        # ========================================================================================================
        # ARRIVAL CLEARANCE (END) 
        # ========================================================================================================

        # ========================================================================================================
        # DEPARTURE CLEARANCE (START) 
        # ========================================================================================================
        Departure_Clearance_Header = (By.XPATH, "//h1[normalize-space()='Departure Clearance']")
        Create_Departure_Clearance = (By.XPATH, "//span[normalize-space()='Create New']")
        Create__Departure_Clearance_Header = (By.XPATH, "//h1[@class='d-inline-flex align-items-center']")
        Departure_Clearance_GO = (By.XPATH, "")
        # ========================================================================================================
        # DEPARTURE CLEARANCE (END) 
        # ========================================================================================================


        # ========================================================================================================
        # VESSEL PROFILE (START) 
        # ========================================================================================================
        Vessel_Profile_Header = (By.XPATH, "//h1[normalize-space()='Vessel Profile']") 
        Create_Vessel_Profile_Header = (By.XPATH, "//h3[normalize-space()='Create New Vessel Profile']")
        Register_New_Vessel_Profile = (By.XPATH, "//span[normalize-space()='Create New']") 
        VP_Basic_Vessel_Information_toggle = (By.XPATH, "//klui-expansion-panel[1]//div[1]//div[1]//button[1]//i[1]") 
        VP_Vessel_Classification_Type_toggle = (By.XPATH, "//klui-expansion-panel[2]//div[1]//div[1]//button[1]//i[1]") 
        VP_Vessel_Specification_toggle = (By.XPATH, "//div[@class='klui-expansion-panel']//i[@class='fal fa-plus-square text-muted']") 
        VP_Vessel_Specification_collapse = (By.XPATH, "(//div[contains(.,'Vessel Specifications')]/preceding::button[contains(@class,'klui-expansion-panel-toggle-btn')][1])[2]") 

        VP_Vessel_Name = (By.XPATH, "//input[@placeholder='Enter vessel name']") 
        VP_IMO_Number = (By.XPATH, "//input[@placeholder='Enter IMO number']") 
        VP_Call_Sign = (By.XPATH, "//input[@placeholder='Enter call sign']") 
        VP_General_Type = (By.XPATH, "//select[@formcontrolname='generalType']") 
        VP_General_Type_select = (By.XPATH, "//select[@formcontrolname='generalType']/option[normalize-space()='Cargo']")
        VP_Vessel_Type = (By.XPATH, "//select[@formcontrolname='vesselType']") 
        VP_Vessel_Type_select = (By.XPATH, "//select[@formcontrolname='vesselType']/option[normalize-space()='Container Ship']") 
        VP_LOA = (By.XPATH, "//input[@placeholder='Enter LOA']") 
        VP_LBP = (By.XPATH, "//input[@placeholder='Enter LBP']") 
        VP_Draft = (By.XPATH, "//input[@placeholder='Enter draft']") 
        VP_Beam = (By.XPATH, "//input[@placeholder='Enter beam']") 

        VP_Vessel_Name_Column_Filter = (By.XPATH, " ") 
        VP_View = (By.XPATH, "//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-last-left-pinned ag-column-first ag-cell-focus']//button[@class='btn btn-outlined btn-sm']") 

        VP_SUBMIT = (By.XPATH, "//button[@type='submit' and normalize-space()='Submit']") 
        VP_SAVE = (By.XPATH, "//button[@type='button' and normalize-space()='Save']") 
        VP_CANCEL = (By.XPATH, "//button[@type='button' and normalize-space()='Cancel']") 
        VP_RESET = (By.XPATH, "//button[@type='button' and normalize-space()='Reset']") 
        # ========================================================================================================
        # VESSEL PROFILE (END) 
        # ========================================================================================================


        # ========================================================================================================
        # VESSEL REGISTRATION (START) 
        # ========================================================================================================
        Register_New_Vessel_Header = (By.XPATH, "//h1[normalize-space()='Register New Vessel']")
        Vessel_Registration_Requests_All = (By.XPATH, "//button[.//small[normalize-space(text())='All']]")
        Vessel_Registration_Requests_Draft = (By.XPATH, "//button[.//small[normalize-space(text())='Draft']]")
        Vessel_Registration_Requests_Submitted = (By.XPATH, "//button[.//small[normalize-space(text())='Submitted']]")
        Vessel_Registration_Requests_Approved = (By.XPATH, "//button[.//small[normalize-space(text())='Approved']]")
        Vessel_Registration_Requests_Cancelled = (By.XPATH, "//button[.//small[normalize-space(text())='Cancelled']]")
        Vessel_Registration_Requests_Rejected = (By.XPATH, "//button[.//small[normalize-space(text())='Rejected']]")

        record_rows = (By.XPATH, "//div[contains(@class,'ag-center-cols-container')]//div[contains(@class,'ag-row')]")
        Vessel_Registration_horizontal_bar = (By.XPATH, " ")

        Vessel_registration_button = (By.XPATH, "//span[normalize-space()='Create New']")
        Vessel_registration_Submit = (By.XPATH, "//button[normalize-space()='Submit']")
        Vessel_registration_SaveAsDraft = (By.XPATH, "//button[normalize-space()='Save as Draft']")
        Vessel_registration_Cancel = (By.XPATH, "//button[normalize-space()='Cancel']")
        Vessel_registration_stay_on_page = (By.XPATH, "//button[@class='klui-btn klui-btn-secondary']")
        Vessel_registration_YES_Cancel = (By.XPATH, "//button[@class='me-1 klui-btn klui-btn-primary']")
        
        ColumnName = (By.XPATH, "//span[@title='Vessel Name' and text()='Vessel Name']")
        CreateNewVesselRegistrationButton = (By.XPATH, "//button[contains(@class, 'btn-circle-plus') and contains(@class, 'float-bottom-right')]")
        text = "Vessel"
        
        # BASIC VESSEL INFORMATION - LOCATORS
        FormVesselName = (By.NAME, "data[profile][vesselName]")
        FormIMO_NO_INPUT = (By.NAME, "data[profile][imoNumber]")
        FormCALL_SIGN_INPUT = (By.NAME, "data[profile][callSign]")
        FormOFFICIAL_NUMBER_INPUT = (By.NAME, "data[profile][officialNumber]")

        # REGISTRATION & COMPLIANCE  - LOCATORS
        REGISTRATION_COMPLIANCE_PANEL = (By.XPATH,"//div[@role='button' and normalize-space()='Registration & Compliance']")
        Ship_Registry_Certificate_No = (By.NAME, "data[profile][registrationCompliance][shipRegistryCertificateNo]")
        Ship_Registry_Date = (By.XPATH, "//input[@name='data[profile][registrationCompliance][shipRegistryDate]']")
        Ship_Registry_Date_Format = (By.XPATH, "//input[@class='form-control input is-invalid']")
        Vessel_Nationality = (By.XPATH, "//span[normalize-space()='Foreign']")
        Vessel_Flag = (By.XPATH, "(//div[@class='form-control ui fluid selection dropdown'])[1]")
        Vessel_Flag_Select = (By.XPATH, "(//div[@class='choices__item choices__item--choice choices__item--selectable is-highlighted'])[1]")
        Port_of_Registry = (By.XPATH, "(//div[@class='form-control ui fluid selection dropdown'])[2]")
        Port_of_Registry_select = (By.XPATH, "(//div[@class='choices__item choices__item--choice choices__item--selectable is-highlighted'])[2]")
        Area_of_operation = (By.XPATH, "(//div[@class='form-control ui fluid selection dropdown'])[3]")
        Area_of_operation_Select = (By.XPATH, "(//div[@class='choices__item choices__item--choice choices__item--selectable is-highlighted'])[3]")

        # VESSEL CLASSIFICATION & TYPE  - LOCATORS
        VESSEL_CLASSIFICATION_TYPE_PANEL = (By.XPATH, "//div[@role='button' and normalize-space()='Vessel Classification & Type']")
        General_Type = (By.XPATH, "(//div[@class='form-control ui fluid selection dropdown'])[4]")
        General_Type_select = (By.XPATH, "(//div[@class='choices__item choices__item--choice choices__item--selectable is-highlighted'])[4]")
        Vessel_Type = (By.XPATH, "(//div[@class='form-control ui fluid selection dropdown'])[5]")
        Vessel_Type_select = (By.XPATH, "(//div[@class='choices__item choices__item--choice choices__item--selectable is-highlighted'])[5]")
        Sub_Type = (By.XPATH, "//input[@name='data[profile][classification][subType]']")

        # VESSEL SPECIFICATIONS  - LOCATORS
        VESSEL_SPECIFICATION_PANEL = (By.XPATH, "//div[@id='etstm46']//div[@role='button']")
        Year_Built = (By.XPATH, "//input[@id='e9z4grd-yearBuilt']")
        Built_Place = (By.XPATH, "//input[@id='e8x33b4-builtPlace']")
        Vessel_With_Gear = (By.XPATH, "//input[@id='ekp7ten-ef5fuq6--true']")
        Type_of_Hull = (By.XPATH, "//div[@id='e19vg86']//div[@class='form-control ui fluid selection dropdown']")
        Position_of_Bridge = (By.XPATH, "//div[@id='enbx6i9']//div[@class='form-control ui fluid selection dropdown']")
        Length_Overall = (By.XPATH, "//input[@id='ezk00h-loa']")
        Depth = (By.XPATH, "//input[@id='enzh20a-depth']")
        Draft = (By.XPATH, "//input[@id='evg7uk8-draft']")
        Freeboard = (By.XPATH, "//input[@id='egw1nfb-freeboard']")
        Length_Between_Perpendiculars = (By.XPATH, "//input[@id='epb6ols-lbp']")
        Beam = (By.XPATH, "//input[@id='ep7y2-beam']")
        Displacement = (By.XPATH, "//input[@id='ehe82w-displacement']")

        # TONNAGE & CAPACITY  - LOCATORS
        Tonnage_Capacity_PANEL = (By.XPATH, "//div[@id='ep8qrxl']//div[@role='button']")
        Gross_Tonnage = (By.XPATH, "//input[@id='emrdv0h-grossTonnage']")
        Net_Tonnage = (By.XPATH, "//input[@id='eizmcl-netTonnage']")
        Deadweight_Tonnage = (By.XPATH, "//input[@id='eeslss5-deadweightTonnage']")
        Crew_Capacity = (By.XPATH, "//input[@id='eknzruh-crew']")
        Passenger_Capacity = (By.XPATH, "//input[@id='ei8cza-passenger']")
        TEU_Capacity = (By.XPATH, "//input[@id='eyy7tvg-teu']")


        # OWNERSHIP & MANAGEMENT  - LOCATORS
        Ownership_Management_PANEL = (By.XPATH, "//div[@id='esqa5gl']//div[@role='button']")
        Owner_Name = (By.XPATH, "//input[@id='eblskw9e-name']")
        Email = (By.XPATH, "//input[@id='ei591ho-email']")
        Mobile_No = (By.XPATH, "//input[@id='e6qe7e3m-phone']")
        Owner_Code = (By.XPATH, "//input[@id='eq4o6jd-ownerCode']")
        Shipping_Line_Name = (By.XPATH, "//input[@id='esheui-shippingLineName']")
        Address_Line_1 = (By.XPATH, "//input[@id='e8niirc-line1']")
        Address_Line_2 = (By.XPATH, "//input[@id='ef8kqwi-line2']")
        Address_Line_3 = (By.XPATH, "//input[@id='esarnwd-line3']")
        City = (By.XPATH, "//div[@id='e2eqnf']//div[@class='form-control ui fluid selection dropdown']")
        State = (By.XPATH, "//div[@id='ewifl1p']//div[@class='form-control ui fluid selection dropdown']")
        Country = (By.XPATH, "//div[@id='etvj8g']//div[@class='form-control ui fluid selection dropdown']")
        Postcode = (By.XPATH, "//input[@id='e96e6f-postalCode']")

        # SHIPPING & OPERATIONS  - LOCATORS
        Shipping_Operations_PANEL = (By.XPATH, "//div[@id='esdb5c']//div[@role='button']")
        Shipping_Agent_Code = (By.XPATH, "//input[@id='ei40g6x-code']")
        Shipping_Agent_Name = (By.XPATH, "//input[@id='ezeoa5v-name']")
        Shipping_Agent_Email = (By.XPATH, "//input[@id='errkako-email']")
        Shipping_Agent_Mobile_No = (By.XPATH, "//input[@id='eagb2bi-mobileNo']")
        Charterer_Details = (By.XPATH, "//input[@id='efm23nk-chartererDetails']")
        Shipping_Agent_Address_Line_1 = (By.XPATH, "//input[@id='e8jgler-line1']")
        Shipping_Agent_Address_Line_2 = (By.XPATH, "//input[@id='ez2frth-line2']")
        Shipping_Agent_Address_Line_3 = (By.XPATH, "//input[@id='eydnies-line3']")
        Shipping_Agent_City = (By.XPATH, "//div[@id='exj2tid']//div[@class='form-control ui fluid selection dropdown']")
        Shipping_Agent_State = (By.XPATH, "//div[@id='evf5w2m']//div[@class='form-control ui fluid selection dropdown']")
        Shipping_Agent_Country = (By.XPATH, "//div[@id='ea5yjs']//div[@class='form-control ui fluid selection dropdown']")
        Shipping_Agent_Postcode = (By.XPATH, "//input[@id='e8qki2i-postalCode']")

        # DOCUMENTS  - LOCATORS
        Documents_PANEL = (By.XPATH, "//div[@id='eqee9s']//div[@role='button']")
        Ship_Registry_Certificate = (By.XPATH, "//div[@id='e3ddz9k']//a[@class='browse']")
        Tonnage_Certificate = (By.XPATH, "//div[@id='e0hat5a']//a[@class='browse']")
        Load_Line_Certificate = (By.XPATH, "//div[@id='eirpl4c']//a[@class='browse']")
        Class_Cerificate = (By.XPATH, "//div[@id='ew7pzi']//a[@class='browse']")
        Owner_Charterer_Authorization_Letter = (By.XPATH, "//div[@id='eibotq']//a[@class='browse']")
        # ========================================================================================================
        # VESSEL REGISTRATION (END) 
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
        # ICP Logout
        # ========================================================================================================                
        ICP_Sign_Out = (By.XPATH, "//span[normalize-space()='Sign Out']")



        # file_path = r"D:\Harshad\PCS\UI Automation\PCS_Selenium\test_data.xlsx"