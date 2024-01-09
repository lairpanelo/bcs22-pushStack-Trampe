# Improved the code-based to display the "Stack overflow", "Empty" and "Element is already in stack"
class PushStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, data):
        if not self.is_full():
            if data not in self.stack:
                self.top += 1
                self.stack.append(data)
                print(f"{data} pushed to the stack")
            else:
                print(f"[{data}] is already in stack")
        else:
            print(f"Stack overflow! Element: [{data}]")

    def pop(self):
        if self.is_empty():
            print("Underflow")
        else:
            popped_element = self.stack.pop(self.top)
            self.top -= 1
            print(f"Popped element: {popped_element}")

    def display_elements(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Elements in the stack:")
            print(f"{self.stack}")


stack = PushStack(max_size=5)

stack.push("Jungkook")
stack.push("V")
stack.push("Jimin")
stack.push("Jimin")
stack.push("RM")
stack.push("Suga")

stack.push("Jin")

stack.push("J-hope")

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()


stack.pop()

stack.display_elements()
