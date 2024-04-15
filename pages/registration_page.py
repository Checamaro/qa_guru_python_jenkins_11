import os
from datetime import datetime

from selene import browser, have, command
from pathlib import Path

import data
from data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.user_email)
        browser.all('[name=gender]').element_by(have.value(user.user_gender)).element('..').click()
        browser.element('#userNumber').type(user.user_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        for subject in user.subject.split(", "):
            browser.element('#subjectsInput').type(subject).press_enter()
        for hobby in user.hobby.split(", "):
            browser.all('.custom-checkbox').element_by(have.text(hobby)).click()
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(data.__file__), f'img/{user.file}')
            )
        )
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()

    def submit(self):
        browser.element('.practice-form-wrapper #submit').click()

    def check_for_submit_form_is_visible(self, users: User):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form'))

        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            f'{users.first_name} {users.last_name}',
            users.user_email,
            users.user_gender,
            users.user_number,
            f'{users.day} {users.month},{users.year}',
            users.subject,
            users.hobby,
            users.file,
            users.current_address,
            f'{users.state} {users.city}'
        ))
