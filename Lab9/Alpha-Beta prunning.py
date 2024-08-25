import math

# Node class to define the structure of a node in the tree
class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def minimax(node, depth, maximizingPlayer, alpha, beta):
    if depth == 0 or is_terminal_node(node):
        return evaluate_node(node)
    
    if maximizingPlayer:
        maxEval = -math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, False, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return maxEval
    else:
        minEval = math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return minEval

def is_terminal_node(node):
    return len(node.children) == 0

def evaluate_node(node):
    return node.value

def get_children(node):
    return node.children

# Example tree structure
root_node = Node(
    children=[
        Node(3),
        Node(
            children=[
                Node(5),
                Node(6)
            ]
        ),
        Node(
            children=[
                Node(9),
                Node(1)
            ]
        )
    ]
)

# Define the depth (assuming we're evaluating 3 levels deep)
depth = 3

# Initial call to the function
best_value = minimax(root_node, depth, True, -math.inf, math.inf)
print("Best value:", best_value)
