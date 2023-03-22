from requests_folder.post_tokens import post_token


class TestPostTokens:
    def test_post_tokens(self):
        response = post_token('test@airportgap.com', 'airportgappassword')
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'