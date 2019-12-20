# https://python-graph-gallery.com/342-animation-on-3d-plot/
# library
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Get the data (csv file is hosted on the web)
url = 'https://python-graph-gallery.com/wp-content/uploads/volcano.csv'
data = pd.read_csv(url)

# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]

# And transform the old column name in something numeric
df['X']=pd.Categorical(df['X'])
df['X']=df['X'].cat.codes

for angle in range(70,210,2):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # We are going to do 20 plots, for 20 different angles

    # Make the plot
    ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
    # Set the angle of the camera
    ax.view_init(30,angle)
    # Save it
    filename='PNG/Volcano_step'+str(angle)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()

# # Then use image magick (this is bash, not python)
# convert -delay 50 Volcano*.png animated_volcano.gif
