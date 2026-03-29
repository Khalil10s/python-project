import json
import os
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self, description, priority=Priority.MEDIUM, due_date=None, category="Allmänt", completed=False, created_at=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.completed = completed
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority.value,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'category': self.category,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data['description'],
            priority=Priority(data['priority']),
            due_date=datetime.fromisoformat(data['due_date']) if data['due_date'] else None,
            category=data.get('category', 'Allmänt'),
            completed=data['completed'],
            created_at=datetime.fromisoformat(data['created_at'])
        )

    def __str__(self):
        status = "[✓]" if self.completed else "[ ]"
        priority_str = {Priority.LOW: "Låg", Priority.MEDIUM: "Med", Priority.HIGH: "Hög"}[self.priority]
        due_str = f" (Förfaller: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else ""
        return f"{status} {self.description} [{priority_str}] {self.category}{due_str}"

    def is_overdue(self):
        return self.due_date and self.due_date < datetime.now() and not self.completed

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        if not self.tasks:
            self.add_initial_tasks()

    def add_initial_tasks(self):
        self.tasks = [
            Task("Lär dig Python", Priority.HIGH, category="Utbildning"),
            Task("Bygg ett webprojekt", Priority.MEDIUM, category="Projekt"),
            Task("Öva GitHub", Priority.LOW, category="Verktyg")
        ]
        self.save_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, KeyError):
                print("Fel vid laddning av uppgiftsfil. Startar med tom lista.")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, description, priority=Priority.MEDIUM, due_date=None, category="Allmänt"):
        task = Task(description, priority, due_date, category)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Uppgift tillagd: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Tog bort: {removed}")
        else:
            print("Ogiltigt uppgiftsnummer.")

    def toggle_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self.save_tasks()
            print(f"Växlade: {self.tasks[index]}")
        else:
            print("Ogiltigt uppgiftsnummer.")

    def edit_task(self, index, **kwargs):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            for key, value in kwargs.items():
                if hasattr(task, key) and value is not None:
                    setattr(task, key, value)
            self.save_tasks()
            print(f"Uppdaterad: {task}")
        else:
            print("Ogiltigt uppgiftsnummer.")

    def show_tasks(self, show_completed=True, filter_priority=None, filter_category=None, sort_by='created_at'):
        tasks_to_show = self.tasks
        if not show_completed:
            tasks_to_show = [t for t in tasks_to_show if not t.completed]
        if filter_priority:
            tasks_to_show = [t for t in tasks_to_show if t.priority == filter_priority]
        if filter_category:
            tasks_to_show = [t for t in tasks_to_show if t.category.lower() == filter_category.lower()]

        # Sort
        if sort_by == 'priority':
            tasks_to_show.sort(key=lambda t: t.priority.value, reverse=True)
        elif sort_by == 'due_date':
            tasks_to_show.sort(key=lambda t: (t.due_date is None, t.due_date))
        elif sort_by == 'created_at':
            tasks_to_show.sort(key=lambda t: t.created_at)

        if not tasks_to_show:
            print("Inga uppgifter hittades.")
        else:
            print(f"\nDina uppgifter ({len(tasks_to_show)} totalt):")
            for i, task in enumerate(tasks_to_show, 1):
                print(f"{i}. {task}")

    def search_tasks(self, query):
        results = [t for t in self.tasks if query.lower() in t.description.lower() or query.lower() in t.category.lower()]
        if results:
            print(f"\nSökresultat för '{query}':")
            for i, task in enumerate(results, 1):
                print(f"{i}. {task}")
        else:
            print(f"Inga uppgifter hittades som matchar '{query}'.")

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue()]

    def get_categories(self):
        return list(set(t.category for t in self.tasks))

def get_priority_from_input():
    while True:
        print("Prioritet: 1-Låg, 2-Med, 3-Hög")
        try:
            choice = int(input("Välj prioritet (1-3): "))
            return Priority(choice)
        except ValueError:
            print("Ange ett nummer 1-3.")

def get_date_from_input():
    date_str = input("Förfallodatum (ÅÅÅÅ-MM-DD) eller lämna tomt: ").strip()
    if date_str:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Ogiltigt datumformat. Använder inget förfallodatum.")
    return None

def main():
    todo = ToDoList()

    while True:
        print("\n--- Avancerad Att-Göra Lista ---")
        print("1. Visa alla uppgifter")
        print("2. Visa pågående uppgifter")
        print("3. Lägg till uppgift")
        print("4. Ta bort uppgift")
        print("5. Växla klar")
        print("6. Redigera uppgift")
        print("7. Sök uppgifter")
        print("8. Visa försenade uppgifter")
        print("9. Visa per kategori")
        print("10. Sortera och visa")
        print("11. Avsluta")

        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            todo.show_tasks(show_completed=False)
        elif choice == "3":
            desc = input("Uppgiftsbeskrivning: ").strip()
            if desc:
                priority = get_priority_from_input()
                due_date = get_date_from_input()
                category = input("Kategori (standard: Allmänt): ").strip() or "Allmänt"
                todo.add_task(desc, priority, due_date, category)
            else:
                print("Beskrivning kan inte vara tom.")
        elif choice == "4":
            todo.show_tasks()
            try:
                index = int(input("Uppgiftsnummer att ta bort: ")) - 1
                todo.remove_task(index)
            except ValueError:
                print("Ange ett giltigt nummer.")
        elif choice == "5":
            todo.show_tasks()
            try:
                index = int(input("Uppgiftsnummer att växla: ")) - 1
                todo.toggle_complete(index)
            except ValueError:
                print("Ange ett giltigt nummer.")
        elif choice == "6":
            todo.show_tasks()
            try:
                index = int(input("Uppgiftsnummer att redigera: ")) - 1
                print("Lämna fält tomma för att behålla nuvarande värden.")
                new_desc = input("Ny beskrivning: ").strip() or None
                print("Ändra prioritet? (j/n): ")
                if input().strip().lower() == 'j':
                    new_pri = get_priority_from_input()
                else:
                    new_pri = None
                print("Ändra förfallodatum? (j/n): ")
                if input().strip().lower() == 'j':
                    new_date = get_date_from_input()
                else:
                    new_date = None
                new_cat = input("Ny kategori: ").strip() or None
                todo.edit_task(index, description=new_desc, priority=new_pri, due_date=new_date, category=new_cat)
            except ValueError:
                print("Ange ett giltigt nummer.")
        elif choice == "7":
            query = input("Sökfråga: ").strip()
            if query:
                todo.search_tasks(query)
            else:
                print("Ange en sökterm.")
        elif choice == "8":
            overdue = todo.get_overdue_tasks()
            if overdue:
                print("Försenade uppgifter:")
                for task in overdue:
                    print(f"  {task}")
            else:
                print("Inga försenade uppgifter.")
        elif choice == "9":
            categories = todo.get_categories()
            if categories:
                print("Tillgängliga kategorier:", ", ".join(categories))
                cat = input("Ange kategori att filtrera: ").strip()
                if cat:
                    todo.show_tasks(filter_category=cat)
                else:
                    print("Ingen kategori angiven.")
            else:
                print("Inga kategorier hittades.")
        elif choice == "10":
            print("Sortera efter: 1-Skapad, 2-Prioritet, 3-Förfallodatum")
            sort_choice = input("Välj sortering (1-3): ").strip()
            sort_by = {'1': 'created_at', '2': 'priority', '3': 'due_date'}.get(sort_choice, 'created_at')
            todo.show_tasks(sort_by=sort_by)
        elif choice == "11":
            todo.save_tasks()
            print("Uppgifter sparade. Hejdå!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()1
    