class Task:
    def __init__(self, id, name, description, ):
        self.__id = id
        self.__name = name
        self.__description = description
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name


class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, parent_id):
        super().__init__(id, name, description)
        self.__parent_id = parent_id

    def get_parent_id(self):
        return self.__parent_id
    

class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description):
        super().__init__(id, name, description)
        self.__subtasks = []

    def get_subtasks(self):
        return self.__subtasks

    def delete_subtask(self, subtask_id):
        self.__subtasks.remove(subtask_id)

    def add_subtask(self, subtask_id):
        if subtask_id not in self.__subtasks:
            self.__subtasks.append(subtask_id)
  
class TaskManager:
    
    id_series = 0
    
    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}
    
    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1 
        return next_id_value
        
    
    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task
    
    
    def create_subtask(self, name, description, parent_id):
        current_id = self.__get_and_increment_id()
        new_subtask = Subtask(current_id, name, description, parent_id)
        self.subtasks[current_id] = new_subtask
        self.complex_tasks[parent_id].add_subtask(new_subtask.get_id())
        return new_subtask
    
    def create_complex_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_complex_task = ComplexTask(current_id, name, description)
        self.complex_tasks[current_id] = new_complex_task
        return new_complex_task
    
    def get_tasks(self):
        return self.tasks
    
    def get_subtasks(self):
        return self.subtasks
    
    def get_complex_tasks(self):
        return self.complex_tasks
    
    def get_tasks_by_id(self, id):
        return self.tasks[id]
    
    def get_subtasks_by_id(self, id):
        return self.subtasks[id]
    
    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks[id]
    
    def remove_tasks(self):
        self.tasks = {}
    
    def remove_subtasks(self):
        self.subtasks = {}
    
    def remove_complex_tasks(self):
        self.complex_tasks = {}
    
    def remove_task_by_id(self, id):
        self.tasks.pop(id, None)
    
    def remove_subtask_by_id(self, id):
        self.complex_tasks[self.subtasks[id].get_parent_id()].delete_subtask(id)
        self.subtasks.pop(id, None)
    
    def remove_complex_task_by_id(self, id):
        self.complex_tasks.pop(id, None)