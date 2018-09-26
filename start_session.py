from towerkit import api, config, utils, exceptions, WSClient
from towerkit.tower.utils import check_related, delete_all, get_all, uses_sessions
from towerkit.tower.utils import as_user as _as_user

def start_session():
    config.credentials = utils.load_credentials('config/credentials.yml')
    root = api.Api()
    config.use_sessions = True
    root.load_session().get()

    v1 = root.available_versions.v1.get()
    v2 = root.available_versions.v2.get()
    return v1, v2
