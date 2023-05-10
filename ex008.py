m = int(input('Digite um número para ser convertido, a sua unidade atual é dada em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('As conversões de medidas ficaram como: \n{} km. \n{} hm. \n{} dam. \n{} m. \n{} dm. \n{} cm.  \n{} mm.' .format(km, hm, dam, m, dm, cm, mm))
