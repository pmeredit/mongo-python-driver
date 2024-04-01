from pymongo import MongoClient
from pymongo.auth import _AUTH_MAP, _authenticate_oidc
from pymongo.auth_oidc import OIDCCallback, OIDCCallbackContext, OIDCCallbackResult

_AUTH_MAP["MONGODB-OIDC"] = _authenticate_oidc

class Foo(OIDCCallback):
     """A base class for defining OIDC callbacks."""

     def fetch(self, context: OIDCCallbackContext) -> OIDCCallbackResult:
         """Convert the given BSON value into our own type."""
         print(context)
         print(context.idp_info)


class UserOIDCAuthState(object):
    def __init__(self, server_info):
        self.server_info = server_info
        self.auth_attempt = None
        self.current_token_set = {}


def get_auth_state(server_info):
    # TODO check if state already exists
    return UserOIDCAuthState(server_info)

def authorization_code_flow(state):
    print("authorization_code_flow")
    code_verifier = code_verifier()
    code_challenge = code_challenge(code_verifier)
    oidc_state_param = random_string()

def initiate_auth_attempt(state, timeout_seconds):
    print("initiate_auth_attempt")
    #TODO: something with timeout, whatever
    authorization_code_flow(state)

def request_token(server_info, context):
    print(server_info)
    print(context)
    print("!!!!!!!!!!!")
    state = get_auth_state(server_info)
    if "access_token" in state.current_token_set:
        return state.current_token_set["access_token"]
    timeout_seconds = context['timeout_seconds']
    return initiate_auth_attempt(server_info, state, timeout_seconds)


x = "mongodb://out-qa-lxonw.z.query.mongodb-dev.net/"
conn = MongoClient(x + "?directConnection=true&tls=true&authMechanism=MONGODB-OIDC",
        authMechanismProperties={"OIDC_HUMAN_CALLBACK": Foo()})

#conn = MongoClient("mongodb://mhuser:pencil@localhost:27017",
#        authMechanismProperties={"request_token_callback": request_token})

db = conn['tdvt']
print (db)
coll = db['batters']
#db = conn['test']
#coll = db['testgen.9']
#print(coll.find_one())
#coll = db['testgen.9']
print("pre find")
print(coll.find_one())
