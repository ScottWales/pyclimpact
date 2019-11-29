library(climdex.pcic)

cd <- climdexInput.csv(
    tmax.file = '1018935_MAX_TEMP.csv',
    tmin.file = '1018935_MIN_TEMP.csv',
    prec.file = '1018935_ONE_DAY_PRECIPITATION.csv',
    data.columns = list(tmin="MIN_TEMP", tmax="MAX_TEMP", prec="ONE_DAY_PRECIPITATION"),
    )

write.table(climdex.fd(cd), 'indices/fd.csv')
