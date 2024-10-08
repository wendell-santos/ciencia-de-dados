{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6e3ad070-63fd-43db-ad04-fa134452cade",
   "metadata": {},
   "outputs": [],
   "source": [
    "#distribuição normal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96c3e4b6-1b2b-44f6-a856-ffd21ad2eeb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importação da função norm\n",
    "from scipy.stats import norm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a855884-f0f0-4dc3-b569-6a0e99d7e84f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Conjunto de objetos numa cesta, a média é 8 e o desvio padrão é 2 (sempre para ambos)\n",
    "#Qual é a probabilidade de tirar um objeto que o peso é menor que 6 kilos?\n",
    "norm.cdf(6, 8, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5063e350-ba95-4af3-8220-60b62236466a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Qual a probabilidade de tirar um objeto que o peso é maior que 6 quilos?\n",
    "norm.sf(6, 8, 2)\n",
    "norm.cdf(6, 8, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c7012c4-2838-4028-a0ba-019a456615e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Qual a probabilidade de tirar um objeto que o peso é menor que 6 quilos ou maior que 10 quilos?\n",
    "norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c305325-9f13-48ce-84ab-a79a157710c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Qual a probabilidade de tirar um objeto que o peso é menor que 10 e menor que 8 quilos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb00654f-446f-4dca-b706-7eaffd508337",
   "metadata": {},
   "outputs": [],
   "source": [
    "norm.sf(10, 8, 2) - norm.cdf(8, 8, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36fd2f52-6774-4dd9-bf96-6214ada90325",
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
