def random_walks( Hist=False, Stats=False ):
    
    import matplotlib.pyplot as pl
    import pandas as pd
    import numpy as np
    from random import randint
    
    # if using Jupyter Notebooks uncooment this line for better plot display
    #%config InlineBackend.figure_format = 'retina'
    pl.matplotlib.rcParams.update({'font.size': 14})
    
    n = int( input(f'Number of steps to take: ') )
    m = int( input(f'Number of walkers that will take {n} steps: ') )

    print(f'You have choosen {"{:,}".format(m)} walkers that will take {"{:,}".format(n)} steps. \n')

    # function that goes on one random walk
    def walks():
        steps = np.zeros( n )
        
        for i in range(1 , n):
            step = randint(0, 1)
            
            if step == 1:
                steps[i] = steps[i - 1] + 1
                
            else:
                steps[i] = steps[i - 1] - 1

        return steps

    
    # going through m random walks with n steps.
    rand_walks = []

    for i in range( m ):
        rand_walks.append( walks()[-1] )
        
    # getting last position of each list
    #last_steps = []
    
    #for i in range(m):
     #   last_steps.append( rand_walks[i][-1] )
    

    if Hist == True:
        pl.figure( figsize=(10, 7.5) )
        pl.hist( rand_walks, bins=np.arange(min(rand_walks), max(rand_walks) + 1, 1),
                        color='C3', edgecolor='black', linewidth=0.5 )
        pl.title(f'Displacements of {"{:,}".format(m)} Random Walkers Taking {"{:,}".format(n)} of Steps')
        pl.xlabel('Distance from Origin of The Walkers')
        pl.ylabel('Number of Occurances')
        pl.grid( alpha=0.1 )
        pl.show()
    
    if Stats == True:
        print('Here are the general statistics:')
        rand_walks = pd.DataFrame(rand_walks)
        print( rand_walks.describe() )
        
  
random_walks( Hist=True, Stats=True )