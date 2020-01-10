# import matplotlib.pyplot as plt


def check_map(mileage):
  """Generates a map, shows how far the player has traveled at that point in the game"""
  img = plt.imread('./img/map.png')
  fig, ax = plt.subplots()

# def check_map(mileage):
#   img = plt.imread('./img/map.png')
#   fig, ax = plt.subplots()


#   x = [880,840,810,760,660,630,560,520,500,460,400,360,300,260,200,160,80]
#   y = [600,610,620,630,650,660,680,690,700,720,740,750,770,780,800,820,840]
#   distances = [0,102,185,304,554,640,830,932,989,1151,1295,1395,1534,1648,1808,1863,2040]
#   locations = ['Independence','Kansas River Crossing','Big Blue River Crossing','Fort Kearney','Chimney Rock','Fort Laramie','Independence Rock','South Pass','Fort Bridger','Green River Crossing','Soda Springs','Fort Hall','Snake River Crossing','Fort Boise','Blue Mountains','Fort Walla Walla','Oregon City']

#   ax.imshow(img, extent=[0, 1500, 0, 1000],cmap='Greys_r')

#   total_path = ax.plot(x, y, 'ko-', label='Total Path')
#   travelled_path = ax.plot((x[0],x[1]), (y[0],y[1]), 'ro-', label='Travelled Path')

#   for i in range(len(x)-1):
#     if mileage > distances[i]:
#       travelled_path = ax.plot((x[i],x[i+1]), (y[i],y[i+1]), 'ro-')
#     else:
#       break
  
#   if mileage < 2040:
#     current_path = ax.plot((x[i],x[i+1]), (y[i],y[i+1]), 'go-',label='Current Path')

#   if mileage > 0:
#     plt.annotate(locations[0],(x[0],y[0]),xytext=(900,580))
#   if mileage < 2040:
#     plt.annotate(locations[i],(x[i+1],y[i+1]))
#   plt.annotate(locations[16],(x[16],y[16]),xytext=(-200,820))

#   legend = ax.legend(loc='lower left')

#   ax.axes.get_xaxis().set_visible(False)
#   ax.axes.get_yaxis().set_visible(False)

#   plt.show()