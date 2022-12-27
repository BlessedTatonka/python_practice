import unittest
from TaskManager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_subtask_removal(self):
        manager = TaskManager()
        ct = manager.create_complex_task('name1', 'description1')
        subtask = manager.create_subtask('name2', 'description2', ct.get_id())
        self.assertEqual(len(manager.get_complex_tasks_by_id(ct.get_id()).get_subtasks()), 1)

        manager.remove_subtask_by_id(subtask.get_id())

        self.assertEqual(len(manager.get_complex_tasks_by_id(ct.get_id()).get_subtasks()), 0)

