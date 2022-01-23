*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Username Should Be Too Short
    Page Should Contain  Username must contain at least 3 characters

Password Should Be Invalid
    Page Should Contain  Password must contain

Passwords Do Not Match
    Page Should Contain  Passwords don't match

Username Or Password Should Be Invalid
    Page Should Contain  Invalid username or password

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Go To Register Page And Reset
    Go To Register Page
    Reset Application

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

