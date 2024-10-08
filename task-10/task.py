

def correlyatsia(sampleX, sampleY) -> float:

    avgX = sum(sampleX) / len(sampleX)
    avgY = sum(sampleY) / len(sampleY)

    sampleLen = len(sampleX)

    # Коэффициент корреляции
    k = (sum([(sampleX[i] - avgX) * (sampleY[i] - avgY) for i in range(sampleLen)]) / 
         ((sum([(sampleX[i] - avgX) ** 2 for i in range(sampleLen)]) * sum([(sampleY[i] - avgY) ** 2 for i in range(sampleLen)])) ** 0.5))

    return k