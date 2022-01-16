*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Registration
    Username Should Be Too Short

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Registration
    Password Should Be Invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle3
    Set Password  kalle1234
    Set Password Confirmation  Kalle1234
    Submit Registration
    Passwords Do Not Match

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Username Should Be Too Short
    Page Should Contain  Username must contain at least 3 characters

Password Should Be Invalid
    Page Should Contain  Password must contain

Passwords Do Not Match
    Page Should Contain  Passwords don't match

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