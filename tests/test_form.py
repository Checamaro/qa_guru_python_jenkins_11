from pages.registration_page import RegistrationPage
from data.users import User
import allure
from allure_commons.types import Severity

@allure.tag('web')
@allure.title('Successfully filled registration form')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Student registration form")
@allure.link("'https://demoqa.com'", name="Testing")
def test_fill_form():
    kirill = User(
        first_name='Kirill',
        last_name='Sharevich',
        user_email='email@example.com',
        user_gender='Male',
        user_number='9119119191',
        year='1988',
        month='April',
        day='30',
        subject='Maths',
        hobby='Sports',
        file='pivottable1.png',
        current_address='Saint-Petersburg',
        state='Haryana',
        city='Karnal'
    )

    registration_page = RegistrationPage()
    with allure.step('Open registration page'):
        registration_page.open()
    with allure.step('Filling in the form'):
        registration_page.fill(kirill)
    with allure.step('Clicking "Submit" button'):
        registration_page.submit()
    with allure.step('Checking filled form info'):
        registration_page.check_for_submit_form_is_visible(kirill)
