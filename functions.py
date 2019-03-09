import database_common

@database_common.connection_handler
def signup_user(cursor, user_name, hash):
    cursor.execute("""
                    INSERT INTO user_table (user_name, hash)
                    VALUES (%(user_name)s, %(hash)s)
    """, ({'user_name':user_name, 'hash':hash}))
