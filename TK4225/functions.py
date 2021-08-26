

class cisBoyz(object):
    def __init__(self):
        super(cisBoyz, self).__init__()

    def example(self,param1,param2):
        """
        *** Description ***\n
        This is a test

        *** Function ***\n
        params:
            - param1
            - param2
        returns:
            - string with params 
        """
        print("u are geh", param1, param2)

    def LotkaVolterra(self, y, t):
        #
        # parameters
        alpha = 1.1
        beta  = 0.7
        gamma = 0.4
        delta = 0.1
        #
        # get the individual variables - for readability
        yPrey = y[0]
        yPred = y[1]
        #
        # individual derivatives
        dyPreydt  =   alpha * yPrey - beta  * yPrey * yPred
        dyPreddt  = - gamma * yPred + delta * yPrey * yPred
        #
        return [ dyPreydt, dyPreddt ]

    
        
        