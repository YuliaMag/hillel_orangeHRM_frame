
def test_successful_login(login_page, valid_user, dashboard_page):
    dashboard_page = login_page.perform_successful_login(valid_user)
    assert dashboard_page.is_displayed(), ""
