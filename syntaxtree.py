import re

cmdline = "echo hello world;echo \"great\" ; ls -l ; echo seomthing else" 

class Node:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Tree(Left: {self.left}, Value: {self.value}, Right: {self.right})"


    def get(self, element):
        current = self
        while current is not None:
            if current.value == element:
                return True
            elif element < current.value:
                current = current.left
            elif element > current.value:
                current = current.right
            else:
                print("Invalid Case")
        return False


    def put(self, element):
        if self.value == None:
            self.value = element
            return True
        
        current = self
        while current is not None:
            if element < current.value:
                if current.left is None:
                    current.left = Node(element)
                    return True
                else:
                    current = current.left
            elif element > current.value:
                if current.right is None:
                    current.right = Node(element)
                    return True
                else:
                    current = current.right
            elif element == current.value:
                current.value = element
                return True
            else:
                print("Invalid Case")





def parse(cmdline):
    root = Node(None, None, None)
    pattern = r"([^;|>]+)([;|>])(.*)"
    match = re.match(pattern, cmdline)
    if match:
        s1 = parse(match.group(1))
        s2 = match.group(2)
        s3 = parse(match.group(3))
        root = Node(s2, s1, s3)
    else:
        root = Node(cmdline, None, None)
    return root

root = parse(cmdline)
print(root)





