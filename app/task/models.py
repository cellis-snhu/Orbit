class Task:
    def __init__(self, task_id, name, description):
        self._task_id = None
        self._name = None
        self._description = None

        # use @property setters to handle validation
        self.task_id = task_id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Task {self.task_id} Name: {self.name} Description: {self.description}>"

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        if self._task_id is not None:
            raise AttributeError("task_id is immutable and cannot be changed once set.")
        if value is None or len(value) > 10:
            raise ValueError(
                "Invalid task_id: must be non-null and <= 10 characters long."
            )
        self._task_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or len(value) > 20:
            raise ValueError(
                "Invalid task name: must be non-null and <= 20 characters long."
            )
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None or len(value) > 50:
            raise ValueError(
                "Invalid description: must be non-null and <= 50 characters long."
            )
        self._description = value

    def to_dict(self):
        return {
            "id": self.task_id,
            "name": self.name,
            "description": self.description,
        }
