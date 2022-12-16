# Реализуйте класс Table, который хранит целые числа в двумерной таблице. При инициализации Table(rows, cols) 
# экземпляру передаются число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля.
# table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col. 
# Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку строки row, столбца col. 
# Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице
# table.n_cols() — вернуть число столбцов в таблице
# table.delete_row(row) — удалить строку с номером row
# table.delete_col(col) — удалить колонку с номером col
# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.
# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.


class Table:

    def __init__(self, rows, cols):
        self.row = rows
        self.col = cols
        self.table = [[0]*self.col for _ in range(self.row)]

    def get_value(self, row, col):
        if row > self.row or col > self.col:
            return None
        else:
            return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.row

    def n_cols(self):
        return self.col

    def delete_row(self, row):
        self.table.pop(row)
        self.row = self.row - 1

    def delete_col(self, col):
        for i in range (self.row):
            del self.table[i][col]  
        self.col = self.col - 1

    def add_row(self,row):
        self.table.insert(row, [0]*self.col)
        self.row +=1

    def add_col(self,col):
        for i in range (self.row):
            self.table[i].insert(col, 0)
        self.col +=1




    
tab = Table(3,5)
tab.set_value(0,1,10)
tab.set_value(1,2,20)
tab.set_value(2,3,30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i,j), end=' ')
    print()
print()
tab.delete_row(1)
tab.delete_col(4)
tab.add_row(2)
tab.add_col(2)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i,j), end=' ')
    print()
print()
    



        