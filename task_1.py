class Node:
   def __init__(self, data=None):
       self.data = data
       self.next = None


class LinkedList:

   def __init__(self):
       self.head = None

   def insert_at_beginning(self, data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
      
   def insert_at_end(self, data):
       new_node = Node(data)
       if self.head is None:
           self.head = new_node
       else:
           cur = self.head
           while cur.next:
               cur = cur.next
           cur.next = new_node

   def insert_after(self, prev_node: Node, data):
       if prev_node is None:
           print("Попереднього вузла не існує.")
           return
       new_node = Node(data)
       new_node.next = prev_node.next
       prev_node.next = new_node

   def delete_node(self, key: int):
      cur = self.head
      if cur and cur.data == key:
          self.head = cur.next
          cur = None
          return
      prev = None
      while cur and cur.data != key:
          prev = cur
          cur = cur.next
      if cur is None:
          return
      prev.next = cur.next
      cur = None

   def search_element(self, data: int) -> Node | None:
       cur = self.head
       while cur:
           if cur.data == data:
              return cur
           cur = cur.next
       return None

   def print_list(self):
      current = self.head
      while current:
          print(current.data)
          current = current.next

   # Реверс списку
   def reverse(self):
        prev = None  # Ініціалізуємо попередній вузол як None
        current = self.head  # Починаємо з голови списку
        while current:  # Поки не дійдемо до кінця списку
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev  # Розвертаємо поточний вузол
            prev = current  # Зміщуємо попередній вузол до поточного
            current = next_node  # Зміщуємо поточний вузол до наступного
        self.head = prev  # Оновлюємо голову списку

    # Сортування злиттям списку
   def merge_sort(self):
        if not self.head or not self.head.next:  # Якщо список порожній або має один елемент
            return self.head

        def get_middle(node):
            slow, fast = node, node.next  # Використовуємо два покажчики: повільний і швидкий
            while fast and fast.next:  # Поки швидкий покажчик не досягне кінця списку
                slow = slow.next  # Повільний покажчик рухається на один вузол
                fast = fast.next.next  # Швидкий покажчик рухається на два вузли
            return slow  # Повертаємо повільний покажчик, який знаходиться посередині списку

        def merge(left, right):
            dummy = Node(0)  # Створюємо тимчасовий вузол для з'єднання списків
            tail = dummy  # Використовуємо хвостовий покажчик для додавання елементів
            while left and right:  # Поки є елементи в обох списках
                if left.data < right.data:  # Порівнюємо дані лівого і правого списків
                    tail.next = left  # Додаємо лівий елемент до результату
                    left = left.next  # Переходимо до наступного елемента лівого списку
                else:
                    tail.next = right  # Додаємо правий елемент до результату
                    right = right.next  # Переходимо до наступного елемента правого списку
                tail = tail.next  # Зміщуємо хвостовий покажчик
            tail.next = left if left else right  # Додаємо залишки списку
            return dummy.next  # Повертаємо результат злиття

        def _merge_sort(node):
            if not node or not node.next:  # Якщо вузол порожній або має один елемент
                return node

            middle = get_middle(node)  # Знаходимо середину списку
            right_head = middle.next  # Отримуємо голову правої половини списку
            middle.next = None  # Розділяємо список на дві половини

            left_sorted = _merge_sort(node)  # Рекурсивно сортуємо ліву половину
            right_sorted = _merge_sort(right_head)  # Рекурсивно сортуємо праву половину

            return merge(left_sorted, right_sorted)  # Об'єднуємо відсортовані половини

        self.head = _merge_sort(self.head)  # Викликаємо рекурсивне сортування

   @staticmethod
    # Об'єднання двох відсортованих списків
   def merge_two_sorted_lists(l1, l2):
        dummy = Node(0)  # Створюємо тимчасовий вузол для з'єднання списків
        tail = dummy  # Використовуємо хвостовий покажчик для додавання елементів
        while l1 and l2:  # Поки є елементи в обох списках
            if l1.data < l2.data:  # Порівнюємо дані вузлів l1 і l2
                tail.next = l1  # Додаємо вузол l1 до результату
                l1 = l1.next  # Переходимо до наступного вузла в l1
            else:
                tail.next = l2  # Додаємо вузол l2 до результату
                l2 = l2.next  # Переходимо до наступного вузла в l2
            tail = tail.next  # Зміщуємо хвостовий покажчик
        tail.next = l1 if l1 else l2  # Додаємо залишки списку l1 або l2
        return dummy.next  # Повертаємо результат злиття

# Приклад використання
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(4)

print("Оригінальний список:")
llist.print_list()

# Приклад сортування списку
llist.merge_sort()
print("Відсортований список:")
llist.print_list()

# Приклад об'єднання двох списків
ll1 = LinkedList()
ll1.insert_at_end(1)
ll1.insert_at_end(3)
ll1.insert_at_end(5)

ll2 = LinkedList()
ll2.insert_at_end(2)
ll2.insert_at_end(4)
ll2.insert_at_end(6)

merged_head = LinkedList.merge_two_sorted_lists(ll1.head, ll2.head)

merged_list = LinkedList()
merged_list.head = merged_head
print("Об'єднаний відсортований список:")
merged_list.print_list()

# Приклад реверсування однозв'язного списку
merged_list.reverse()
print("Реверсування однозв'язного списку")
merged_list.print_list()
