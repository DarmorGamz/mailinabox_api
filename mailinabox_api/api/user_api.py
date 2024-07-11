from mailinabox_api.api_client import ApiClient

class UserApi(object):
    """
    UserAPI class
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
    
    def add_user(self, email: str = "", password: str = ""):
        """
        Add a user
        """

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {
            'email': email,
            'password': password
        }

        body_params = None

        return self.api_client.call_api(
            "/admin/mail/users/add",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
        )
