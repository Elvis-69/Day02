annee = int(input("Saissez une année.\n"))
if (annee%4 != 0 ) :
  print ("Cette année n'est pas bissextile.")
else :
  if (annee%100 == 0 and annee%400 != 0) :
    print ("Cette année n'est pas bissextile")
  else :
    print ("Cette année est bissextile")