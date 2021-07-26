class KNN():
        
    # Método Construtor
    def __init__(self, dados_1, dados_2, k):
        """
        dados_1: lista data
        dados_2: lista no_class
        k: numero int ímpar 
        """
        self.dados_1 = dados_1
        self.dados_2 = dados_2
        self.k = k
        
    # Método para calcular a distância entre os pontos
    def distancia(self):
        """Função para calcular distância entre os pontos"""
        lista_distancia = []
        for x in range(len(self.dados_2)):
            lista = []
            for y in range(len(self.dados_1)):
                dist = 0
                for z in range(len(self.dados_1[0][2])):
                    dist += (self.dados_2[x][2][z] - self.dados_1[y][2][z])**2
                dist = dist**(1/2)
                resultado = dist
                lista.append([resultado, self.dados_1[y][1]])
            lista_distancia.append(lista)
        return lista_distancia
    
    def lista_sort(self, lista):
        """Função para determinar as menores distâncias
        lista = lista gerada do método 'distancia'"""
        lista_sort = []
        for x in range(len(lista)):
            lista_sel = lista[x]
            lista_sel = sorted(lista_sel, key= lambda x: x[0])
            lista_sort.append(lista_sel)
        return lista_sort
    
    def classificação(self, lista):
        """Função para classificar o perfil de acordo com o valor de k
        lista = lista gerada do método 'lista_sort'"""
        lista_classificacao = []
        for x in range(len(lista)):
            classificacao = []
            for y in range(self.k):
                classificacao.append(lista[x][y][1])
            lista_classificacao.append(classificacao)
        return lista_classificacao
    
    def count(self,lista):
        """Função que determina o perfil
        lista = lista gerada do método 'classificacao'"""
        classificacao = []
        for x in range(len(lista)):
            conservador = lista[x].count("Conservador")
            moderado = lista[x].count("Moderado")
            agressivo = lista[x].count("Agressivo")
            if conservador > moderado and conservador > agressivo:
                resultado = "Conservador"
                classificacao.append(resultado)
            elif moderado > conservador and moderado > agressivo:
                resultado = "Moderado"
                classificacao.append(resultado)
            else:
                resultado = "Agressivo"
                classificacao.append(resultado)
        return classificacao
    
    def dic(self, lista):
        """Função que gera um dicionário do perfil de acordo com o cpf
        lista = lista gerada do método 'count'"""
        classificacao_perfil = []
        for x in range(len(lista)):
            var = [self.dados_2[x][0], lista[x]]
            classificacao_perfil.append(var)
        return dict(classificacao_perfil)