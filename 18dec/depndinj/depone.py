class Database():
    def connect(self):
        return "Database connection established"
    
class Server():
    def __init__(self):
        self.db = Database() # tight coupling

    def getdata(self):
        return self.db.connect()

# usage
server = Server()
print(server.getdata())
