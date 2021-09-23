import csv
class Todo:
    status:str
    description:str
    title:str
    
    def __init__(self,description,title,status):
        self.title = title
        self.description = description
        self.status = status
        
    @staticmethod
    def create(title,description,status):
        return Todo(title=title,description=description,status=status)
    
    def save(self):
        with open('TodoList.csv','a') as f:
            writer = csv.writer(f,lineterminator='\n')
            writer.writerow([self.title,self.description,self.status])

    @staticmethod
    def readcsv():
        listOfTodos = []
        with open('TodoList.csv','r') as f:
            csvRead = csv.reader(f)
            for line in csvRead:
                listOfTodos.append(Todo.create(*line))
        return listOfTodos