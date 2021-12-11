# Node class
class Node():

    # Constructor
    def __init__(self, name, ID, nodeTree, parent=None):
        self.name = name
        self.ID = ID
        self.nodeTree = nodeTree
        self.parent = parent

    # Awake event (Initialization)
    def awake(self):
        pass
    
    # Start event (After initialization)
    def start(self):
        pass
    
    # Update event (For input handling)
    def update(self, deltaTime):
        pass

    # Render event (After update, for rendering)
    def render(self, deltaTime):
        pass
    
    # Destroy event (Once node is destroyed)
    def destroy(self):
        pass