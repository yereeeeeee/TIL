class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'Other Model'
    
    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type
    
    def display_info(self):
        print(f'PK: {BaseModel.PK}, TYPE: {self.TYPE}, Extended Type: {self.extended_type}')
    
    def save(self):
        print('데이터를 확장해서 저장합니다.')
    

extended_instance = ExtendedModel('Data Type', 'Title', 'Content', 'Created at', 'Updated at', 'Author', 'Extended Type')
extended_instance.display_info()
extended_instance.save()
