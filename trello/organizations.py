import requests

class Organizations(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idOrg_or_name, actions=None, actions_limit=None, action_fields=None, members=None, member_fields=None, boards=None, board_fields=None, board_actions=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, actions=actions, actions_limit=actions_limit, action_fields=action_fields, members=members, member_fields=member_fields, boards=boards, board_fields=board_fields, board_actions=board_actions, board_actions_format=board_actions_format, board_actions_since=board_actions_since, board_actions_limit=board_actions_limit, board_action_fields=board_action_fields, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_field(self, field, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/%s" % (idOrg_or_name, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_action(self, idOrg_or_name, filter=None, fields=None, limit=None, format=None, since=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/organizations/%s/actions" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, format=format, since=since, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_board(self, idOrg_or_name, filter=None, fields=None, actions=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, lists=None):
        resp = requests.get("https://trello.com/1/organizations/%s/boards" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, actions=actions, actions_limit=actions_limit, actions_format=actions_format, actions_since=actions_since, action_fields=action_fields, lists=lists), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_board_filter(self, filter, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/boards/%s" % (idOrg_or_name, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_member(self, idOrg_or_name, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s/members" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_member_filter(self, filter, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/members/%s" % (idOrg_or_name, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def update(self, idOrg_or_name, name=None, displayName=None, desc=None, website=None, permissionLevel=None):
        resp = requests.put("https://trello.com/1/organizations/%s" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(name=name, displayName=displayName, desc=desc, website=website, permissionLevel=permissionLevel))
        resp.raise_for_status()
        return resp.json()

    def update_desc(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/desc" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_displayName(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/displayName" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_name(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/name" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_pref_permissionLevel(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/permissionLevel" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_website(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/website" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def new(self, name, displayName=None, desc=None, website=None):
        resp = requests.post("https://trello.com/1/organizations" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, displayName=displayName, desc=desc, website=website))
        resp.raise_for_status()
        return resp.json()

    def delete(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def delete_member_idMember(self, idMember, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s/members/%s" % (idOrg_or_name, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    
