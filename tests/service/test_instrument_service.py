# tests/service/test_instrument_service.py

import pytest
from unittest.mock import MagicMock
from service.instrument_service import (
    create_instrument_service,
    list_instruments_service,
    get_instrument_service,
    update_instrument_service,
    delete_instrument_service
)
from schema.instrument_schema import InstrumentCreate, InstrumentUpdate


# Define um fixture para o objeto de banco de dados (mock)
@pytest.fixture
def mock_db():
    return MagicMock()

# Define um fixture para o mock do repositório
@pytest.fixture
def mock_repository(monkeypatch):
    mock_repo = MagicMock()
    # "Patcheia" a importação do módulo real com nosso mock
    monkeypatch.setattr("service.instrument_service.instrument_repository", mock_repo)
    return mock_repo

def test_create_instrument_service(mock_db, mock_repository):
    # Simula um objeto de instrumento a ser criado
    instrument_data = InstrumentCreate(
        nome="Guitarra",
        marca="Fender",
        modelo="Stratocaster",
        preco=1500.00,
        orquestra=False,  # Adicionado o campo 'orquestra'
        comentario="Ideal para rock e blues."  # Adicionado o campo 'comentario'
    )
    
    # Simula o objeto que o repositório retornaria após a criação
    mock_repository.create_instrument.return_value = {
        "id": 1,
        "nome": "Guitarra",
        "marca": "Fender",
        "modelo": "Stratocaster",
        "preco": 1500.00,
        "orquestra": False,
        "comentario": "Ideal para rock e blues."
    }
    
    # Chama a função de serviço
    result = create_instrument_service(mock_db, instrument_data)
    
    # Verifica se a função de repositório foi chamada corretamente
    mock_repository.create_instrument.assert_called_once_with(mock_db, instrument_data)
    
    # Verifica se o resultado é o esperado
    assert result["id"] == 1
    assert result["nome"] == "Guitarra"
    assert result["orquestra"] == False


def test_list_instruments_service(mock_db, mock_repository):
    # Simula uma lista de instrumentos a ser retornada pelo repositório
    mock_repository.get_instruments.return_value = [
        {"id": 1, "nome": "Guitarra", "orquestra": False},
        {"id": 2, "nome": "Bateria", "orquestra": False}
    ]

    # Chama a função de serviço
    result = list_instruments_service(mock_db)

    # Verifica se a função de repositório foi chamada
    mock_repository.get_instruments.assert_called_once_with(mock_db)

    # Verifica se o resultado é o esperado
    assert len(result) == 2
    assert result[0]["nome"] == "Guitarra"

def test_get_instrument_service(mock_db, mock_repository):
    # Simula um instrumento a ser retornado pelo repositório
    instrument_id = 1
    mock_repository.get_instrument_by_id.return_value = {"id": 1, "nome": "Guitarra"}

    # Chama a função de serviço
    result = get_instrument_service(mock_db, instrument_id)

    # Verifica se a função de repositório foi chamada corretamente
    mock_repository.get_instrument_by_id.assert_called_once_with(mock_db, instrument_id)

    # Verifica o resultado
    assert result is not None
    assert result["id"] == 1

def test_get_instrument_service_not_found(mock_db, mock_repository):
    # Simula um caso em que o instrumento não é encontrado
    instrument_id = 99
    mock_repository.get_instrument_by_id.return_value = None

    # Chama a função de serviço
    result = get_instrument_service(mock_db, instrument_id)

    # Verifica o resultado
    assert result is None

def test_update_instrument_service(mock_db, mock_repository):
    # Simula um objeto de atualização
    instrument_id = 1

    # Agora o Pydantic aceitará apenas o campo 'preco'
    update_data = InstrumentUpdate(preco=1600.00)

    # Simula o instrumento atualizado retornado
    mock_repository.update_instrument.return_value = {
        "id": 1,
        "nome": "Guitarra",
        "marca": "Fender",
        "modelo": "Stratocaster",
        "preco": 1600.00,
        "orquestra": False,
        "comentario": "Ideal para rock e blues."
    }

    # Chama a função de serviço
    result = update_instrument_service(mock_db, instrument_id, update_data)

    # Verifica a chamada e o resultado
    mock_repository.update_instrument.assert_called_once_with(mock_db, instrument_id, update_data)
    assert result["preco"] == 1600.00

    # Verifica a chamada e o resultado
    mock_repository.update_instrument.assert_called_once_with(mock_db, instrument_id, update_data)
    assert result["preco"] == 1600.00

def test_delete_instrument_service(mock_db, mock_repository):
    # Simula que a exclusão foi bem-sucedida
    instrument_id = 1
    mock_repository.delete_instrument.return_value = True

    # Chama a função de serviço
    result = delete_instrument_service(mock_db, instrument_id)

    # Verifica a chamada e o resultado
    mock_repository.delete_instrument.assert_called_once_with(mock_db, instrument_id)
    assert result is True

def test_delete_instrument_service_not_found(mock_db, mock_repository):
    # Simula um caso de exclusão que falhou
    instrument_id = 99
    mock_repository.delete_instrument.return_value = False

    # Chama a função de serviço
    result = delete_instrument_service(mock_db, instrument_id)

    # Verifica a chamada e o resultado
    mock_repository.delete_instrument.assert_called_once_with(mock_db, instrument_id)
    assert result is False