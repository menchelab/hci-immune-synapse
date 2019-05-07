import pandas as pd
import numpy as np
from contrastive import CPCA
import umap as u
from scipy import stats

# Following functions are defined here and called directly from R notebook using the 'reticulate' package

def read_pickle_file(file):
    """Read and return content of a pickle file"""
    pickle_data = pd.read_pickle(file)
    return pickle_data

def contrastive_pca(background, foreground, alpha = np.log10(0.5), n = 50):
   """Perform a contrastive PCA to maximize variance in foreground data and minimize variance of
   background data, for a given tradeoff parameter alpha, and return best n axes
   """
   background_data = np.array(background)
   foreground_data = np.array(foreground)
   assert foreground_data.shape[1]==background_data.shape[1]
   mdl = CPCA(n_components=n)
   projected_data = mdl.fit_transform(foreground_data, background_data, alpha_selection='manual', alpha_value=alpha)
   return(projected_data)

def umap(dataFrame, labels = None, n = 2, neighbors = 5, min_dist = 0.3, metric = 'correlation', state = 42):
   """Perform a Uniform Manifold Approximation and Projection"""
   data = np.array(dataFrame)
   n_neighbors = int(neighbors)
   n_components = int(n)
   state = int(state)
   dUmap = u.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, metric=metric, n_components=n_components, random_state=state)
   if labels:
      y = np.array(labels)
      print(type(y))
      print(y.shape)
      return(dUmap.fit_transform(data, y))
   return(dUmap.fit_transform(data))

def umap_fit(dataFrame, labels = None, n = 2, neighbors = 5, min_dist = 0.3, metric = 'correlation', state = 42):
   """Fits a UMAP to data"""
   data = np.array(dataFrame)
   n_neighbors = int(neighbors)
   n_components = int(n)
   state = int(state)
   dUmap = u.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, metric=metric, n_components=n_components, random_state=state)
   if labels:
      y = np.array(labels)
      print(type(y))
      print(y.shape)
      return(dUmap.fit(data, y))
   return(dUmap.fit(data))

def umap_transform(umapObject, dataFrame):
    """Embed data based on a given UMAP fit
    """
    data = np.array(dataFrame)
    return(umapObject.transform(data))

def uncorrelate(dataFrame, orderCol = None, threshold = 0.8):
  """Returns column  of 'dataFrame' that are never pairwise-correlated more than 'threshold',
     prioritizing columns by a giver order 'orderCol' (defaults to left to right).
     (!) For use with reticulate, note that orderCol should be using 0-based indices.
  """
  data = np.array(dataFrame)
  if not orderCol:
    orderCol = range(data.shape[1])
  # Columns to sort
  L1 = np.array(orderCol, dtype=np.int32)
  # Sorted columns to keep
  L2 = []
  while L1.size > 0:
    refFt = L1[0]
    L2.append(refFt)
    L1 = L1[1:]
    stillToKeep = []
    for ift, ft in enumerate(L1):
      if stats.pearsonr(data[:,refFt], data[:,ft])[0] < threshold:
        stillToKeep.append(ift)
    L1 = L1[stillToKeep]
  return(L2)
