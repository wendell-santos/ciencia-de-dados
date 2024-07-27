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
   "execution_count": null,
   "id": "9bc80f27-b614-4487-8db7-6ccdb849d38b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Carregamento da base de dados e contagem de quantos registros por classe\n",
    "\n",
    "infert = pd.read_csv('infert.csv')\n",
    "infert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "deec8468-6963-4e3c-9445-847881ee22fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d77f064a-1c20-493b-b772-2c49a6c76a8f",
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
