*** Settings ***
Resource  resource.robot
Test Setup  Create Test User And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  rami  rami1234
    Output Should Contain  New user registered 

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle1234
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  a  abc1234
    Output Should Contain  Username must contain at least 3 characters

Register With Username Containing Invalid Characters
    Input Credentials  Rami  abc1234
    Output Should Contain  Username can only contain characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  rami  rami123
    Output Should Contain  Password must contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  rami  abcdefghtadf
    Output Should Contain  Password must contain at one non-letter

*** Keywords ***
Create Test User And Create User
    Create User  kalle  kalle123
    Input New Command