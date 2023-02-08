
from dijsktra import Graph
    
def run_gas_graph():
  edges =[
    ("Vn", "LV", 327),
    ("Vn", "Bo", 561),
    ("Vn", "NY", 603),
    ("Mi", "NY", 237),
    ("Ch", "NY", 226),
    ("Ch", "LV", 254),
    ("NY", "FL", 299),
    ("NY", "LV", 617),
    ("NY", "Bo", 133),
    ("FL", "LV", 99),
    ("FL", "LA", 676),
    ("LA", "SL", 222),
    ("LV", "SL", 69),
    ("FL", "Bo", 465),
    ("LA", "LV", 169)

  ]
  graph = Graph(edges)
  start = 'SL'
  stop = 'Mi'
  
  path = graph.dijsktra_shortest_path(start, stop)
  
  (S, *L, F) = path
  
  layover = 0

  while layover < len(L):
    
    layover = layover + 1 
 
  print (str("There is"), int(layover), str("Layovers they are"), L, str("."))
  print(str("This is your flight path:"), path)




def main():
  
  run_gas_graph()

if __name__ == "__main__":
  main()
  