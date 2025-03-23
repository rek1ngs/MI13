import Heiristic


# ----------------------------
# MINIMAX FUNKCIJA
# ----------------------------
# Pēc #https://graspcoding.com/build-a-tic-tac-toe-python-game-using-the-minimax-algorithm/ pseidokoda
# Izmantojot ChatGTP + nedaudz pielabots
# Tiek ievadīts funkcijā virsotne, dziļums, spēles koks un sākuma spēlētajs
def minimax(current_node, depth, game_tree, is_maximizing_player, maksimizetajs):

    # Tad mēs pārbaudām ja dziļums ir nulle (ja nav virsotnu) un vai ir gala virsotne (izsauc papildus funkciju)
    if depth == 0 or is_terminal(current_node, game_tree):
        heuristic_value = Heiristic.heiristiska(current_node, maksimizetajs)
        print(f"Terminal or max depth reached: virkne={current_node.virkne}, Heuristic value={heuristic_value}")
        return heuristic_value, current_node 

    # Mēs izejam katram bērnam no loku kopas pēc sobrīdējas virsotnes
    if is_maximizing_player:
        best_value = float('-inf')
        best_node = None
        for child_id in game_tree.loku_kopa.get(current_node.id, []):
            child = find_node_by_id(game_tree, child_id)
            value, _ = minimax(child, depth - 1, game_tree, False, maksimizetajs)
            if value > best_value:
                best_value = value
                best_node = child
        return best_value, best_node
    else:
        best_value = float('inf')
        best_node = None
        for child_id in game_tree.loku_kopa.get(current_node.id, []):
            child = find_node_by_id(game_tree, child_id)
            value, _ = minimax(child, depth - 1, game_tree, True, maksimizetajs)
            if value < best_value:
                best_value = value
                best_node = child
        return best_value, best_node





# ----------------------------
# ALFA BETA FUNKCIJA
# ----------------------------
# https://www.geeksforgeeks.org/alpha-beta-pruning-in-adversarial-search-algorithms/
# Ar papildus labojumiem


def alpha_beta_pruning(node, depth, alpha, beta, player_1, game_tree, maximizing_player, maksimizetajs):

    # Tad mēs pārbaudām ja dziļums ir nulle (ja nav virsotnu) un vai ir gala virsotne (izsauc papildus funkciju)
    if depth == 0 or is_terminal(node, game_tree):
        return Heiristic.heiristiska(node, maksimizetajs)

    #Saglabāsim labāko virsoni uz kuru pārvietoties
    best_child = None

    # Ja šobrīd ir maksimizēšana, tad
    if maximizing_player:

        # Sagatavojam mainīgos glabāšanai
        max_eval = float('-inf')

        # Mēs izejam katram bērnam no loku kopas pēc sobrīdējas virsotnes
        for child in game_tree.loku_kopa.get(node.id, []):
            # Attiecīgi no child_id mes atrodam šo virsotni
            child = find_node_by_id(game_tree, id)
            # Attiecīgi novērtējam šī virsotnes bērnus
            eval, _ = alpha_beta_pruning(child, depth-1, alpha, beta, player_1, game_tree, maximizing_player, maksimizetajs)
            # Atrod no šobrīdejā un atrastā maksimālo vērtību
            if eval > max_eval:
                max_eval = eval
                best_child = child
            # Tiek pārbaudīta alpha vērtība
            alpha = max(alpha, eval)
            # Ja beta vērtība ir mazāka vai vienāda par alpha veicam nogriešanu beta
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval, best_child
    


    # Ja šobrīd ir minimizētaja, tad
    else:
        # Sagatavojam mainīgos glabāšanai
        min_eval = float('inf')
        # Mēs izejam katram bērnam no loku kopas pēc sobrīdējas virsotnes
        for child in game_tree.loku_kopa.get(node.id, []):
            # Attiecīgi no child_id mes atrodam šo virsotni
            child = find_node_by_id(game_tree, id)
            # Attiecīgi novērtējam šī virsotnes bērnus
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, player_1, game_tree,  maximizing_player, maksimizetajs)
            # Atrod no šobrīdejā un atrastā minimālo vērtību
            if eval < min_eval:
                min_eval = eval
                best_child = child
            # Tiek pārbaudīta beta vērtība
            beta = min(beta, eval)
            # Ja beta vērtība ir mazāka vai vienāda par alpha, veicam nogriešanu
            if beta <= alpha:
                break 
        return min_eval, best_child

# ----------------------------
# ALFA BETA FUNKCIJA #2
# ----------------------------
# https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/
# Ar papildus labojumiem


'''
class AlphaBeta:
    def __init__(self, game_tree):
        self.game_tree = game_tree  # Your Speles_koks object
        self.root = game_tree.virsotnu_kopa[0]  # Root node (first node in virsotnu_kopa)
        return

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.get_successors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print(f"AlphaBeta: Utility Value of Root Node: {best_val}")
        print(f"AlphaBeta: Best State is: {best_state.virkne}")
        return best_state

    def max_value(self, node, alpha, beta):
        print(f"AlphaBeta–>MAX: Visited Node :: {node.virkne}")
        if self.is_terminal(node):
            return self.get_utility(node)
        infinity = float('inf')
        value = -infinity

        successors = self.get_successors(node)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        print(f"AlphaBeta–>MIN: Visited Node :: {node.virkne}")
        if self.is_terminal(node):
            return self.get_utility(node)
        infinity = float('inf')
        value = infinity

        successors = self.get_successors(node)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    # Utility methods
    def get_successors(self, node):
        assert node is not None
        # Get child nodes from loku_kopa
        child_ids = self.game_tree.loku_kopa.get(node.id, [])
        return [self.find_node_by_id(child_id) for child_id in child_ids]

    def is_terminal(self, node):
        assert node is not None
        return len(self.game_tree.loku_kopa.get(node.id, [])) == 0

    def get_utility(self, node):
        assert node is not None
        # Use your heuristic function to evaluate the node
        from Heiristic import heiristiska
        return heiristiska(node, 'P1')  # Adjust 'P1' or 'P2' based on the player

    def find_node_by_id(self, node_id):
        for node in self.game_tree.virsotnu_kopa:
            if node.id == node_id:
                return node
        return None
'''



# ----------------------------
# PALĪGFUNKCIJAS ALGORITMIEM
# ----------------------------
# Izmantojot ChatGTP + nedaudz pielabots
#Funckijas noskaidro vai ir strupceļvirsotne
def is_terminal(node, game_tree):
    # Pārbauda vai virsotnei vairs nav bērnu, ja nav tad ta ir strupceļa
    return len(game_tree.loku_kopa.get(node.id, [])) == 0


# Izmantojot ChatGTP + nedaudz pielabots
#Funckija atrod virsotni no id
def find_node_by_id(game_tree, node_id):
    # Ņemam katru virsotni no visas kopas
    for node in game_tree.virsotnu_kopa:
        # Ja virstnes id sakrīt ar meklētas virstones id
        if node.id == node_id:
            #Atgriežam virsotni
            return node
    return None
