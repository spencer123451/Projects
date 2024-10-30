import pandas as pd
import faiss
import requests
import numpy as np


df= pd.read_excel("Book1.xlsx")


def create_textual_representation(row):
    textual_representation=f"""Type:{row['lead_text']},
Original_URL:{row['url']},
Photo_Url:{row['photo_url']},
wikipedia_link:{row['wikipedia_link']}"""
    return textual_representation

df['textual_representation']=df.apply(create_textual_representation,axis=1)

#print(df['textual_representation'].values[0])


dim=4096
index=faiss.IndexFlatL2(dim)

X=np.zeros((len(df['textual_representation']),dim),dtype='float32')


#for i , representation in enumerate(df['textual_representation']):
#    if i%30==0:
#        print("Processed",str(i),'instances')
#    res=requests.post('http://localhost:11434/api/embeddings',
#                json={
##                    'model':'llama2',
#                   'prompt':representation
#                }
#    )

 #   embedding=res.json()['embedding']
 #   X[i]=np.array(embedding)

#index.add(X)



index=faiss.read_index(index)
print(df[df.lead_text.str.contains("Bernard")])
