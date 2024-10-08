
def matOzhidaniye(sample) -> float:
    return sum(sample) / len(sample)


def dispersiya(sample) -> float:
    mx = matOzhidaniye(sample)
    return sum([(x - mx) ** 2 for x in sample]) / (len(sample) - 1)

def sredneKvadraticheskoeOtklonenie(sample) -> float:
    return dispersiya(sample) ** 0.5


def koVariatsiya(sample) -> float:
    return sredneKvadraticheskoeOtklonenie(sample) / matOzhidaniye(sample)

def doveritelniyInterval(sample, probability) -> tuple[float, float]:
    # Значения обратной функции Лапласа (табл.)
    assert probability in {0.9, 0.95, 0.99}
    tp = {0.9 : 1.643, 0.95 : 1.960, 0.99 : 2.576} [probability]
    
    # СКО оценки мат. ожидания
    sko = (dispersiya(sample) / len(sample)) ** 0.5

    eps = sko * tp
    mx = matOzhidaniye(sample)
    return (mx - eps, mx + eps)

def otkloneniyePercent(value, etalon) -> float:
    return (1 - value / etalon) * 100

