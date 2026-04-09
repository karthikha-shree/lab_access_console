class User:
    def __init__(self,user_id,username,role):
        self.__user_id=user_id
        self.__username=username
        self.__role=role
    def get_user_id(self):
        return self.__user_id
    def get_username(self):
        return self.__username
    def get_user_role(self):
        return self.__role
    
