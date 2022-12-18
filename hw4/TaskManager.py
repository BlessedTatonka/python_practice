import random

class Task:
    def __init__(self, id=None, name=None, description=None, status=None):
        if id is not None:
            self.id = id
        else:
            self.id = int(random.randint(1, 1e+10))
        self.name = name
        self.description = description
        self.status = status
        self.subtask = None

class Subtask(Task):
    # have comlex task id
    def __init__(self, parent_id):
        super.__init__(self)
        self.parent_id = parent_id

class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self):
        super.__init__(self)
        self.subtasks = []   
        
        
class TaskManager:

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}
    
    def create_task(self, task: Task=None):
        if task is not None:
            self.tasks[task.id] = task
        else:
            new_task = Task()
            self.tasks[new_task.id] = new_task
    
    def create_subtask(self, subtask: Subtask):
        self.subtasks[subtask.id] = subtask
    
    def create_complex_task(self, complex_task: ComplexTask):
        self.complex_tasks[complex_task.id] = complex_task
    
    def get_tasks(self):
        return self.tasks
    
    def get_subtasks(self):
        return self.subtasks
    
    def get_complex_tasks(self):
        return self.complex_tasks
    
    def get_tasks_by_id(self, id):
        try:
            return self.tasks[id]
        except:
            print('An error occured :(')
    
    def get_subtasks_by_id(self, id):
        try:
            return self.subtasks[id]
        except:
            print('An error occured :(')
    
    def get_complex_tasks_by_id(self, id):
        try:
            return self.complex_tasks[id]
        except:
            print('An error occured :(')
    
    def remove_tasks(self):
        self.tasks = {}
    
    def remove_subtasks(self):
        self.subtasks = {}
    
    def remove_complex_tasks(self):
        self.complex_tasks = {}
    
    def remove_task_by_id(self, id):
        self.tasks.pop(id, None)

    def remove_subtask_by_id(self, id):
        self.subtasks.pop(id, None)
    
    def remove_complex_task_by_id(self, id):
        self.complex_tasks.pop(id, None)
    
    def update_status(self, id, status):
        try:
            self.tasks[id].status = status
        except:
            print('An error occured :(')
        
        
        
        
manager = TaskManager()
manager.create_task()     