# Import modules
import json

# Scene class
class Scene():
    
    # Constructor
    def __init__(self, name, ID, rootNode, settings, nodeTree, parent=None):
        self.name = name
        self.ID = ID
        self.rootNode = rootNode
        self.settings = settings
        self.nodeTree = nodeTree
        self.parent = parent
    
    # Getter for root node
    def getRoot(self):
        return self.rootNode

# Load scene from file
def loadScene(sceneFile):
    # Open, read & close specified file
    scene = open(sceneFile, 'r')
    sceneData = scene.read()
    scene.close()

    # Return JSON object
    sceneObject = json.loads(sceneData)
    return sceneObject
