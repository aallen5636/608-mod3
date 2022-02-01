{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a66e0b65-fbf6-44f9-ae26-c7bcf8a97093",
   "metadata": {},
   "outputs": [],
   "source": [
    "def maximum(value1, value2, value3):\n",
    "    \"\"\"Return the maximum of three value Ashley Allen\"\"\"\n",
    "    max_value = value1\n",
    "    if value2 > max_value:\n",
    "        max_value = value2\n",
    "    if value3 > max_value:\n",
    "        max_value = value3\n",
    "    return print (max_value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "36838322-4b2d-49cc-96cb-6a3983335e2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "maximum(12, 27, 36)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e4962f3f-c286-4f1e-8700-175f28714d18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45.6\n"
     ]
    }
   ],
   "source": [
    "maximum(12.3, 45.6, 9.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8893ef9d-9845-4cb2-b3dc-17a9d1cfdc55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yellow\n"
     ]
    }
   ],
   "source": [
    "maximum('yellow', 'red', 'orange')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "70f9eb10-60cb-4b4c-804e-d614ac5649d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max(12, 27, 36)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "79ffad29-ff00-4f44-b735-6bb58e2355f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min(15, 9, 27, 14)"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
