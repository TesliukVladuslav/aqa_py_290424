from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome()

file_path = 'C:/Users/влад/PycharmProjects/aqa_py_290424/lesson_27/dz.html'
driver.get(f'file:///{file_path}')

def verify_in_frame(frame_id, input_id, secret_text):

    driver.switch_to.frame(frame_id)

    input_field = driver.find_element(By.ID, input_id)
    input_field.send_keys(secret_text)

    driver.find_element(By.XPATH, "//button[text()='Перевірити']").click()

    alert = Alert(driver)
    assert alert.text == "Верифікація пройшла успішно!", f"Перевірка для {frame_id} не пройшла успішно!"

    alert.accept()

    driver.switch_to.default_content()

verify_in_frame('frame1', 'input1', 'Frame1_Secret')

verify_in_frame('frame2', 'input2', 'Frame2_Secret')

driver.quit()

