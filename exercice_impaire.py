def impairs(a,b):
    resultat = []
    for imp in range(int(a),int(b)):
        if imp % 2 != 0 :
            resultat.append(imp)

    return resultat
        
print (impairs(26.3,52.4))
