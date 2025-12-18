class Database():
    def connect(self):
        return "Database connection established"
    
class Server():
    def __init__(self,db):
        self.db = db# loose coupling not dirctly dependedent

    def getdata(self):
        return self.db.connect()

# usage
db = Database()
server = Server(db)
print(server.getdata())