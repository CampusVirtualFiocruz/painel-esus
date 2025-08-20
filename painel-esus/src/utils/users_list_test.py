import src.utils.users_list as user_list


def test_load_conf():
    users_list = user_list.get_users_list()
    assert len(users_list) > 0

    print([ user['user'] for user in users_list])
