# red_team/authorization.py
import os
from config.config import Config

def allowed():
    # requires env var and a token file ./red_team/approval.token
    if not Config.RED_TEAM_ENABLED: return False
    return os.path.exists(os.getenv("RED_TEAM_APPROVAL_FILE", "./red_team/approval.token"))
