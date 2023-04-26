#Nome: Lucas Fernandes 
#Turma Comp 2022

#código 1
def inteiro_para_binario(num):
    """Função que converte um número inteiro em binário"""
    if num == 0:
        return '0'  # Trata o caso especial em que num é 0
    binario = ''
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num //= 2
    print(binario)    
    return binario

# O Algoritmo 1 converte para base 2 um número inteiro que está na base 10. Ele é um
# algoritmo iterativo que em cada iteração efetua uma divisão por 2. O dividendo inicial é o
# próprio número de entrada. O processo iterativo consta nas linhas 10 a 13, ele é feito enquanto
# o dividendo for maior do que zero (linha 10). Em cada iteração o dígito do número binário é
# calculado pelo resto da divisão do dividendo por 2 (linha 11) e é adicionado à esquerda do
# último dígito calculado (linha 12). O quociente da divisão passa ser o dividendo da iteração
# seguinte (linha 13). Caso o número inteiro a ser convertido seja zero o algoritmo retorna zero
# e termina antes de iniciar o processo iterativo (linhas 7 a 9).

####################################################################################################


#código 2
def decimal_para_binario_fracionario(num, digitos_disponiveis ):
    """Função que converte um número da forma 0,XXXXX em binário"""
    """Ela imprime os dígitos (0 ou 1) à direita da vírgula"""
    fracao = ''
    while digitos_disponiveis > 0:
        num *= 2
        if num > 1:
            fracao += '1'
            num -= 1
        else:
            if num == 1:
                fracao += '1'
                print(fracao)
                return fracao
            else:
                fracao += '0'
        digitos_disponiveis -= 1
    print(fracao)
    return fracao

# O Algoritmo 2 converte para base 2 um número decimal que está na base 10. Ele é um
# algoritmo iterativo que em cada iteração efetua uma multiplicação por 2. O fator inicial é o
# próprio número de entrada. O processo iterativo consta nas linhas 34 a 46, ele é feito enquanto
# o numero de digitos binarios for maior do que zero (linha 34). Em cada iteração é gerado um bit de cada 
# vez e adcnionando na string fracao (lnha 37) ou (linha 41). Se num é igual a 1, a função adiciona '1' 
# à string fracao e retorna a string (linha 48). Se digitos_disponiveis chega a zero, a função para e 
# retorna a string fracao atual.

###################################################################################################

#Código 3
"""Função que converte um número inteiro binário em número inteiro decimal"""
def binario_inteiro_para_decimal(num_binario):
    numero_binario = str(num_binario)
    numero_decimal = 0
    expoente = len(numero_binario) - 1
    for digito in numero_binario:
        numero_decimal += int(digito) * 2 ** expoente
        expoente -= 1
    print("O número decimal correspondente é:", numero_decimal)

# O Algoritmo 3 converte um número inteiro binário em um número inteiro decimal. Ele é um algoritmo iterativo 
# que em cada iteração multiplica cada dígito do número binário por 2 elevadoao expoente correspondente (linha 67). 
# O numero inicial é o próprio número de entrada que deve ser composto apenas por 0 ou 1. O processo iterativo consta
# nas linhas 66 a 68. Em cada interação O código percorre cada dígito do número binário, começando pelo dígito mais à 
# esquerda, e calcula o valor correspondente em decimal. A soma desses valores é atribuída à variável numero_decimal, 
# que é o valor final na base decimal. O resultado é impresso na tela usando a função print (linha 69).

##############################################################################################################################

#Código 4
"""Função que converte um número binário da forma 0,XXXX em número decimal na base 10"""
def binario_fracionario_para_decimal(num_binario_fracionario):
    numero_binario_fracionario = str(num_binario_fracionario)
    numero_decimal = 0
    expoente = - 1
    conta = 0
    for digito in numero_binario_fracionario:
        if conta >= 2:
            numero_decimal += int(digito) * 2 ** expoente
            expoente -= 1
        conta = conta + 1    
    print("O número decimal correspondente é:", numero_decimal)

# O Algoritmo 4 converte um número binário fracionário em um número decimal. Ele é um algoritmo iterativo 
# que em cada iteração percorre cada dígito do número binário fracionário. O processo iterativo consta nas 
# linhas 86 a 90. A função recebe um argumento, num_binario_fracionario, que deve ser uma string (linha 82)  
# representando a fração binária. Em seguida, itera sobre cada dígito na string, começando pelo dígito mais 
# à esquerda. Se a função encontrar um dígito que não seja o primeiro ou o segundo dígito na string (ou seja, se conta >= 2), 
# ela converte o dígito em um número inteiro e o multiplica por 2 elevado à potência negativa do expoente atual 
# (ou seja, 2 ** expoente) (linha 88). O valor resultante é adicionado a numero_decimal. O expoente é então decrementado em 1 (linha 90).

#######################################################################
#Codigo 5
def bissecao(f, e, d, tol1 , tol2, maxiter):
    """
    Encontra a raiz da função f no intervalo [e, d] com a tolerâncias tol1 e tol2 com número máximo de iterações maxiter
    Retorna o valor da raiz r e o número de iterações necessárias.
    """
    fe = f(e)
    fd = f(d)
    if fe * fd >= 0:
        raise ValueError("f(e) e f(d) devem ter sinais opostos!")
    r_anterior = e #só para entrar no loop. Poderia ser d também. 
    r = (e + d) / 2
    fr = f(r)
    n = 1 #conta iterações a partir de 1 porque já fez a primeira aproximação
    if (fr == 0):
            print(f'Bisseção: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )    
            return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
    dif_relativa = tol2 + 1 # para evitar satisfazer critério de parada
    while  abs(fr) > tol1 or abs(dif_relativa) > tol2:  # algoritmo vai parar quando os dois critérios de parada forem satisfeitos
    #while  abs(fr) > tol :    
        if (n > maxiter):
            print(f'Bissecao: Quantidade de iterações máximo ultrapassado a última raiz é: {r:.08f}')
            return (r, 1) # 1 indica que o algoritmo falhou
        if fe * fr < 0:# verifica se fica com o intervalo esquerdo
            d = r
            fd = fr
        else:
            e = r
            fe = fr
        r_anterior = r #guarda a aproximação antes de atualizá-la    
        r = (e + d) / 2
        n += 1
        fr = f(r)
        if (fr == 0):
            print(f'Bisseção: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )     
            return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
        if r != 0:
            dif_relativa = abs((r - r_anterior)/r)  # se r = 0 há divisão por zero. Nesse caso específico utiliza a diferença sem relativizar 
        else:
            dif_relativa = abs(r - r_anterior)
    print(f'Bisseção: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )     
    return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 

    # Este código está implementando o Método da Bisseção para encontrar a raiz de uma determinada função f dentro de um 
    # intervalo especificado [e, d], com tolerâncias tol1 e tol2 e um número máximo de iterações maxiter. A função começa calculando 
    # os valores de f(e) ef(d) e verificando se eles têm sinais opostos, levantando um ValueError se não tiverem. Em seguida, 
    # ele inicializa a aproximação anterior da raiz como e e a aproximação atual como o ponto médio do intervalo, (e+d)/2.
    # Em seguida, a função entra em um loop while que continua até que o valor absoluto da função avaliada na aproximação atual 
    # (|f(r)|) seja menor que tol1 ou a diferença relativa entre as aproximações atual e anterior seja menor que tol2. 
    # O loop também verifica o número máximo de iterações e retorna um código de erro 1 se o loop exceder o número máximo de 
    # iterações sem encontrar uma aproximação satisfatória. Dentro do loop, a função atualiza o intervalo [e, d] comparando os sinais 
    # de f(e) ef(r) e definindo o novo intervalo de acordo. Ele também atualiza a aproximação anterior da raiz e calcula a nova 
    # aproximação como o ponto médio do intervalo atualizado. Por fim, a função verifica se a aproximação atual é uma raiz da função 
    # e calcula a diferença relativa entre as aproximações atual e anterior.

#######################################################################  
# Codigo 6
def regula_falsi(f, e, d, tol1, tol2 ,  maxiter):
    """
    Encontra a raiz da função f no intervalo [e, d] com a tolerâncias tol1 e tol2 com número máximo de iterações maxiter
    Retorna o valor da raiz r e o número de iterações necessárias.
    """
    fe = f(e)
    fd = f(d)
    if fe * fd >= 0:
        raise ValueError("f(e) e f(d) devem ter sinais opostos!")
    r_anterior = e #só para entrar no loop. Poderia ser d também. 
    r = (e - fe*( (e - d)/(fe - fd)  ))
    fr = f(r)
    n = 1 #conta iterações a partir de 1 porque ja fez a primeira aproximação
    if (fr == 0):
            print(f'Regula Falsi: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )     
            return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
    dif_relativa = tol2 + 1 # para evitar satisfazer critério de parada
    while  abs(fr) > tol1 or  abs(dif_relativa )  > tol2  :  # algoritmo vai parar quando os dois critérios de parada forem satisfeitos
    #while  abs(fr) > tol :
        if (n > maxiter):
            print("Regula Falsi: Quantidade de iterações máximo ultrapassado, última aproximação obtida é:", r)
            return (r, 1) # 1 indica que o algoritmo falhou
        if fe * fr < 0:# verifica se fica com o intervalo esquerdo
            d = r
            fd = fr
        else:
            e = r
            fe = fr
        r_anterior = r #guarda a aproximação antes de atualizá-la    
        r = (e - fe*( (e - d)/(fe - fd)  ))
        n +=1
        fr = f(r)
        if (fr == 0):
            print(f'Regula Falsi: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )        
            return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
        if r != 0:
            dif_relativa = abs((r - r_anterior)/r)  # se r = 0 há divisão por zero. Nesse caso específico utiliza a diferença sem relativizar 
        else:
            dif_relativa = abs(r - r_anterior)
    print(f'Regula Falsi: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )     
    return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações

    # O método Regula Falsi é um algoritmo numérico de localização de raízes que usa uma combinação do método da bisseção 
    # e interpolação linear. A cada iteração, ele cria uma linha secante entre os valores da função nas duas extremidades do 
    # intervalo e encontra a interseção dessa linha secante com o eixo x. Esse ponto de interseção torna-se a nova estimativa 
    # para a raiz da função. O intervalo é então atualizado com base no sinal do valor da função na nova estimativa e o processo 
    # é repetido até que uma raiz suficientemente precisa seja encontrada ou o número máximo de iterações seja atingido. A função 
    # primeiro verifica se os valores da função nas duas extremidades têm sinais opostos. Se não o fizerem, ele gera um ValueError. 
    # Se o valor da função na nova estimativa for zero, ela retorna a estimativa como a raiz e o número de iterações como 0. Se o 
    # número máximo de iterações for atingido antes que uma raiz suficientemente precisa seja encontrada, ela retorna a última 
    # estimativa como a raiz e o número de iterações como 1 (indicando falha). A função também verifica dois critérios para 
    # interromper as iterações: o valor absoluto do valor da função na nova estimativa é menor que tol1 e o valor absoluto da 
    # diferença relativa entre a nova estimativa e a anterior é menor que tol2. Esses dois critérios garantem que a raiz seja 
    # encontrada com um nível especificado de precisão

################################################################################################################
#Código 7
def pegaso(f, e, d, tol1, tol2 ,  maxiter):
    """
    Encontra a raiz da função f no intervalo [e, d] com a tolerâncias tol1 e tol2 com número máximo de iterações maxiter
    Retorna o valor da raiz r e o número de iterações necessárias.
    """
    fe = f(e)
    fd = f(d)
    if fe * fd >= 0:
        raise ValueError("f(e) e f(d) devem ter sinais opostos!")
    r_anterior = e #só para entrar no loop. Poderia ser d também.
    fr_anterior = f(r_anterior) 
    r = (e - fe*( (e - d)/(fe - fd)  ))
    fr = f(r)
    n = 1 #conta iterações a partir de 1 porque já fez a primeira aproximação
    if (fr == 0):
        print(f'Pégaso: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )     
        return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
    dif_relativa = tol2 + 1 # para evitar satisfazer critério de parada
    while  abs(fr) > tol1 or abs(dif_relativa )  > tol2 :  # algoritmo vai parar quando os dois critérios de parada forem satisfeitos
    #while  abs(fr) > tol :
        if (n > maxiter):
            print(f'Pégaso: Quantidade de iterações máximo ultrapassado a última raiz é: {r:.08f}')
            return (r, 1) # 1 indica que o algoritmo falhou
        if fe * fr < 0:# verifica se fica com o intervalo esquerdo
            d = r
            fd = fr
            if (fr * fr_anterior > 0 and n >=2 ):  # condicao para verificar se "e" está repetindo duas vezes 
                fe = fe*(fr_anterior/(fr_anterior + fr)) #ajusta imagem de e
        else:
            e = r
            fe = fr
            if (fr * fr_anterior > 0 and n >=2 ):  # condicao para verificar se "d" está repetindo duas vezes  
                fd = fd*(fr_anterior/(fr_anterior + fr)) #ajusta imagem de d
        r_anterior = r #guarda a aproximação antes de atualizá-la    
        fr_anterior = f(r) #guarda também o valor da última aproximação
        r = (e - fe*( (e - d)/(fe - fd)  ))
        n +=1 
        fr = f(r)
        if (fr == 0):
            print(f'Pégaso: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )       
            return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
        if r != 0:
            dif_relativa = abs((r - r_anterior)/r)  # se r = 0 há divisão por zero. Nesse caso específico utiliza a diferença sem relativizar 
        else:
            dif_relativa = abs(r - r_anterior)
    print(f'Pégaso: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )    
    return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações

    # A função primeiro verifica isso f(e)e f(d)tem sinais opostos, o que é necessário para que o método Pegasus funcione. 
    # Em seguida, ele calcula a primeira aproximação r da raiz usando a fórmula Pegasus e inicia um loop que atualizará e e 
    # d calculará novas aproximações até que os critérios de parada sejam atendidos. Os critérios de parada são que o erro 
    # absoluto |f(r)| seja menor que tol1ou o erro relativo |r - r_anterior| / |r| seja menor que tol2. A função também verifica 
    # se o número de iterações nnão excede maxiter, e retorna um valor de (r, 0)se a raiz for encontrada ou (r, 1) se o número
    # máximo de iterações for excedido. A função imprime o resultado final, que é o valor da raiz re o número de iterações n.

########################################################################################################################

#codigo 8
def newton(f, df, x0, tol1, tol2, maxiter):
    """
    Encontra uma raiz da função f a partir de um ponto x0. Não tem eficácia garantida em todos o casos
    Precisa fornecer a derivada da função df. 
    """
    n = 0 # conta iterações
    r = x0 # primeira aproximacao para a raiz
    r_anterior = r + 1000 # qualquer valor distante de r  
    fr = f(r)
    dfr = df(r)
    if (fr == 0):
        print(f'Newton: a raiz é: {r:.08f}', 'Quantidade de iterações é', n)    
        return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
    dif_relativa = tol2 + 1 # para evitar satisfazer critério de parada
    while abs(fr) > tol1 or abs(dif_relativa)  > tol2  :
    #while abs(f.subs(x, r)) > tol1 or  abs( (r - r_anterior)/r  > tol2  ):
        n += 1
        if (n > maxiter):
            print(f'Newton: Quantidade de iterações máximo ultrapassado a última raiz é: {r:.08f}')
            return (r, 1) # 1 indica que o algoritmo falhou
        r_anterior = r
        r = r - fr/dfr
        fr = f(r)
        dfr = df(r)
        if (fr == 0):
            print(f'Newton: a raiz é: {r:.08f}', 'Quantidade de iterações é', n )       
            return (r, 0) # 0 indica que a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 
        if r != 0:
            dif_relativa = abs((r - r_anterior)/r)  # se r = 0 há divisão por zero. Nesse caso específico utiliza a diferença sem relativizar 
        else:
            dif_relativa = abs(r - r_anterior)
    print(f'Newton: a raiz é: {r:.08f}',  'Quantidade de iterações é', n )    
    return (r, 0) # 0 indica que uma a raiz foi encontrada com a precisão dada dentro do número máximo de iterações 

    # A função retorna uma tupla contendo a raiz estimada e um sinalizador indicando se o método convergiu ou não.
    # O algoritmo funciona inicializando algumas variáveis ​​e, em seguida, entrando em um loop que melhora iterativamente
    # a estimativa da raiz. O loop continua até que o erro absoluto ou o erro relativo seja menor que suas respectivas 
    # tolerâncias, ou até que o número máximo de iterações seja atingido. A cada iteração, o algoritmo calcula o valor 
    # da função e a derivada na estimativa atual da raiz e atualiza a estimativa usando a fórmula de Newton-Raphson. 
    # Ele também calcula o erro relativo entre a estimativa atual e a anterior e verifica se é menor que a tolerância.
    # Se o valor da função na estimativa atual for exatamente zero, o algoritmo encontrou uma raiz e a retorna imediatamente. 
    # Se o erro relativo for muito grande ou o número máximo de iterações for atingido, o algoritmo termina e retorna a estimativa 
    # atual junto com um sinalizador indicando falha na convergência.

####################################################################################################################
   
#Exemplo:

#Definição da funcao
import math  # biblioteca para usar função matemáticas
def f(x):
    #return math.sin(x)
    return x**2 - 1
#e,d, tol1, tol2, maxiter = -3 , 0.5 , 0.000000000001, 0.0001 , 5000
e,d, tol1, tol2, maxiter = 0 , 10 , 0.000000000001, 0.0001 , 5000  
bissecao(f, e, d, tol1, tol2,  maxiter)
regula_falsi(f, e, d, tol1, tol2, maxiter)
pegaso(f, e, d, tol1, tol2, maxiter)


#Método de Newton 
def df(x):
    #return math.cos(x)
    return 2*x
#x0 = -1
x0 = 5
newton(f,df, x0 ,tol1,tol2, maxiter) 

## Para executar funções implementadas em uma máquina que opera com windows com o Python instalado:
## 1) Abrir prompt de comando 
## 2) Acessar no prompt de comando a pasta onde este arquivo está salvo
## 3) Digitar no terminal: python codigos.py## Testando... 
#binario_fracionario_para_decimal(0.1011)
#decimal_para_binario_fracionario(0.0001, 10)
#binario_fracionario_para_decimal(0.5)
## 4) Digitando no terminal: python codigos.py
## 5) Deve imprimir 10011001 na tela


##################################################################################
########################### MÉTODO DE LAGRANGE ##################################
#################################################################################
# Código 9
def lagrange_interpolation(x_values, y_values, x):
    """
    Realiza a interpolação polinomial de Lagrange para encontrar o valor de y correspondente a um dado valor x.
    
    Parâmetros:
    x_values (list): lista de valores x conhecidos
    y_values (list): lista de valores y correspondentes aos valores x conhecidos
    x (float): valor de x para o qual queremos encontrar o valor correspondente de y
    
    Retorna:
    y (float): valor interpolado de y correspondente a x
    """
    n = len(x_values)  # quantidade de pontos
    y = 0.0 
    
    for i in range(n):   #constroi cada polinômio de lagrange
        # Calcula o valor do polinômio de Lagrange L_i(x)
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
        
        # Adiciona o termo do polinômio interpolador correspondente a y[i]
        y += y_values[i] * L_i
    print("O valor interpolado de p(", x, ") é", y,  " utilizando o Método de Lagrange")
    return y

#Exemplo: interpola polinomialmente o valor de 9 considerando os pontos (1,1); (4,2) e (16,4)   
x_values = [-3, -1, 1, 3]
y_values = [-2, 8, 0, 5]
lagrange_interpolation(x_values, y_values, 0)



#################################################################################
########################### MÉTODO DE NEWTON ####################################
#################################################################################

#Código 10
def diferenca_dividida(pontos):
    n = len(pontos)
    tabela = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        tabela[i][0] = pontos[i][1]
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (pontos[i+j][0] - pontos[i][0])
    return tabela[0]

def polinomio_interp(x, pontos):
    n = len(pontos)
    a = diferenca_dividida(pontos)
    resultado = a[n-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - pontos[i][0]) + a[i]
    print("O valor interpolado de p(", x, ") é", resultado,  " utilizando o Método de Newton")
    return resultado

#Exemplo: interpola polinomialmente o valor de 9 considerando os pontos (1,1); (4,2) e (16,4)  
pontos = [(1,1), (4,2), (16,4)]
x = 0
valor_interp = polinomio_interp(x, pontos)