*** Settings ***
Documentation    Sandbox for development purposes.

Resource    ${CURDIR}/core/utils.resource

*** Tasks ***
Some Pointless Task
    ${condition}=    Set Variable    ${TRUE}
    ${text}=    Run Keyword If    ${condition}
        ...    Create A Story About    James Ellwood
        ...    ELSE    Set Variable    ${EMPTY}

    ${cond}=    Check Condition    ${text}

    Log    The text is: "${text}"; ${cond}.    level=DEBUG

*** Keywords ***
Create A Story About
    [ARGUMENTS]    ${name}

    RETURN    This is a story about ${name} and co.

Check Condition
    [Arguments]    ${name}

    ${cond}=    Does String Match Pattern    ${name}    ^Th

    RETURN    ${cond}
