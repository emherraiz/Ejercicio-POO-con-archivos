class Parte_1:
    def __init__(self, df):
        self.df = df

    def ordenar(self):
        return self.df.sort_values(by = 'Apellidos')
