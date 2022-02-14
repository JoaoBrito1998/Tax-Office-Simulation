import os
try:
    os.system('rm 100.txt')
except:()

for i in range(0,100):
    os.system('python3 main.py >> 100.txt')

file = open("100.txt", "r") 
lines=file.readlines()
flag_espera= False
flag_ocupacao= False

l=0
#tempos_de_espera={'1':{'0-7200':{},'7200-14400':{},'14400-21600':{},'21600-28800':{},'28800-30506':{},'tot':{},},'2_A':{},'2_B':{},'2_C':{},'3':{},'Tot':{},}

def devolve(frase):
    minimo=frase.split('=>')[1].split(':')[1].split(' ')[1]
    medio=frase.split('=>')[1].split(':')[2].split(' ')[1]
    maximo=frase.split('=>')[1].split(':')[3].split(' ')[1]
    return(minimo,medio,maximo)



tempos_de_espera_fase_1={'0-7200':{'minimo':0,'medio':0,'máximo':0,'count':0},'7200-14400':{'minimo':0,'medio':0,'máximo':0,'count':0},'14400-21600':{'minimo':0,'medio':0,'máximo':0,'count':0},'21600-28800':{'minimo':0,'medio':0,'máximo':0,'count':0},'28800-30506':{'minimo':0,'medio':0,'máximo':0,'count':0},'tot':{'minimo':0,'medio':0,'máximo':0,'count':0},}
tempos_de_espera_fase_2_A={'0-7200':{'minimo':0,'medio':0,'máximo':0,'count':0},'7200-14400':{'minimo':0,'medio':0,'máximo':0,'count':0},'14400-21600':{'minimo':0,'medio':0,'máximo':0,'count':0},'21600-28800':{'minimo':0,'medio':0,'máximo':0,'count':0},'28800-30506':{'minimo':0,'medio':0,'máximo':0,'count':0},'tot':{'minimo':0,'medio':0,'máximo':0,'count':0},}
tempos_de_espera_fase_2_B={'0-7200':{'minimo':0,'medio':0,'máximo':0,'count':0},'7200-14400':{'minimo':0,'medio':0,'máximo':0,'count':0},'14400-21600':{'minimo':0,'medio':0,'máximo':0,'count':0},'21600-28800':{'minimo':0,'medio':0,'máximo':0,'count':0},'28800-30506':{'minimo':0,'medio':0,'máximo':0,'count':0},'tot':{'minimo':0,'medio':0,'máximo':0,'count':0},}
tempos_de_espera_fase_2_C={'0-7200':{'minimo':0,'medio':0,'máximo':0,'count':0},'7200-14400':{'minimo':0,'medio':0,'máximo':0,'count':0},'14400-21600':{'minimo':0,'medio':0,'máximo':0,'count':0},'21600-28800':{'minimo':0,'medio':0,'máximo':0,'count':0},'28800-30506':{'minimo':0,'medio':0,'máximo':0,'count':0},'tot':{'minimo':0,'medio':0,'máximo':0,'count':0},}
tempos_de_espera_fase_3={'0-7200':{'minimo':0,'medio':0,'máximo':0,'count':0},'7200-14400':{'minimo':0,'medio':0,'máximo':0,'count':0},'14400-21600':{'minimo':0,'medio':0,'máximo':0,'count':0},'21600-28800':{'minimo':0,'medio':0,'máximo':0,'count':0},'28800-30506':{'minimo':0,'medio':0,'máximo':0,'count':0},'tot':{'minimo':0,'medio':0,'máximo':0,'count':0},}
tempos_de_espera_global={'0-7200':{'minimo':0,'medio':0,'máximo':0,'count':0},'7200-14400':{'minimo':0,'medio':0,'máximo':0,'count':0},'14400-21600':{'minimo':0,'medio':0,'máximo':0,'count':0},'21600-28800':{'minimo':0,'medio':0,'máximo':0,'count':0},'28800-30506':{'minimo':0,'medio':0,'máximo':0,'count':0},'tot':{'minimo':0,'medio':0,'máximo':0,'count':0},}

taxa_fase_1={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}
taxa_fase_2_A1={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}
taxa_fase_2_A2={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}
taxa_fase_2_B1={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}
taxa_fase_2_B2={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}
taxa_fase_2_C={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}
taxa_fase_3={'0-7200':0,'7200-14400':0,'14400-21600':0,'21600-28800':0,'28800-30506':0,'tot':0,}




count=0
i=0
while i < len(lines):
    if(lines[i] == ''):
        i=i+1
    else:    
        if 'TEMPOS DE ESPERA MÍNIMOS,' in lines[i] :
            flag_espera=True
            flag_ocupacao=False
            i=i+3
            count+=1
        if 'TAXAS DE OCUPAÇÃO' in lines[i] :
            flag_espera=False
            flag_ocupacao=True
            i=i+3
        if(flag_espera):
            for j in range(6):
                if( j == 0):
                    minimo,medio,maximo=devolve(lines[i])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_1['0-7200']['count']==0):
                            tempos_de_espera_fase_1['0-7200']['minimo'],tempos_de_espera_fase_1['0-7200']['medio'],tempos_de_espera_fase_1['0-7200']['máximo'],tempos_de_espera_fase_1['0-7200']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_1['0-7200']['count']+1
                        else:
                            tempos_de_espera_fase_1['0-7200']['minimo'],tempos_de_espera_fase_1['0-7200']['medio'],tempos_de_espera_fase_1['0-7200']['máximo'],tempos_de_espera_fase_1['0-7200']['count']=(((tempos_de_espera_fase_1['0-7200']['minimo']*(tempos_de_espera_fase_1['0-7200']['count']))+float(minimo))/((tempos_de_espera_fase_1['0-7200']['count'])+1)),(((tempos_de_espera_fase_1['0-7200']['medio']*(tempos_de_espera_fase_1['0-7200']['count']))+float(medio))/((tempos_de_espera_fase_1['0-7200']['count'])+1)),(((tempos_de_espera_fase_1['0-7200']['máximo']*(tempos_de_espera_fase_1['0-7200']['count']))+float(maximo))/((tempos_de_espera_fase_1['0-7200']['count'])+1)),tempos_de_espera_fase_1['0-7200']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+1])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_1['7200-14400']['count']==0):
                            tempos_de_espera_fase_1['7200-14400']['minimo'],tempos_de_espera_fase_1['7200-14400']['medio'],tempos_de_espera_fase_1['7200-14400']['máximo'],tempos_de_espera_fase_1['7200-14400']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_1['7200-14400']['count']+1
                        else:
                            tempos_de_espera_fase_1['7200-14400']['minimo'],tempos_de_espera_fase_1['7200-14400']['medio'],tempos_de_espera_fase_1['7200-14400']['máximo'],tempos_de_espera_fase_1['7200-14400']['count']=(((tempos_de_espera_fase_1['7200-14400']['minimo']*(tempos_de_espera_fase_1['7200-14400' ]['count']))+float(minimo))/((tempos_de_espera_fase_1['7200-14400']['count'])+1)),(((tempos_de_espera_fase_1['7200-14400']['medio']*( tempos_de_espera_fase_1['7200-14400' ]['count'] ))+float(medio))/((tempos_de_espera_fase_1['7200-14400']['count'])+1)),(((tempos_de_espera_fase_1['7200-14400']['máximo']*(tempos_de_espera_fase_1['7200-14400' ]['count']))+float(maximo))/((tempos_de_espera_fase_1['7200-14400']['count'])+1)),tempos_de_espera_fase_1['7200-14400']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+2])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_1['14400-21600']['count']==0):
                            tempos_de_espera_fase_1['14400-21600']['minimo'],tempos_de_espera_fase_1['14400-21600']['medio'],tempos_de_espera_fase_1['14400-21600']['máximo'],tempos_de_espera_fase_1['14400-21600']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_1['14400-21600']['count']+1
                        else:
                            tempos_de_espera_fase_1['14400-21600']['minimo'],tempos_de_espera_fase_1['14400-21600']['medio'],tempos_de_espera_fase_1['14400-21600']['máximo'],tempos_de_espera_fase_1['14400-21600']['count']=(((tempos_de_espera_fase_1['14400-21600']['minimo']*(tempos_de_espera_fase_1['14400-21600' ]['count']))+float(minimo))/((tempos_de_espera_fase_1['14400-21600']['count'])+1)),(((tempos_de_espera_fase_1['14400-21600']['medio']*(tempos_de_espera_fase_1['14400-21600' ]['count']))+float(medio))/((tempos_de_espera_fase_1['14400-21600']['count'])+1)),(((tempos_de_espera_fase_1['14400-21600']['máximo']*(tempos_de_espera_fase_1['14400-21600' ]['count']))+float(maximo))/((tempos_de_espera_fase_1['14400-21600']['count'])+1)),tempos_de_espera_fase_1['14400-21600']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+3])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_1['21600-28800']['count']==0):
                            tempos_de_espera_fase_1['21600-28800']['minimo'],tempos_de_espera_fase_1['21600-28800']['medio'],tempos_de_espera_fase_1['21600-28800']['máximo'],tempos_de_espera_fase_1['21600-28800']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_1['21600-28800']['count']+1
                        else:
                            tempos_de_espera_fase_1['21600-28800']['minimo'],tempos_de_espera_fase_1['21600-28800']['medio'],tempos_de_espera_fase_1['21600-28800']['máximo'],tempos_de_espera_fase_1['21600-28800']['count']=(((tempos_de_espera_fase_1['21600-28800']['minimo']*( tempos_de_espera_fase_1['21600-28800']['count'] ))+float(minimo))/((tempos_de_espera_fase_1['21600-28800']['count'])+1)),(((tempos_de_espera_fase_1['21600-28800']['medio']*( tempos_de_espera_fase_1['21600-28800']['count'] ))+float(medio))/((tempos_de_espera_fase_1['21600-28800']['count'])+1)),(((tempos_de_espera_fase_1['21600-28800']['máximo']*( tempos_de_espera_fase_1['21600-28800']['count'] ))+float(maximo))/((tempos_de_espera_fase_1['21600-28800']['count'])+1)),tempos_de_espera_fase_1['21600-28800']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+4])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_1['28800-30506']['count']==0):
                            tempos_de_espera_fase_1['28800-30506']['minimo'],tempos_de_espera_fase_1['28800-30506']['medio'],tempos_de_espera_fase_1['28800-30506']['máximo'],tempos_de_espera_fase_1['28800-30506']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_1['28800-30506']['count']+1
                        else:
                            tempos_de_espera_fase_1['28800-30506']['minimo'],tempos_de_espera_fase_1['28800-30506']['medio'],tempos_de_espera_fase_1['28800-30506']['máximo'],tempos_de_espera_fase_1['28800-30506']['count']=(((tempos_de_espera_fase_1['28800-30506']['minimo']*( tempos_de_espera_fase_1['28800-30506']['count'] ))+float(minimo))/((tempos_de_espera_fase_1['28800-30506']['count'])+1)),(((tempos_de_espera_fase_1['28800-30506']['medio']*( tempos_de_espera_fase_1['28800-30506']['count'] ))+float(medio))/((tempos_de_espera_fase_1['28800-30506']['count'])+1)),(((tempos_de_espera_fase_1['28800-30506']['máximo']*( tempos_de_espera_fase_1['28800-30506']['count'] ))+float(maximo))/((tempos_de_espera_fase_1['28800-30506']['count'])+1)),tempos_de_espera_fase_1['28800-30506']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+5])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_1['tot']['count']==0):
                            tempos_de_espera_fase_1['tot']['minimo'],tempos_de_espera_fase_1['tot']['medio'],tempos_de_espera_fase_1['tot']['máximo'],tempos_de_espera_fase_1['tot']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_1['tot']['count']+1
                        else:
                            tempos_de_espera_fase_1['tot']['minimo'],tempos_de_espera_fase_1['tot']['medio'],tempos_de_espera_fase_1['tot']['máximo'],tempos_de_espera_fase_1['tot']['count']=(((tempos_de_espera_fase_1['tot']['minimo']*( tempos_de_espera_fase_1['tot']['count'] ))+float(minimo))/((tempos_de_espera_fase_1['tot']['count'])+1)),(((tempos_de_espera_fase_1['tot']['medio']*( tempos_de_espera_fase_1['tot']['count'] ))+float(medio))/((tempos_de_espera_fase_1['tot']['count'])+1)),(((tempos_de_espera_fase_1['tot']['máximo']*( tempos_de_espera_fase_1['tot']['count'] ))+float(maximo))/((tempos_de_espera_fase_1['tot']['count'])+1)),tempos_de_espera_fase_1['tot']['count']+1
                    i= i+9
                    '''if(count == 1 ):
                        tempos_de_espera_fase_1['0-7200']['minimo'], tempos_de_espera_fase_1['0-7200']['medio'] ,tempos_de_espera_fase_1['0-7200']['máximo'] =devolve(lines[i])
                        tempos_de_espera_fase_1['7200-14400']['minimo'], tempos_de_espera_fase_1['7200-14400']['medio'] ,tempos_de_espera_fase_1['7200-14400']['máximo'] =devolve(lines[i+1])
                        tempos_de_espera_fase_1['14400-21600']['minimo'], tempos_de_espera_fase_1['14400-21600']['medio'] ,tempos_de_espera_fase_1['14400-21600']['máximo'] =devolve(lines[i+2])
                        tempos_de_espera_fase_1['21600-28800']['minimo'], tempos_de_espera_fase_1['21600-28800']['medio'] ,tempos_de_espera_fase_1['21600-28800']['máximo'] =devolve(lines[i+3])
                        tempos_de_espera_fase_1['28800-30506']['minimo'], tempos_de_espera_fase_1['28800-30506']['medio'] ,tempos_de_espera_fase_1['28800-30506']['máximo'] =devolve(lines[i+4])
                        tempos_de_espera_fase_1['tot']['minimo'], tempos_de_espera_fase_1['tot']['medio'] ,tempos_de_espera_fase_1['tot']['máximo'] =devolve(lines[i+5])
                        
                        i= i+9
                    else:
                        minimo,medio,maximo=devolve(lines[i])
                        tempos_de_espera_fase_1['0-7200']['minimo'], tempos_de_espera_fase_1['0-7200']['medio'] ,tempos_de_espera_fase_1['0-7200']['máximo'] = (((tempos_de_espera_fase_1['0-7200']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_1['0-7200']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_1['0-7200']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+1])
                        tempos_de_espera_fase_1['7200-14400']['minimo'], tempos_de_espera_fase_1['7200-14400']['medio'] ,tempos_de_espera_fase_1['7200-14400']['máximo'] =(((tempos_de_espera_fase_1['7200-14400']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_1['7200-14400']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_1['7200-14400']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+2])
                        tempos_de_espera_fase_1['14400-21600']['minimo'], tempos_de_espera_fase_1['14400-21600']['medio'] ,tempos_de_espera_fase_1['14400-21600']['máximo'] =(((tempos_de_espera_fase_1['14400-21600']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_1['14400-21600']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_1['14400-21600']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+3])
                        tempos_de_espera_fase_1['21600-28800']['minimo'], tempos_de_espera_fase_1['21600-28800']['medio'] ,tempos_de_espera_fase_1['21600-28800']['máximo'] =(((tempos_de_espera_fase_1['21600-28800']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_1['21600-28800']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_1['21600-28800']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+4])
                        tempos_de_espera_fase_1['28800-30506']['minimo'], tempos_de_espera_fase_1['28800-30506']['medio'] ,tempos_de_espera_fase_1['28800-30506']['máximo'] =(((tempos_de_espera_fase_1['28800-30506']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_1['28800-30506']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_1['28800-30506']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+5])
                        tempos_de_espera_fase_1['tot']['minimo'], tempos_de_espera_fase_1['tot']['medio'] ,tempos_de_espera_fase_1['tot']['máximo'] =(((tempos_de_espera_fase_1['tot']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_1['tot']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_1['tot']['máximo']*( ....................................... ))+float(maximo))/count)
                        i= i+9'''

                elif(j == 1):
                    minimo,medio,maximo=devolve(lines[i])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_A['0-7200']['count']==0):
                            tempos_de_espera_fase_2_A['0-7200']['minimo'],tempos_de_espera_fase_2_A['0-7200']['medio'],tempos_de_espera_fase_2_A['0-7200']['máximo'],tempos_de_espera_fase_2_A['0-7200']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_A['0-7200']['count']+1
                        else:
                            tempos_de_espera_fase_2_A['0-7200']['minimo'],tempos_de_espera_fase_2_A['0-7200']['medio'],tempos_de_espera_fase_2_A['0-7200']['máximo'],tempos_de_espera_fase_2_A['0-7200']['count']=(((tempos_de_espera_fase_2_A['0-7200']['minimo']*( tempos_de_espera_fase_2_A['0-7200']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_A['0-7200']['count'])+1)),(((tempos_de_espera_fase_2_A['0-7200']['medio']*( tempos_de_espera_fase_2_A['0-7200']['count'] ))+float(medio))/((tempos_de_espera_fase_2_A['0-7200']['count'])+1)),(((tempos_de_espera_fase_2_A['0-7200']['máximo']*( tempos_de_espera_fase_2_A['0-7200']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_A['0-7200']['count'])+1)),tempos_de_espera_fase_2_A['0-7200']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+1])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_A['7200-14400']['count']==0):
                            tempos_de_espera_fase_2_A['7200-14400']['minimo'],tempos_de_espera_fase_2_A['7200-14400']['medio'],tempos_de_espera_fase_2_A['7200-14400']['máximo'],tempos_de_espera_fase_2_A['7200-14400']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_A['7200-14400']['count']+1
                        else:
                            tempos_de_espera_fase_2_A['7200-14400']['minimo'],tempos_de_espera_fase_2_A['7200-14400']['medio'],tempos_de_espera_fase_2_A['7200-14400']['máximo'],tempos_de_espera_fase_2_A['7200-14400']['count']=(((tempos_de_espera_fase_2_A['7200-14400']['minimo']*( tempos_de_espera_fase_2_A['7200-14400']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_A['7200-14400']['count'])+1)),(((tempos_de_espera_fase_2_A['7200-14400']['medio']*( tempos_de_espera_fase_2_A['7200-14400']['count'] ))+float(medio))/((tempos_de_espera_fase_2_A['7200-14400']['count'])+1)),(((tempos_de_espera_fase_2_A['7200-14400']['máximo']*( tempos_de_espera_fase_2_A['7200-14400']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_A['7200-14400']['count'])+1)),tempos_de_espera_fase_2_A['7200-14400']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+2])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_A['14400-21600']['count']==0):
                            tempos_de_espera_fase_2_A['14400-21600']['minimo'],tempos_de_espera_fase_2_A['14400-21600']['medio'],tempos_de_espera_fase_2_A['14400-21600']['máximo'],tempos_de_espera_fase_2_A['14400-21600']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_A['14400-21600']['count']+1
                        else:
                            tempos_de_espera_fase_2_A['14400-21600']['minimo'],tempos_de_espera_fase_2_A['14400-21600']['medio'],tempos_de_espera_fase_2_A['14400-21600']['máximo'],tempos_de_espera_fase_2_A['14400-21600']['count']=(((tempos_de_espera_fase_2_A['14400-21600']['minimo']*( tempos_de_espera_fase_2_A['14400-21600']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_A['14400-21600']['count'])+1)),(((tempos_de_espera_fase_2_A['14400-21600']['medio']*( tempos_de_espera_fase_2_A['14400-21600']['count'] ))+float(medio))/((tempos_de_espera_fase_2_A['14400-21600']['count'])+1)),(((tempos_de_espera_fase_2_A['14400-21600']['máximo']*( tempos_de_espera_fase_2_A['14400-21600']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_A['14400-21600']['count'])+1)),tempos_de_espera_fase_2_A['14400-21600']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+3])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_A['21600-28800']['count']==0):
                            tempos_de_espera_fase_2_A['21600-28800']['minimo'],tempos_de_espera_fase_2_A['21600-28800']['medio'],tempos_de_espera_fase_2_A['21600-28800']['máximo'],tempos_de_espera_fase_2_A['21600-28800']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_A['21600-28800']['count']+1
                        else:
                            tempos_de_espera_fase_2_A['21600-28800']['minimo'],tempos_de_espera_fase_2_A['21600-28800']['medio'],tempos_de_espera_fase_2_A['21600-28800']['máximo'],tempos_de_espera_fase_2_A['21600-28800']['count']=(((tempos_de_espera_fase_2_A['21600-28800']['minimo']*( tempos_de_espera_fase_2_A['21600-28800']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_A['21600-28800']['count'])+1)),(((tempos_de_espera_fase_2_A['21600-28800']['medio']*( tempos_de_espera_fase_2_A['21600-28800']['count'] ))+float(medio))/((tempos_de_espera_fase_2_A['21600-28800']['count'])+1)),(((tempos_de_espera_fase_2_A['21600-28800']['máximo']*( tempos_de_espera_fase_2_A['21600-28800']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_A['21600-28800']['count'])+1)),tempos_de_espera_fase_2_A['21600-28800']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+4])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_A['28800-30506']['count']==0):
                            tempos_de_espera_fase_2_A['28800-30506']['minimo'],tempos_de_espera_fase_2_A['28800-30506']['medio'],tempos_de_espera_fase_2_A['28800-30506']['máximo'],tempos_de_espera_fase_2_A['28800-30506']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_A['28800-30506']['count']+1
                        else:
                            tempos_de_espera_fase_2_A['28800-30506']['minimo'],tempos_de_espera_fase_2_A['28800-30506']['medio'],tempos_de_espera_fase_2_A['28800-30506']['máximo'],tempos_de_espera_fase_2_A['28800-30506']['count']=(((tempos_de_espera_fase_2_A['28800-30506']['minimo']*( tempos_de_espera_fase_2_A['28800-30506']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_A['28800-30506']['count'])+1)),(((tempos_de_espera_fase_2_A['28800-30506']['medio']*( tempos_de_espera_fase_2_A['28800-30506']['count'] ))+float(medio))/((tempos_de_espera_fase_2_A['28800-30506']['count'])+1)),(((tempos_de_espera_fase_2_A['28800-30506']['máximo']*( tempos_de_espera_fase_2_A['28800-30506']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_A['28800-30506']['count'])+1)),tempos_de_espera_fase_2_A['28800-30506']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+5])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_A['tot']['count']==0):
                            tempos_de_espera_fase_2_A['tot']['minimo'],tempos_de_espera_fase_2_A['tot']['medio'],tempos_de_espera_fase_2_A['tot']['máximo'],tempos_de_espera_fase_2_A['tot']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_A['tot']['count']+1
                        else:
                            tempos_de_espera_fase_2_A['tot']['minimo'],tempos_de_espera_fase_2_A['tot']['medio'],tempos_de_espera_fase_2_A['tot']['máximo'],tempos_de_espera_fase_2_A['tot']['count']=(((tempos_de_espera_fase_2_A['tot']['minimo']*( tempos_de_espera_fase_2_A['tot']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_A['tot']['count'])+1)),(((tempos_de_espera_fase_2_A['tot']['medio']*( tempos_de_espera_fase_2_A['tot']['count'] ))+float(medio))/((tempos_de_espera_fase_2_A['tot']['count'])+1)),(((tempos_de_espera_fase_2_A['tot']['máximo']*( tempos_de_espera_fase_2_A['tot']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_A['tot']['count'])+1)),tempos_de_espera_fase_2_A['tot']['count']+1
                    i= i+8
                    '''if(count == 1 ):
                        tempos_de_espera_fase_2_A['0-7200']['minimo'], tempos_de_espera_fase_2_A['0-7200']['medio'] ,tempos_de_espera_fase_2_A['0-7200']['máximo'] =devolve(lines[i])
                        tempos_de_espera_fase_2_A['7200-14400']['minimo'], tempos_de_espera_fase_2_A['7200-14400']['medio'] ,tempos_de_espera_fase_2_A['7200-14400']['máximo'] =devolve(lines[i+1])
                        tempos_de_espera_fase_2_A['14400-21600']['minimo'], tempos_de_espera_fase_2_A['14400-21600']['medio'] ,tempos_de_espera_fase_2_A['14400-21600']['máximo'] =devolve(lines[i+2])
                        tempos_de_espera_fase_2_A['21600-28800']['minimo'], tempos_de_espera_fase_2_A['21600-28800']['medio'] ,tempos_de_espera_fase_2_A['21600-28800']['máximo'] =devolve(lines[i+3])
                        tempos_de_espera_fase_2_A['28800-30506']['minimo'], tempos_de_espera_fase_2_A['28800-30506']['medio'] ,tempos_de_espera_fase_2_A['28800-30506']['máximo'] =devolve(lines[i+4])
                        tempos_de_espera_fase_2_A['tot']['minimo'], tempos_de_espera_fase_2_A['tot']['medio'] ,tempos_de_espera_fase_2_A['tot']['máximo'] =devolve(lines[i+5])
                        
                        i= i+8
                    else:
                        minimo,medio,maximo=devolve(lines[i])
                        tempos_de_espera_fase_2_A['0-7200']['minimo'], tempos_de_espera_fase_2_A['0-7200']['medio'] ,tempos_de_espera_fase_2_A['0-7200']['máximo'] = (((tempos_de_espera_fase_2_A['0-7200']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_2_A['0-7200']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_2_A['0-7200']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+1])
                        tempos_de_espera_fase_2_A['7200-14400']['minimo'], tempos_de_espera_fase_2_A['7200-14400']['medio'] ,tempos_de_espera_fase_2_A['7200-14400']['máximo'] =(((tempos_de_espera_fase_2_A['7200-14400']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_2_A['7200-14400']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_2_A['7200-14400']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+2])
                        tempos_de_espera_fase_2_A['14400-21600']['minimo'], tempos_de_espera_fase_2_A['14400-21600']['medio'] ,tempos_de_espera_fase_2_A['14400-21600']['máximo'] =(((tempos_de_espera_fase_2_A['14400-21600']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_2_A['14400-21600']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_2_A['14400-21600']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+3])
                        tempos_de_espera_fase_2_A['21600-28800']['minimo'], tempos_de_espera_fase_2_A['21600-28800']['medio'] ,tempos_de_espera_fase_2_A['21600-28800']['máximo'] =(((tempos_de_espera_fase_2_A['21600-28800']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_2_A['21600-28800']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_2_A['21600-28800']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+4])
                        tempos_de_espera_fase_2_A['28800-30506']['minimo'], tempos_de_espera_fase_2_A['28800-30506']['medio'] ,tempos_de_espera_fase_2_A['28800-30506']['máximo'] =(((tempos_de_espera_fase_2_A['28800-30506']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_2_A['28800-30506']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_2_A['28800-30506']['máximo']*( ....................................... ))+float(maximo))/count)
                        minimo,medio,maximo=devolve(lines[i+5])
                        tempos_de_espera_fase_2_A['tot']['minimo'], tempos_de_espera_fase_2_A['tot']['medio'] ,tempos_de_espera_fase_2_A['tot']['máximo'] =(((tempos_de_espera_fase_2_A['tot']['minimo']*( ....................................... ))+float(minimo))/count), (((tempos_de_espera_fase_2_A['tot']['medio']*( ....................................... ))+float(medio))/count) ,(((tempos_de_espera_fase_2_A['tot']['máximo']*( ....................................... ))+float(maximo))/count)
                        i= i+8'''
                elif(j == 2):
                    minimo,medio,maximo=devolve(lines[i])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_B['0-7200']['count']==0):
                            tempos_de_espera_fase_2_B['0-7200']['minimo'],tempos_de_espera_fase_2_B['0-7200']['medio'],tempos_de_espera_fase_2_B['0-7200']['máximo'],tempos_de_espera_fase_2_B['0-7200']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_B['0-7200']['count']+1
                        else:
                            tempos_de_espera_fase_2_B['0-7200']['minimo'],tempos_de_espera_fase_2_B['0-7200']['medio'],tempos_de_espera_fase_2_B['0-7200']['máximo'],tempos_de_espera_fase_2_B['0-7200']['count']=(((tempos_de_espera_fase_2_B['0-7200']['minimo']*( tempos_de_espera_fase_2_B['0-7200']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_B['0-7200']['count'])+1)),(((tempos_de_espera_fase_2_B['0-7200']['medio']*( tempos_de_espera_fase_2_B['0-7200']['count'] ))+float(medio))/((tempos_de_espera_fase_2_B['0-7200']['count'])+1)),(((tempos_de_espera_fase_2_B['0-7200']['máximo']*( tempos_de_espera_fase_2_B['0-7200']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_B['0-7200']['count'])+1)),tempos_de_espera_fase_2_B['0-7200']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+1])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_B['7200-14400']['count']==0):
                            tempos_de_espera_fase_2_B['7200-14400']['minimo'],tempos_de_espera_fase_2_B['7200-14400']['medio'],tempos_de_espera_fase_2_B['7200-14400']['máximo'],tempos_de_espera_fase_2_B['7200-14400']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_B['7200-14400']['count']+1
                        else:
                            tempos_de_espera_fase_2_B['7200-14400']['minimo'],tempos_de_espera_fase_2_B['7200-14400']['medio'],tempos_de_espera_fase_2_B['7200-14400']['máximo'],tempos_de_espera_fase_2_B['7200-14400']['count']=(((tempos_de_espera_fase_2_B['7200-14400']['minimo']*( tempos_de_espera_fase_2_B['7200-14400']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_B['7200-14400']['count'])+1)),(((tempos_de_espera_fase_2_B['7200-14400']['medio']*( tempos_de_espera_fase_2_B['7200-14400']['count'] ))+float(medio))/((tempos_de_espera_fase_2_B['7200-14400']['count'])+1)),(((tempos_de_espera_fase_2_B['7200-14400']['máximo']*( tempos_de_espera_fase_2_B['7200-14400']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_B['7200-14400']['count'])+1)),tempos_de_espera_fase_2_B['7200-14400']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+2])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_B['14400-21600']['count']==0):
                            tempos_de_espera_fase_2_B['14400-21600']['minimo'],tempos_de_espera_fase_2_B['14400-21600']['medio'],tempos_de_espera_fase_2_B['14400-21600']['máximo'],tempos_de_espera_fase_2_B['14400-21600']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_B['14400-21600']['count']+1
                        else:
                            tempos_de_espera_fase_2_B['14400-21600']['minimo'],tempos_de_espera_fase_2_B['14400-21600']['medio'],tempos_de_espera_fase_2_B['14400-21600']['máximo'],tempos_de_espera_fase_2_B['14400-21600']['count']=(((tempos_de_espera_fase_2_B['14400-21600']['minimo']*( tempos_de_espera_fase_2_B['14400-21600']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_B['14400-21600']['count'])+1)),(((tempos_de_espera_fase_2_B['14400-21600']['medio']*( tempos_de_espera_fase_2_B['14400-21600']['count'] ))+float(medio))/((tempos_de_espera_fase_2_B['14400-21600']['count'])+1)),(((tempos_de_espera_fase_2_B['14400-21600']['máximo']*( tempos_de_espera_fase_2_B['14400-21600']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_B['14400-21600']['count'])+1)),tempos_de_espera_fase_2_B['14400-21600']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+3])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_B['21600-28800']['count']==0):
                            tempos_de_espera_fase_2_B['21600-28800']['minimo'],tempos_de_espera_fase_2_B['21600-28800']['medio'],tempos_de_espera_fase_2_B['21600-28800']['máximo'],tempos_de_espera_fase_2_B['21600-28800']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_B['21600-28800']['count']+1
                        else:
                            tempos_de_espera_fase_2_B['21600-28800']['minimo'],tempos_de_espera_fase_2_B['21600-28800']['medio'],tempos_de_espera_fase_2_B['21600-28800']['máximo'],tempos_de_espera_fase_2_B['21600-28800']['count']=(((tempos_de_espera_fase_2_B['21600-28800']['minimo']*( tempos_de_espera_fase_2_B['21600-28800']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_B['21600-28800']['count'])+1)),(((tempos_de_espera_fase_2_B['21600-28800']['medio']*( tempos_de_espera_fase_2_B['21600-28800']['count'] ))+float(medio))/((tempos_de_espera_fase_2_B['21600-28800']['count'])+1)),(((tempos_de_espera_fase_2_B['21600-28800']['máximo']*( tempos_de_espera_fase_2_B['21600-28800']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_B['21600-28800']['count'])+1)),tempos_de_espera_fase_2_B['21600-28800']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+4])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_B['28800-30506']['count']==0):
                            tempos_de_espera_fase_2_B['28800-30506']['minimo'],tempos_de_espera_fase_2_B['28800-30506']['medio'],tempos_de_espera_fase_2_B['28800-30506']['máximo'],tempos_de_espera_fase_2_B['28800-30506']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_B['28800-30506']['count']+1
                        else:
                            tempos_de_espera_fase_2_B['28800-30506']['minimo'],tempos_de_espera_fase_2_B['28800-30506']['medio'],tempos_de_espera_fase_2_B['28800-30506']['máximo'],tempos_de_espera_fase_2_B['28800-30506']['count']=(((tempos_de_espera_fase_2_B['28800-30506']['minimo']*( tempos_de_espera_fase_2_B['28800-30506']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_B['28800-30506']['count'])+1)),(((tempos_de_espera_fase_2_B['28800-30506']['medio']*( tempos_de_espera_fase_2_B['28800-30506']['count'] ))+float(medio))/((tempos_de_espera_fase_2_B['28800-30506']['count'])+1)),(((tempos_de_espera_fase_2_B['28800-30506']['máximo']*( tempos_de_espera_fase_2_B['28800-30506']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_B['28800-30506']['count'])+1)),tempos_de_espera_fase_2_B['28800-30506']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+5])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_B['tot']['count']==0):
                            tempos_de_espera_fase_2_B['tot']['minimo'],tempos_de_espera_fase_2_B['tot']['medio'],tempos_de_espera_fase_2_B['tot']['máximo'],tempos_de_espera_fase_2_B['tot']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_B['tot']['count']+1
                        else:
                            tempos_de_espera_fase_2_B['tot']['minimo'],tempos_de_espera_fase_2_B['tot']['medio'],tempos_de_espera_fase_2_B['tot']['máximo'],tempos_de_espera_fase_2_B['tot']['count']=(((tempos_de_espera_fase_2_B['tot']['minimo']*( tempos_de_espera_fase_2_B['tot']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_B['tot']['count'])+1)),(((tempos_de_espera_fase_2_B['tot']['medio']*( tempos_de_espera_fase_2_B['tot']['count'] ))+float(medio))/((tempos_de_espera_fase_2_B['tot']['count'])+1)),(((tempos_de_espera_fase_2_B['tot']['máximo']*( tempos_de_espera_fase_2_B['tot']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_B['tot']['count'])+1)),tempos_de_espera_fase_2_B['tot']['count']+1
                    i= i+8
                elif(j == 3):
                    minimo,medio,maximo=devolve(lines[i])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_C['0-7200']['count']==0):
                            tempos_de_espera_fase_2_C['0-7200']['minimo'],tempos_de_espera_fase_2_C['0-7200']['medio'],tempos_de_espera_fase_2_C['0-7200']['máximo'],tempos_de_espera_fase_2_C['0-7200']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_C['0-7200']['count']+1
                        else:
                            tempos_de_espera_fase_2_C['0-7200']['minimo'],tempos_de_espera_fase_2_C['0-7200']['medio'],tempos_de_espera_fase_2_C['0-7200']['máximo'],tempos_de_espera_fase_2_C['0-7200']['count']=(((tempos_de_espera_fase_2_C['0-7200']['minimo']*( tempos_de_espera_fase_2_C['0-7200']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_C['0-7200']['count'])+1)),(((tempos_de_espera_fase_2_C['0-7200']['medio']*( tempos_de_espera_fase_2_C['0-7200']['count'] ))+float(medio))/((tempos_de_espera_fase_2_C['0-7200']['count'])+1)),(((tempos_de_espera_fase_2_C['0-7200']['máximo']*( tempos_de_espera_fase_2_C['0-7200']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_C['0-7200']['count'])+1)),tempos_de_espera_fase_2_C['0-7200']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+1])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_C['7200-14400']['count']==0):
                            tempos_de_espera_fase_2_C['7200-14400']['minimo'],tempos_de_espera_fase_2_C['7200-14400']['medio'],tempos_de_espera_fase_2_C['7200-14400']['máximo'],tempos_de_espera_fase_2_C['7200-14400']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_C['7200-14400']['count']+1
                        else:
                            tempos_de_espera_fase_2_C['7200-14400']['minimo'],tempos_de_espera_fase_2_C['7200-14400']['medio'],tempos_de_espera_fase_2_C['7200-14400']['máximo'],tempos_de_espera_fase_2_C['7200-14400']['count']=(((tempos_de_espera_fase_2_C['7200-14400']['minimo']*( tempos_de_espera_fase_2_C['7200-14400']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_C['7200-14400']['count'])+1)),(((tempos_de_espera_fase_2_C['7200-14400']['medio']*( tempos_de_espera_fase_2_C['7200-14400']['count'] ))+float(medio))/((tempos_de_espera_fase_2_C['7200-14400']['count'])+1)),(((tempos_de_espera_fase_2_C['7200-14400']['máximo']*( tempos_de_espera_fase_2_C['7200-14400']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_C['7200-14400']['count'])+1)),tempos_de_espera_fase_2_C['7200-14400']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+2])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_C['14400-21600']['count']==0):
                            tempos_de_espera_fase_2_C['14400-21600']['minimo'],tempos_de_espera_fase_2_C['14400-21600']['medio'],tempos_de_espera_fase_2_C['14400-21600']['máximo'],tempos_de_espera_fase_2_C['14400-21600']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_C['14400-21600']['count']+1
                        else:
                            tempos_de_espera_fase_2_C['14400-21600']['minimo'],tempos_de_espera_fase_2_C['14400-21600']['medio'],tempos_de_espera_fase_2_C['14400-21600']['máximo'],tempos_de_espera_fase_2_C['14400-21600']['count']=(((tempos_de_espera_fase_2_C['14400-21600']['minimo']*( tempos_de_espera_fase_2_C['14400-21600']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_C['14400-21600']['count'])+1)),(((tempos_de_espera_fase_2_C['14400-21600']['medio']*( tempos_de_espera_fase_2_C['14400-21600']['count'] ))+float(medio))/((tempos_de_espera_fase_2_C['14400-21600']['count'])+1)),(((tempos_de_espera_fase_2_C['14400-21600']['máximo']*( tempos_de_espera_fase_2_C['14400-21600']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_C['14400-21600']['count'])+1)),tempos_de_espera_fase_2_C['14400-21600']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+3])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_C['21600-28800']['count']==0):
                            tempos_de_espera_fase_2_C['21600-28800']['minimo'],tempos_de_espera_fase_2_C['21600-28800']['medio'],tempos_de_espera_fase_2_C['21600-28800']['máximo'],tempos_de_espera_fase_2_C['21600-28800']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_C['21600-28800']['count']+1
                        else:
                            tempos_de_espera_fase_2_C['21600-28800']['minimo'],tempos_de_espera_fase_2_C['21600-28800']['medio'],tempos_de_espera_fase_2_C['21600-28800']['máximo'],tempos_de_espera_fase_2_C['21600-28800']['count']=(((tempos_de_espera_fase_2_C['21600-28800']['minimo']*( tempos_de_espera_fase_2_C['21600-28800']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_C['21600-28800']['count'])+1)),(((tempos_de_espera_fase_2_C['21600-28800']['medio']*( tempos_de_espera_fase_2_C['21600-28800']['count'] ))+float(medio))/((tempos_de_espera_fase_2_C['21600-28800']['count'])+1)),(((tempos_de_espera_fase_2_C['21600-28800']['máximo']*( tempos_de_espera_fase_2_C['21600-28800']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_C['21600-28800']['count'])+1)),tempos_de_espera_fase_2_C['21600-28800']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+4])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_C['28800-30506']['count']==0):
                            tempos_de_espera_fase_2_C['28800-30506']['minimo'],tempos_de_espera_fase_2_C['28800-30506']['medio'],tempos_de_espera_fase_2_C['28800-30506']['máximo'],tempos_de_espera_fase_2_C['28800-30506']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_C['28800-30506']['count']+1
                        else:
                            tempos_de_espera_fase_2_C['28800-30506']['minimo'],tempos_de_espera_fase_2_C['28800-30506']['medio'],tempos_de_espera_fase_2_C['28800-30506']['máximo'],tempos_de_espera_fase_2_C['28800-30506']['count']=(((tempos_de_espera_fase_2_C['28800-30506']['minimo']*( tempos_de_espera_fase_2_C['28800-30506']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_C['28800-30506']['count'])+1)),(((tempos_de_espera_fase_2_C['28800-30506']['medio']*( tempos_de_espera_fase_2_C['28800-30506']['count'] ))+float(medio))/((tempos_de_espera_fase_2_C['28800-30506']['count'])+1)),(((tempos_de_espera_fase_2_C['28800-30506']['máximo']*( tempos_de_espera_fase_2_C['28800-30506']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_C['28800-30506']['count'])+1)),tempos_de_espera_fase_2_C['28800-30506']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+5])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_2_C['tot']['count']==0):
                            tempos_de_espera_fase_2_C['tot']['minimo'],tempos_de_espera_fase_2_C['tot']['medio'],tempos_de_espera_fase_2_C['tot']['máximo'],tempos_de_espera_fase_2_C['tot']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_2_C['tot']['count']+1
                        else:
                            tempos_de_espera_fase_2_C['tot']['minimo'],tempos_de_espera_fase_2_C['tot']['medio'],tempos_de_espera_fase_2_C['tot']['máximo'],tempos_de_espera_fase_2_C['tot']['count']=(((tempos_de_espera_fase_2_C['tot']['minimo']*( tempos_de_espera_fase_2_C['tot']['count'] ))+float(minimo))/((tempos_de_espera_fase_2_C['tot']['count'])+1)),(((tempos_de_espera_fase_2_C['tot']['medio']*( tempos_de_espera_fase_2_C['tot']['count'] ))+float(medio))/((tempos_de_espera_fase_2_C['tot']['count'])+1)),(((tempos_de_espera_fase_2_C['tot']['máximo']*( tempos_de_espera_fase_2_C['tot']['count'] ))+float(maximo))/((tempos_de_espera_fase_2_C['tot']['count'])+1)),tempos_de_espera_fase_2_C['tot']['count']+1
                    i= i+8
                elif(j == 4):
                    minimo,medio,maximo=devolve(lines[i])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_3['0-7200']['count']==0):
                            tempos_de_espera_fase_3['0-7200']['minimo'],tempos_de_espera_fase_3['0-7200']['medio'],tempos_de_espera_fase_3['0-7200']['máximo'],tempos_de_espera_fase_3['0-7200']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_3['0-7200']['count']+1
                        else:
                            tempos_de_espera_fase_3['0-7200']['minimo'],tempos_de_espera_fase_3['0-7200']['medio'],tempos_de_espera_fase_3['0-7200']['máximo'],tempos_de_espera_fase_3['0-7200']['count']=(((tempos_de_espera_fase_3['0-7200']['minimo']*( tempos_de_espera_fase_3['0-7200']['count'] ))+float(minimo))/((tempos_de_espera_fase_3['0-7200']['count'])+1)),(((tempos_de_espera_fase_3['0-7200']['medio']*( tempos_de_espera_fase_3['0-7200']['count'] ))+float(medio))/((tempos_de_espera_fase_3['0-7200']['count'])+1)),(((tempos_de_espera_fase_3['0-7200']['máximo']*( tempos_de_espera_fase_3['0-7200']['count'] ))+float(maximo))/((tempos_de_espera_fase_3['0-7200']['count'])+1)),tempos_de_espera_fase_3['0-7200']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+1])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_3['7200-14400']['count']==0):
                            tempos_de_espera_fase_3['7200-14400']['minimo'],tempos_de_espera_fase_3['7200-14400']['medio'],tempos_de_espera_fase_3['7200-14400']['máximo'],tempos_de_espera_fase_3['7200-14400']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_3['7200-14400']['count']+1
                        else:
                            tempos_de_espera_fase_3['7200-14400']['minimo'],tempos_de_espera_fase_3['7200-14400']['medio'],tempos_de_espera_fase_3['7200-14400']['máximo'],tempos_de_espera_fase_3['7200-14400']['count']=(((tempos_de_espera_fase_3['7200-14400']['minimo']*( tempos_de_espera_fase_3['7200-14400']['count'] ))+float(minimo))/((tempos_de_espera_fase_3['7200-14400']['count'])+1)),(((tempos_de_espera_fase_3['7200-14400']['medio']*( tempos_de_espera_fase_3['7200-14400']['count'] ))+float(medio))/((tempos_de_espera_fase_3['7200-14400']['count'])+1)),(((tempos_de_espera_fase_3['7200-14400']['máximo']*( tempos_de_espera_fase_3['7200-14400']['count'] ))+float(maximo))/((tempos_de_espera_fase_3['7200-14400']['count'])+1)),tempos_de_espera_fase_3['7200-14400']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+2])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_3['14400-21600']['count']==0):
                            tempos_de_espera_fase_3['14400-21600']['minimo'],tempos_de_espera_fase_3['14400-21600']['medio'],tempos_de_espera_fase_3['14400-21600']['máximo'],tempos_de_espera_fase_3['14400-21600']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_3['14400-21600']['count']+1
                        else:
                            tempos_de_espera_fase_3['14400-21600']['minimo'],tempos_de_espera_fase_3['14400-21600']['medio'],tempos_de_espera_fase_3['14400-21600']['máximo'],tempos_de_espera_fase_3['14400-21600']['count']=(((tempos_de_espera_fase_3['14400-21600']['minimo']*( tempos_de_espera_fase_3['14400-21600']['count'] ))+float(minimo))/((tempos_de_espera_fase_3['14400-21600']['count'])+1)),(((tempos_de_espera_fase_3['14400-21600']['medio']*( tempos_de_espera_fase_3['14400-21600']['count'] ))+float(medio))/((tempos_de_espera_fase_3['14400-21600']['count'])+1)),(((tempos_de_espera_fase_3['14400-21600']['máximo']*( tempos_de_espera_fase_3['14400-21600']['count'] ))+float(maximo))/((tempos_de_espera_fase_3['14400-21600']['count'])+1)),tempos_de_espera_fase_3['14400-21600']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+3])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_3['21600-28800']['count']==0):
                            tempos_de_espera_fase_3['21600-28800']['minimo'],tempos_de_espera_fase_3['21600-28800']['medio'],tempos_de_espera_fase_3['21600-28800']['máximo'],tempos_de_espera_fase_3['21600-28800']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_3['21600-28800']['count']+1
                        else:
                            tempos_de_espera_fase_3['21600-28800']['minimo'],tempos_de_espera_fase_3['21600-28800']['medio'],tempos_de_espera_fase_3['21600-28800']['máximo'],tempos_de_espera_fase_3['21600-28800']['count']=(((tempos_de_espera_fase_3['21600-28800']['minimo']*( tempos_de_espera_fase_3['21600-28800']['count'] ))+float(minimo))/((tempos_de_espera_fase_3['21600-28800']['count'])+1)),(((tempos_de_espera_fase_3['21600-28800']['medio']*( tempos_de_espera_fase_3['21600-28800']['count'] ))+float(medio))/((tempos_de_espera_fase_3['21600-28800']['count'])+1)),(((tempos_de_espera_fase_3['21600-28800']['máximo']*( tempos_de_espera_fase_3['21600-28800']['count'] ))+float(maximo))/((tempos_de_espera_fase_3['21600-28800']['count'])+1)),tempos_de_espera_fase_3['21600-28800']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+4])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_3['28800-30506']['count']==0):
                            tempos_de_espera_fase_3['28800-30506']['minimo'],tempos_de_espera_fase_3['28800-30506']['medio'],tempos_de_espera_fase_3['28800-30506']['máximo'],tempos_de_espera_fase_3['28800-30506']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_3['28800-30506']['count']+1
                        else:
                            tempos_de_espera_fase_3['28800-30506']['minimo'],tempos_de_espera_fase_3['28800-30506']['medio'],tempos_de_espera_fase_3['28800-30506']['máximo'],tempos_de_espera_fase_3['28800-30506']['count']=(((tempos_de_espera_fase_3['28800-30506']['minimo']*( tempos_de_espera_fase_3['28800-30506']['count'] ))+float(minimo))/((tempos_de_espera_fase_3['28800-30506']['count'])+1)),(((tempos_de_espera_fase_3['28800-30506']['medio']*( tempos_de_espera_fase_3['28800-30506']['count'] ))+float(medio))/((tempos_de_espera_fase_3['28800-30506']['count'])+1)),(((tempos_de_espera_fase_3['28800-30506']['máximo']*( tempos_de_espera_fase_3['28800-30506']['count'] ))+float(maximo))/((tempos_de_espera_fase_3['28800-30506']['count'])+1)),tempos_de_espera_fase_3['28800-30506']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+5])
                    if(medio != '-'):
                        if(tempos_de_espera_fase_3['tot']['count']==0):
                            tempos_de_espera_fase_3['tot']['minimo'],tempos_de_espera_fase_3['tot']['medio'],tempos_de_espera_fase_3['tot']['máximo'],tempos_de_espera_fase_3['tot']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_fase_3['tot']['count']+1
                        else:
                            tempos_de_espera_fase_3['tot']['minimo'],tempos_de_espera_fase_3['tot']['medio'],tempos_de_espera_fase_3['tot']['máximo'],tempos_de_espera_fase_3['tot']['count']=(((tempos_de_espera_fase_3['tot']['minimo']*( tempos_de_espera_fase_3['tot']['count'] ))+float(minimo))/((tempos_de_espera_fase_3['tot']['count'])+1)),(((tempos_de_espera_fase_3['tot']['medio']*( tempos_de_espera_fase_3['tot']['count'] ))+float(medio))/((tempos_de_espera_fase_3['tot']['count'])+1)),(((tempos_de_espera_fase_3['tot']['máximo']*( tempos_de_espera_fase_3['tot']['count'] ))+float(maximo))/((tempos_de_espera_fase_3['tot']['count'])+1)),tempos_de_espera_fase_3['tot']['count']+1
                    i= i+8
                elif(j == 5):
                    minimo,medio,maximo=devolve(lines[i])
                    if(medio != '-'):
                        if(tempos_de_espera_global['0-7200']['count']==0):
                            tempos_de_espera_global['0-7200']['minimo'],tempos_de_espera_global['0-7200']['medio'],tempos_de_espera_global['0-7200']['máximo'],tempos_de_espera_global['0-7200']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_global['0-7200']['count']+1
                        else:
                            tempos_de_espera_global['0-7200']['minimo'],tempos_de_espera_global['0-7200']['medio'],tempos_de_espera_global['0-7200']['máximo'],tempos_de_espera_global['0-7200']['count']=(((tempos_de_espera_global['0-7200']['minimo']*( tempos_de_espera_global['0-7200']['count'] ))+float(minimo))/((tempos_de_espera_global['0-7200']['count'])+1)),(((tempos_de_espera_global['0-7200']['medio']*( tempos_de_espera_global['0-7200']['count'] ))+float(medio))/((tempos_de_espera_global['0-7200']['count'])+1)),(((tempos_de_espera_global['0-7200']['máximo']*( tempos_de_espera_global['0-7200']['count'] ))+float(maximo))/((tempos_de_espera_global['0-7200']['count'])+1)),tempos_de_espera_global['0-7200']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+1])
                    if(medio != '-'):
                        if(tempos_de_espera_global['7200-14400']['count']==0):
                            tempos_de_espera_global['7200-14400']['minimo'],tempos_de_espera_global['7200-14400']['medio'],tempos_de_espera_global['7200-14400']['máximo'],tempos_de_espera_global['7200-14400']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_global['7200-14400']['count']+1
                        else:
                            tempos_de_espera_global['7200-14400']['minimo'],tempos_de_espera_global['7200-14400']['medio'],tempos_de_espera_global['7200-14400']['máximo'],tempos_de_espera_global['7200-14400']['count']=(((tempos_de_espera_global['7200-14400']['minimo']*( tempos_de_espera_global['7200-14400']['count'] ))+float(minimo))/((tempos_de_espera_global['7200-14400']['count'])+1)),(((tempos_de_espera_global['7200-14400']['medio']*( tempos_de_espera_global['7200-14400']['count'] ))+float(medio))/((tempos_de_espera_global['7200-14400']['count'])+1)),(((tempos_de_espera_global['7200-14400']['máximo']*( tempos_de_espera_global['7200-14400']['count'] ))+float(maximo))/((tempos_de_espera_global['7200-14400']['count'])+1)),tempos_de_espera_global['7200-14400']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+2])
                    if(medio != '-'):
                        if(tempos_de_espera_global['14400-21600']['count']==0):
                            tempos_de_espera_global['14400-21600']['minimo'],tempos_de_espera_global['14400-21600']['medio'],tempos_de_espera_global['14400-21600']['máximo'],tempos_de_espera_global['14400-21600']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_global['14400-21600']['count']+1
                        else:
                            tempos_de_espera_global['14400-21600']['minimo'],tempos_de_espera_global['14400-21600']['medio'],tempos_de_espera_global['14400-21600']['máximo'],tempos_de_espera_global['14400-21600']['count']=(((tempos_de_espera_global['14400-21600']['minimo']*( tempos_de_espera_global['14400-21600']['count'] ))+float(minimo))/((tempos_de_espera_global['14400-21600']['count'])+1)),(((tempos_de_espera_global['14400-21600']['medio']*( tempos_de_espera_global['14400-21600']['count'] ))+float(medio))/((tempos_de_espera_global['14400-21600']['count'])+1)),(((tempos_de_espera_global['14400-21600']['máximo']*( tempos_de_espera_global['14400-21600']['count'] ))+float(maximo))/((tempos_de_espera_global['14400-21600']['count'])+1)),tempos_de_espera_global['14400-21600']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+3])
                    if(medio != '-'):
                        if(tempos_de_espera_global['21600-28800']['count']==0):
                            tempos_de_espera_global['21600-28800']['minimo'],tempos_de_espera_global['21600-28800']['medio'],tempos_de_espera_global['21600-28800']['máximo'],tempos_de_espera_global['21600-28800']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_global['21600-28800']['count']+1
                        else:
                            tempos_de_espera_global['21600-28800']['minimo'],tempos_de_espera_global['21600-28800']['medio'],tempos_de_espera_global['21600-28800']['máximo'],tempos_de_espera_global['21600-28800']['count']=(((tempos_de_espera_global['21600-28800']['minimo']*( tempos_de_espera_global['21600-28800']['count'] ))+float(minimo))/((tempos_de_espera_global['21600-28800']['count'])+1)),(((tempos_de_espera_global['21600-28800']['medio']*( tempos_de_espera_global['21600-28800']['count'] ))+float(medio))/((tempos_de_espera_global['21600-28800']['count'])+1)),(((tempos_de_espera_global['21600-28800']['máximo']*( tempos_de_espera_global['21600-28800']['count'] ))+float(maximo))/((tempos_de_espera_global['21600-28800']['count'])+1)),tempos_de_espera_global['21600-28800']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+4])
                    if(medio != '-'):
                        if(tempos_de_espera_global['28800-30506']['count']==0):
                            tempos_de_espera_global['28800-30506']['minimo'],tempos_de_espera_global['28800-30506']['medio'],tempos_de_espera_global['28800-30506']['máximo'],tempos_de_espera_global['28800-30506']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_global['28800-30506']['count']+1
                        else:
                            tempos_de_espera_global['28800-30506']['minimo'],tempos_de_espera_global['28800-30506']['medio'],tempos_de_espera_global['28800-30506']['máximo'],tempos_de_espera_global['28800-30506']['count']=(((tempos_de_espera_global['28800-30506']['minimo']*( tempos_de_espera_global['28800-30506']['count'] ))+float(minimo))/((tempos_de_espera_global['28800-30506']['count'])+1)),(((tempos_de_espera_global['28800-30506']['medio']*( tempos_de_espera_global['28800-30506']['count'] ))+float(medio))/((tempos_de_espera_global['28800-30506']['count'])+1)),(((tempos_de_espera_global['28800-30506']['máximo']*( tempos_de_espera_global['28800-30506']['count'] ))+float(maximo))/((tempos_de_espera_global['28800-30506']['count'])+1)),tempos_de_espera_global['28800-30506']['count']+1
                    
                    minimo,medio,maximo=devolve(lines[i+5])
                    if(medio != '-'):
                        if(tempos_de_espera_global['tot']['count']==0):
                            tempos_de_espera_global['tot']['minimo'],tempos_de_espera_global['tot']['medio'],tempos_de_espera_global['tot']['máximo'],tempos_de_espera_global['tot']['count']=float(minimo),float(medio),float(maximo),tempos_de_espera_global['tot']['count']+1
                        else:
                            tempos_de_espera_global['tot']['minimo'],tempos_de_espera_global['tot']['medio'],tempos_de_espera_global['tot']['máximo'],tempos_de_espera_global['tot']['count']=(((tempos_de_espera_global['tot']['minimo']*( tempos_de_espera_global['tot']['count'] ))+float(minimo))/((tempos_de_espera_global['tot']['count'])+1)),(((tempos_de_espera_global['tot']['medio']*( tempos_de_espera_global['tot']['count'] ))+float(medio))/((tempos_de_espera_global['tot']['count'])+1)),(((tempos_de_espera_global['tot']['máximo']*( tempos_de_espera_global['tot']['count'] ))+float(maximo))/((tempos_de_espera_global['tot']['count'])+1)),tempos_de_espera_global['tot']['count']+1
                    i= i+8
            flag_espera=False
        elif(flag_ocupacao):
            for j in range(7):
                if( j == 0):
                    if(count == 1 ):
                        
                        taxa_fase_1['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_1['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_1['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_1['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_1['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_1['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        taxa_fase_1['0-7200'] = (((taxa_fase_1['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_1['7200-14400'] = (((taxa_fase_1['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_1['14400-21600'] = (((taxa_fase_1['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_1['21600-28800'] = (((taxa_fase_1['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_1['28800-30506'] = (((taxa_fase_1['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_1['tot'] = (((taxa_fase_1['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8

                elif(j == 1):
                    if(count == 1 ):
                        taxa_fase_2_A1['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_2_A1['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_2_A1['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_2_A1['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_2_A1['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_2_A1['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        #print(taxa_fase_2_A1['14400-21600'],(float(lines[i+2].split('=>')[1].split('%')[0])) )

                        taxa_fase_2_A1['0-7200'] = (((taxa_fase_2_A1['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A1['7200-14400'] = (((taxa_fase_2_A1['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A1['14400-21600'] = (((taxa_fase_2_A1['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A1['21600-28800'] = (((taxa_fase_2_A1['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A1['28800-30506'] = (((taxa_fase_2_A1['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A1['tot'] = (((taxa_fase_2_A1['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8
                elif(j == 2):
                    if(count == 1 ):
                        taxa_fase_2_A2['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_2_A2['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_2_A2['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_2_A2['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_2_A2['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_2_A2['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        taxa_fase_2_A2['0-7200'] = (((taxa_fase_2_A2['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A2['7200-14400'] = (((taxa_fase_2_A2['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A2['14400-21600'] = (((taxa_fase_2_A2['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A2['21600-28800'] = (((taxa_fase_2_A2['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A2['28800-30506'] = (((taxa_fase_2_A2['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_A2['tot'] = (((taxa_fase_2_A2['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8
                elif(j == 3):
                    if(count == 1 ):
                        taxa_fase_2_B1['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_2_B1['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_2_B1['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_2_B1['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_2_B1['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_2_B1['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        taxa_fase_2_B1['0-7200'] = (((taxa_fase_2_B1['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B1['7200-14400'] = (((taxa_fase_2_B1['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B1['14400-21600'] = (((taxa_fase_2_B1['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B1['21600-28800'] = (((taxa_fase_2_B1['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B1['28800-30506'] = (((taxa_fase_2_B1['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B1['tot'] = (((taxa_fase_2_B1['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8
                elif(j == 4):
                    if(count == 1 ):
                        taxa_fase_2_B2['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_2_B2['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_2_B2['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_2_B2['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_2_B2['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_2_B2['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        taxa_fase_2_B2['0-7200'] = (((taxa_fase_2_B2['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B2['7200-14400'] = (((taxa_fase_2_B2['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B2['14400-21600'] = (((taxa_fase_2_B2['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B2['21600-28800'] = (((taxa_fase_2_B2['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B2['28800-30506'] = (((taxa_fase_2_B2['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_B2['tot'] = (((taxa_fase_2_B2['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8
                elif(j == 5):
                    if(count == 1 ):
                        taxa_fase_2_C['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_2_C['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_2_C['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_2_C['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_2_C['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_2_C['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        taxa_fase_2_C['0-7200'] = (((taxa_fase_2_C['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_C['7200-14400'] = (((taxa_fase_2_C['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_C['14400-21600'] = (((taxa_fase_2_C['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_C['21600-28800'] = (((taxa_fase_2_C['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_C['28800-30506'] = (((taxa_fase_2_C['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_2_C['tot'] = (((taxa_fase_2_C['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8
                elif(j == 6):
                    if(count == 1 ):
                        taxa_fase_3['0-7200'] = float(lines[i].split('=>')[1].split('%')[0])
                        taxa_fase_3['7200-14400'] = float(lines[i+1].split('=>')[1].split('%')[0])
                        taxa_fase_3['14400-21600'] = float(lines[i+2].split('=>')[1].split('%')[0])
                        taxa_fase_3['21600-28800'] = float(lines[i+3].split('=>')[1].split('%')[0])
                        taxa_fase_3['28800-30506'] = float(lines[i+4].split('=>')[1].split('%')[0])
                        taxa_fase_3['tot'] = float(lines[i+5].split('=>')[1].split('%')[0]) 
                        
                        i= i+8
                    else:
                        taxa_fase_3['0-7200'] = (((taxa_fase_3['0-7200']*(count-1))+(float(lines[i].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_3['7200-14400'] = (((taxa_fase_3['7200-14400']*(count-1))+(float(lines[i+1].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_3['14400-21600'] = (((taxa_fase_3['14400-21600']*(count-1))+(float(lines[i+2].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_3['21600-28800'] = (((taxa_fase_3['21600-28800']*(count-1))+(float(lines[i+3].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_3['28800-30506'] = (((taxa_fase_3['28800-30506']*(count-1))+(float(lines[i+4].split('=>')[1].split('%')[0])))/count)
                        taxa_fase_3['tot'] = (((taxa_fase_3['tot']*(count-1))+(float(lines[i+5].split('=>')[1].split('%')[0])))/count)
                        
                        i= i+8
            flag_ocupacao=False
        else:
            i=i+1
print('\nGLOBAL\n\n')

for f in tempos_de_espera_global.items():
    print(f)

print('\nTriagem\n\n')

for f in tempos_de_espera_fase_1.items():
    print(f)

print('\n2_A\n\n')

for f in tempos_de_espera_fase_2_A.items():
    print(f)

print('\n2_B\n\n')

for f in tempos_de_espera_fase_2_B.items():
    print(f)

print('\n2_C\n\n')

for f in tempos_de_espera_fase_2_C.items():
    print(f)

print('\n3\n\n')

for f in tempos_de_espera_fase_3.items():
    print(f)





print('\nTriagem\n\n')

for f in taxa_fase_1.items():
    print(f)

print('\n2_A1\n\n')

for f in taxa_fase_2_A1.items():
    print(f)

print('\n2_A2\n\n')

for f in taxa_fase_2_A2.items():
    print(f)

print('\n2_B1\n\n')

for f in taxa_fase_2_B1.items():
    print(f)

print('\n2_B2\n\n')

for f in taxa_fase_2_B2.items():
    print(f)

print('\n2_C\n\n')

for f in taxa_fase_2_C.items():
    print(f)

print('\n3\n\n')

for f in taxa_fase_3.items():
    print(f)



#print(taxa_global.items())
                        
                    
                    
                        




