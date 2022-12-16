# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и 
# среднее арифметическое последовательности целых чисел. Экземпляры классов инициализируются без аргументов.
#  Метод add_number должен добавлять в статистику число, которое будет учтено при вычислении финального 
# результата методом result. Для экземпляров MinStat и MaxStat result должен возвращать целое число,
#  для AverageStat — число типа float (это число будет сравниваться с правильным ответом до седьмой значащей цифры).
# Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен возвращать None.


class MinStat:
    def __init__(self):
        self.min = []

    def add_number(self, n):
        self.min.append(n)

    def result(self):
        if self.min == []:
            return None
        else:
            return min(self.min)

class MaxStat:
    def __init__(self):
        self.max = []

    def add_number(self, n):
        self.max.append(n)

    def result(self):
        if self.max == []:
            return None
        else:
            return max(self.max)

class AverageStat:
    def __init__(self):
        self.aver = []

    def add_number(self, n):
        self.aver.append(n)

    def result(self):
        if self.aver == []:
            return None
        else:
            l = len(self.aver)
            s = sum(self.aver)
            return s/l





values = [1,2,4,5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

values = [1,0,0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


