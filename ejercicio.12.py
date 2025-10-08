#programa12
lado=input("introduce el var de lado de un trapecio isósceles") 
base_menor=input("introduce el var del base_menor del mismo trapecio isósceles")
base_mayor=input("introduce el var del base_mayor del mismo trapecio isósceles")
altura=input("introduce el var del altura del mismo trapecio isósceles")
perímetro=float(lado)+float(lado)+float(base_menor)+float(base_mayor)
área=float(float(base_menor)+float(base_mayor))/2*float(altura)
print(f"perímetro del trapecio isósceles és":{perímetro})
print(f"área del trapecio isósceles és": {área})
