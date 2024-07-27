{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "24a0dddd-080e-4d98-adc2-ce6335557b80",
   "metadata": {},
   "outputs": [],
   "source": [
    "#importação das bibliotecas: pandas para carregar arquivos .csv e train_test_split para divisão da base de dados (separar amostras)\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dbe8bcee-28f5-40c3-ae5c-30f01fef080b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "class\n",
       "Iris-setosa        50\n",
       "Iris-versicolor    50\n",
       "Iris-virginica     50\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#carregamento da base de dados e contagem de quantos registros existem por classe\n",
    "iris = pd.read_csv('iris.csv')\n",
    "iris['class'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "32741d4c-6357-4545-851f-cc2b79e8843c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "class\n",
       "Iris-setosa        25\n",
       "Iris-virginica     25\n",
       "Iris-versicolor    25\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#iris.iloc[:, 0:4]: buscamos somente os atributos previsores, ou seja, os dados sobre pétala e sétala de planta\n",
    "#iris.iloc[:, 4]: buscamos somente a classe, que é a espécie da planta (setosa, virginica ou versicolor)\n",
    "#test_size: selecionamos 50% da base de dados, que serão copiados para as variáveis X e Y. Essa função retorna 4 valores,\n",
    "#porém, vamos usar somente 50% da base de dados e por isso colocamos \"_\" para outros valores\n",
    "#stratify: para retornar uma amostra baseada na clase\n",
    "\n",
    "x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],\n",
    "                              test_size = 0.5, stratify = iris.iloc[:, 4])\n",
    "y.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9bc80f27-b614-4487-8db7-6ccdb849d38b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>education</th>\n",
       "      <th>age</th>\n",
       "      <th>parity</th>\n",
       "      <th>induced</th>\n",
       "      <th>case</th>\n",
       "      <th>spontaneous</th>\n",
       "      <th>stratum</th>\n",
       "      <th>pooled.stratum</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0-5yrs</td>\n",
       "      <td>26</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0-5yrs</td>\n",
       "      <td>42</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0-5yrs</td>\n",
       "      <td>39</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0-5yrs</td>\n",
       "      <td>34</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>6-11yrs</td>\n",
       "      <td>35</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>243</th>\n",
       "      <td>244</td>\n",
       "      <td>12+ yrs</td>\n",
       "      <td>31</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>79</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>244</th>\n",
       "      <td>245</td>\n",
       "      <td>12+ yrs</td>\n",
       "      <td>34</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>80</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>245</th>\n",
       "      <td>246</td>\n",
       "      <td>12+ yrs</td>\n",
       "      <td>35</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>81</td>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>246</th>\n",
       "      <td>247</td>\n",
       "      <td>12+ yrs</td>\n",
       "      <td>29</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>247</th>\n",
       "      <td>248</td>\n",
       "      <td>12+ yrs</td>\n",
       "      <td>23</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>83</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>248 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Unnamed: 0 education  age  parity  induced  case  spontaneous  stratum  \\\n",
       "0             1    0-5yrs   26       6        1     1            2        1   \n",
       "1             2    0-5yrs   42       1        1     1            0        2   \n",
       "2             3    0-5yrs   39       6        2     1            0        3   \n",
       "3             4    0-5yrs   34       4        2     1            0        4   \n",
       "4             5   6-11yrs   35       3        1     1            1        5   \n",
       "..          ...       ...  ...     ...      ...   ...          ...      ...   \n",
       "243         244   12+ yrs   31       1        0     0            1       79   \n",
       "244         245   12+ yrs   34       1        0     0            0       80   \n",
       "245         246   12+ yrs   35       2        2     0            0       81   \n",
       "246         247   12+ yrs   29       1        0     0            1       82   \n",
       "247         248   12+ yrs   23       1        0     0            1       83   \n",
       "\n",
       "     pooled.stratum  \n",
       "0                 3  \n",
       "1                 1  \n",
       "2                 4  \n",
       "3                 2  \n",
       "4                32  \n",
       "..              ...  \n",
       "243              45  \n",
       "244              47  \n",
       "245              54  \n",
       "246              43  \n",
       "247              40  \n",
       "\n",
       "[248 rows x 9 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Carregamento da base de dados e contagem de quantos registros por classe\n",
    "\n",
    "infert = pd.read_csv('infert.csv')\n",
    "infert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "deec8468-6963-4e3c-9445-847881ee22fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "education\n",
       "6-11yrs    120\n",
       "12+ yrs    116\n",
       "0-5yrs      12\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "infert['education'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d77f064a-1c20-493b-b772-2c49a6c76a8f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01508c4e-afaa-4a8a-91cb-530c7d60c992",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
