from selene import browser, have
import os


def test_complete_todo():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')

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

    browser.element('#uploadPicture').send_keys(os.path.abspath('../pict.png'))

    browser.element('#currentAddress').type('Moscow')

    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element(".modal-content").element("tbody").all("tr").all("td").even.should(have.exact_texts((
        'Ivan Ivanov',
        'ivanovivan78@gmail.com',
        'Male',
        '0123456789',
        '06 April,1978',
        'Maths',
        'Sports, Music',
        'pict.png',
        'Moscow',
        'Haryana Karnal'
    )))
