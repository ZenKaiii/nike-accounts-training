import time
import random
import threading
from selenium import webdriver


def getAccounts():
    accounts = []
    file = open("setting.txt", 'r')
    line = file.readline()
    line = line[:-1]
    delay_time = float(line.split(':')[1])
    while line:
        line = file.readline()
        line = line[:-1]
        if line != '':
            accounts.append(line.split(' '))
    print ('[ZenKaiTraining]>Get ' + str(len(accounts)) + ' accounts')
    return delay_time, accounts

def printRights():
    print("""                                                                                                          
      `;!!;'.               ';!!!!!!!!!;'..                                                               
   :&#########@;     :$###@$|;'.....``''';|$@#@%:.     `%@@###@%'                                         
 `%##############@##&!`                        `!&#&%$###########@!.                                      
 :@#############@!.                                `|@#############$`                                     
 :@###########@;                                      ;@############;                                     
 ;@##########$'                                        '$###########%.     '%$$$$$$$$$$$$$$$$$$$$$$$$$$$$%
 :@#########%`                       `!%&&&&%|:.        `%##########%.     ;;                             
 :@########%.               .':'.    .:!||!!;;;:.        `%#########!      ;:                             
 :&#######$`          .:!$&@@@&$%;'. `:;:`                '&#######%.      ;:                  .``.       
  `$#####&'         .!&&&$%||||%%%!` .`';!|%&%:.           :&####%`        ;:     .;!'..':!%|;`           
     :$#@;          `:;:.   `';:'``.    .'!$%'.             :@$'           ;:     `!%%%|:.                
      '&%.          `'. :%@##@%:            ..               !@;           ;:                             
     .|&:            .:!!:';;'                               `%%`          ;; .':'':'`':::'`':::::'. `::`.
     ;@|.                  .               .':'.              ;&!          ;;'||!!|%%||%|%%|%!!||!|%%%|!;`
    `$&'                        :;`     .`..`:||:.            .%$'         ;;`!%%!|%%%%|||%%|::|%|%|||%|:.
    !@!                       `!%;::!$&&$%%%!`  `''.           !@!         ;;`';|%%%||%%|%||%|!|||%!::!%|'
   '&%`                      .::..;%$$$$$%;.       .           ;@$`        ;;'|%!:;|:`;|||!';|||!:;||||!`.
  `$#!                   .`':;:`       `';!%$$!.               :@#!        ::                             
 '&#@;                  `'':;;:::`.`!&@@$%!;|&#$'              '&#@;       ;:                             
 :@#@:                     ..`:;;:;$@@&$$$$%|$%:               '&##&:      ;;                             
 :@##|.                     .`'::':|$%;`                       :@###@;                 ;@#########@;      
 :@##@;                   ...`'''''`````....`:;:`              !######&:               ;###########!      
 :@####|.                  ...``':''';|$&&&&&%;`              !#########@!.            ;###########%.     
 :@#####@;                    .``''''```````..              ;&##############$;.       .|###########&:     
 :@#######@|.                                            '$########################@&&@#############!     
 :@##########&!.                                     .;&############################################!     
 :@#############@%'                              `!&################################################!     
 :@###################@&%|;'.          .`';|$@######################################################!     
 :@################################################################################################$`     
 :@###############################################################################################%.      
                                                                                                          
                                                                                                          
                                                                                                          
 .`''.  .`.     ..  .`.   .`.  .``..     .`''.               `!;.:%:      .'::::::::::` `::;!!'.;%'       
|%||%|'`;%%%:  '||'`!%;.'|%|'.:||%%%%|:'|%||%|'              ;%::%%%%%$$|` `'''!%!''''. .`;%;  '|%%%%!`   
%|;`   .;%||%;.:||'.!%||%|'   :%!'.:|%;;||;`                ;%|!%;.:%:'%;`:;;;;|%|;;;;;:!$%%%$%%|'.;|`    
`;|%%|'`;|;'!%!!|!'`!%|||;.   :|%%%%|:. `;|%%|'            '%%!``|!!$!!|` .```:||:'````. `;%;``:|;'|;     
``.`!%;';|;..;%|||'`!%;'!%%;. :%!':%|:  ``.`!%;.            '!|:!|':%;:%;    '|%||!.    :%!:!%; :%%!`     
|%%%%!`.;%;   :%%|'`!%;  `!%|:;%!` :%%;;|%%%%;. `|%:        .!|:;: :$:.;!` :|%!`'|!`.;%::%;';%;'!%%%;     
                                                 :!`        .!|` '|%!`    '|;.   '|%%|' :%;`;%%|;. '!'  """)
    print("Please fill in your account info and browsing time for each item in setting.txt")

def train(username,password):
    isEmail = not username.isdigit()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--log-level=2')
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://store.nike.com/cn/zh_cn/pw/mens-shoes/7puZoi3")


    time.sleep(13) #这里注意，暂停一段时间等待登录按钮加载出来，根据设备性能与网速自行调试
    driver.find_element_by_xpath("//*[@id='AccountNavigationContainer']/button").click()

    if isEmail:
        print("[ZenKaiTraining]>A new account username:" + username + " using Email")
        driver.find_element_by_link_text('使用电子邮件登录。').click()
        login_username = "emailAddress"
    else:
        print("[ZenKaiTraining]>A new account username:" + username + " using Mobile")
        login_username = "verifyMobileNumber"

    driver.find_element_by_name(login_username).send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("[value='登录']").click()

    time.sleep(10)

    new_shoes = driver.find_elements_by_css_selector("[class='product-card__body']")

    random.shuffle(new_shoes)
    print("[ZenKaiTraining]>Have " + str(len(new_shoes)) + " items.")

    for i in range(len(new_shoes)):
        href = new_shoes[i].find_element_by_tag_name('a').get_attribute("href")
        js = 'window.open("' + href + '");'
        driver.execute_script(js)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        print(username + ">Browse shoes:[" + driver.title.replace(u'\xa0', u'') + "]")
        time.sleep(delay_time)
        driver.close()
        driver.switch_to.window(windows[0])

    driver.quit()



printRights()
delay_time,accounts = getAccounts()

for i in range(len(accounts)):
    username = accounts[i][0]
    password = accounts[i][1]
    client_thread = threading.Thread(target=train,args=(username,password))
    client_thread.start()
