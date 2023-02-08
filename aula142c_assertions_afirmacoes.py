"""
Assertions (Afirmações/Checagens/Questionamentos)

ele passou este exemplo onde somente um adminsitrador poderia deletar todo
o sistema (mas com a flag -O qualquer usuário poderia burlar istto)

"""


def destroi_todo_o_sistema():
    print('seu sistema está sendo destruído, depois do Adeus, já era!')


def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores podem fazer coisas ruins!'
    destroi_todo_o_sistema()
    return 'Adeus'
