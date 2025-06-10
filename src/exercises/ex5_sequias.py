def calcula_periodos(x, y_smooth, umbral=60):
    
    """
    Calcula los periodos de sequía en una serie temporal suavizada según un umbral.

    Identifica los intervalos en los que los valores de `y_smooth` están por debajo del `umbral`,
    y devuelve una lista con los rangos (inicio, fin) de cada uno de esos periodos.

    Args:
        x (list or array-like): Lista de fechas o valores temporales (en formato decimal o numérico).
        y_smooth (list or array-like): Serie temporal suavizada (por ejemplo, salida de `savgol_filter`).
        umbral (float, optional): Valor umbral por debajo del cual se considera que hay sequía. 
                                  Por defecto es 60.

    Returns:
        list of list: Lista de periodos de sequía, donde cada periodo es una lista de dos valores [inicio, fin].
    """
    periodos = []
    en_sequia = False
    inicio = None
    for i in range(len(y_smooth)):
        if y_smooth[i] < umbral and not en_sequia:
            inicio = x[i]
            en_sequia = True
        elif y_smooth[i] >= umbral and en_sequia:
            fin = x[i]
            periodos.append([round(inicio, 2), round(fin, 2)])
            en_sequia = False
    if en_sequia:
        periodos.append([round(inicio, 2), round(x[-1], 2)])
    return periodos
