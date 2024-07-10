def test_reset_password_cancel(reset_page, valid_user):
    reset_page.click_cancel_button(valid_user)
    assert reset_page.is_displayed(), ""

