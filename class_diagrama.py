class diagrama:
    def __init__(self):
        self.codigo=""
        self.variables={"numero_var":0}
        self.identacion=""
    def fin(self):
        self.codigo+="raw_input('')" 
        print self.codigo
    def ingreso(self,nombre_var,texto,tipo_var):
        self.codigo+=self.identacion
        if(tipo_var=="entero"):self.codigo+=nombre_var+"=int(raw_input("+texto+")) \n"
        elif(tipo_var=="decimal"):self.codigo+=nombre_var+"=float(raw_input("+texto+")) \n"
        else:self.codigo+=nombre_var+"=raw_input("+texto+") \n"      
    def salida(self,*elementos):
        self.codigo+=self.identacion
        self.codigo+="print "
        salida=""         
        for elemento in elementos:
            salida+="str("+elemento+")"+" + "
        salida=salida[0:-3]
        self.codigo+=salida+"\n"
    def asignacion (self,tipo_var,nombre_var,nuevo_valor):
        self.codigo+=self.identacion
        if(tipo_var=="entero"): self.codigo+= nombre_var+" = "+nuevo_valor+" \n"
    def condicional(self,valor1,condicion,valor2):
        self.codigo+=self.identacion
        self.codigo+="if("+ valor1 +condicion + valor2+"): \n"
        self.identacion+="\t"
    def fin_buble_o_condicional(self):
        self.identacion=self.identacion[0:-1]
    def si_no(self,valor1,condicion,valor2):
        self.identacion=self.identacion[0:-1]
        self.codigo+=self.identacion
        self.codigo+="elif("+ valor1 +condicion + valor2+"): \n"
        self.identacion+="\t"
    def de_lo_contrario(self):
        self.identacion=self.identacion[0:-1]
        self.codigo+=self.identacion
        self.codigo+="else: \n"
        self.identacion+="\t"
    def bucle(self,numero_iteraciones):
        self.codigo+=self.identacion
        self.codigo+="for i in range("+numero_iteraciones+"): \n"
        self.identacion+="\t"



sombra=diagrama()
sombra.ingreso("num1","'ingrese numero 1: '","entero")
sombra.ingreso("num2","'ingrese numero 2: '","entero")
sombra.condicional("num1","==","num2")
sombra.salida("'Numero 1 es igual a Numero 2, se multiplicara'")
sombra.asignacion("entero","num3","num1*num2")
sombra.salida("'numero1= '","num1","' * '","'numero2= '","num2","' = '","'numero3='","num3")
sombra.si_no("num1","<","num2")
sombra.salida("'Numero 1 es menor a Numero 2, se sumara'")
sombra.asignacion("entero","num3","num1+num2")
sombra.salida("'numero1= '","num1","' + '","'numero2= '","num2","' = '","'numero3='","num3")
sombra.de_lo_contrario()
sombra.salida("'Numero 1 es mayor a Numero 2, se realizara un blucle de '","num2","' iteraciones.'")
sombra.asignacion("entero","num4","0")
sombra.bucle("num2")
sombra.asignacion("entero","num4","num4+1")
sombra.salida("num4")
sombra.fin_buble_o_condicional()
sombra.fin()   

##accion=1
##sombra=diagrama()
##while (accion!=0):
##    print "Ya se ha iniciado, que desea hacer ahora"
##    print "1 => Pedir una valor"
##    print "2 => Mostrar un mensaje"
##    print "3 => asignar un valor"
##    print "4 => Abrir una condicional"
##    print "5 => Abrir un bucle"
##    
##    print "0 => Teminar"
##    accion = raw_input("Escoga una opcion")
##    if(action=="0"):break
##    if(action=="1"):
##        men=raw_input("Que mensaje desea mostar para pedir el valor:")
##
##
##sombra.ingreso("num","'ingrese numero: '","entero")
##sombra.salida("'nuevo numero: '","num")
##sombra.condicional("num","==","3")
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.si_no("num","==","4")
##sombra.salida("'nuevo numero: '","num")
##sombra.condicional("num","==","3")
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.si_no("num","==","4")
##sombra.salida("'nuevo numero: '","num")
##sombra.bucle("4")
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.bucle("4")
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.fin_buble_o_condicional()
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.fin_buble_o_condicional()
##sombra.salida("'nuevo numero: '","num")
##sombra.si_no("num","==","5")
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.de_lo_contrario()
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.fin_buble_o_condicional()
##sombra.salida("'nuevo numero: '","num")
##sombra.si_no("num","==","5")
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.de_lo_contrario()
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")
##sombra.fin_buble_o_condicional()
##sombra.salida("'nuevo numero: '","num")
##sombra.salida("'nuevo numero: '","num")


##################################################################################################################

##sombra.ingreso("num","'ingrese numero: '","entero")
##sombra.salida("'numero= '","num ","' numero2= '","num")
##sombra.asignacion("entero","num","num+1")
##sombra.salida("'nuevo numero: '","num")
##sombra.asignacion("entero","num","'Hola'")
##sombra.salida("'nuevo numero: '","num")
##sombra.asignacion("entero","num","3")
##sombra.condicional("num","==","3")
##sombra.salida("'dentro del if: '","num")
##sombra.condicional("num","==","3")
##sombra.salida("'dentro del if: '","num")
##sombra.si_no("num","==","4")
##sombra.salida("'dentro del if: '","num")
##sombra.si_no("num","==","5")
##sombra.salida("'dentro del if: '","num")
##sombra.de_lo_contrario()
##sombra.salida("'dentro del if: '","num")
##sombra.fin_condicional()
##sombra.de_lo_contrario()
##sombra.salida("'dentro del if: '","num")
##sombra.fin_condicional()
##sombra.salida("'dentro del if: '","num")
##sombra.salida("'dentro del if: '","num")
##
##sombra.salida("'dentro del if: '","num")
##sombra.fin()

num1=int(raw_input('ingrese numero 1: ')) 
num2=int(raw_input('ingrese numero 2: ')) 
if(num1==num2): 
	print str('Numero 1 es igual a Numero 2, se multiplicara')
	num3 = num1*num2 
	print str('numero1= ') + str(num1) + str(' * ') + str('numero2= ') + str(num2) + str(' = ') + str('numero3=') + str(num3)
elif(num1<num2): 
	print str('Numero 1 es menor a Numero 2, se sumara')
	num3 = num1+num2 
	print str('numero1= ') + str(num1) + str(' + ') + str('numero2= ') + str(num2) + str(' = ') + str('numero3=') + str(num3)
else: 
	print str('Numero 1 es mayor a Numero 2, se realizara un blucle de ') + str(num2) + str(' iteraciones.')
	num4 = 0 
	for i in range(num2): 
		num4 = num4+1 
		print str(num4)
raw_input('')
