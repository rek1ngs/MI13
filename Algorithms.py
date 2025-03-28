# ----------------------------
# Informācijas avots Python:
# https://www.w3schools.com/python/
# ----------------------------



import Heiristic


# ----------------------------
# MINIMAX FUNKCIJA
# ----------------------------

# Informācijas avots (Ghimire. Build a Tic-Tac-Toe Python Game using the minimax algorithm. Tiešsaistē. n. d. Pieejams: https://graspcoding.com/build-a-tic-tac-toe-python-game-using-the-minimax-algorithm/ [skatīts 03.03.2025.])
# Modificēts no (Shalvale. Alpha-Beta pruning in Adversarial Search Algorithms. Tiešsaistē. n. d. Pieejams: https://www.geeksforgeeks.org/alpha-beta-pruning-in-adversarial-search-algorithms/ [skatīts 03.03.2025.])

# ! Tiek ievadīts funkcijā virsotne, dziļums, spēles koks un sākuma spēlētajs
# ! Dators vienmēr būs maksimizētājs
def minimax(current_node, depth, game_tree, is_maximizing_player, maksimizetajs):

    # Tad mēs pārbaudām ja dziļums ir nulle (ja nav virsotnu) un vai ir gala virsotne (izsauc papildus funkciju)
    if depth == 0 or is_terminal(current_node, game_tree):
        heuristic_value = Heiristic.heiristiska(current_node, maksimizetajs)
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

# Modificēts no (Shalvale. Alpha-Beta pruning in Adversarial Search Algorithms. Tiešsaistē. n. d. Pieejams: https://www.geeksforgeeks.org/alpha-beta-pruning-in-adversarial-search-algorithms/ [skatīts 03.03.2025.])



def alpha_beta_pruning(current_node, depth, alpha, beta, game_tree, is_maximizing_player, maksimizetajs):

    # Tad mēs pārbaudām ja dziļums ir nulle (ja nav virsotnu) un vai ir gala virsotne (izsauc papildus funkciju)
    if depth == 0 or is_terminal(current_node, game_tree):
        heuristic_value = Heiristic.heiristiska(current_node, maksimizetajs)
        return heuristic_value, current_node 

    #Saglabāsim labāko virsoni uz kuru pārvietoties
    best_child = None

    # Ja šobrīd ir maksimizēšana, tad
    if is_maximizing_player:

        # Sagatavojam mainīgos glabāšanai
        max_eval = float('-inf')

        # Mēs izejam katram bērnam no loku kopas pēc sobrīdējas virsotnes
        for child_id in game_tree.loku_kopa.get(current_node.id, []):
            # Attiecīgi no child_id mes atrodam šo virsotni
            child = find_node_by_id(game_tree, child_id)
            # Attiecīgi novērtējam šī virsotnes bērnus
            eval, _ = alpha_beta_pruning(child, depth-1, alpha, beta, game_tree, False, maksimizetajs)
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
        for child_id in game_tree.loku_kopa.get(current_node.id, []):
            # Attiecīgi no child_id mes atrodam šo virsotni
            child = find_node_by_id(game_tree, child_id)
            # Attiecīgi novērtējam šī virsotnes bērnus
            eval, _ = alpha_beta_pruning(child, depth-1, alpha, beta, game_tree,  True, maksimizetajs)
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
# PALĪGFUNKCIJAS ALGORITMIEM
# ----------------------------

# !!!!!!!!!!!!!!!!!!!!!!
# Aizgūts no (OpenAI. ChatGPT https://chatgtp.com/)
# !!!!!!!!!!!!!!!!!!!!!!

#Funckijas noskaidro vai ir strupceļvirsotne
def is_terminal(node, game_tree):
    # Pārbauda vai virsotnei vairs nav bērnu, ja nav tad ta ir strupceļa
    return len(game_tree.loku_kopa.get(node.id, [])) == 0

#Funckija atrod virsotni no id
def find_node_by_id(game_tree, node_id):
    # Ņemam katru virsotni no visas kopas
    for node in game_tree.virsotnu_kopa:
        # Ja virstnes id sakrīt ar meklētas virstones id
        if node.id == node_id:
            #Atgriežam virsotni
            return node
    return None