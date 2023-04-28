from example import len_url_content, get_url_content
from unittest.mock import patch, MagicMock


@patch("example.get_url_content")
def test_len_content(mock_get_url_content):
    return_value = MagicMock()
    return_value.text = "heh"
    mock_get_url_content.return_value = return_value
    assert len_url_content() == 3


@patch("example.requests")
def test_get_content(mock_requests):

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "AHAHAHA"

    mock_requests.get.return_value = mock_response

    result = get_url_content()
    assert result.text == "AHAHAHA"
