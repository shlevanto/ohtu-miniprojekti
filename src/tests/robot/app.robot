*** Settings ***
#Test Setup   Start App
Resource  resource.robot
Test Setup  Start
Test Teardown  Reset

*** Test Cases ***
Test Welcome
    Output Should Contain  Welcome to Bookmarker!
    Output should Contain  Type 'h' for help

Test Help
    Input Help Command
    Output Should Contain  To delete a bookmark, first select 'edit' and then 'delete'
    Output Should Contain  (Not implemented yet)

Test Add Command
    Input  add
    Read Command
    Input  http://www.princess-mononoke.com
    Execute Command
    Prompt Should Be  Url:${SPACE}
    Output Should Be  Bookmark "1 Welcome to Princess Mononoke" created!


Test Show Empty Command
    Input Show Command
    Output Should Be  No bookmarks

Test Show Command
    Add Bookmark  http://www.princess-mononoke.com
    Input Show Command
    Output Should Be  Welcome to Princess Mononoke

Test Find Command
    Add Bookmark  http://www.princess-mononoke.com
    Input  search
    Read Command
    Input  *elcome*
    Execute Command
    Prompt Should Be  Term:${SPACE}
    Output Should Be  Welcome to Princess Mononoke

Test Empty Command
    Input Empty Command
    Output Should Contain  Acceptable commands:
    Output Should Contain  'q' - quit,
    Output Should Contain  'h' - help,
    Output Should Contain  'add' - add a new bookmark,
    Output Should Contain  'show' - show given amount of bookmarks,
    Output Should Contain  'edit' - edit a bookmark


*** Keywords ***
Start
    Welcome