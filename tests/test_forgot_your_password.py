
def test_forgot_your_password(login_page, valid_user, reset_page):
    login_page.perform_forgot_your_password_redirect(valid_user)
    assert reset_page.is_displayed(), ""
