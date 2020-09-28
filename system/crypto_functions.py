import uuid, random, string, hashlib
import bcrypt


def gen_uuid():
    return str(uuid.uuid4())


def random_string(string_length=10):
    letters = string.ascii_lowercase + '0123456789'
    return ''.join(random.choice(letters) for i in range(string_length))


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('charmap'), salt)
    return hashed.decode('charmap')


def check_hash(pwd_hash, password):
    return bcrypt.hashpw(password.encode('charmap'),
                         pwd_hash.encode('charmap')) == pwd_hash.encode(
        'charmap')


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def md5_hex_str(cleartext: string) -> string:
    return hashlib.md5(cleartext.encode('utf-8')).hexdigest()


def sha1_hex_str(cleartext: string) -> string:
    return hashlib.sha1(cleartext.encode('utf-8')).hexdigest()
