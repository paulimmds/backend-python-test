"""
Home Blueprint :
    - Testar se a rota home retorna um status_code = 200
    - Testar se a rota home renderiza o arquivo readme
    - Testar se, quando o usuário não está logado, aparece o botão de log-in
    - Testar se, quando o usuário está logado, aparece o botão de log-out
"""
from flask_login import current_user

def test_if_home_view_returns_status_code_200(test_client):
    """Test if the request to the home route returns a successfull status_code response"""
    res = test_client.get('/')
    assert res.status_code == 200

def test_if_home_view_renders_readme_file(test_client):
    """Test if the home route renders the readme file in the html content"""
    res = test_client.get('/')
    assert b'Alayacare Python skill test' in res.data
    assert res.status_code == 200

def test_if_route_view_returns_login_button_when_user_is_not_logged(test_client):
    """ Test if the home route renders the right button when
        the user is not logged in"""
    
    with test_client:
        res = test_client.get('/')
        assert b'Login' in res.data
        assert current_user.is_anonymous
        assert res.status_code == 200

def test_if_route_view_returns_logout_button_when_user_is_logged_in(test_client):
    """ Test if the home route renders the right button when
        the user is logged in"""
    
    with test_client:
        res = test_client.post('/login', data={'username':'user1', 'password':'user1'})
        res = test_client.get('/')
        assert b'user1 Logout' in res.data
        assert res.status_code == 200