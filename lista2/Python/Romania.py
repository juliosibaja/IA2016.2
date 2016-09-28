
from search import *

romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

#Creation of the Problem
romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)

#Execution of the search algorithn
solution1 = breadth_first_tree_search(romania_problem );
solution2 = depth_first_graph_search(romania_problem);
solution3 = depth_limited_search(romania_problem);
solution4 = uniform_cost_search(romania_problem);
solution5 = iterative_deepening_search(romania_problem);
solution6 = best_first_graph_search(romania_problem, romania_problem.h); #greedy
solution7 = astar_search(romania_problem);

#Print
def printPath(node):
    if node.parent != None:
        printPath(node.parent);
    print(node, ', cost: ', node.path_cost);


printPath(solution1);
input();
printPath(solution2);
input();
printPath(solution3);
input();
printPath(solution4);
input();
printPath(solution5);
input();
printPath(solution6);
input();
