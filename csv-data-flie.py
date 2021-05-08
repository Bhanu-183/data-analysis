import urllib.request

urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 
    'climate.txt')

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
weights = np.array([0.3, 0.2, 0.5])
yield=np.matmul(climate_data,weights)

climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)

np.savetxt('climate_results.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments='')
