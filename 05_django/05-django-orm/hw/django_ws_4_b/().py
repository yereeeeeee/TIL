# coding: utf-8
todo = Todo()
todos = Todo()
Todo.objects.create(work='첫 번째 작업', content='서브1', is_completed=False)
Todo.objects.create(work='두 번째 작업', content='서브2', is_completed=True)
Todo.objects.all()
todo = Todo.objects.filter(pk=1)
todo.work()
todo = Todo.objects.get(pk=-1)
todo = Todo.objects.get(pk=1)
todo.work()
todo.content
todo.work
todo.is_completed
todo.work = '수정된 첫 번째 할 일'
