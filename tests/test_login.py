import pytest

@pytest.mark.login
def test_inventory_access(session_user_login):
    driver = session_user_login.driver
    assert "inventory" in driver.current_url