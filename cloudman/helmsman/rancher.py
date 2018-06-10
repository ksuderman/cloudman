import requests
from requests.auth import AuthBase


class RancherAuth(AuthBase):

    def __init__(self, client):
        # setup any auth-related data here
        self.client = client

    def __call__(self, r):
        # modify and return the request
        r.headers['content-type'] = "application/json"
        r.headers['authorization'] = "Bearer " + self.client.token
        return r


class RancherClient(object):

    INSTALLED_APP_URL = ("{rancher_url}/v3/projects/{project_id}/app"
                         "?targetNamespace=galaxy-ns")

    def __init__(self, rancher_url, token, project_id):
        self.rancher_url = rancher_url
        self.token = token
        self.project_id = project_id

    def format_url(self, url):
        return url.format(rancher_url=self.rancher_url,
                          project_id=self.project_id)

    def get_auth(self):
        return RancherAuth(self)

    def _api_get(self, url):
        return requests.get(self.format_url(url), auth=self.get_auth(),
                            verify=False).json()

    def _api_post(self, url, data):
        return requests.post(self.format_url(url), auth=self.get_auth(),
                             verify=False, json=data).json()

    def _api_put(self, url, data):
        return requests.put(self.format_url(url), auth=self.get_auth(),
                            verify=False, json=data).json()

    def list_installed_charts(self):
        return self._api_get(self.INSTALLED_APP_URL).get('data')

    def update_installed_chart(self, data):
        r = self._api_put(data.get('links').get('self'), data)
        return r
