Feature: ICP Sanity features

  Background:
    Given I launch the browser

# ====================================================================================================
# LOGIN (START)
# ====================================================================================================    
Scenario: Login with valid credentials for COMMUNITY ADMIN
    When I open the login page
    And I enter valid Community Admin's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button


Scenario: Check for display of all pages for COMMUNITY ADMIN
    When I open the login page
    And I enter valid Community Admin's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================      
    And I click on Avatar button
    And I click on ICP Sign Out button    

Scenario: Login with valid credentials for SHIPPING AGENT
    When I open the login page
    And I enter valid Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar      
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for SHIPPING AGENT
    When I open the login page
    And I enter valid Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for MARINE DEPARTMENT
    When I open the login page
    And I enter valid Marine Department's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for MARINE DEPARTMENT
    When I open the login page
    And I enter valid Marine Department's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for MINISTRY
    When I open the login page
    And I enter valid Ministry's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for MINISTRY
    When I open the login page
    And I enter valid Ministry's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for PRIVATE JETTY
    When I open the login page
    And I enter valid Private Jetty's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for PRIVATE JETTY
    When I open the login page
    And I enter valid Private Jetty's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for TERMINAL OPERATOR
    When I open the login page
    And I enter valid Terminal Operator's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for TERMINAL OPERATOR
    When I open the login page
    And I enter valid Terminal Operator's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for IMMIGRATION
    When I open the login page
    And I enter valid Immigration's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for IMMIGRATION
    When I open the login page
    And I enter valid Immigration's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for CUSTOMS
    When I open the login page
    And I enter valid Custom's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for CUSTOMS
    When I open the login page
    And I enter valid Custom's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for TERMINAL USER
    When I open the login page
    And I enter valid Terminal Operator's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button  
    
Scenario: Check for display of all pages for TERMINAL USER
    When I open the login page
    And I enter valid Terminal Operator's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Login with valid credentials for PORT_OPERATOR
    When I open the login page
    And I enter valid Port Operator's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I click on Avatar button
    And I click on ICP Sign Out button

Scenario: Check for display of all pages for PORT_OPERATOR
    When I open the login page
    And I enter valid Port Operator's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
# ==========================================================================    
    And I search for Registration Template in the sidebar
    And I navigate to Registration Template page
    And I search for Transaction Template in the sidebar
    And I navigate to Transaction Template page
    And I search for Registration Requests in the sidebar
    And I navigate to Registration Requests page
    And I search for Registration Approval Workflow in the sidebar
    And I navigate to Registration Approval Workflow page
    And I search for Transaction Approval Workflow in the sidebar
    And I navigate to Transaction Approval Workflow page
    And I search for Vessel Profile in the sidebar
    And I navigate to Vessel Profile page
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And I search for Stakeholder Management  in the sidebar
    And I navigate to Stakeholder Management page
    And I search for Terminal Configuration  in the sidebar
    And I navigate to Terminal Configuration page
# ==========================================================================     
    And I click on Avatar button
    And I click on ICP Sign Out button    


Scenario: NEW Shipping Agent should be able to Register new Vessel
    When I open the login page
    And I enter NEW Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I search for Vessel Registration in the sidebar
    And I navigate to Vessel Registration page
    And NEW Shipping Agent clicks on Create New button in Vessel Registration
    And Register New Vessel page should be displayed
    Then I enter vessel name on Register New Vessel page
    Then I enter IMO number on Register New Vessel page
    Then I enter Call Sign on Register New Vessel page
    Then I enter Official Number on Register New Vessel page
    When I click on Avatar button
    When I click on ICP Sign Out button

Scenario: NEW Shipping Agent should be able to create SCN
    When I open the login page
    And I enter NEW Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I search for Ship Call Number  in the sidebar
    And I navigate to Ship Call Number
    # And I should see the Ship Call Number page
    And Validate SCN page header
    And User clicks on Create SCN button
    And Validate Create New ePAN page header
    And User enters valid Vessel ID
    And User clicks on GO button
    
Scenario: NEW Shipping Agent should be able to create ePAN
    When I open the login page
    And I enter NEW Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I search for Pre-Arrival Notification  in the sidebar
    And I navigate to Pre-Arrival Notification
    And Validate ePAN page header
    And User clicks on Create ePAN button
    And Validate Create New ePAN page header
    And User enters SCN Number
    And User clicks on EPAN GO button

Scenario: NEW Shipping Agent should be able to create Arrival Clearance
    When I open the login page
    And I enter NEW Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I search for Arrival Clearance  in the sidebar
    And I navigate to Arrival Clearance
    And Validate Arrival Clearance page header
    And User clicks on Create Arrival Clearance button
    And Validate Create New Arrival Clearance page header
    And User enters SCN Number
    And User clicks on Arrival Clearance GO button

Scenario: NEW Shipping Agent should be able to create Departure Clearance
    When I open the login page
    And I enter NEW Shipping Agent's username and password
    And I click the ICP SignIn button
    And I should see the dashboard page
    And I click to expand sidebar
    And I search for Departure Clearance  in the sidebar
    And I navigate to Departure Clearance
    And Validate Departure Clearance page header
    And User clicks on Create Departure Clearance button
    And Validate Create New Departure Clearance page header
    # And User selects SCN Number
    # And User clicks on Departure Clearance GO button    