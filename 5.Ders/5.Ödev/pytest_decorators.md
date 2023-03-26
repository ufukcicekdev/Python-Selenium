# Pytest Decoratos


@pytest.fixture
Bir test işlevi, fikstür adından bir giriş parametresi olarak bahsederek bir fikstür kullanabilir.
Testlere girdi sağlayan fikstür fonksiyonu oluşturulur.Fikstür işlevine erişmek için testlerin, fikstür adını giriş parametresi olarak belirtmesi gerekir.

@pytest.mark.skipif() Koşullu olarak testleri atlamak için kullanılır

@pytest.mark.skip kullanılarak testler atlatılıyor

@pytest.mark.parametrize kullanarak testleri parametreleştirebiliriz

@pytest.mark.xfail testin başarısız olmasını beklediğimiz durumlarda kullanılır

@pytest.mark.timeout() Testin zaman aşımı yönetimi için kullanılır