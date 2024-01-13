import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
def clear_input_field(input_element):
    input_element.send_keys(Keys.CONTROL + 'a')
    input_element.send_keys(Keys.DELETE)
def Login(id, password):
    driver.get("http://182.163.99.86/login")
    username = id
    password = password

    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))) 
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']")))

    username_input.send_keys(username)
    password_input.send_keys(password)
    button.click()
    time.sleep(2)
def User():
        button1 = driver.find_element(By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[3]/a/div")
        button1.click()
        time.sleep(2)

def UserCreate(name,gender,inst,password,role,email,dob,qua,mob):
        
        button1 = driver.find_element(By.XPATH, "//button[.='Add User']")
        button1.click()
        time.sleep(2)
        full_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'full_name')))
        gender_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'gender')))
        institution_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'institution_name')))
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        role_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'role')))
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        dob_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'dob')))
        qualification_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'qualification')))
        mobile_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'mobile')))
        clear_input_field(full_name_input)
        clear_input_field(institution_name_input)
        clear_input_field(password_input)
        clear_input_field(email_input)
        clear_input_field(qualification_input)
        clear_input_field(mobile_input)
        full_name_input.send_keys(name)
        gender_select.send_keys(gender)
        institution_name_input.send_keys(inst)
        password_input.send_keys(password)
        role_select.send_keys(role)
        email_input.send_keys(email)
        dob_input.send_keys(dob)
        qualification_input.send_keys(qua)
        mobile_input.send_keys(mob)
        try:
            add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
            add_button.click()
            # print("Button Clicked")
            time.sleep(1)
            try:
                section = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section[1]')))
                div_elements = section.find_elements(By.TAG_NAME, 'div')
                is_printed = False
                for div_element in div_elements:
                    text = div_element.text
                    if text:
                        # print(text)
                        if text == "User created successfully":
                            #print("Valid")
                            is_printed = True
                        else :
                            #print("Invalid")
                            is_printed = True
                            if "exists" not in text:
                                cross  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/img"))) 
                                cross.click()
                    if is_printed:
                        break


            except TimeoutException:
                print("")
        except TimeoutException:
            #print("Invalid")
            cross  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/img"))) 
            cross.click()

        time.sleep(2)
def deleteUser(name):
        time.sleep(2)
        user_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[1]/div[3]/input')))
        user_name.send_keys(name)
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div/span[3]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]").click()
        time.sleep(3)
     
def Project():
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button").click()
        time.sleep(3)   
def projectCreate(name):
        driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[1]/button").click()
        time.sleep(3)
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'name')))
        description_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'description')))
        name_input.send_keys(name)
        description_input.send_keys("This is test project")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section/div/div/div[1]/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[1]/button/div").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[5]/button/div").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[7]/button/div").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()
        time.sleep(3)
def projectDelete(name):
        project_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/div[1]/div[2]/input')))

        project_name.send_keys(name)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr/td[9]/div/span[3]/img").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]").click()
        time.sleep(3)
      
def File_Upload(name):
        project_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/div[1]/div[2]/input')))
        clear_input_field(project_name)
        project_name.send_keys(name)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[1]/td[9]/div/span[1]/a/img").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section/div[1]/div/div/div[1]/div/div/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section/div[2]/div/span/a").click()
        time.sleep(3)
        Keyboard = Controller()
        Keyboard.type("C:\\Users\\Ahmad\\Downloads\\upload_data_sample (1).xlsx")
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)

        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()
        time.sleep(3)
def Logout():
    button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[1]/nav/div/button/div/p[1]/span")
    button.click()
    time.sleep(1)
    logout_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div")
    logout_button.click()
    time.sleep(1)
def SearchProject(project_name):
    goto_project = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[2]/a/div')))
    goto_project.click()


    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div/input')))
    search.send_keys(project_name)
    time.sleep(2)
    view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody/tr/td[9]/div/a')))
    view.click()

    time.sleep(2)
def Annotation(group_name):
    group = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/div/input')))
    group.send_keys(group_name)
    time.sleep(2)

    start_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')))
    start_btn.click()
    time.sleep(2)

    while True:
        try:
            tag_grid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section[2]')))
            spans = tag_grid.find_elements(By.TAG_NAME, "span")
            time.sleep(2)

            if not spans:
                print("Done")
                break
            for span in spans: #iterate over tags
                time.sleep(2)
                span.click()
                break
            actions = ActionChains(driver)
            sentence = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section[3]/div/div/div')))
            sentence_span = sentence.find_elements(By.TAG_NAME, "span")
            for span in sentence_span: #iterate over words
                actions.double_click(span).perform()
                break
            time.sleep(1)
            submit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]')))
            submit_btn.click()

        except TimeoutException:
            print("tag_grid not found. Breaking the loop.")
            break
    time.sleep(1)
def Validation(group_name):
    group = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/div/input')))
    group.send_keys(group_name)
    time.sleep(2)

    start_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')))
    start_btn.click()
    time.sleep(2)

    cnt = 0
    while len(driver.find_elements(By.CLASS_NAME, '_like-edit-section_1ctbc_32')) > 0:
        print("size ")
        print(len(driver.find_elements(By.CLASS_NAME, '_like-edit-section_1ctbc_32')))

        like_edit_divs = driver.find_elements(By.CLASS_NAME, '_like-edit-section_1ctbc_32')
        like_edit_div = like_edit_divs[0]
        like_btn_div = like_edit_div.find_element(By.CLASS_NAME, '_like-btn_1ctbc_42')
        edit_btn_div = like_edit_div.find_element(By.CLASS_NAME, '_edit-btn_1ctbc_50')

        if cnt%2 == 0:
            time.sleep(1)
            like_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_like-button_1ctbc_77')))
            like_btn.click()
            time.sleep(1)
        else:
            edit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_edit-btn_1ctbc_50')))
            edit_btn.click()
            time.sleep(1)

            # After clicking edit button
            # class = _annotation-type-container_1bu34_10 col-lg-3 col-md-4 tag containner
                # tag name in class = _annotation-type-title_1bu34_16
                # class = _ner-sub-category-badge-selected_1bu34_22 badge bg-transparent selected tag
                # class = _ner-sub-category-badge_1bu34_22 badge bg-transparent not selected tag
            # _ner-annotaion-text_1bu34_44

            tag_classes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_annotation-type-container_1bu34_10.col-lg-3.col-md-4')))

            clicked = False
            for tag_class in tag_classes:
                try:
                    span_element = tag_class.find_element(By.CLASS_NAME, '_ner-sub-category-badge_1bu34_22.badge.bg-transparent')
                    span_element.click()
                    clicked = True
                    time.sleep(2)
                except NoSuchElementException:
                    print("No span found in this div")
                if clicked:
                    break
            

            annotaion_text_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_ner-annotaion-text_1bu34_44'))
            )

            # Find and iterate over the mark and span tags
            mark_tag = annotaion_text_div.find_element(By.TAG_NAME, 'mark')
            driver.execute_script("arguments[0].click();", mark_tag)
            time.sleep(1)
            span_tags = annotaion_text_div.find_elements(By.TAG_NAME, 'span')
            first_span_tag = span_tags[0]
            actions = ActionChains(driver)
            actions.double_click(first_span_tag).perform()
            time.sleep(1)

            submit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]')))
            submit_btn.click()

            time.sleep(1)                                                                                
        cnt = cnt + 1

if __name__ == '__main__':
    '''
    #Case 1: Wrong ID 

    Login("admin111@gigatech.com","Abc@123")
    time.sleep(2)

    #Case 2: Without password
    Login("admin@gigatech.com","")
    time.sleep(2)

    #Case 3: Without ID and pass
    Login("","")
    time.sleep(2)

    #Case 4 : Without ID
    Login("","Abc@123")
    time.sleep(2)

    #Case 5 : Only past part of the email
    Login("admin111","Abc@123")
    time.sleep(2)
    
    #Case 6 :Currect ID and Pass
    Login("admin@gigatech.com","Abc@123")
    time.sleep(1)
    User()

    #Case 7 Create user without role
    
    UserCreate("Ahs","Male","NSU","Abc@123","","e11@gmail.com","10/10/2000","Nothing","01800000000")
    
    #Case 8 Create user without Email
    
    UserCreate("A10","Male","NSU","Abc@123","Annotator","","10/10/2000","Nothing","01800000000")
    
    #Case 9 Create user without pass requirment
    
    UserCreate("A10","Male","NSU","Abcd123","Annotator","e22@gmail.com","10/10/2000","Nothing","01800000000")
    
    #Case 10 Create user without name
    
    UserCreate("","Male","NSU","Abc@123","Annotator","e23@gmail.com","10/10/2000","Nothing","01800000000")
    
    #Case 11 Create user All valid info
    
    UserCreate("Ah","Male","NSU","Abc@123","Annotator","e33@gmail.com","10/10/2000","Nothing","01800000000")

    #Case 12 Create user pass size>14
    
    UserCreate("Ah","Male","NSU","Abcdef@123456789","Annotator","e44@gmail.com","10/10/2000","Nothing","01800000000")

    #Case 13 Create user with big name
    
    UserCreate("Ahmaddddddddsssdddddddddddddddddddd","Male","NSU","Abc@123","Annotator","e50@gmail.com","10/10/2000","Nothing","01800000000")
    
    #Case 14 Create user without gender
    
    UserCreate("Ahmad","","NSU","Abc@123","Annotator","e60@gmail.com","10/10/2000","Nothing","01800000000")

    #Case 15 Create user without valid email
    
    UserCreate("Ahmaddddddddddssssssdddddddddddddddddd","Male","NSU","Abc@123","Annotator","e22gmailcom","10/10/2000","Nothing","01800000000")
    
    #Case 16 Again create a user mobile number not integer
   
    UserCreate("Ahmad","Male","NSU","Abc@123","Annotator","e12@gmailcom","10/10/2000","Nothing","abcdefghijk")

    #Case 17 Delete a User 
    time.sleep(3)
    deleteUser("b60@gmail.com")
    time.sleep(3)

    #Case 18 Logout
    Logout()
    time.sleep(3)
    
    
    #(website crash)
    #Case 19 Again create a user mobile number<11(digit)
    Login("admin@gigatech.com","Abc@123")
    User()
    UserCreate("Ahmad","Male","NSU","Abc@123","Annotator","d12@gmailcom","10/10/2000","Nothing","01800")
    
    
    
    #Case 20 Again create a user mobile number>11(digit)
    Login("admin@gigatech.com","Abc@123")
    User()
    UserCreate("Ahmad","Male","NSU","Abc@123","Annotator","d12@gmailcom","10/10/2000","Nothing","01800000000000000")
    



    #Projects related test cases
    Login("admin@gigatech.com","Abc@123")
    Project()

    #Case 21 Create new project 
    projectCreate("CSE434-3")

    #Case 22 Try to create a project same as already created project  
    projectCreate("CSE434-3")

    #Case 23 Delete peoject
    projectDelete("CSE434-3")

    
    #Case 24 File upload in the project
    File_Upload("Demo888")
    time.sleep(3)
    Logout()
    time.sleep(3)
    '''


    #Case 25 Annotator

    #Case 26,27 Validator (edit,not edit)

    #Case 28 Configuration

    #Case 29 Guest Login

    #Case 30 Mo

    
    