import sys
import community
import networkx as nx
import itertools

def read_dimacs_format(lines):
    number_of_variables = None
    number_of_clauses = None
    
    clauses = []

    for line in lines:
        tokens = line.split()
        if not len(tokens) or tokens[0] == 'c':
            continue
	elif tokens[0] == 'p' and tokens[1] == 'cnf':
            number_of_variables = int(tokens[2])
            number_of_clauses = int(tokens[3])
        elif tokens[-1] == '0':
            clause = [int(i) for i in tokens[:-1]]
            clauses.append(clause)
    return number_of_variables, number_of_clauses, tuple(clauses)

def build_graph(G, sat_instance):
    '''
    Construct Variable Incidence Graph 
    '''
    for clause in sat_instance:
        if len(clause) > 1:
            weight = 1.0 / (len(clause) - 1)
            for combination in itertools.combinations(clause, 2):
                a=abs(combination[0])
                b=abs(combination[1])
                if G.has_edge(a, b):
                    G[a][b]['weight']+=weight
                else:
                    G.add_edge(a, b, weight=weight)

if __name__ == '__main__':
    filename = sys.argv[1]
    
    content = []
    with open(filename, "r") as f:
        content = f.readlines()

    number_of_variables, number_of_clauses, sat_instance = read_dimacs_format(content)
    G = nx.Graph()
    build_graph(G, sat_instance)
    
    partition = community.best_partition(G)
    
    for k in partition.keys():
        print("{0} {1}".format(k - 1, partition[k]))
    
