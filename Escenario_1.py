# Utilizando la función print en Python, realiza la siguiente actividad,
# deberás solicitar al usuario que ingrese dos verbos,
# un adjetivo y un sustantivo en plural los cuales deberán
# ser utilizados en una frase como por ejemplo:
# ! Programa es ________! Siempre me emociona porque me
# encanta ________ problemas. !
# Aprende a _________ en el taller de Python y Alcanza tus _______!


verb1 = str(input("Inserta el primer verbo: \n"))
verb2 = str(input("Inserta el segundo verbo: \n"))
adjetivo = str(input("Inserta un adjetivo:\n"))
sustantivo = str(input("Inserta un sustantivo: \n"))

print("Progamar es {}! Siempreme emociona porque me encanta {} problmas \n. \
! Aprende a {} en el taller de Python y Alcanza \
tus {}".format(verb1, verb2, adjetivo, sustantivo))
