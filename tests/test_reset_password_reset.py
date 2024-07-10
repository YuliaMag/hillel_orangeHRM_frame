def test_reset_password_reset(reset_page, valid_user):
    reset_reset = reset_page.display_reset_password_link()
    assert reset_reset.is_displayed(), ""
