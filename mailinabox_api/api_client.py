import logging

import requests
from .error import (ApiException)
from requests.auth import HTTPBasicAuth

class ApiClient(object):
    """
    blah
    """
    def __init__(self, host: str ="https://box.example.com/admin", username=None, password=None):
        if not username or not password:
            raise ApiException("Missing MailinaBox username or password")
        """
        Username for HTTP basic authentication
        """
        self.username = username
        """
        Password for HTTP basic authentication
        """
        self.password = password
        """
        Host for HTTP path
        """
        self.host = host
        """
        Logging Settings
        """
        self.logger = {}
        self.logger["mailinabox_api"] = logging.getLogger("mailinabox_api")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """
        close
        """
        pass

    def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        _host=None,
    ):

        # request url
        if _host is None:
            url = self.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        try:
            # perform request and return response
            response_data = self.request(
                method,
                url,
                query_params=query_params,
                headers=header_params,
                post_params=post_params,
                body=body,
            )
            return response_data
        except ApiException as e:
            raise e

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        post_params=None,
        body=None,
    ):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            print("GET")
            pass
        elif method == "POST":
            print("POST")
            auth = HTTPBasicAuth(self.username, self.password)
            response = requests.post(url, data=post_params, auth=auth)
            return response
        else:
            raise ApiException(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )
