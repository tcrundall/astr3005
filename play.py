import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt

crvad2 = Table.read('C:/Users/Tim/Documents/Academic/ASTR3005/code/crvad2.dat',
             readme='C:/Users/Tim/Documents/Academic/ASTR3005/code/crvad2.ReadMe',
             format='ascii.cds')

#plt.plot(crvad2['RAhour'],crvad2['DEdeg'],'.')

# Important to remember that some parrallaxes are negative... (?)
#good_stars = np.where( (crvad2['e_RV'] < 5) &
#                   (crvad2['Plx']/crvad2['e_Plx'] >  5))[0]
#print(good_stars)
    
bad_stars = np.where( (crvad2['e_RV'] > 10) &
    ((crvad2['e_Plx']/crvad2['Plx'] >=  0.2) |
     (crvad2['e_Plx']/crvad2['Plx'] <= -0.2)))[0]

good_stars = (crvad2['e_RV'] < 5) & \
                   (crvad2['Plx']/crvad2['e_Plx'] >  5)

boundary = 80
close_stars = np.where( (crvad2['Plx'] < -boundary) |
                        (crvad2['Plx'] >  boundary))[0]

bright_stars = np.where( (crvad2['Bmag']) <3.8)[0]

#far_stars = np.where( (crvad2['Plx'] > 0))[0]
 
#plt.plot(crvad2['RAhour'],crvad2['DEdeg'],'.')
   
#plt.plot(crvad2['RAhour'][good_stars],crvad2['DEdeg'][good_stars],'.')
plt.plot(crvad2['RAhour'][bright_stars],crvad2['DEdeg'][bright_stars],'.')
plt.plot(crvad2['RAhour'][close_stars],crvad2['DEdeg'][close_stars],'.')
#plt.plot(crvad2['RAhour'],crvad2['DEdeg'],'.')
    
#plt.plot(crvad2['Plx'],crvad2['e_Plx'],'.')

#plt.plot(crvad2['Plx'][good_stars],crvad2['Bmag'][good_stars],'.')