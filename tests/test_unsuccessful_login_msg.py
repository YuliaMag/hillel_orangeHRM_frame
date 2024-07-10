
def test_unsuccessful_login_msg(login_page, invalid_user):
    login_page.perform_unsuccessful_login(invalid_user)
    assert login_page.show_error_msg.is_displayed(), ""
