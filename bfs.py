from collections import deque

graph = {}
graph["__init__"] = ["if", "while", "break"]
graph["while"] = ["def"]
graph["if"] = ["def"]
graph["break"] = ["x >= y"]
graph["def"] = []

def item_exists(serch_item, item):
    if serch_item in item:
      return item

def search(serch_item, item):
    search_queue = deque()
    search_queue += graph[item]
    visited = []
    while search_queue:
        check_item = search_queue.popleft()
        if not check_item in visited:
            if item_exists(serch_item, check_item):
                print (check_item)
                break
            else:
                search_queue += graph[check_item]
                visited.append(check_item)
    return False

serch_item = input()
search(serch_item, "__init__")