from base64 import b64encode
import uuid

print b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)