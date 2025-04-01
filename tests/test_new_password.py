import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters



def test_password_lenght():
    assert len(generate_password(100)) == 100


def test_password_not_the_same():
    for i in range(1, 101):
        assert generate_password(i) != generate_password(i)


def test_password_unique():
    assert generate_password(8) not in [generate_password(8) for _ in range(1000000)]

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
