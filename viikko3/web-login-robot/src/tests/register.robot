*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Reset

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
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Registration
    Password Should Be Invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  Kalle1234
    Submit Registration
    Passwords Do Not Match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle12
    Submit Credentials
    Username Or Password Should Be Invalid    