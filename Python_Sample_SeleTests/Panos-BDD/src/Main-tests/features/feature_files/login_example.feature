Feature: Login - Homepage

    Background: Feature test setup - Connect to Main Webpage
        Given Connect to Main Webpage


    @login @TESTTAG001 @regression
    Scenario: Login - Validate Homepage and Dashboard [TESTTAG001]
       When Navigate to Login using URL
       And Login as user using staging environment (user_tag_creds,@example_user@)
      Then Validate Homepage and Dashboard
       And Logout as user

        @login @TESTTAG002 @regression
    Scenario: Login - Validate Homepage and Verify translations Dashboard [TESTTAG002]
       When Navigate to Login using URL
       And Login as user using staging environment (user_tag_creds,@example_user@)
      Then Verify Translations
       And Logout as user