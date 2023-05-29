*** Settings ***
Documentation    Basic utility methods.

Library    String


*** Keywords ***
Pass
    [Documentation]    Does nothing
    RETURN

Variable Is Empty
    [Documentation]    Determins if variable is null/emptystring/empty list.
    [Arguments]    ${arg1}

    ${is_empty}=    Run Keyword And Return Status    Should Be Empty      ${arg1}
    RETURN    ${is_empty}

Does String Match Pattern
    [Arguments]    ${text}
    ...    ${pattern}

    ${m}=    Get Regexp Matches    ${text}    ${pattern}
    ${matches}=    Set Variable    ${TRUE}
    Run Keyword If    ${m} == []
    ...    Set Local Variable    ${matches}    ${FALSE}

    RETURN    ${matches}
