import sys, re, l3, re 

# Opening a file 
conllu = open('am_geeztypes-train.conllu', 'w', encoding="utf-8",  newline='') 
#, newline=''

def sentences(s):
	return [i + '።' for i in s.split('።')[:-1]]

def tokenise(s):
	punct = ['፠','፡','።','፣','፤','፥','፦','፧','፨']
	o = s
	for p in punct:
		o = o.replace(p, ' ' + p + ' ')
	o = re.sub('  *', ' ', o)
	return o.strip().split(' ')


f = open("./conllu/am_corpus.txt", encoding='utf-8', errors='ignore')
sent_id = 1
# Each Line
for line in f.readlines():
    line = line.strip('\n')	
    # Each sentence
    for sent in sentences(line):
        tokens = tokenise(sent.strip())
        phon = [l3.phon(lang_abbrev='am', word=i, raw=True)[0][0] for i in tokens]
        #print(tokens)
        #
        #print('# sent_id = %d' % sent_id)        
        conllu.write('# sent_id = %d' % sent_id) 
        conllu.write('\r\n')

        #print('# text = %s' % sent.strip())
        conllu.write('# text = %s' % sent.strip()) 
        conllu.write('\r\n')

        #print('# text[phon] = %s' % ' '.join(phon))
        conllu.write('# translit = %s' % ' '.join(phon)) 
        conllu.write('\r\n')
        
        for (idx, token) in enumerate(tokens):
            res = l3.anal(language='am', word=token, raw=True, rank=True)
            if res:
                for a in res:
                    # 4 በነበረ beneb_ere ('nbr', [-acc,as='smp',ax=None,cj2=None,-def,-neg,ob=[-expl],pos='v',pp='be',+rel,rl=[-acc,+p],sb=[-fem,-p1,-p2,-plr],+sub,tm='prf',vc='smp',-ye], 387)
                    # 5 ጊዜ gizE ('gizE', [-acc,cnj=None,-def,-dis,-gen,-itu,-plr,pos='n',poss=[-expl],pp=None,-prp,rl=[-acc,-gen,-p],v=None], 5427)
                    xpos = '_'
                    feats = ''
                    if a[0] == '.':
                        xpos = 'punct'
                    elif len(a) > 1:
                        if 'pos' in a[1]:
                            xpos = a[1]['pos']
                        for k in a[1]:
                            if type(a[1][k]) == l3.morpho.fs.FeatStruct:
                                #print('Y', k, type(a[1][k]), a[1][k]._features)
                                for f in a[1][k]._features:
                                    if a[1][k]._features[f]:	
                                        feats += ',' + k + '/' + f + '=' + str(a[1][k]._features[f])
                            else:
                        #		print('Z', k, type(a[1][k]),a[1][k])
                                if a[1][k]:
                                    feats += ',' + k + '=' + str(a[1][k])
                        feats = feats.strip(',')
                        #print(feats)
                        #conllu.write(feats) 
                        #conllu.write('\r\n')
                            
                    conllu_line = (idx+1, token, '_','_',xpos,'_','_','_','_','Translit='+phon[idx] + '|Feats='+feats)
                    #print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % conllu_line)
                    conllu.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % conllu_line) 
                    conllu.write('\r\n')
            else:
                    conllu_line = (idx+1, token, '_','_','_','_','_','_','_','Tr='+phon[idx])
                    #print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % conllu_line)
                    conllu.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % conllu_line) 
                    conllu.write('\r\n')
        print(sent_id)
        sent_id += 1

""" maybe write straight to sql db. then on next run it knows what was already done and eliminates
    writing again. then reuse that entry to figure out if tokenization has already been done for a
    specific word instead of readding it manually. Grows exponentually
 """           


# Closing file 
conllu.close() 

# Checking if the data is 
# written to file or not 
#conllu = open('UD_Amharic-GEEZTYPES.conllu', 'r',  encoding="utf-8")  
#print(conllu.read()) 
#conllu.close() 
