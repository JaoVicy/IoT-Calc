import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_index_get(client):
    """Deve carregar a página com GET e sem resultado."""
    url = reverse("index")  # Nome da sua rota no urls.py
    response = client.get(url)

    assert response.status_code == 200
    assert b"<form" in response.content
    assert b"km" not in response.content  # Sem resultado

@pytest.mark.django_db
def test_index_post_valido(client):
    """Deve calcular a distância entre duas coordenadas válidas."""
    url = reverse("index")
    data = {
        "lat1": -23.5505,
        "lon1": -46.6333,
        "lat2": -22.9068,
        "lon2": -43.1729,
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert b"km" in response.content  # Resultado deve aparecer
    assert b"0.00 km" not in response.content  # Não deve ser zero

@pytest.mark.django_db
def test_index_post_invalido(client):
    """Deve retornar erro se coordenadas inválidas forem enviadas."""
    url = reverse("index")
    data = {
        "lat1": "abc",
        "lon1": "xyz",
        "lat2": 1000,  # Fora do intervalo
        "lon2": 2000,  # Fora do intervalo
    }
    response = client.post(url, data)

    # Mesmo com erro, view renderiza página
    assert response.status_code == 200
    # A view não retorna resultado, pois form é inválido
    assert b"km" not in response.content

@pytest.mark.django_db
def test_index_erro_interno(monkeypatch, client):
    """Deve retornar mensagem de erro se geodesic falhar."""
    from app import views

    def fake_geodesic(*args, **kwargs):
        raise Exception("Erro simulado")

    monkeypatch.setattr(views, "geodesic", fake_geodesic)

    url = reverse("index")
    data = {
        "lat1": -23.55,
        "lon1": -46.63,
        "lat2": -22.90,
        "lon2": -43.17,
    }
    response = client.post(url, data)

    assert b"Erro simulado" in response.content
