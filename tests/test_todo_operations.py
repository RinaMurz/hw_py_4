from selene import browser, have, be
import os


def test_complete_todo():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ivanov')
    browser.element('#lastName').type('Ivan')
    #browser.all('[id= "userName-wrapper>div"]').should(have.size(2))

    browser.element('#userEmail').type('ivanovivan78@gmail.com')

    browser.element('[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value= "3"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value= "1978"]').click()
    browser.element('.react-datepicker__day--006').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('element').send_keys(os.path.abspath('hw_py_4_picture.png'))

    browser.element('#currentAddress').type('Moscow')

    browser.element('#state').click().element('#react-select-3-option_1').click()
    browser.element('#city').click().element('#react-select-4-option_1').click()



