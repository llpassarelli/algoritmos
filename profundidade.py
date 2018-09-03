
grafo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
adj = [[1,2,3],[2,4,5],[3,6,7],[4,8,9],[5,10,11],[6,12,13],[7,14,15]]

print ("grafo", grafo)
print ("adj", adj)

def busca_profundidade():
	visited=[]
	stack=[]
	remove=False
	print 'busca em profundidade'
	stack.append(grafo[0])
	while len(stack)>0 and len(visited) < len(grafo):
			v=stack[0]
			print 'stack', stack
			print 'visitando', v
			print 'visited', visited
			if not v in visited:
				visited.append(v)
				#pecorre lista de adjacencia		
				for a in adj:
					# tem adjacentes 
					if a[0]==v and len(a)>1: 
						print 'adjacentes:', v, a[1:]
						#percorre os adjacentes
						for ad in a[1:]:
							if not ad in stack and not ad in visited: #nao foi visitado				
								stack.insert(0,ad)
			elif len(stack)>0:
				print 'stack', stack
				stack.pop(0)
								
	print 'visitados profundidade', visited

busca_profundidade()