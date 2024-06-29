import pickle
count = 0
with open('counts.pkl','wb') as f:
    pickle.dump(count,f)
