import pytest
from prueba import get_data, save_db

def test_get_data_names():
    result = get_data('https://restcountries.com/v3.1/subregion/ame')
    assert result['Name'].to_numpy().transpose().tolist() == ['Venezuela', 'Brazil', 'Colombia', 'Guyana', 'Falkland Islands', 'Argentina', 'Bolivia', 'Suriname', 'Peru', 'Ecuador', 'Paraguay', 'Uruguay', 'Chile', 'French Guiana'], ['Spanish', 'Portuguese', 'Spanish', 'English', 'English', 'Guaraní,Spanish', 'Aymara,Guaraní,Quechua,Spanish', 'Dutch', 'Aymara,Quechua,Spanish', 'Spanish', 'Guaraní,Spanish', 'Spanish', 'Spanish', 'French']

def test_get_data_languages():
    result = get_data('https://restcountries.com/v3.1/subregion/ame')
    assert result['Language'].to_numpy().transpose().tolist() ==  ['Spanish', 'Portuguese', 'Spanish', 'English', 'English', 'Guaraní,Spanish', 'Aymara,Guaraní,Quechua,Spanish', 'Dutch', 'Aymara,Quechua,Spanish', 'Spanish', 'Guaraní,Spanish', 'Spanish', 'Spanish', 'French']

def test_get_data_population():
    result = get_data('https://restcountries.com/v3.1/subregion/ame')
    assert result['population'].to_numpy().transpose().tolist() ==  [28435943, 212559409, 50882884, 786559, 2563, 45376763, 11673029, 586634, 32971846, 17643060, 7132530, 3473727, 19116209, 254541]



