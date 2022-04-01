"""
Todo Blueprint:
    - Testar  se usuários, quando logados, conseguem visualizar as suas tasks
    - Testar se usuários anônimos não possuem acesso a dados de tasks
    - Testar se usuário não consegue ver a task de outros usuários 
"""

def test_if_user_have_access_to_todo_view_when_logged_in(test_client):
    with test_client:
        res = test_client.post('/login', data={'username':'user1', 'password':'user1'})
        res = test_client.get('todo/')
        assert res.status_code == 200
        assert b'Todo List' in res.data

def test_if_user_have_no_access_to_todo_view_when_not_logged_in(test_client):
    with test_client:
        res = test_client.get('todo/')
        assert res.status_code == 401

def test_if_user_cant_see_other_user_tasks(test_client):
    with test_client:
        res = test_client.post('/login', data={'username':'user2', 'password':'user2'})
        res = test_client.get('todo/11')
        assert res.status_code == 302